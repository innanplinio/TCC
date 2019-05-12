# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

import gzip
import json
import os
import sys
import time

import facebook_attributes as search_elements

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

def getAudienceDicts(input_file):
    raw_values_dict = {}
    percent_values_dict = {}
    total_amount = 0
    total_expats = 0
    count_number_of_lines = 0
    zero_facebook_value = 1000
    for line in input_file:
        #print('line: %s' % line)
        #         continue
        count_number_of_lines += 1
        line_s = line.strip()
        if not line_s:
            continue
        elements = line_s.split(',')
        #print('elements: %s' % elements)
        cat = elements[0]
        subcat = elements[1]
        amount = int(elements[2])
        if cat == 'all':
            total_amount = 0 if amount == zero_facebook_value else amount
        if cat == 'expat' and subcat == 'expats':
            total_expats = 0 if amount == zero_facebook_value else amount
        if cat in raw_values_dict:
            categorie_dict = raw_values_dict[cat]
        else:
            categorie_dict = {}
        categorie_dict[subcat] = 0 if amount == zero_facebook_value else amount
        raw_values_dict[cat] = categorie_dict

    #     the total interest is only 1000. Percentages will not be valid
    if 'all' in raw_values_dict:
        all_value = raw_values_dict['all']['all']
    else:
        raw_values_dict['all'] = {'all': 0}
        all_value = -1
    #         print raw_values_dict
    if all_value == 0 or all_value == -1:
        return raw_values_dict, None
    # getting values for grouped categories
    # education_status
    if 'education_status' in raw_values_dict:
        group_category_dict = {}
        for grouped_cat in search_elements.education_status_grouped:
            list_of_subcategories = search_elements.education_status_grouped[grouped_cat]
            group_category_dict[grouped_cat] = 0
            for subcategory in list_of_subcategories:
                #                 print grouped_cat
                #                 print subcategory
                group_category_dict[grouped_cat] += raw_values_dict['education_status'][subcategory]
        raw_values_dict['education_status_grouped'] = group_category_dict

        # education_status grouped 2
        group_category_dict = {}
        for grouped_cat in search_elements.education_status_grouped_2:
            list_of_subcategories = search_elements.education_status_grouped_2[grouped_cat]
            group_category_dict[grouped_cat] = 0
            for subcategory in list_of_subcategories:
                #                 print grouped_cat
                #                 print subcategory
                group_category_dict[grouped_cat] += raw_values_dict['education_status'][subcategory]
        raw_values_dict['education_status_grouped_2'] = group_category_dict

    for category in raw_values_dict:
        if category == 'all':
            continue
        categorie_dict = raw_values_dict[category]
        total_audience_amount = 0
        percent_category_dict = {}
        for subcat in categorie_dict:
            if subcat != 'UNSPECIFIED' and subcat != 'expats':
                #                     unspecified_audience=categorie_dict[subcat]
                #                 else:
                total_audience_amount += categorie_dict[subcat]
        for subcat in categorie_dict:
            if subcat == 'UNSPECIFIED':
                if categorie_dict[subcat] + total_audience_amount == 0:
                    percent_category_dict[subcat] = 0
                else:
                    percent_category_dict[subcat] = float(categorie_dict[subcat]) / (
                            categorie_dict[subcat] + total_audience_amount)
            elif subcat == 'expats':
                if total_amount == 0:
                    percent_category_dict[subcat] = 0
                else:
                    percent_category_dict[subcat] = float(categorie_dict[subcat]) / total_amount
            elif 'expats_' in subcat:
                if total_expats == 0:
                    percent_category_dict[subcat] = 0
                else:
                    percent_category_dict[subcat] = float(categorie_dict[subcat]) / total_expats
            else:
                if total_audience_amount == 0:
                    percent_category_dict[subcat] = 0
                else:
                    percent_category_dict[subcat] = float(categorie_dict[subcat]) / total_audience_amount
        percent_values_dict[category] = percent_category_dict

    #         checking the gender category
    if 'gender' in percent_values_dict:
        if percent_values_dict['gender']['male'] == 1 or percent_values_dict['gender']['female'] == 1:
            high_percent_group = 'male' if percent_values_dict['gender']['male'] == 1 else 'female'
            if raw_values_dict['all']['all'] > percent_values_dict['gender'][high_percent_group]:
                #                 print '%s - %s' % ('gender', high_percent_group)
                #                 print 'male: %.3f - female: %.3f' % (percent_values_dict['gender']['male'],percent_values_dict['gender']['female'])
                #                 print 'all: %d - male: %d - female: %d' % (raw_values_dict['all']['all'], raw_values_dict['gender']['male'],raw_values_dict['gender']['female'])
                #                 print interest_filename
                low_percent_gender = 'male' if high_percent_group == 'female' else 'female'
                new_high_value = float(raw_values_dict['gender'][high_percent_group]) / raw_values_dict['all']['all']
                new_low_value = float(raw_values_dict['all']['all'] - raw_values_dict['gender'][high_percent_group]) / \
                                raw_values_dict['all']['all']
                percent_values_dict['gender'][high_percent_group] = new_high_value
                percent_values_dict['gender'][low_percent_gender] = new_low_value
            #                 print '%s: %.3f - %s: %.3f' % (low_percent_gender, new_low_value, high_percent_group, new_high_value)
    #                 sys.exit()
    #     print json.dumps(raw_values_dict)
    #     print json.dumps(percent_values_dict)
    return raw_values_dict, percent_values_dict


