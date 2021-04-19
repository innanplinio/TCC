# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

#from facebookads.adobjects.adaccount import AdAccount
#from facebookads.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
import SimpleSearchingElements as search_elements
import sys, time, gzip, csv

sleep_time = 0.1
output_file_path = '/Users/range/Documents/GitHub/TCC/Code/OutputBR/'
token = "EAAbPAyrnxo0BAEzRou8xgETD7tR4W1g4i0DQr5Nt4xEZCyuT3Akuc9SEMRGSKHG71t970Cr3FtdsDCxiOZAcJHWGWUXfERkK0vm03xqd1EOhTmZBaUuPMa9uxCQOF8iDKlMdd73gXzMrjj1RpQ6FFX90bCFZBC8ZD"
act_id = "140203616062598"
secret = "-"


# https://developers.facebook.com/docs/marketing-api/targeting-search/

targeting_spec = {
    "geo_locations": {"countries":["BR"]},
    "publisher_platforms": ["facebook", "instagram"],
    "facebook_positions": ["feed", "instream_video"], #feed, right_hand_column
    "device_platforms": ["mobile", "desktop"],
    "excluded_publisher_categories": [],
    "excluded_publisher_list_ids": [],
    "user_device": [],
    "excluded_user_device": [],
    "user_os": [],
    "wireless_carrier": [],
    'behaviors': [],
    'interests': [],
    "flexible_spec": []        
}

def getCurrentTime():
    return '%s' % (time.strftime("%Y-%m-%d--%H-%M-%S"))

def get_ad_account():
    
    if secret != '-':
        FacebookAdsApi.init(access_token=token, app_secret=secret, api_version='v8.0')
    else:
        FacebookAdsApi.init(access_token=token, api_version='v8.0')
    account = AdAccount('act_' + act_id)
    return account


def make_request(account, targeting_spec):
    api_params = {
        'targeting_spec': targeting_spec
    }
    
    reach_estimate = account.get_reach_estimate(params=api_params)
    number = reach_estimate[0]['users']
    return number

def multiple_interests_or(account):
    donald_trump_interest = "6003210792176"
    hillary_clinton_interest = "6003361373387"
    targeting_spec['age_min']=18
#     targeting_spec['age_max']=65    
#     targeting_spec['interests'] = [donald_trump_interest]    
    targeting_spec['interests'] = [donald_trump_interest,hillary_clinton_interest] 
    print('audience_size: %d' % make_request(account,targeting_spec))


def multiple_interests_and(account):
    donald_trump_interest = "6003210792176"
    hillary_clinton_interest = "6003361373387"
    targeting_spec['age_min']=13
#     targeting_spec['age_max']=65    
#     targeting_spec['interests'] = [donald_trump_interest]    
#     targeting_spec['interests'] = [donald_trump_interest,hillary_clinton_interest] 
    targeting_spec['flexible_spec'] = [{'interests': [{"id":"6003210792176"}]},{'interests': [{"id":"6003361373387"}]}]  
    print('audience_size: %d' % make_request(account,targeting_spec))


def interest_and_behavior(account):
    donald_trump_interest = "6003210792176"
    targeting_spec['interests'] = [donald_trump_interest]
#     targeting_spec['flexible_spec'] = [{'behaviors': [{"id":"6018745176183","name":"African American (US)"}]}] 
    targeting_spec['flexible_spec'] = [{'behaviors': [{"id":"6003133212372","name":"Hispanic (US - All)"}]}]
    print('audience_size: %d' % make_request(account,targeting_spec))
    
    
def interests_and_demographics_and_race(account):
    donald_trump_interest = "6003210792176"
    targeting_spec['interests'] = [donald_trump_interest]
    targeting_spec['age_min']=18
    targeting_spec['age_max']=40
    targeting_spec['education_statuses'] = [9,11]
    targeting_spec['flexible_spec'] = [{'behaviors': [{"id":"6003133212372","name":"Hispanic (US - All)"}]}]   
    print('audience_size: %d' % make_request(account,targeting_spec))


