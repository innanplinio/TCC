# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

import gzip
import json
import os
import sys
import time
import matplotlib.pyplot as plt

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
        # print('line: %s' % line)
        #         continue
        count_number_of_lines += 1
        line_s = line.strip()
        if not line_s:
            continue
        elements = line_s.split(',')
        # print('elements: %s' % elements)
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

        interest_filename = '%s%s.gz' % (interests_path, interest)

        output_file_json = open('%s%s.json' % (interests_path, interest), 'w')
        print('\nPATH:')
        print(interest_filename)
        print('Data from %s' % interest)

        if os.path.isfile(interest_filename):
            try:
                input_file = gzip.open(interest_filename, mode='rt')
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
        # print(raw_values_dict)
        # print(percent_values_dict)

        output_file_json.write(
            json.dumps({'percent_values_dict': percent_values_dict, 'raw_values_dict': raw_values_dict}))
    #         if total_count >10:
    #             break

    output_file_json.close()
    print('\nERROR LOG:')
    print('total_count:%d' % total_count)
    print('absent_file_count:%d' % absent_file_count)
    print('under_1k_count:%d' % under_1k_count)
    print('error_in_file_count:%d' % error_in_file_count)


def pause():
    input("\nPress the <ENTER> key to continue...")
    print('\n')


#Atualiza arquivos dentro da pasta de Coletas
def processFolder(jsonfiles, gzfiles):
    jsonfiles.clear()
    gzfiles.clear()
    for entry in os.listdir('C:/Users/range/Documents/GitHub/TCC/Code/OutputUS/Coletas/'):
        if entry.find('gz') == -1:
            jsonfiles.append(entry[:-5])
        else:
            gzfiles.append(entry[:-3])
    jsonfiles.sort(reverse=True)
    gzfiles.sort(reverse=True)
    print_files = ''
    for x in range(1, len(jsonfiles)+1):
        print_files = print_files + '%d.%s\n' % (x, jsonfiles[x-1])
    return print_files


def processData(jsonfiles, gzfiles, interests_path):
    print('\n-----PROCESSING-----')
    processFolder(jsonfiles, gzfiles)
    # Start processing JSON file
    list_of_interests = gzfiles
    getInterestsDemographics(interests_path, list_of_interests)


