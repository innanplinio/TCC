# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"


targeting_spec = {
    "geo_locations": {"countries":["US"]},
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


countries={}


dictionaries ={
   "political_alignment":['conservative', 'very_conservative', 'moderate', 'liberal', 'very_liberal']
}


expats_all_facebook={
    'expats_india': [{'id':'6016916298983', 'name':'Expats (India)'}],
    'expats_kenya': [{'id':'6018796980983', 'name':'Expats (Kenya)'}],
    'expats_nigeria': [{'id':'6018797004183', 'name':'Expats (Nigeria)'}],
    'expats_cameroon': [{'id':'6018797036783', 'name':'Expats (Cameroon)'}],
    'expats_philippines': [{'id':'6018797091183', 'name':'Expats (Philippines)'}],
    'expats_cuba': [{'id':'6018797127383', 'name':'Expats (Cuba)'}],
    'expats_ethiopia': [{'id':'6018797165983', 'name':'Expats (Ethiopia)'}],
    'expats_haiti': [{'id':'6018797373783', 'name':'Expats (Haiti)'}],
    'expats_spain': [{'id':'6019366943583', 'name':'Expats (Spain)'}],
    'expats_france': [{'id':'6019367014383', 'name':'Expats (France)'}],
    'expats_germany': [{'id':'6019367052983', 'name':'Expats (Germany)'}],
    'expats_switzerland': [{'id':'6019377644783', 'name':'Expats (Switzerland)'}],
    'expats_united_states': [{'id':'6019396649183', 'name':'Expats (United States)'}],
    'expats_poland': [{'id':'6019396657183', 'name':'Expats (Poland)'}],
    'expats_italy': [{'id':'6019396654583', 'name':'Expats (Italy)'}],
    'expats_ireland': [{'id':'6019396650783', 'name':'Expats (Ireland)'}],
    'expats_hungary': [{'id':'6019396638383', 'name':'Expats (Hungary)'}],
    'expats_canada': [{'id':'6019396764183', 'name':'Expats (Canada)'}],
    'expats_china': [{'id':'6019452369983', 'name':'Expats (China)'}],
    'expats_puerto_rico': [{'id':'6019520122583', 'name':'Expats (Puerto Rico)'}],
    'expats_brazil': [{'id':'6019564340583', 'name':'Expats (Brazil)'}],
    'expats_indonesia': [{'id':'6019564344583', 'name':'Expats (Indonesia)'}],
    'expats_south_africa': [{'id':'6019564383383', 'name':'Expats (South Africa)'}],
    'expats_zimbabwe': [{'id':'6019673233983', 'name':'Expats (Zimbabwe)'}],
    'expats_ghana': [{'id':'6019673448383', 'name':'Expats (Ghana)'}],
    'expats_uganda': [{'id':'6019673501783', 'name':'Expats (Uganda)'}],
    'expats_colombia': [{'id':'6019673525983', 'name':'Expats (Colombia)'}],
    'expats_dominican_republic': [{'id':'6019673762183', 'name':'Expats (Dominican Republic)'}],
    'expats_el_salvador': [{'id':'6019673777983', 'name':'Expats (El Salvador)'}],
    'expats_guatemala': [{'id':'6019673808383', 'name':'Expats (Guatemala)'}],
    'expats_united_kingdom': [{'id':'6021354152983', 'name':'Expats (United Kingdom)'}],
    'expats_australia': [{'id':'6021354857783', 'name':'Expats (Australia)'}],
    'expats_portugal': [{'id':'6021354882783', 'name':'Expats (Portugal)'}],
    'expats_estonia': [{'id':'6023287351383', 'name':'Expats (Estonia)'}],
    'expats_norway': [{'id':'6023287459983', 'name':'Expats (Norway)'}],
    'expats_denmark': [{'id':'6023287455983', 'name':'Expats (Denmark)'}],
    'expats_czech_republic': [{'id':'6023287438783', 'name':'Expats (Czech Republic)'}],
    'expats_sweden': [{'id':'6023287397383', 'name':'Expats (Sweden)'}],
    'expats_netherlands': [{'id':'6023287393783', 'name':'Expats (Netherlands)'}],
    'expats_bangladesh': [{'id':'6023356562783', 'name':'Expats (Bangladesh)'}],
    'expats_tanzania': [{'id':'6023356926183', 'name':'Expats (Tanzania)'}],
    'expats_nepal': [{'id':'6023356955383', 'name':'Expats (Nepal)'}],
    'expats_jamaica': [{'id':'6023356956983', 'name':'Expats (Jamaica)'}],
    'expats_thailand': [{'id':'6023356966183', 'name':'Expats (Thailand)'}],
    'expats_sierra_leone': [{'id':'6023356986383', 'name':'Expats (Sierra Leone)'}],
    'expats_senegal': [{'id':'6023357000583', 'name':'Expats (Senegal)'}],
    'expats_ivory_coast': [{'id':'6023422105983', 'name':'Expats (Ivory Coast)'}],
    'expats_sri_lanka': [{'id':'6023516315983', 'name':'Expats (Sri Lanka)'}],
    'expats_morocco': [{'id':'6023516338783', 'name':'Expats (Morocco)'}],
    'expats_uae': [{'id':'6023516430783', 'name':'Expats (UAE)'}],
    'expats_new_zealand': [{'id':'6023516368383', 'name':'Expats (New Zealand)'}],
    'expats_congo_drc': [{'id':'6023516373983', 'name':'Expats (Congo DRC)'}],
    'expats_singapore': [{'id':'6023516403783', 'name':'Expats (Singapore)'}],
    'expats_united_states': [{'id':'6023620475783', 'name':'Expats (United States)'}],
    'expats_austria': [{'id':'6023675997383', 'name':'Expats (Austria)'}],
    'expats_cyprus': [{'id':'6023676002183', 'name':'Expats (Cyprus)'}],
    'expats_finland': [{'id':'6068209522983', 'name':'Expats (Finland)'}],
    'expats_greece': [{'id':'6023676017583', 'name':'Expats (Greece)'}],
    'expats_hong_kong': [{'id':'6023676022783', 'name':'Expats (Hong Kong)'}],
    'expats_japan': [{'id':'6023676028783', 'name':'Expats (Japan)'}],
    'expats_latvia': [{'id':'6068613839383', 'name':'Expats (Latvia)'}],
    'expats_lithuania': [{'id':'6023676039183', 'name':'Expats (Lithuania)'}],
    'expats_luxembourg': [{'id':'6023676044383', 'name':'Expats (Luxembourg)'}],
    'expats_malta': [{'id':'6023676045583', 'name':'Expats (Malta)'}],
    'expats_monaco': [{'id':'6023676048183', 'name':'Expats (Monaco)'}],
    'expats_slovakia': [{'id':'6023676055383', 'name':'Expats (Slovakia)'}],
    'expats_slovenia': [{'id':'6023676060183', 'name':'Expats (Slovenia)'}],
    'expats_mexico': [{'id':'6023676072183', 'name':'Expats (Mexico)'}],
    'expats_argentina': [{'id':'6025000826583', 'name':'Expats (Argentina)'}],
    'expats_israel': [{'id':'6025000823583', 'name':'Expats (Israel)'}],
    'expats_russia': [{'id':'6025000815983', 'name':'Expats (Russia)'}],
    'expats_ksa': [{'id':'6025000813183', 'name':'Expats (KSA)'}],
    'expats_chile': [{'id':'6025054896983', 'name':'Expats (Chile)'}],
    'expats_rwanda': [{'id':'6025670492783', 'name':'Expats (Rwanda)'}],
    'expats_venezuela': [{'id':'6026404871583', 'name':'Expats (Venezuela)'}],
    'expats_malaysia': [{'id':'6027147160983', 'name':'Expats (Malaysia)'}],
    'expats_romania': [{'id':'6027148962983', 'name':'Expats (Romania)'}],
    'expats_south_korea': [{'id':'6027148973583', 'name':'Expats (South Korea)'}],
    'expats_serbia': [{'id':'6027149004983', 'name':'Expats (Serbia)'}],
    'expats_vietnam': [{'id':'6027149006383', 'name':'Expats (Vietnam)'}],
    'expats_peru': [{'id':'6027149008183', 'name':'Expats (Peru)'}],
    'expats_belgium': [{'id':'6043702804583', 'name':'Expats (Belgium)'}],
    'expats_zambia': [{'id':'6047219032183', 'name':'Expats (Zambia)'}],
    'expats_honduras': [{'id':'6059793664583', 'name':'Expats (Honduras)'}],
    'expats_lebanon': [{'id':'6068844014183', 'name':'Expats (Lebanon)'}],
    'expats_jordan': [{'id':'6068843912183', 'name':'Expats (Jordan)'}],
    'expats_algeria': [{'id':'6071248932383', 'name':'Expats (Algeria)'}],
    'expats_nicaragua': [{'id':'6071248894383', 'name':'Expats (Nicaragua)'}],
    'expats_kuwait': [{'id':'6071248981583', 'name':'Expats (Kuwait)'}],
    'expats_qatar': [{'id':'6071249058983', 'name':'Expats (Qatar)'}],}

expats={
#     'all': '',
    'expats': {"id":"6015559470583","name":"Expats (All)"},
    'expats_mexico': {"id":"6023676072183","name":"Expats (Mexico)"},
    'expats_china': {"id":"6019452369983","name":"Expats (China)"},
    'expats_india': {"id":"6016916298983","name":"Expats (India)"},
    'expats_philippines': {"id":"6018797091183","name":"Expats (Philippines)"},
    'expats_el_salvador': {"id":"6019673777983","name":"Expats (El Salvador)"},
    'expats_vietnam': {"id":"6027149006383","name":"Expats (Vietnam)"},
    'expats_cuba': {"id":"6018797127383","name":"Expats (Cuba)"},
    'expats_dominican_republic': {"id":"6019673762183","name":"Expats (Dominican Republic)"},
    'expats_south_korea': {"id":"6027148973583","name":"Expats (South Korea)"},
    'expats_guatemala': {"id":"6019673808383","name":"Expats (Guatemala)"} 
} 

expats_new={
#     'all': '',
    'expats': [{"id":"6015559470583","name":"Expats (All)"}],
    'expats_mexico': [{"id":"6023676072183","name":"Expats (Mexico)"}],

    'expats_europe': [{"id":"6019396764183","name":"Expats (Canada)"}, {"id":"6019367052983","name":"Expats (Germany)"}, {"id":"6019396657183","name":"Expats (Poland) "}, {"id":"6021354152983","name":"Expats (UK)"},
        {"id":"6021354857783","name":"Expats (Australia)"}, {"id":"6019396654583","name":"Expats (Italy)"}, {"id":"6019367014383","name":"Expats (France)"},{"id":"6027148962983","name":"Expats (Romania)"}, 
        {"id":"6021354882783","name":"Expats (Portugal)"},{"id":"6023676017583","name":"Expats (Greece)"},{"id":"6019396650783","name":"Expats (Ireland)"},{"id":"6019366943583","name":"Expats (Spain)"}],
    
    'expats_africa': [{"id":"6018797004183","name":"Expats (Nigeria)"},{"id":"6019564383383","name":"Expats (South Africa)"},{"id":"6018797165983","name":"Expats (Ethiopia)"},
        {"id":"6019673448383","name":"Expats (Ghana)"},{"id":"6018796980983","name":"Expats (Kenya)"}],

    

    'expats_asian': [{"id":"6018797091183","name":"Expats (Philippines)"}, {"id":"6027149006383","name":"Expats (Vietnam)"}, {"id":"6027148973583","name":"Expats (South Korea)"}, 
        {"id":"6019452369983","name":"Expats (China)"},{"id":"6023676028783","name":"Expats (Japan)"}],

    'expats_latin_america': [{"id":"6019673808383","name":"Expats (Guatemala)"},{"id":"6019673777983","name":"Expats (El Salvador)"}, {"id":"6019673762183","name":"Expats (Dominican Republic)"},
        {"id":"6018797127383","name":"Expats (Cuba)"}, {"id":"6019673525983","name":"Expats (Colombia)"}, {"id":"6018797373783","name":"Expats (Haiti)"}, {"id":"6059793664583","name":"Expats (Honduras)"},
        {"id":"6027149008183","name":"Expats (Peru)"},{"id":"6019564340583","name":"Expats (Brazil)"},{"id":"6026404871583","name":"Expats (Venezuela)"}, {"id":"6025000826583","name":"Expats (Argentina)"}],
            
    'expats_russia':[{"id":"6025000815983","name":"Expats (Russia)"}],
    
    'expats_midle_east': [{"id":"6023516338783","name":"Expats (Morocco)"},{"id":"6071248932383","name":"Expats (Algeria)"},{"id":"6071248981583","name":"Expats (Kuwait)"},{"id":"6068843912183","name":"Expats (Jordan)"},{"id":"6068844014183","name":"Expats (Lebanon)"}, {"id":"6025000823583","name":"Expats (Israel)"}, {"id":"6025000813183","name":"Expats (Saudi Arabia)"}],

    'expats_south_asia': [{"id":"6023516315983","name":"Expats (Sri Lanka)"},{"id":"6016916298983","name":"Expats (India)"}, {"id":"6023356562783","name":"Expats (Bangladesh)"}, {"id":"6023356955383","name":"Expats (Nepal)"}],
}



consumer_habits = {
#         'all': [],                         
    'mid_low_value': [{"id":"6038940913482","name":"(D) Afinidade para bens de médio/baixo valor"}],
    'mid_value': [{"id":"6038940911882","name":"(C) Afinidade para bens de médio valor"}],   
    'mid_high_value': [{"id":"6038940911682","name":"(B) Afinidade para bens de médio/alto valor "}],
    'high_value':[ {"id":"6038940910682","name":"(A) Afinidade para bens de alto valor"}],
 
}


# absent: ecuador, jamaica,iran, pakistan, ukraine, guyana, nicaragua, thailand, trinida and tobago, egypt, iraq, laos, cambodia, turkey, lebanon,myanmar
# 1: single, 2: in_relationship,3: married,4: engaged,6: not specified,7: in a civil union,8: in a domestic partnership,9: In an open relationship
# 10: It's complicated, 11: Separated, 12: Divorced,13: Widowed  
#     https://developers.facebook.com/docs/marketing-api/buying-api/targeting  
#  https://www.facebook.com/ads/audience-insights/people?act=391957370816504&age=18-&country=US 
relationship_statuses = {
#         'all':[],
    'single' :[1], # ** audience insights does not include divorced, widowed, etc
    'in_relationship':[2],
    'engaged': [4],         
    'married':[3], 
    'civil_union': [7],
    'domestic_partnership':[8],
    'open_relationship': [9],
    'complicated': [10],
    'separated': [11],
    'divorced': [12],
    'widowed': [13],   
    'unspecified':[6]             
#         old usage
#         'single' :[1,11,12,13],
#         'dating' :[2, 4],                     
#         'married':[3, 7, 8],
#         'divorced_widowed':[12,13],
#         'other': [9,10],
}
       
# (i) Adolescent (13 – 19 years),
# (ii) Young (‘Early adulthood’ in Erikson’s parlance) (20 – 39 years)
# (iii) Mid-aged (‘Adulthood’) (40 – 64 years)
# (iv) Old (‘Maturity’) (65 years and above)
age_intervals = {
#         'all':{'age_min': 18}, 
# adapted              
    'adolescent' :{'age_min': 13, 'age_max': 17},
    'young_1' :{'age_min': 18, 'age_max': 24},
    'young_2' :{'age_min': 25, 'age_max': 34},
    'mid_aged_1' :{'age_min': 35, 'age_max': 44},
    'mid_aged_2' :{'age_min': 45, 'age_max': 54},        
    'old_1': {'age_min': 55, 'age_max': 64},
    'old_2': {'age_min': 65}                 
#         'adolescent' :{'age_min': 13, 'age_max': 19},
#         'young' :{'age_min': 20, 'age_max': 39},                  
}




# genders go into "genders" in api_params
genders = {
#     "all": [],            
    'male': [1],
    'female': [2]
}

#     https://developers.facebook.com/docs/marketing-api/targeting-specs - education_statuses
# 1: HIGH_SCHOOL,2: UNDERGRAD,3: ALUM,4: HIGH_SCHOOL_GRAD,5: SOME_COLLEGE,6: ASSOCIATE_DEGREE,7: IN_GRAD_SCHOOL,8: SOME_GRAD_SCHOOL
# 9: MASTER_DEGREE,10: PROFESSIONAL_DEGREE,11: DOCTORATE_DEGREE,12: UNSPECIFIED,13: SOME_HIGH_SCHOOL,
scholarities = {
#         'all':[], 
            "high_school":[1],            
            "UNDERGRAD":[2],
            "ALUM":[3],
            "HIGH_SCHOOL_GRAD":[4],            
            "SOME_COLLEGE":[5],
            "ASSOCIATE_DEGREE":[6],                        
            "IN_GRAD_SCHOOL":[7],
            'SOME_GRAD_SCHOOL':[8],
            'MASTER_DEGREE':[9],
            "PROFESSIONAL_DEGREE":[10],                        
            "DOCTORATE_DEGREE":[11],
            'UNSPECIFIED':[12],
            'SOME_HIGH_SCHOOL':[13],                                      
}

# scholarities_grouped = {
education_status_grouped = {                                             
    'college':['UNDERGRAD','ALUM','SOME_COLLEGE','ASSOCIATE_DEGREE'],
    "high_school":['high_school','HIGH_SCHOOL_GRAD','SOME_HIGH_SCHOOL'],
    'grad_school':['IN_GRAD_SCHOOL','SOME_GRAD_SCHOOL','MASTER_DEGREE','PROFESSIONAL_DEGREE','DOCTORATE_DEGREE'],                  
}

education_status_grouped_brazil = {    
    "incomplete_high_school":['high_school','SOME_HIGH_SCHOOL'],                                                  
    "high_school":['HIGH_SCHOOL_GRAD','UNDERGRAD', 'SOME_COLLEGE'],
    'college':['IN_GRAD_SCHOOL','SOME_GRAD_SCHOOL','MASTER_DEGREE','PROFESSIONAL_DEGREE','DOCTORATE_DEGREE','ALUM','ASSOCIATE_DEGREE'],               
}

education_status_grouped_2 = {  

#     UNDERGRAD = in college = 8.2 Mi - Na faculdade
#       ALUM = College grad = 72 Mi - formação universitaria
#     SOME_COLLEGE =  some college - 9.6 Mi - Alguma faculdade
# e - Graduação profissional - 1.1 Mi

# ASSOCIATE_DEGREE - diploma de curso tecnico - indisponível 


# HIGH_SCHOOL_GRAD = high school grad = 40 Mi - concluiu o ensino medio
# high school = In high school = 2.5 Mi - No ensino medio
# SOME_HIGH_SCHOOL = some high school 4.8 Mi - ensino medio incompleto

# 'IN_GRAD_SCHOOL' = studying grad school - 1.1 Mi

# SOME_GRAD_SCHOOL = some grad school                                     
    "incomplete_high_school":['high_school','SOME_HIGH_SCHOOL'],
    "high_school":['HIGH_SCHOOL_GRAD'],
    'in_college':['UNDERGRAD', 'SOME_COLLEGE'],    
    'college':['ALUM','ASSOCIATE_DEGREE'],
    'grad_school':['SOME_GRAD_SCHOOL','MASTER_DEGREE','DOCTORATE_DEGREE', 'PROFESSIONAL_DEGREE', 'IN_GRAD_SCHOOL'],                  
    'UNSPECIFIED':['UNSPECIFIED']
}



racial_affinities = {
#         'all': [],                         
    'african_american': {"id":"6018745176183","name":"African American (US)"},
    'asian_american': {"id":"6021722613183","name":"Asian American (US)"},
    'hispanic_all': {"id":"6003133212372","name":"Hispanic (US - All)"},
    'other': 'dealt with specially' #excluded
    # this goes into behaviors in exclusions     
}

caucasian_spec = {
    "behaviors":[
        {"id":"6018745176183","name":"African American (US)"},
        {"id":"6021722613183","name":"Asian American (US)"},
        {"id":"6003133212372","name":"Hispanic (US - All)"}
    ]
} 
# people's political leaning. goes into politics in flexible_spec
political_alignment = {
#     "all": [],
    "conservative": [{"id":"6015760532183","name":"US politics (conservative)"}],
    "liberal": [{"id":"6015760027783","name":"US politics (liberal)"}],
    "moderate": [{"id":"6015760036783","name":"US politics (moderate)"}],
    "very_conservative": [{"id":"6015762142783","name":"US politics (very conservative)"}],
    "very_liberal": [{"id":"6015759997983","name":"US politics (very liberal)"}]  
            
}

# People whose activity on Facebook suggests that they're more likely to engage with/distribute liberal political content 
political_engagement ={
    "conservative": [{"id":"6029977111383","name":"US politics engagement (conservative)"}],
    "liberal": [{"id":"6031978535383","name":"US politics engagement (liberal)"}],
    "moderate": [{"id":"6031978554983","name":"US politics engagement (moderate)"}],
}
    

income_levels={
#         'all': [],
#         'all': [],
    '30k_to_40k':[{"id": "6018510070532","name": "$30,000 - $40,000"}],                 
    '40k_to_50k':[{"id": "6018510087532","name": "$40,000 - $50,000"}],
    '50k_to_75k':[{"id": "6018510122932","name": "$50,000 - $75,000"}],        
    '75k_to_100k':[{"id": "6018510100332","name": "$75,000 - $100,000"}],
    '100k_to_125k':[{"id": "6018510083132","name": "$100,000 - $125,000"}],
    '125k_to_150k':[{"id": "6017897162332","name": "$125,000 - $150,000"}],
    '150k_to_250k':[{"id": "6017897374132","name": "$150,000 - $250,000"}],
    '250k_to_350k':[{"id": "6017897397132","name": "$250,000 - $350,000"}], 
    '350k_to_500k':[{"id": "6017897416732","name": "$350,000 - $500,000"}],
    'over_500k':[{"id": "6017897439932","name": "Over $500,000"}]                                                            
}
           