def collection(account):
    cur_time = getCurrentTime()
    list_of_interests = ['all_%s' % cur_time]
    destfilename = '%s%s.gz' % (output_file_path, list_of_interests[0])
    output_file = gzip.open(destfilename, 'wt')
    writer = csv.writer(output_file)
    targeting_spec['age_min'] = 13
    results_row = ['all', 'BR', make_request(account,targeting_spec)]
    writer.writerow(results_row)
    output_file.flush()
    time.sleep(sleep_time)



    ################## EXPATS_ALL_FACEBOOK #################
    for expats in search_elements.expats_all_facebook:
        flexible_spec = []
        behaviors_expats = search_elements.expats_all_facebook[expats]
        flexible_spec.append({'behaviors': behaviors_expats})
        targeting_spec['flexible_spec'] = flexible_spec
        number = make_request(account,targeting_spec)
        results_row = ['expats', expats, number]
        writer.writerow(results_row)
        output_file.flush()
        time.sleep(sleep_time)
    del targeting_spec['flexible_spec']
    print('Finished expats_all_facebook')
    


    ################## EXPATS_NEW #####################
    for expats in search_elements.expats_new:
        flexible_spec = []
        behaviors_expats = search_elements.expats_new[expats]
        flexible_spec.append({'behaviors': behaviors_expats})
        targeting_spec['flexible_spec'] = flexible_spec
        number = make_request(account,targeting_spec)
        results_row = ['expats_grouped', expats, number]
        writer.writerow(results_row)
        output_file.flush()
        time.sleep(sleep_time)
    del targeting_spec['flexible_spec']
    print('Finished expats_new')



    ################ EDUCATIONAL_STATUSES ##############

    for field in search_elements.scholarities:
        targeting_spec['education_statuses'] = search_elements.scholarities[field]
        number = make_request(account,targeting_spec)
        results_row = ['scholarities', field, number]
        writer.writerow(results_row)
        output_file.flush()
        time.sleep(sleep_time)
    del targeting_spec['education_statuses']
    print('Finished education')


     ################ EDUCATIONAL_STATUSES_GROUPED ##############

    targeting_spec['education_statuses'] = [12]
    results_row = ['scholarities_grouped', 'unspecified', make_request(account, targeting_spec)]
    writer.writerow(results_row)
    output_file.flush()
    time.sleep(sleep_time)
    for field in search_elements.education_status_grouped_brazil:
        targeting_spec['education_statuses'] = search_elements.education_status_grouped_brazil2[field]
        number = make_request(account, targeting_spec)
        results_row = ['scholarities_grouped', field, number]
        writer.writerow(results_row)
        output_file.flush()
        time.sleep(sleep_time)
    del targeting_spec['education_statuses']
    print('Finished education_grouped')



    ############## RELATIONSHIP_STATUSES ##############

    for field in search_elements.relationship_statuses:
        targeting_spec['relationship_statuses'] = search_elements.relationship_statuses[field]
        number = make_request(account,targeting_spec)
        results_row = ['relationship', field, number]
        writer.writerow(results_row)
        output_file.flush()
        time.sleep(sleep_time)
    del targeting_spec['relationship_statuses']
    print('Finished relationships')



    ################ GENDER ################
    for gender in search_elements.genders:
        targeting_spec['genders'] = search_elements.genders[gender]
        number = make_request(account, targeting_spec)
        results_row = ['gender', gender, number]
        writer.writerow(results_row)
        output_file.flush()
        time.sleep(sleep_time)
    del targeting_spec['genders']
    print('Finished gender')


    ############## RELIGIONS ###############
    for religions in search_elements.religions:
        targeting_spec['interests'] = search_elements.religions[religions]
        number = make_request(account,targeting_spec)
        results_row = ['religions', religions, number]
        writer.writerow(results_row)
        output_file.flush()
        time.sleep(sleep_time)
    del targeting_spec['interests']
    print('Finished religions')


    ############## AGE_INTERVALS ###############
    for age in search_elements.age_intervals:
        if 'age_min' in targeting_spec:
            del targeting_spec['age_min']
        if 'age_max' in targeting_spec:
            del targeting_spec['age_max']
        targeting_spec['age_min'] = search_elements.age_intervals[age]['age_min']
        if (age != 'old_2' and age != 'educational_age' and age != 'all'):
            targeting_spec['age_max'] = search_elements.age_intervals[age]['age_max']
        number = make_request(account, targeting_spec)
        results_row = ['age_interval', age, number]
        writer.writerow(results_row)
        output_file.flush()
        time.sleep(sleep_time)
    if 'age_min' in targeting_spec:
        del targeting_spec['age_min']
    if 'age_max' in targeting_spec:
        del targeting_spec['age_max']
    print('Finished age intervals')


    
def main(argv):
    account = get_ad_account()

    collection(account)
#    multiple_interests_or(account)
#    multiple_interests_and(account)
#    interest_and_behavior(account)
#    interests_and_demographics_and_race(account)


if __name__ == "__main__":   
    main(sys.argv[1:])