def main(argv):

    interests_path = 'C:/Users/range/Documents/GitHub/TCC/Code/OutputUS/Coletas/'
    jsonfiles = []
    gzfiles = []
    processFolder(jsonfiles, gzfiles)


    # Primary Interests
    int_prim = ['education_status',
                'political_alignment',
                'relationship_status',
                'age_intervals',
                'racial_affinities',
                'expat',
                'gender']
    int_print = 'Primary Interest:'
    for entry in int_prim:
        int_print = int_print + '\n%d.%s' % (int_prim.index(entry) + 1, entry)
    int_print = int_print + '\n%d.Exit' % (len(int_prim) + 1)

    # Secondary interests
    int_sec = {'education_status': ['high_school',
                                    'UNDERGRAD',
                                    'ALUM',
                                    'HIGH_SCHOOL_GRAD',
                                    'SOME_COLLEGE',
                                    'ASSOCIATE_DEGREE',
                                    'IN_GRAD_SCHOOL',
                                    'SOME_GRAD_SCHOOL',
                                    'MASTER_DEGREE',
                                    'PROFESSIONAL_DEGREE',
                                    'DOCTORATE_DEGREE',
                                    'UNSPECIFIED',
                                    'SOME_HIGH_SCHOOL'],
               'political_alignment': ['conservative',
                                       'liberal',
                                       'moderate',
                                       'very_conservative',
                                       'very_liberal'],
               'relationship_status': ['single',
                                       'in_relationship',
                                       'engaged',
                                       'married',
                                       'civil_union',
                                       'domestic_partnership',
                                       'open_relationship',
                                       'complicated',
                                       'separated',
                                       'divorced',
                                       'widowed',
                                       'unspecified'],
               'age_intervals': ['adolescent',
                                 'young_1',
                                 'young_2',
                                 'mid_aged_1',
                                 'mid_aged_2',
                                 'old_1',
                                 'old_2'],
               'racial_affinities': ['african_american',
                                     'asian_american',
                                     'hispanic_all',
                                     'other'],
               'expat': ['expats',
                         'expats_mexico',
                         'expats_europe',
                         'expats_africa',
                         'expats_asian',
                         'expats_latin_america',
                         'expats_russia',
                         'expats_midle_east',
                         'expats_south_asia'],
               'gender': ['male',
                          'female']}

    # Aux to secondary interests
    print_sec = {1: '1.high_school'
                    '\n2.UNDERGRAD'
                    '\n3.ALUM'
                    '\n4.HIGH_SCHOOL_GRAD'
                    '\n5.SOME_COLLEGE'
                    '\n6.ASSOCIATE_DEGREE'
                    '\n7.IN_GRAD_SCHOOL'
                    '\n8.SOME_GRAD_SCHOOL'
                    '\n9.MASTER_DEGREE'
                    '\n10.PROFESSIONAL_DEGREE'
                    '\n11.DOCTORATE_DEGREE'
                    '\n12.UNSPECIFIED'
                    '\n13.SOME_HIGH_SCHOOL',
                 2: '1.conservative'
                    '\n2.liberal'
                    '\n3.moderate'
                    '\n4.very_conservative'
                    '\n5.very_liberal',
                 3: '1.single'
                    '\n2.in_relationship'
                    '\n3.engaged'
                    '\n4.married'
                    '\n5.civil_union'
                    '\n6.domestic_partnership'
                    '\n7.open_relationship'
                    '\n8.complicated'
                    '\n9.separated'
                    '\n10.divorced'
                    '\n11.widowed'
                    '\n12.unspecified',
                 4: '1.adolescent'
                    '\n2.young_1'
                    '\n3.young_2'
                    '\n4.mid_aged_1'
                    '\n5.mid_aged_2'
                    '\n6.old_1'
                    '\n7.old_2',
                 5: '1.african_american'
                    '\n2.asian_american'
                    '\n3.hispanic_all'
                    '\n4.other',
                 6: '1.expats'
                    '\n2.expats_mexico'
                    '\n3.expats_europe'
                    '\n4.expats_africa'
                    '\n5.expats_asian'
                    '\n6.expats_latin_america'
                    '\n7.expats_russia'
                    '\n8.expats_middle_east'
                    '\n9.expats_south_asia',
                 7: '1.male'
                    '\n2.female'}

    while 1:
        print('-----SELECT AN OPTION-----'
              '\n1.Process all collected data.'
              '\n2.Search by interest.'
              '\n3.Plot Charts.'
              '\n4.Exit')
        cond = int(input())
        if cond < 1 or cond > 3:
            break

        # Process collected data
        if cond == 1:
            processData(jsonfiles, gzfiles, interests_path)

        # Search by interest
        elif cond == 2:
            print_files = processFolder(jsonfiles, gzfiles)
            print('Choose the file to be searched:')
            print(print_files)

            # Opening JSON File
            json_interest_file = open('%s%s.json' % (interests_path, jsonfiles[int(input())-1]))
            values_dict = json.loads(json_interest_file.readline())
            while 1:
                # Print Menu
                print(int_print)
                menu = int(input())
                if menu > 7 or menu < 1:
                    break
                prim = int_prim[menu - 1]
                print('Select the secondary interest:')
                print(print_sec[menu])
                item = int(input())
                sec = int_sec[prim][item-1]
                print('Search for [%s, %s]\n' % (prim.upper(), sec.upper()))
                print('%s Percentage: %.2f' %
                      (sec, values_dict['percent_values_dict'][prim][sec] * 100))
                print('%s Raw: %d' %
                      (sec, values_dict['raw_values_dict'][prim][sec]))
                print('\nNew Search?'
                      '\n1.Yes'
                      '\n2.No')
                menu = int(input())
                if menu == 1:
                    print()
                else:
                    break

        # Plot Charts
        elif cond == 3:
            processData(jsonfiles, gzfiles, interests_path)
            xaxis = []
            yaxis = {}
            print('\n-----SELECT AN OPTION-----')
            print(int_print)
            n = int(input())
            # Exit
            if n < 1 or n > 7:
                break

            print('\nRaw or Percent'
                  '\n1.Raw'
                  '\n2.Percent')
            rp = int(input())
            if rp == 1:
                value = 'raw_values_dict'
                legend = 'Raw Values'
            elif rp == 2:
                value = 'percent_values_dict'
                legend = 'Percent Values'
            else:
                break

            jsonfiles.reverse()
            for entry in jsonfiles:
                json_interest_file = open('%s%s.json' % (interests_path, entry))
                xaxis.append('%s/%s/%s' % (entry[12:14], entry[9:11], entry[4:8]))
                values_dict = json.loads(json_interest_file.readline())

                for j in range(len(int_sec[int_prim[n-1]])):
                    if j not in yaxis:
                        yaxis[j] = []
                    yaxis[j].append(round(values_dict[value][int_prim[n-1]][int_sec[int_prim[n-1]][j-1]], 2))

            plt.text(xaxis[0],
                     yaxis[0][0],
                     "%d" % 21234)

            for i in range(len(int_sec[int_prim[n-1]])):
                for j in range(len(xaxis)):
                    print(yaxis[i][j])
                    plt.text(xaxis[j],
                             yaxis[i][j],
                             "%d" % yaxis[i][j])
                plt.plot(xaxis,
                         yaxis[i],
                         label=int_sec[int_prim[n-1]][i-1])
                plt.scatter(xaxis,
                            yaxis[i])
                print("%s: " % int_sec[int_prim[n-1]][i-1], yaxis[i])
            print(xaxis)

            plt.xlabel('Collection Data :')
            plt.ylabel(legend)
            plt.title(int_prim[n-1])
            plt.legend()
            plt.show()
            jsonfiles.reverse()

        pause()

    print('TCC FINALIZADO COM SUCESSO')
    pause()

    #   Plotting graphics based on interests
    #   Some tests, dont bother.

    #plt.plot(['jan', 'fev', 'abr', 'mai', 'jun'], [21000, 14444, 30000, 10000, 15000], label='conservative')

    #plt.xlabel('Collection Data :')
    #plt.ylabel('Raw Values')
    #plt.title("Interests")
    #plt.legend()
    #plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
