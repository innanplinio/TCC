# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"

from facebook_business.adobjects.targetingsearch import TargetingSearch
# from facebookads.adobjects.targetingsearch import TargetingSearch
# from facebookads.api import FacebookAdsApi
from facebook_business.api import FacebookAdsApi

# import facebookads.adobjects.targeting.Targeting

# https://developers.facebook.com/docs/marketing-api/targeting-search/

token = "EAAbPAyrnxo0BAEzRou8xgETD7tR4W1g4i0DQr5Nt4xEZCyuT3Akuc9SEMRGSKHG71t970Cr3FtdsDCxiOZAcJHWGWUXfERkK0vm03xqd1EOhTmZBaUuPMa9uxCQOF8iDKlMdd73gXzMrjj1RpQ6FFX90bCFZBC8ZD"
act_id = "140203616062598"
secret = "-"

def getFacebookAPI(token, act_id, secret):
    token, act_id, secret
    if secret != '-':
        api = FacebookAdsApi.init(access_token=token, app_secret=secret)
    else:
        api = FacebookAdsApi.init(access_token=token)
        
    return api

def getInterestIDFromText(api, text):

#     print text.decode('utf-8')
    params = {
        'q': text,        
        'type': 'adinterest',
        'limit': 1000,        
    }
    resp = TargetingSearch.search(params=params, api=api)
    return resp

def getSuggestions(api, element):
    
    params = {
        'type': TargetingSearch.TargetingSearchTypes.interest_suggestion,
        'interest_list': [element],
        'limit':1000
    }
    
    resp = TargetingSearch.search(params=params, api=api)
    return resp

def validateInterestIdByInterest(api, list_interests): 
    params = {
        'type': 'adinterestvalid',
#             'interest_list': list_interests,
        'interest_fbid_list': list_interests,
    }
    resp = TargetingSearch.search(params=params, api=api)  
    return resp

# def getLocationElement(api, location_name, location_type='country'):        
#     responses = getLocations(location_name,api, location_type=location_type)
#     return resopn
# #     print responses
def getLocationElement(api, element, location_type="country"):
    
#     type=adgeolocation&location_types=['region']:   
    params = {
        'q': element,
        'type': 'adgeolocation',
#         'location_types': ['city'],
#         'location_types': ['region'],
        'location_types': [location_type],
#         'countries': ['US']
#         'match_country_code' :True 
    }
    responses = TargetingSearch.search(params=params)
    return responses

####################################################################################
######################## searching for locations and their types
#################################################################################### 
def testSearchForLocationCode(api):
#     available location types: country, country_group, region, city,
#     resp = getLocationElement(api, "São Paulo", location_type="city")  
#     print '###### Searching for city - São Paulo #######' 
#     print resp
     
#     resp = getLocationElement(api, "Minas Gerais", location_type="region")
#     print '###### Searching for state/region - Minas Gerais #######'   
#     print resp 
# 
    resp = getLocationElement(api, "Italy", location_type="country") 
    print('###### Searching for country - Canada #######')
    print(resp)

####################################################################################
######################## validating interests for a given list
### interests may be excluded and must be validated from time to time
#################################################################################### 
def  testeValidateInterests(api):
    interests_list = ['6015760532183']
    resp = validateInterestIdByInterest(api, interests_list)
    for valid_element in resp: 
        print('******* valid *******')
        print(valid_element["id"])
           

####################################################################################
######################## searching for suggestions for a given text
#################################################################################### 
def testSuggestions(api):
    list_of_interests_to_search = ["moderate"]
    for interest in list_of_interests_to_search:
        print('**********  SUGGESTIONS SEARCHING FOR %s  **********'  % interest)
        search_result = getSuggestions(api, interest)
#         print search_result
        
        for element in search_result: 
            print("*********** NEW INTEREST *************")
            print("interest_id: %s" % element["id"])
            print("name: %s" % element["name"])
            print("audience_size: %s" % element["audience_size"])
#     getSuggestions("Web counter")
#     getSuggestionsBehaviors("school")    



####################################################################################
######################## validating interests
####################################################################################  
def testValidateInterest(facebook_api):
#     list_of_interests_to_validate = ["6002936693259", "6002839660079"]
#     list_of_interests_to_validate = ["6003184467302", "6003093235817", "6003331774171", "6003300230060"]
    list_of_interests_to_validate = ['6015760532183']
    params = {
        'type': 'adinterestvalid',
        'interest_fbid_list': list_of_interests_to_validate,
        'locale':'en_US'
    }
    resp = TargetingSearch.search(params=params, api=facebook_api)
    print(resp)
    
    

####################################################################################
######################## searching for interests for a given text
####################################################################################   
def testInterestSearch(api): 
#     list_of_interests_to_search = ["Ciro Gomes", "Feijoada", "Politics"]
    list_of_interests_to_search = ["liberal"]
    for interest in list_of_interests_to_search:
        print('**********  SEARCHING FOR %s  **********'  % interest)
        search_result = getInterestIDFromText(api, interest)
#         print search_result
         
        for element in search_result: 
            print("*********** NEW INTEREST *************")
            print("interest_id: %s" % element["id"])
            print("name: %s" % element["name"])
            print("audience_size: %s" % element["audience_size"])
            print("category: %s" % (element['disambiguation_category']  if 'disambiguation_category' in element else '-'))
            print("topic: %s" % element['topic']  if 'topic' in element else '-')
#             not all responses have a topic and category defined.  
#             print "topic: %s" % element["topic"] 
#             print "disambiguation_category: %s" % element["disambiguation_category"]     


def main():
        
    facebook_api = getFacebookAPI(token, act_id, secret)
#    testInterestSearch(facebook_api)
#    testeValidateInterests(facebook_api)
#    testSuggestions(facebook_api)-
#     testeValidateInterests(facebook_api)
#     testSearchForLocationCode(facebook_api)
#     testValidateInterest(facebook_api)
    

if __name__ == "__main__":
    main()    