def getInterestsDemographics(interests_path, list_of_interests):
    total_count = 0
    absent_file_count = 0
    under_1k_count = 0
    file_without_lines_count = 0
    error_in_file_count = 0
    calc_error_count = 0
    count_demographic_file_not_found = 0

    for interest in list_of_interests:

        total_count += 1

        print('data from %s' % interest)

        interest_filename = '%s%s.gz' % (interests_path, interest)

        output_file_json = open('%s%s.json' % (interests_path, interest), 'w')
        print('\nPATH:')
        print(interest_filename)

        if os.path.isfile(interest_filename):
            try:
                input_file = gzip.open(interest_filename,mode='rt')
            #                 print input_file.readline()
            except:
                error_in_file_count += 1
        else:
            absent_file_count += 1
            continue

        raw_values_dict, percent_values_dict = getAudienceDicts(input_file)

        all_value = raw_values_dict['all']['all']

        if all_value == 0:
            under_1k_count += 1
            continue
        elif all_value == -1:
            file_without_lines_count += 1
            continue

        #         break

        if raw_values_dict is None or percent_values_dict is None:
            #                log_file.write('%s\t%s\n' %(interest_id, 'demographic_file_not_found'))
            count_demographic_file_not_found += 1
            print('demographic info not found')
            #             calc_error_count+=1
            continue
        #print(raw_values_dict)
        #print(percent_values_dict)

        output_file_json.write(json.dumps({'percent_values_dict':percent_values_dict, 'raw_values_dict':raw_values_dict}))
    #         if total_count >10:
    #             break

    output_file_json.close()
    print('\nERROR LOG:')
    print('total_count:%d' % total_count)
    print('absent_file_count:%d' % absent_file_count)
    print('under_1k_count:%d' % under_1k_count)
    print('error_in_file_count:%d' % error_in_file_count)

def main(argv):
    interests_path = 'C:/Users/range/Documents/GitHub/TCC/Code/OutputUS/'
    filename = 'all_2019-05-12--15-04-13'
    #     para reunir os dados demográficos dos eua inserir na lista abaixo o nome do arquivo que contem all_ concatenado com
    #     dia e hora da coleta all_<data_hora_coleta>
#    list_of_interests = [filename]
#    getInterestsDemographics(interests_path, list_of_interests)

#     opening json files
    json_interest_file = open('%s%s.json' % (interests_path, filename))
    values_dict = json.loads(json_interest_file.readline())
    print('\n')
    print('male percentage: %.2f' % (values_dict['percent_values_dict']['gender']['female']*100))
#    print('male raw: %d' % (values_dict['raw_values_dict']['gender']['male']))
#    print('conservative percentage: %.2f' % (values_dict['percent_values_dict']['political_alignment']['conservative']*100))


if __name__ == "__main__":
    main(sys.argv[1:])
