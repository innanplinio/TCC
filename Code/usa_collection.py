# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi
from facebook_business.exceptions import FacebookError
import json, os, time, gzip, getopt, traceback
import csv, sys
import facebook_attributes as search_elements
import codecs, psycopg2

DEBUG_REQUEST = True
DEBUG_CATEGORIES = True
MAXIMUM_EXCEPTIONS = 15

DATABASE_LOCAL_BLACK = 1
DATABASE_MPI = 2


# facebook api
# https://github.com/facebook/facebook-python-ads-sdk
# readme file - https://github.com/facebook/facebook-python-ads-sdk/blob/master/README.md

def verifyDir(dir_path):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)


def getCurrentTime():
    return '%s' % (time.strftime("%Y-%m-%d--%H-%M-%S"))

def removingIncompleteOutputFile(output_file, output_path, log_file):
    output_file.close()
    log_file.write('removing: %s' % output_path)
    if os.path.isfile(output_path):
        try:
            os.remove(output_path)
            log_file.write('file removed')
        except:
            log_file.write('file NOT removed')
    log_file.flush()


#         return True

def crawlInterest(interest_id, destination_file_path, account, log_file, exception_log, count_total_requests,
                  count_sequenced_exceptions, count_exceptions, sleep_time):
    targeting_spec = search_elements.targeting_spec
    targeting_spec['interests'] = []

    try:
        log_file.write('************* FACEBOOK PAGE *************\n')
        try:
            log_file.write('%s\n' % (interest_id))
        except:
            print('Exception writing - %s' % (interest_id))
        log_file.flush()
    except:
        print('error when logging')

    if 'all' not in interest_id:
        targeting_spec['interests'] = [interest_id]

    destfilename = '%s%s.gz' % (destination_file_path, interest_id)

    if os.path.isfile(destfilename):
        #                 print 'file already collected %s\n' % destination_file_path
        log_file.write('interest already collected:- %s\n' % interest_id)
        log_file.flush()
        return count_total_requests, count_sequenced_exceptions, count_exceptions

    output_file = gzip.open(destfilename, 'wt')
    writer = csv.writer(output_file)

    # ********************************** GLOBAL INTEREST **********************************
    targeting_spec['age_min'] = 13
    count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000 = executeRequest('all',
                                                                                                             'all',
                                                                                                             interest_id,
                                                                                                             targeting_spec,
                                                                                                             account,
                                                                                                             exception_log,
                                                                                                             writer,
                                                                                                             output_file,
                                                                                                             count_total_requests,
                                                                                                             count_sequenced_exceptions,
                                                                                                             count_exceptions,
                                                                                                             sleep_time)

    if count_sequenced_exceptions == MAXIMUM_EXCEPTIONS:
        removingIncompleteOutputFile(output_file, destfilename, log_file)
        return count_total_requests, count_sequenced_exceptions, count_exceptions

    if audience_below_1000 == True:
        try:
            log_file.write('Facebook_interest_interruped(audience = 1000): %s\n' % interest_id)
            log_file.flush()
        except:
            print('exception when logging')
        output_file.close()
        count_sequenced_exceptions = 0
        return count_total_requests, count_sequenced_exceptions, count_exceptions

    # ********************************** EDUCATION_STATUSES **********************************
    targeting_spec['education_statuses'] = []
    for scholarity_field in search_elements.scholarities:
        if DEBUG_CATEGORIES: print(scholarity_field)
        targeting_spec['education_statuses'] = search_elements.scholarities[scholarity_field]
        count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000 = executeRequest(
            'education_status', scholarity_field, interest_id,
            targeting_spec, account, exception_log, writer, output_file, count_total_requests,
            count_sequenced_exceptions,
            count_exceptions, sleep_time)
        if count_sequenced_exceptions == MAXIMUM_EXCEPTIONS:
            removingIncompleteOutputFile(output_file, destfilename, log_file)
            return count_total_requests, count_sequenced_exceptions, count_exceptions
    del targeting_spec['education_statuses']

    # ********************************** POLITICAL_ALIGNMENT **********************************
    '''for political_leaning in search_elements.political_alignment:
        if DEBUG_CATEGORIES: print(political_leaning)
        flexible_spec = []
        politics_elements = search_elements.political_alignment[political_leaning]
        flexible_spec.append({'politics': politics_elements})
        targeting_spec['flexible_spec'] = flexible_spec
        count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000 = executeRequest(
            'political_alignment', political_leaning, interest_id,
            targeting_spec, account, exception_log, writer, output_file, count_total_requests,
            count_sequenced_exceptions,
            count_exceptions, sleep_time)
        if count_sequenced_exceptions == MAXIMUM_EXCEPTIONS:
            removingIncompleteOutputFile(output_file, destfilename, log_file)
            return count_total_requests, count_sequenced_exceptions, count_exceptions
    del targeting_spec['flexible_spec']'''
    
    # ********************************** RELATIONSHIP_STATUSES **********************************
    for relationship_status in search_elements.relationship_statuses:
        if DEBUG_CATEGORIES: print(relationship_status)
        targeting_spec['relationship_statuses'] = search_elements.relationship_statuses[relationship_status]
        count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000 = executeRequest(
            'relationship_status', relationship_status, interest_id,
            targeting_spec, account, exception_log, writer, output_file, count_total_requests,
            count_sequenced_exceptions,
            count_exceptions, sleep_time)
        if count_sequenced_exceptions == MAXIMUM_EXCEPTIONS:
            removingIncompleteOutputFile(output_file, destfilename, log_file)
            return count_total_requests, count_sequenced_exceptions, count_exceptions
    del targeting_spec['relationship_statuses']

    # ********************************** AGE GROUP **********************************
    del targeting_spec['age_min']
    for age_group in search_elements.age_intervals:
        if (DEBUG_CATEGORIES):
            print(age_group)
        if 'age_min' in targeting_spec:
            del targeting_spec['age_min']
        if 'age_max' in targeting_spec:
            del targeting_spec['age_max']
        targeting_spec['age_min'] = search_elements.age_intervals[age_group]['age_min']
        if (age_group != 'old_2' and age_group != 'all'):
            targeting_spec['age_max'] = search_elements.age_intervals[age_group]['age_max']

        count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000 = executeRequest(
            'age_intervals', age_group, interest_id,
            targeting_spec, account, exception_log, writer, output_file, count_total_requests,
            count_sequenced_exceptions,
            count_exceptions, sleep_time)
        if (count_sequenced_exceptions == MAXIMUM_EXCEPTIONS):
            removingIncompleteOutputFile(output_file, destfilename, log_file)
            return count_total_requests, count_sequenced_exceptions, count_exceptions

    #del targeting_spec['age_max']
    targeting_spec['age_min'] = 13

    # ********************************** RACE **********************************
    '''
    for race in search_elements.racial_affinities:
        if DEBUG_CATEGORIES:
            print(race)
        exclusions_race = []
        behaviors_race = []
        flexible_spec = []
        if race == 'other':
            targeting_spec['behaviors'] = []
            exclusions_race = search_elements.caucasian_spec['behaviors']
            targeting_spec['exclusions'] = {'behaviors': exclusions_race}

            count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000 = executeRequest(
                'racial_affinities', race, interest_id,
                targeting_spec, account, exception_log, writer, output_file, count_total_requests,
                count_sequenced_exceptions,
                count_exceptions, sleep_time)
            if count_sequenced_exceptions == MAXIMUM_EXCEPTIONS:
                removingIncompleteOutputFile(output_file, destfilename, log_file)
                return count_total_requests, count_sequenced_exceptions, count_exceptions

            del targeting_spec['exclusions']

        elif race != 'all':
            behaviors_race.append(search_elements.racial_affinities[race])
            flexible_spec.append({'behaviors': behaviors_race})
            targeting_spec['flexible_spec'] = flexible_spec
            count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000 = executeRequest(
                'racial_affinities', race, interest_id,
                targeting_spec, account, exception_log, writer, output_file, count_total_requests,
                count_sequenced_exceptions,
                count_exceptions, sleep_time)
            if count_sequenced_exceptions == MAXIMUM_EXCEPTIONS:
                removingIncompleteOutputFile(output_file, destfilename, log_file)
                return count_total_requests, count_sequenced_exceptions, count_exceptions
            del targeting_spec['flexible_spec']'''

        # ********************************** EXPAT **********************************
    #         for expat in search_elements.expats:
    for expats in search_elements.expats_new:
        behaviors_expats = []
        flexible_spec = []
        if DEBUG_CATEGORIES: print(expats)
        #         behaviors_expats.append(search_elements.expats[expats])
        behaviors_expats = search_elements.expats_new[expats]
        flexible_spec.append({'behaviors': behaviors_expats})
        targeting_spec['flexible_spec'] = flexible_spec
        count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000 = executeRequest(
            'expat', expats, interest_id,
            targeting_spec, account, exception_log, writer, output_file, count_total_requests,
            count_sequenced_exceptions,
            count_exceptions, sleep_time)
        if count_sequenced_exceptions == MAXIMUM_EXCEPTIONS:
            removingIncompleteOutputFile(output_file, destfilename, log_file)
            return count_total_requests, count_sequenced_exceptions, count_exceptions

    del targeting_spec['flexible_spec']

    # ********************************** GENDER **********************************
    for gender in search_elements.genders:
        if DEBUG_CATEGORIES: print(gender)
        targeting_spec['genders'] = search_elements.genders[gender]

        count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000 = executeRequest(
            'gender', gender, interest_id,
            targeting_spec, account, exception_log, writer, output_file, count_total_requests,
            count_sequenced_exceptions,
            count_exceptions, sleep_time)
        if count_sequenced_exceptions == MAXIMUM_EXCEPTIONS:
            removingIncompleteOutputFile(output_file, destfilename, log_file)
            return count_total_requests, count_sequenced_exceptions, count_exceptions

    del targeting_spec['genders']

    try:
        log_file.write('Facebook interest finished\n')
        log_file.flush()
    except:
        print('exception when logging')
    output_file.close()
    return count_total_requests, count_sequenced_exceptions, count_exceptions


