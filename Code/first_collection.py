# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

from facebookads.adobjects.adaccount import AdAccount
from facebookads.api import FacebookAdsApi
import sys


token = "-"
act_id = "-"
secret = "-"


# https://developers.facebook.com/docs/marketing-api/targeting-search/

targeting_spec = {
    "geo_locations": {"countries":["US"], 'location_types': ['recent', 'home'],},
#     "geo_locations": {"countries":["US"], 'location_types': ['home']},
    "publisher_platforms": ["facebook", "instagram"],
    "facebook_positions": ["feed", "instream_video"], #feed, right_hand_column
#     "device_platforms": ["mobile", "desktop"],
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

def get_ad_account():
    
    if secret != '-':
        FacebookAdsApi.init(access_token=token, app_secret=secret, api_version='v4.0')
    else:
        FacebookAdsApi.init(access_token=token, api_version='v4.0')
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
    print 'audience_size: %d' % make_request(account,targeting_spec)    


def multiple_interests_and(account):
    donald_trump_interest = "6003210792176"
    hillary_clinton_interest = "6003361373387"
    targeting_spec['age_min']=13
#     targeting_spec['age_max']=65    
#     targeting_spec['interests'] = [donald_trump_interest]    
#     targeting_spec['interests'] = [donald_trump_interest,hillary_clinton_interest] 
    targeting_spec['flexible_spec'] = [{'interests': [{"id":"6003210792176"}]},{'interests': [{"id":"6003361373387"}]}]  
    print 'audience_size: %d' % make_request(account,targeting_spec)


def interest_and_behavior(account):
    donald_trump_interest = "6003210792176"
    targeting_spec['interests'] = [donald_trump_interest]
#     targeting_spec['flexible_spec'] = [{'behaviors': [{"id":"6018745176183","name":"African American (US)"}]}] 
    targeting_spec['flexible_spec'] = [{'behaviors': [{"id":"6003133212372","name":"Hispanic (US - All)"}]}]
    print 'audience_size: %d' % make_request(account,targeting_spec)
    
    
def interests_and_demographics_and_race(account):
    donald_trump_interest = "6003210792176"
    targeting_spec['interests'] = [donald_trump_interest]
    targeting_spec['age_min']=18
    targeting_spec['age_max']=40
    targeting_spec['education_statuses'] = [9,11]
    targeting_spec['flexible_spec'] = [{'behaviors': [{"id":"6003133212372","name":"Hispanic (US - All)"}]}]   
    print 'audience_size: %d' % make_request(account,targeting_spec)    
    
def main(argv): 
    account = get_ad_account() 
    multiple_interests_or(account)   
#     multiple_interests_and(account)
#     interest_and_behavior(account)
#     interests_and_demographics_and_race(account)


if __name__ == "__main__":   
    main(sys.argv[1:])