def executeRequest(category, value, interest_id, targeting_spec, account, exception_log, writer, output_file,
                   count_total_requests, count_sequenced_exceptions, count_exceptions, sleep_time):
    # All params are ready. query the database
    api_params = {
        'targeting_spec': targeting_spec
    }
    audience_below_1000 = False
    request_ok = True
    number = -10
    while request_ok:
        number = -10
        try:
            if DEBUG_REQUEST:
                print(api_params)
            reach_estimate = account.get_reach_estimate(params=api_params)
            number = reach_estimate[0]['users']
            #             print number
            request_ok = False
            count_total_requests += 1
            count_sequenced_exceptions = 0
            if number == 1000:
                audience_below_1000 = True
        # oh shit k
        except FacebookError as e:
            if DEBUG_REQUEST:
                print(e)
            count_sequenced_exceptions += 1
            count_exceptions += 1
            try:
                exception_log.write('<<<<<<<< Exception >>>>>>>>>\n')
                exception_log.write('\t# exceptions: %d\n' % count_sequenced_exceptions)
                exception_log.write('\t#ELEMENTS READ: %d\n' % count_total_requests)
                exception_log.write('\terror_type: %s\n' % e.api_error_type())
                exception_log.write('\terror_code: %s\n' % e.api_error_code())
                exception_log.write('\terror_type: %s\n' % e.api_error_message())
                exception_log.write('\terror_type:api_params %s\n' % api_params)
                exception_log.write('\t%s\n' % interest_id)
                exception_log.flush()
            except:
                exception_log.write('\tlog_failed: %d \n' % count_total_requests)
                exception_log.write('\t# exceptions: %d\n' % count_sequenced_exceptions)
                exception_log.flush()
            if count_sequenced_exceptions >= 3 and e.api_error_message() == 'An unknown error occurred':
                exception_log.write('\t unknow error - jumping request\n')
                exception_log.flush()
                request_ok = False
                number = -10
            if count_sequenced_exceptions == 10:
                exception_log.write('******* Try next request ******* \n')
                exception_log.flush()
                request_ok = False
                number = -10
            if count_sequenced_exceptions == MAXIMUM_EXCEPTIONS:
                exception_log.write('******* Finish Execution after %d errors ******* \n' % (MAXIMUM_EXCEPTIONS))
                #                 log_file.write('total of interest ids: %d \n' % count_interest_ids)
                exception_log.write('total of requests: %d \n' % count_total_requests)
                exception_log.write('total of exceptions: %d \n' % count_exceptions)
                exception_log.flush()
                # # safe exit
                exception_log.close()
                #                 already_save_file.close()
                output_file.close()
                return count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000

            if count_sequenced_exceptions == 0:
                time_to_sleep = (5 * 60)
                exception_log.write('Waiting %.2lf minutes to restart again...\n' % (float(time_to_sleep) / 60))
            else:
                time_to_sleep = (5 * 60) * (count_sequenced_exceptions)
                exception_log.write('Waiting %.2lf minutes to restart again...\n' % (float(time_to_sleep) / 60))
            #             exception_log.write('Waiting 5 minutes to restart again...\n')
            exception_log.flush()
            time.sleep(time_to_sleep)
        except Exception as ex:
            exception_log.write('<<<<<<<< REGULAR Exception >>>>>>>>>\n')
            exception_log.write('\t#ELEMENTS READ: %d\n' % count_total_requests)
            exception_log.write('exception_msg: %s' % str(ex))
            exception_log.write('\t# exceptions: %d\n' % count_sequenced_exceptions)
            count_sequenced_exceptions += 1
            exception_log.write('Waiting 5 minutes to restart again...\n')
            exception_log.flush()
            time.sleep(5 * 60)

    if number != -10:
        results_row = [category, value, number]

        writer.writerow(results_row)
        output_file.flush()
        time.sleep(sleep_time)

    return count_total_requests, count_sequenced_exceptions, count_exceptions, audience_below_1000


def crawlDemographicsWithoutInterest(token_number, sleep_time):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open('%s/credentials.json' % dir_path, 'r') as cred_file:
        credentials_file = json.load(cred_file)

    credentials = credentials_file['token%s' % token_number]
    country = 'US'
    destination_file_path = '/home/filipe/social_alexa/facebook_ad_api/demographics/%s/' % (country)

    log_file = codecs.open('%slog_all.txt' % (destination_file_path), 'w', encoding='utf-8')
    exception_log_file = codecs.open('%sexception_log_all.txt' % (destination_file_path), 'w', encoding='utf-8')
    print(credentials)
    #     exit
    # Bootstrap API
    #     FacebookAdsApi.init(credentials['app_id'], credentials['secret'], credentials['token'])
    FacebookAdsApi.init(access_token=credentials['token'])
    # Initialize ad account
    account = AdAccount('act_' + credentials['account_id'])
    #     account = AdAccount()
    count_total_requests = 0
    count_interest_ids = 0
    count_exceptions = 0
    count_sequenced_exceptions = 0

    cur_time = getCurrentTime()
    log_file.write('Execution initialized: %s \n' % cur_time)
    count_interest_ids += 1
    interest_id = 'all_%s' % cur_time
    crawlInterest(interest_id, destination_file_path, account, log_file, exception_log_file, interest_id,
                  count_total_requests, count_sequenced_exceptions, count_exceptions, sleep_time)

    log_file.write('total of interest ids: %d \n' % count_interest_ids)
    log_file.write('total of requests: %d \n' % count_total_requests)
    log_file.write('total of exceptions: %d \n' % count_exceptions)
    log_file.write('Execution finalized: %s \n' % getCurrentTime())

    # # safe exit
    log_file.close()


def crawlDemographics(output_file_path, sleep_time):
    #     token = ""
    #     act_id = ""
    #     secret = "-"

    token = "EAAbPAyrnxo0BAEzRou8xgETD7tR4W1g4i0DQr5Nt4xEZCyuT3Akuc9SEMRGSKHG71t970Cr3FtdsDCxiOZAcJHWGWUXfERkK0vm03xqd1EOhTmZBaUuPMa9uxCQOF8iDKlMdd73gXzMrjj1RpQ6FFX90bCFZBC8ZD"
    act_id = "140203616062598"
    secret = "-"

    print(token)
    print(act_id)

    country = 'US'
    destination_file_path = '%s%s/' % (output_file_path, country)

    verifyDir(destination_file_path)
    print(destination_file_path)

    log_file = codecs.open('%slog_all.txt' % (destination_file_path), 'w', encoding='utf-8')
    exception_log_file = codecs.open('%sexception_log_all.txt' % (destination_file_path), 'w', encoding='utf-8')
    #     print credentials
    #     exit
    # Bootstrap API
    #     FacebookAdsApi.init(credentials['app_id'], credentials['secret'], credentials['token'])
    if secret != '-':
        FacebookAdsApi.init(access_token=token, app_secret=secret, api_version='v9.0')
    else:
        FacebookAdsApi.init(access_token=token, api_version='v9.0')
    account = AdAccount('act_' + act_id)

    count_total_requests = 0
    count_interest_ids = 0
    count_exceptions = 0
    count_sequenced_exceptions = 0

    cur_time = getCurrentTime()
    log_file.write('Execution initialized: %s \n' % cur_time)
    count_interest_ids += 1

    # first element of the following list indicates to the crawler to collect the demographics for the US only whereas second and third one are
    # the interests related to the new york times and washington post, respectively.

    list_of_interests = ['all_%s' % cur_time]
    for interest_id in list_of_interests:
        #         interest_id =  'all_%s' % cur_time
        #         crawlInterest(interest_id, destination_file_path, account, log_file, exception_log_file, sleep_time)
        count_total_requests, count_sequenced_exceptions, count_exceptions = crawlInterest(interest_id,
                                                                                           destination_file_path,
                                                                                           account, log_file,
                                                                                           exception_log_file,
                                                                                           count_total_requests,
                                                                                           count_sequenced_exceptions,
                                                                                           count_exceptions, sleep_time)
        if count_sequenced_exceptions == MAXIMUM_EXCEPTIONS:
            log_file.write('******** Sequenced exceptions == %d **********\n' % MAXIMUM_EXCEPTIONS)
            log_file.write('******** Going to terminate **********\n')
            break

    log_file.write('total of interest ids: %d \n' % count_interest_ids)
    log_file.write('total of requests: %d \n' % count_total_requests)
    log_file.write('total of exceptions: %d \n' % count_exceptions)
    log_file.write('Execution finalized: %s \n' % getCurrentTime())

    # # safe exit
    log_file.close()


def main(argv):
    output_file_path = '/Users/range/Documents/GitHub/TCC/Code/OutputTest'
    sleep_time = 1
    crawlDemographics(output_file_path, sleep_time)


if __name__ == "__main__":
    main(sys.argv[1:])
