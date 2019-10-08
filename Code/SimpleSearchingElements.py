# -*- coding: utf-8 -*-
__author__ = "Filipe Ribeiro"



# Number of requests done in 12 hours with one account - near 10.000
# first test 2×7×5×3×5×5×6×5×6 = 945000 for each domain - unfeasable

# search reduced: status, scholarity, income, age 
# after reducing  2×4×4×3×4×4×4×4×3 = 73728 (still high)

# Targeting spec template to be used
targeting_spec = {
#     "geo_locations": {"countries":["US"]},
#     new york state
#     "geo_locations": {"regions":[{"key":3875,"name":"New York"}]},
#     new york city
    "geo_locations": {"cities":[{"key":"2490299", "name": "New York", "region": "New York", "radius":15, "distance_unit":"mile"}]},
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

# brazilian_states={
#     'rio_de_janeiro': [{"key":454,"name":"Rio de Janeiro"}],
#     'rio_grande_do_norte': [{"key":455,"name":"Rio Grande do Norte"}],    
#     'rio_grande_do_sul': [{"key":456,"name":"Rio Grande do Sul"}],    
#     }

brazilian_states={
"acre": [{"key":"438","name":"Acre"}],
"alagoas": [{"key":"439","name":"Alagoas"}],
"amapa": [{"key":"440","name":"Amapá"}],
"amazonas": [{"key":"441","name":"Amazonas"}],
"bahia": [{"key":"442","name":"Bahia"}],
"ceara": [{"key":"443","name":"Ceará"}],
"distrito_federal": [{"key":"444","name":"Distrito Federal"}],
"espirito_santo": [{"key":"445","name":"Espírito Santo"}],
"goias": [{"key":"462","name":"Goiás"}],
"maranhao": [{"key":"447","name":"Maranhão"}],
"mato_grosso": [{"key":"448","name":"Mato Grosso"}],
"mato_grosso_do_sul": [{"key":"446","name":"Mato Grosso do Sul"}],
"minas_gerais": [{"key":"449","name":"Minas Gerais"}],
"parana": [{"key":"452","name":"Paraná"}],
"paraiba": [{"key":"451","name":"Paraíba"}],
"para": [{"key":"450","name":"Pará"}],
"pernambuco": [{"key":"463","name":"Pernambuco"}],
"piaui": [{"key":"453","name":"Piauí"}],
"rio_grande_do_norte": [{"key":"455","name":"Rio Grande do Norte"}],
"rio_grande_do_sul": [{"key":"456","name":"Rio Grande do Sul"}],
"rio_de_janeiro": [{"key":"454","name":"Rio de Janeiro"}],
"rondonia": [{"key":"457","name":"Rondônia"}],
"roraima": [{"key":"458","name":"Roraima"}],
"santa_catarina": [{"key":"459","name":"Santa Catarina"}],
"sergipe": [{"key":"461","name":"Sergipe"}],
"sao_paulo": [{"key":"460","name":"São Paulo"}],
"tocantins": [{"key":"464","name":"Tocantins"}],
}

us_states={
    "alabama": [{"key":3843,"name":"Alabama"}],
    "alaska": [{"key":3844,"name":"Alaska"}],
    "arizona": [{"key":3845,"name":"Arizona"}],
    "arkansas": [{"key":3846,"name":"Arkansas"}],
    "california": [{"key":3847,"name":"California"}],
    "colorado": [{"key":3848,"name":"Colorado"}],
    "connecticut": [{"key":3849,"name":"Connecticut"}],  
    "delaware": [{"key":3850,"name":"Delaware"}],
    "washington_dc": [{"key":3851,"name":"Washington, District of Columbia"}],  
    "florida": [{"key":3852,"name":"Florida"}],
    "georgia": [{"key":3853,"name":"Georgia"}],
    "hawaii": [{"key":3854,"name":"Hawaii"}],
    "idaho": [{"key":3855,"name":"Idaho"}],
    "illinois": [{"key":3856,"name":"Illinois"}],
    "indiana": [{"key":3857,"name":"Indiana"}],
    "iowa": [{"key":3858,"name":"Iowa"}],
    "kansas": [{"key":3859,"name":"Kansas"}],
    "kentucky": [{"key":3860,"name":"Kentucky"}],
    "louisiana": [{"key":3861,"name":"Louisiana"}],
    "maine": [{"key":3862,"name":"Maine"}],
    "maryland": [{"key":3863,"name":"Maryland"}],
    "massachusetts": [{"key":3864,"name":"Massachusetts"}],
    "michigan": [{"key":3865,"name":"Michigan"}],
    "minnesota": [{"key":3866,"name":"Minnesota"}],
    "mississippi": [{"key":3867,"name":"Mississippi"}],
    "missouri": [{"key":3868,"name":"Missouri"}],
    "montana": [{"key":3869,"name":"Montana"}],
    "nebraska": [{"key":3870,"name":"Nebraska"}],
    "nevada": [{"key":3871,"name":"Nevada"}],
    "new_hampshire": [{"key":3872,"name":"New Hampshire"}],
    "new_jersey": [{"key":3873,"name":"New Jersey"}],
    "new_mexico": [{"key":3874,"name":"New Mexico"}],
    "new_york": [{"key":3875,"name":"New York"}],
    "north_carolina": [{"key":3876,"name":"North Carolina"}],
    "north_dakota": [{"key":3877,"name":"North Dakota"}],
    "ohio": [{"key":3878,"name":"Ohio"}],
    "oklahoma": [{"key":3879,"name":"Oklahoma"}],
    "oregon": [{"key":3880,"name":"Oregon"}],
    "pennsylvania": [{"key":3881,"name":"Pennsylvania"}],
    "rhode_island": [{"key":3882,"name":"Rhode Island"}],
    "south_carolina": [{"key":3883,"name":"South Carolina"}],
    "south_dakota": [{"key":3884,"name":"South Dakota"}],
    "tennessee": [{"key":3885,"name":"Tennessee"}],
    "texas": [{"key":3886,"name":"Texas"}],
    "utah": [{"key":3887,"name":"Utah"}],
    "vermont": [{"key":3888,"name":"Vermont"}],
    "virginia": [{"key":3889,"name":"Virginia"}],
    "washington": [{"key":3890,"name":"Washington"}],
    "west_virginia": [{"key":3891,"name":"West Virginia"}],
    "wisconsin": [{"key":3892,"name":"Wisconsin"}],
    "wyoming": [{"key":3893,"name":"Wyoming"}],
}

brazilian_regions={
    'south':['parana','rio_grande_do_sul','santa_catarina'],
    "southeast":['espirito_santo','minas_gerais','rio_de_janeiro','sao_paulo'],
    'north':['acre','amapa','amazonas', 'para', 'rondonia','roraima','tocantins'],
    "northeast":['alagoas','bahia','ceara','maranhao','paraiba','pernambuco', 'piaui','rio_grande_do_norte','sergipe'],    
    'midwest':['distrito_federal','goias','mato_grosso','mato_grosso_do_sul'],                 
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
#     'expats_china': ,
#     'expats_india': ,
#     'expats_philippines': },
#     'expats_el_salvador': ,
#     'expats_vietnam': ,
#     'expats_cuba': ,

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

# http://www.pewresearch.org/fact-tank/2017/05/03/key-findings-about-u-s-immigrants/ - immigrants living in the US
# http://assets.pewresearch.org/wp-content/uploads/sites/7/2017/04/12122207/PH_Stat-Portraits_Foreign-Born-2015_current-05.png
# Top Ten expats: Mexico, China, India, Philippines, El Salvador, Vietnam, Cuba, Dominican Republic, Korea, Guatemala 
expats_top_thirty={
#     'all': '',
    'expats': [{"id":"6015559470583","name":"Expats (All)"}],
    'expats_mexico': [{"id":"6023676072183","name":"Expats (Mexico)"}],
    'expats_china': [{"id":"6019452369983","name":"Expats (China)"}],
    'expats_india': [{"id":"6016916298983","name":"Expats (India)"}],
    'expats_philippines': [{"id":"6018797091183","name":"Expats (Philippines)"}],
    'expats_el_salvador': [{"id":"6019673777983","name":"Expats (El Salvador)"}],
    'expats_vietnam': [{"id":"6027149006383","name":"Expats (Vietnam)"}],
    'expats_cuba': [{"id":"6018797127383","name":"Expats (Cuba)"}],
    'expats_dominican_republic': [{"id":"6019673762183","name":"Expats (Dominican Republic)"}],
    'expats_south_korea': [{"id":"6027148973583","name":"Expats (South Korea)"}],
    'expats_guatemala': [{"id":"6019673808383","name":"Expats (Guatemala)"}],
 
#     missing Ecuador and Iran 
    'expats_canada':[{"id":"6019396764183","name":"Expats (Canada)"}],
    'expats_jamaica':[{"id":"6023356956983","name":"Expats (Jamaica)"}],
    'expats_colombia':[{"id":"6019673525983","name":"Expats (Colombia)"}],    
    'expats_haiti': [{"id":"6018797373783","name":"Expats (Haiti)"}],
    'expats_honduras': [{"id":"6059793664583","name":"Expats (Honduras)"}],    
    'expats_germany': [{"id":"6019367052983","name":"Expats (Germany)"}],
    'expats_peru': [{"id":"6027149008183","name":"Expats (Peru)"}],  
    'expats_poland': [{"id":"6019396657183","name":"Expats (Poland) "}],
 
#     missing pakistan, ukraine, England alone, Guyana
     
    'expats_russia': [{"id":"6025000815983","name":"Expats (Russia)"}],
    'expats_brazil': [{"id":"6019564340583","name":"Expats (Brazil)"}],
    'expats_italy': [{"id":"6019396654583","name":"Expats (Italy)"}],   
    'expats_japan': [{"id":"6023676028783","name":"Expats (Japan)"}],
    'expats_nigeria': [{"id":"6018797004183","name":"Expats (Nigeria)"}],
    'expats_uk':[{"id":"6021354152983","name":"Expats (UK)"}], 
    'expats_nicaragua':[{"id":"6071248894383","name":"Expats (Nicaragua)"}],

} 

# data from pew_research:

# Middle East consists of Afghanistan, Iran, Iraq, Israel/Palestine, Jordan, 
# Kuwait, Lebanon, Saudi Arabia, Syria, Turkey, Yemen, Algeria, Egypt, Morocco and Sudan. 
# Missing middle east:Afghanistan, Iran, Iraq, Palestine, Syria, Turkey, Yemen, Egypt, Sudan
# 9/15

# south asia: source wikipedia: https://en.wikipedia.org/wiki/South_Asia
#  Bangladesh, Bhutan, Maldives, Nepal, India, Pakistan, and Sri Lanka
# missing: Bhuthan, Maldives, Pakistan
# 3/6: 

# east asia: 
# countries: China, Hong Kong, Macau, Japan, Mongolia, Taiwan, North Korea, and South Korea
# missing: Macau, Mongolia, Taiwan, North Korea
# 4/8
# 

# southeast asia: https://en.wikipedia.org/wiki/Southeast_Asia
# countries: Brunei Darussalam , Cambodia , East Timor , Indonesia , Laos , Malaysia , Myanmar , Philippines , 
# Singapore , Thailand , Vietnam
# missing: Brunei, Cambodia, East Timor, Laos, Myanmar
# 5/11 

# sout_america: wikipedia
#countries: Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Guyana, Paraguay, Peru, Suriname, Uruguay, and Venezuela
# missing: Bolivia, Ecuador, Guyana, Paraguay, Suriname, Uruguay 
# 6/12: 

# central america: https://en.wikipedia.org/wiki/Central_America
# countries: Belize, Costa Rica, El Salvador, Guatemala, Honduras, Nicaragua, and Panama
# missing: Belize, Costa Rica, Panama
# 3/7: 

# caribbean: https://en.wikipedia.org/wiki/List_of_Caribbean_countries_by_population
# countries: Aruba, Curaçao, Barbados, Bonaire, the Cayman Islands, Saint Croix, Bahamas, Antigua, Saint Martin,
#  Cuba, Haiti, Puerto Rico, Jamaica, Dominica, Montserrat, Saba, Sint Eustatius,Saint Kitts, Saint Lucia,  
#  Saint Thomas, Saint John, Tortola, Grenada, Saint Vincent, Guadeloupe, Martinique, Trinidad and Tobag, Dominican Republic
# found: Cuba, Dominican Republic, Haiti, Jamaica, Puerto Rico (eliminated - because is considered US)
# 23/28: 

# european: http://www.worldometers.info/geography/how-many-countries-in-europe/
# countries:Russia , Germany , U.K. , France , Italy , Spain , Ukraine , Poland , Romania , Netherlands , Belgium , 
# Greece , Czech Republic , Portugal , Sweden , Hungary , Belarus , Serbia , Austria , Switzerland , Bulgaria ,
# Denmark , Finland , Slovakia , Norway , Ireland , Croatia , Moldova , Bosnia & Herzegovina , Albania , 
# Lithuania , TFYR Macedonia , Slovenia , Latvia , Estonia , Montenegro , Luxembourg , Malta , Iceland , 
# Andorra , Monaco , Liechtenstein , San Marino , Holy See , cyprus
# missing: Ukraine, Belarus, Bulgaria, Croatia, Moldova , Bosnia & Herzegovina , Albania,TFYR Macedonia,Montenegro, Iceland , 
#          Andorra , Liechtenstein , San Marino , Holy See 
# 14/45

# subsaharan africa:
# countries: Angola,  Burundi,  Democratic Republic of the Congo,  Cameroon,  Central African Republic,  Chad,  
# Republic of the Congo,  Equatorial Guinea,  Gabon,  Kenya,  Nigeria,  Rwanda,  São Tomé and Príncipe,  Tanzania,  
# Uganda,  Sudan,  South Sudan,  Djibouti,  Eritrea,  Ethiopia,  Somalia,  Botswana,  Comoros,  Lesotho,  Madagascar, 
#  Malawi,  Mauritius,  Mozambique,  Namibia,  Seychelles,  South Africa,  Swaziland,  Zambia,  Zimbabwe,  Benin, 
# Mali,  Burkina Faso,  Cape Verde,  Ivory Coast,  Gambia,  Ghana,  Guinea,  Guinea-Bissau,  Liberia,  Mauritania, 
#  Niger,  Senegal,  Sierra Leone,  Togo, 
# missing: Angola,  Burundi, Central African Republic, Chad,  Republic of the Congo, Equatorial Guinea,  Gabon,
#  São Tomé and Príncipe,  Sudan,  South Sudan, Djibouti,  Eritrea, Somalia,Botswana, Comoros, Lesotho, Madagascar,
# Malawi, Mauritius, Mozambique, Namibia, Seychelles, Swaziland, Benin, Mali,Burkina Faso,Cape Verde, Gambia,Guinea, 
# Guinea-Bissau, Liberia,  Mauritania, Niger, Togo
# 34/49


expats_census_map={
    'expats_africa': 'Sub-Saharan Africa',
    'expats_europe': 'Europe/Canada',
    'expats_caribbean': 'Caribbean',
    'expats_central_america':'Central America',
    'expats_south_america':'South America',
    'expats_mexico':'Mexico',
    'expats_south_and_east_asia':'South and East Asia',
    'expats_midle_east':'Middle East',
    }
expats_census_output_order = ['expats_mexico', 'expats_south_and_east_asia','expats_europe', 'expats_caribbean','expats_central_america','expats_south_america','expats_midle_east' , 'expats_africa']

expats_census={
    'expats_africa': [
        {"id":"6018797004183","name":"Expats (Nigeria)"},{"id":"6019564383383","name":"Expats (South Africa)"},{"id":"6018797165983","name":"Expats (Ethiopia)"},
        {"id":"6019673448383","name":"Expats (Ghana)"},{"id":"6018796980983","name":"Expats (Kenya)"},
#         added later
        {"id":"6023356986383","name":"Expats (Sierra Leone)"},{"id":"6023357000583","name":"Expats (Senegal)"},{"id":"6023422105983","name":"Expats (Ivory Coast)"},
        {"id":"6019673233983","name":"Expats (Zimbabwe)"},{"id":"6047219032183","name":"Expats (Zambia)"},{"id":"6019673501783","name":"Expats (Uganda)"},
        {"id":"6023356926183","name":"Expats (Tanzania)"},{"id":"6025670492783","name":"Expats (Rwanda)"},{"id":"6018797036783","name":"Expats (Cameroon)"},
        {"id":"6023516373983","name":"Expats (Congo DRC)"}],
               
               
    'expats_europe': [{"id":"6019396764183","name":"Expats (Canada)"},{"id":"6025000815983","name":"Expats (Russia)"}, {"id":"6019367052983","name":"Expats (Germany)"}, 
        {"id":"6021354152983","name":"Expats (UK)"}, {"id":"6019396657183","name":"Expats (Poland) "}, {"id":"6023287393783","name":"Expats (Netherlands) "},
        {"id":"6019396654583","name":"Expats (Italy)"}, {"id":"6019367014383","name":"Expats (France)"},{"id":"6027148962983","name":"Expats (Romania)"}, 
        {"id":"6021354882783","name":"Expats (Portugal)"},{"id":"6023676017583","name":"Expats (Greece)"},{"id":"6019396650783","name":"Expats (Ireland)"},{"id":"6019366943583","name":"Expats (Spain)"},
#         inserted later
        {"id":"6023676048183","name":"Expats (Monaco)"},{"id":"6023676045583","name":"Expats (Malta)"},{"id":"6023676044383","name":"Expats (Luxembourg)"},
        {"id":"6023287351383","name":"Expats (Estonia)"},{"id":"6068613839383","name":"Expats (Latvia)"},{"id":"6023676060183","name":"Expats (Slovenia)"},
        {"id":"6023676039183","name":"Expats (Lithuania)"},{"id":"6023287459983","name":"Expats (Norway)"},{"id":"6023676055383","name":"Expats (Slovakia)"},
        {"id":"6068209522983","name":"Expats (Finland)"},{"id":"6023287455983","name":"Expats (Denmark)"},{"id":"6019377644783","name":"Expats (Switzerland)"},
        {"id":"6023675997383","name":"Expats (Austria)"},{"id":"6027149004983","name":"Expats (Serbia)"},{"id":"6019396638383","name":"Expats (Hungary)"},
        {"id":"6023287397383","name":"Expats (Sweden)"},{"id":"6023287438783","name":"Expats (Czech Republic)"},{"id":"6043702804583","name":"Expats (Belgium)"},
        {"id":"6023676002183","name":"Expats (Cyprus)"}],               
               
    'expats_caribbean': [{"id":"6018797127383","name":"Expats (Cuba)"}, {"id":"6019673762183","name":"Expats (Dominican Republic)"}, 
        {"id":"6018797373783","name":"Expats (Haiti)"}, {"id":"6023356956983","name":"Expats (Jamaica)"}],
# , {"id":"6019520122583","name":"Expats (Puerto Rico)"}                              
               
    'expats_central_america': [{"id":"6019673777983","name":"Expats (El Salvador)"},{"id":"6019673808383","name":"Expats (Guatemala)"},
        {"id":"6059793664583","name":"Expats (Honduras)"},{"id":"6071248894383","name":"Expats (Nicaragua)"},],
    
    'expats_south_america': [{"id":"6025000826583","name":"Expats (Argentina)"},{"id":"6019564340583","name":"Expats (Brazil)"},{"id":"6025054896983","name":"Expats (Chile)"}
        ,{"id":"6019673525983","name":"Expats (Colombia)"},{"id":"6027149008183","name":"Expats (Peru)"},{"id":"6026404871583","name":"Expats (Venezuela)"}, ],
               
               
#     'expats_asian': [{"id":"6023676022783","name":"Expats (Hong Kong)"},  {"id":"6027148973583","name":"Expats (South Korea)"}, 
#         {"id":"6019452369983","name":"Expats (China)"},{"id":"6023676028783","name":"Expats (Japan)"}],        

#     'expats': [{"id":"6015559470583","name":"Expats (All)"}],
    'expats_mexico': [{"id":"6023676072183","name":"Expats (Mexico)"}],
# {"id":"6021354857783","name":"Expats (Australia)"},
    
    'expats_south_and_east_asia': [{"id":"6023516315983","name":"Expats (Sri Lanka)"},{"id":"6016916298983","name":"Expats (India)"},
        {"id":"6023356562783","name":"Expats (Bangladesh)"}, {"id":"6023356955383","name":"Expats (Nepal)"},{"id":"6023676022783","name":"Expats (Hong Kong)"},  {"id":"6027148973583","name":"Expats (South Korea)"}, 
        {"id":"6019452369983","name":"Expats (China)"},{"id":"6023676028783","name":"Expats (Japan)"},
#         southeast asia
        {"id":"6023356966183","name":"Expats (Thailand)"},{"id":"6023516403783","name":"Expats (Singapore)"},{"id":"6027147160983","name":"Expats (Malaysia)"},{"id":"6019564344583","name":"Expats (Indonesia)"},{"id":"6018797091183","name":"Expats (Philippines)"}, {"id":"6027149006383","name":"Expats (Vietnam)"},
        ],

    'expats_midle_east': [{"id":"6023516338783","name":"Expats (Morocco)"},{"id":"6071248932383", "name":"Expats (Algeria)"},
        {"id":"6071248981583","name":"Expats (Kuwait)"},{"id":"6068843912183","name":"Expats (Jordan)"},{"id":"6068844014183","name":"Expats (Lebanon)"},
        {"id":"6025000823583","name":"Expats (Israel)"}, {"id":"6025000813183","name":"Expats (Saudi Arabia)"}],
            
}

consumer_habits = {                         
    'mid_low_value': [{"id":"6038940913482","name":"(D) Afinidade para bens de médio/baixo valor"}],
    'mid_value': [{"id":"6038940911882","name":"(C) Afinidade para bens de médio valor"}],   
    'mid_high_value': [{"id":"6038940911682","name":"(B) Afinidade para bens de médio/alto valor "}],
    'high_value':[ {"id":"6038940910682","name":"(A) Afinidade para bens de alto valor"}],
}

presidenciaveis = {
    'fhc': {"id":"6003379837737","name":"Fernando Henrique Cardoso"},
    'ciro': {"id":"6003351633200","name":"Ciro Gomes"},
    'manuela': {"id":"6013805400887","name":"Manuela D'\u00c1vila"},
    'haddad': {"id":"6003280320043","name":"Fernando Haddad"},
    'lula': {"id":"6003368368602","name": "Luiz In\u00e1cio Lula da Silva"},
    'dilma': {"id":"6003279281580","name":"Dilma Rousseff"},
    'collor': {"id":"6003168906208","name":"Fernando Collor de Mello"},
    'alckmin': {"id":"6002877867972","name": "Geraldo Alckmin"},
    'doria': {"id":"1100727893273169","name":"Jo\u00e3o Doria"},
    'aecio': {"id":"6003147180149","name":"A\u00e9cio Neves"},
    'marina': {"id":"6003098123058","name": "Marina Silva"},
    'temer': {"id":"6003122022534","name":"Michel Temer"},
    'alvaro_dias': {"id":"6012462369384","name":"Alvaro Dias"},
    'serra': {"id":"6003487634480","name": "Jos\u00e9 Serra"},
    'cristovam': {"id":"6003491744031","name":"Cristovam Buarque"},
    'barbosa': {"id":"6003215629872","name":"Joaquim Barbosa"},
    'bolsonaro': {"id":"6013219668741","name": "Jair Bolsonaro"},
    'huck': {"id":"6003453358242","name": "Luciano Huck"},
    'all': [ {"id":"6003379837737","name":"Fernando Henrique Cardoso"}, {"id":"6003280320043","name":"Fernando Haddad"}, {"id":"6003368368602","name": "Luiz In\u00e1cio Lula da Silva"},
    {"id":"6003279281580","name":"Dilma Rousseff"}, {"id":"6003168906208","name":"Fernando Collor de Mello"}, {"id":"6002877867972","name": "Geraldo Alckmin"},
    {"id":"1100727893273169","name":"Jo\u00e3o Doria"}, {"id":"6003147180149","name":"A\u00e9cio Neves"},
    {"id":"6003098123058","name": "Marina Silva"},  {"id":"6003122022534","name":"Michel Temer"},
    {"id":"6012462369384","name":"Alvaro Dias"},  {"id":"6003487634480","name": "Jos\u00e9 Serra"},
    {"id":"6003491744031","name":"Cristovam Buarque"}, {"id":"6003215629872","name":"Joaquim Barbosa"},
    {"id":"6013219668741","name": "Jair Bolsonaro"},{"id":"6003453358242","name": "Luciano Huck"},
    {"id":"6003351633200","name": "Ciro Gomes"},{"id":"6013805400887","name": "Manuela D'\u00c1vila"}]
}

religions = {
    "protestants":[
{ "id":"6003589124027",  "name": "Adventism"},
{ "id":"6003201144882",  "name": "Assembleias de Deus"},
{ "id":"6003593639487",  "name": "Assemblies of god church"},
{ "id":"6003338956996",  "name": "Baptist church"},
{ "id":"6003373700357",  "name": "Brazil for Christ Pentecostal Church"},
{ "id":"6003057442932",  "name": "Evangelicalism"},
# { "id":"6002934036059",  "name": "Evangelism"},
{ "id":"6003667860620",  "name": "God is Love Pentecostal Church"},
# { "id":"6003505890395",  "name": "Gospel"},
{ "id":"1639220963012682",  "name": "Igreja Batista da  Lagoinha"},
{ "id":"6003259998688",  "name": "Igreja Renascer em Cristo"},
{ "id":"1587826828164693",  "name": "Igreja Universal"},
{ "id":"6003460212425",  "name": "International Church of God's Grace"},
{ "id":"6003393532763",  "name": "International Church of the Foursquare Gospel"},
{ "id":"6003450277842",  "name": "Lutheranism"},
{ "id":"6003042965515",  "name": "Methodism"},
{ "id":"6003108539033",  "name": "Pentecostalism"},
{ "id":"6003280279759",  "name": "Presbyterianism"},
{ "id":"6003252221201",  "name": "Protestantism"},
{ "id":"6002893210222",  "name": "Seventh-day Adventist Church"},
{ "id":"6002868949222",  "name": "Universal Church of the Kingdom of God"}],
             
"catholics": [
{ "id":"6014466576902",  "name": "Catholic and Proud"},
{ "id":"6009835851982",  "name": "Catholic Bible"},
{ "id":"6003225407745",  "name": "Catholic Charismatic Renewal"},
{ "id":"6003021658693",  "name": "Catholic Church"},
{ "id":"6003178114366",  "name": "Catholicism"},
{ "id":"6003289528402",  "name": "Eucharist"},
{ "id":"6003321945297",  "name": "Hail Mary"},
{ "id":"6004026791506",  "name": "Immaculate Heart of Mary"},
{ "id":"6002911030679",  "name": "Mary (mother of Jesus)"},
{ "id":"6003491406547",  "name": "Mass (liturgy)"},
{ "id":"6002876800172",  "name": "Nossa Senhora Aparecida"},
{ "id":"6002958514650",  "name": "Our Lady of Aparecida"},
{ "id":"6003150781134",  "name": "Our Lady of Fátima"},
{ "id":"6003116458426",  "name": "Our Lady of Guadalupe"},
{ "id":"6003254600088",  "name": "Our Lady of Lourdes"},
{ "id":"6003098206258",  "name": "Our Lady of Perpetual Help"},
{ "id":"6003157806208",  "name": "Our Lady of Sorrows"},
{ "id":"6003157842084",  "name": "Our Lady of the Rosary"},
{ "id":"6003126096388",  "name": "Roman Catholic devotions"},
{ "id":"6003117116826",  "name": "Rosary"}
],
"spiritism": [
{ "id":"6003108495235",  "name": "Espiritismo"},
{ "id":"6003554003103",  "name": "Mediumship"},
{ "id":"6003222755698",  "name": "Spiritism"},],
 
"atheists": [
{ "id":"6003633771195",  "name": "Agnosticism"},
{ "id":"6003469024347",  "name": "Atheism"},
{ "id":"6003294073651",  "name": "Criticism of religion"},
{ "id":"6003521003970",  "name": "Irreligion"},
{ "id":"6003227576099",  "name": "Freethought"}],
             
              
             
"all":[
{ "id":"6003108495235",  "name": "Espiritismo"},
{ "id":"6003554003103",  "name": "Mediumship"},
{ "id":"6003222755698",  "name": "Spiritism"},
{ "id":"6014466576902",  "name": "Catholic and Proud"},
{ "id":"6009835851982",  "name": "Catholic Bible"},
{ "id":"6003225407745",  "name": "Catholic Charismatic Renewal"},
{ "id":"6003021658693",  "name": "Catholic Church"},
{ "id":"6003009886419",  "name": "Catholic Online"},
{ "id":"6003178114366",  "name": "Catholicism"},
{ "id":"6003289528402",  "name": "Eucharist"},
{ "id":"6003321945297",  "name": "Hail Mary"},
{ "id":"6004026791506",  "name": "Immaculate Heart of Mary"},
{ "id":"6002911030679",  "name": "Mary (mother of Jesus)"},
{ "id":"6003491406547",  "name": "Mass (liturgy)"},
{ "id":"6002876800172",  "name": "Nossa Senhora Aparecida"},
{ "id":"6002958514650",  "name": "Our Lady of Aparecida"},
{ "id":"6003150781134",  "name": "Our Lady of Fátima"},
{ "id":"6003116458426",  "name": "Our Lady of Guadalupe"},
{ "id":"6003254600088",  "name": "Our Lady of Lourdes"},
{ "id":"6003098206258",  "name": "Our Lady of Perpetual Help"},
{ "id":"6003157806208",  "name": "Our Lady of Sorrows"},
{ "id":"6003157842084",  "name": "Our Lady of the Rosary"},
{ "id":"6003126096388",  "name": "Roman Catholic devotions"},
{ "id":"6003117116826",  "name": "Rosary"},
{ "id":"6003589124027",  "name": "Adventism"},
{ "id":"6003201144882",  "name": "Assembleias de Deus"},
{ "id":"6003593639487",  "name": "Assemblies of god church"},
{ "id":"6003338956996",  "name": "Baptist church"},
{ "id":"6003373700357",  "name": "Brazil for Christ Pentecostal Church"},
{ "id":"6003057442932",  "name": "Evangelicalism"},
# { "id":"6002934036059",  "name": "Evangelism"},
{ "id":"6003667860620",  "name": "God is Love Pentecostal Church"},
# { "id":"6003505890395",  "name": "Gospel"},
{ "id":"1639220963012682",  "name": "Igreja Batista da  Lagoinha"},
{ "id":"6003259998688",  "name": "Igreja Renascer em Cristo"},
{ "id":"1587826828164693",  "name": "Igreja Universal"},
{ "id":"6003460212425",  "name": "International Church of God's Grace"},
{ "id":"6003393532763",  "name": "International Church of the Foursquare Gospel"},
{ "id":"6003450277842",  "name": "Lutheranism"},
{ "id":"6003042965515",  "name": "Methodism"},
{ "id":"6003108539033",  "name": "Pentecostalism"},
{ "id":"6003280279759",  "name": "Presbyterianism"},
{ "id":"6003252221201",  "name": "Protestantism"},
{ "id":"6002893210222",  "name": "Seventh-day Adventist Church"},
{ "id":"6002868949222",  "name": "Universal Church of the Kingdom of God"}
]
}

# atheists = [{ "id":"6003108495235",  "name": "Espiritismo"}]

all_christians =[{ "id":"6003108495235",  "name": "Espiritismo"},{ "id":"6003554003103",  "name": "Mediumship"},{ "id":"6003222755698",  "name": "Spiritism"},{ "id":"6014466576902",  "name": "Catholic and Proud"},{ "id":"6009835851982",  "name": "Catholic Bible"},
{ "id":"6003225407745",  "name": "Catholic Charismatic Renewal"},{ "id":"6003021658693",  "name": "Catholic Church"},{ "id":"6003009886419",  "name": "Catholic Online"},{ "id":"6003178114366",  "name": "Catholicism"},{ "id":"6003289528402",  "name": "Eucharist"},
{ "id":"6003321945297",  "name": "Hail Mary"},{ "id":"6004026791506",  "name": "Immaculate Heart of Mary"},{ "id":"6002911030679",  "name": "Mary (mother of Jesus)"},{ "id":"6003491406547",  "name": "Mass (liturgy)"},{ "id":"6002876800172",  "name": "Nossa Senhora Aparecida"},{ "id":"6002958514650",  "name": "Our Lady of Aparecida"},
{ "id":"6003150781134",  "name": "Our Lady of Fátima"},{ "id":"6003116458426",  "name": "Our Lady of Guadalupe"},{ "id":"6003254600088",  "name": "Our Lady of Lourdes"},{ "id":"6003098206258",  "name": "Our Lady of Perpetual Help"},{ "id":"6003157806208",  "name": "Our Lady of Sorrows"},
{ "id":"6003157842084",  "name": "Our Lady of the Rosary"},{ "id":"6003126096388",  "name": "Roman Catholic devotions"}, { "id":"6003117116826",  "name": "Rosary"},
{ "id":"6003589124027",  "name": "Adventism"},{ "id":"6003201144882",  "name": "Assembleias de Deus"},{ "id":"6003593639487",  "name": "Assemblies of god church"},{ "id":"6003338956996",  "name": "Baptist church"},
{ "id":"6003373700357",  "name": "Brazil for Christ Pentecostal Church"},{ "id":"6003057442932",  "name": "Evangelicalism"},{ "id":"6003667860620",  "name": "God is Love Pentecostal Church"}, { "id":"6003505890395",  "name": ""},{ "id":"1639220963012682",  "name": "Igreja Batista da  Lagoinha"},
{ "id":"6003259998688",  "name": "Igreja Renascer em Cristo"},{ "id":"1587826828164693",  "name": "Igreja Universal"},{ "id":"6003460212425",  "name": "International Church of God's Grace"},{ "id":"6003393532763",  "name": "International Church of the Foursquare Gospel"},
{ "id":"6003450277842",  "name": "Lutheranism"},{ "id":"6003042965515",  "name": "Methodism"},{ "id":"6003108539033",  "name": "Pentecostalism"},{ "id":"6003280279759",  "name": "Presbyterianism"},{ "id":"6003252221201",  "name": "Protestantism"},
{ "id":"6002893210222",  "name": "Seventh-day Adventist Church"},{ "id":"6002868949222",  "name": "Universal Church of the Kingdom of God"},
{ "id":"6003505890395",  "name": "Gospel"},{ "id":"6004128067106",  "name": "Holy Spirit"},{ "id":"6004099944209",  "name": "Jesus"},{ "id":"6003077008693",  "name": "God"},{ "id":"6003644807546",  "name": "Worship"},
{ "id":"6003116800826",  "name": "Christian music"},{ "id":"6002900223962",  "name": "Christian ministry"},{ "id":"6003135047608",  "name": "Christian Church"},
{ "id":"6003198436882",  "name": "Pope"},{ "id":"6003073296797",  "name": "Sacred Heart"}
]

religions_exclusions = {
    "protestants":[
{ "id":"6003108495235",  "name": "Espiritismo"},
{ "id":"6003554003103",  "name": "Mediumship"},
{ "id":"6003222755698",  "name": "Spiritism"},
{ "id":"6014466576902",  "name": "Catholic and Proud"},
{ "id":"6009835851982",  "name": "Catholic Bible"},
{ "id":"6003225407745",  "name": "Catholic Charismatic Renewal"},
{ "id":"6003021658693",  "name": "Catholic Church"},
{ "id":"6003009886419",  "name": "Catholic Online"},
{ "id":"6003178114366",  "name": "Catholicism"},
{ "id":"6003289528402",  "name": "Eucharist"},
{ "id":"6003321945297",  "name": "Hail Mary"},
{ "id":"6004026791506",  "name": "Immaculate Heart of Mary"},
{ "id":"6002911030679",  "name": "Mary (mother of Jesus)"},
{ "id":"6003491406547",  "name": "Mass (liturgy)"},
{ "id":"6002876800172",  "name": "Nossa Senhora Aparecida"},
{ "id":"6002958514650",  "name": "Our Lady of Aparecida"},
{ "id":"6003150781134",  "name": "Our Lady of Fátima"},
{ "id":"6003116458426",  "name": "Our Lady of Guadalupe"},
{ "id":"6003254600088",  "name": "Our Lady of Lourdes"},
{ "id":"6003098206258",  "name": "Our Lady of Perpetual Help"},
{ "id":"6003157806208",  "name": "Our Lady of Sorrows"},
{ "id":"6003157842084",  "name": "Our Lady of the Rosary"},
{ "id":"6003126096388",  "name": "Roman Catholic devotions"},
{ "id":"6003117116826",  "name": "Rosary"},
{ "id":"6003633771195",  "name": "Agnosticism"},
{ "id":"6003469024347",  "name": "Atheism"},
{ "id":"6003294073651",  "name": "Criticism of religion"},
{ "id":"6003521003970",  "name": "Irreligion"},
{ "id":"6003227576099",  "name": "Freethought"}
],
"catholics": [
{ "id":"6003108495235",  "name": "Espiritismo"},
{ "id":"6003554003103",  "name": "Mediumship"},
{ "id":"6003222755698",  "name": "Spiritism"}, 
{ "id":"6003589124027",  "name": "Adventism"},
{ "id":"6003201144882",  "name": "Assembleias de Deus"},
{ "id":"6003593639487",  "name": "Assemblies of god church"},
{ "id":"6003338956996",  "name": "Baptist church"},
{ "id":"6003373700357",  "name": "Brazil for Christ Pentecostal Church"},
{ "id":"6003057442932",  "name": "Evangelicalism"},
# { "id":"6002934036059",  "name": "Evangelism"},
{ "id":"6003667860620",  "name": "God is Love Pentecostal Church"},
# { "id":"6003505890395",  "name": "Gospel"},
{ "id":"1639220963012682",  "name": "Igreja Batista da  Lagoinha"},
{ "id":"6003259998688",  "name": "Igreja Renascer em Cristo"},
{ "id":"1587826828164693",  "name": "Igreja Universal"},
{ "id":"6003460212425",  "name": "International Church of God's Grace"},
{ "id":"6003393532763",  "name": "International Church of the Foursquare Gospel"},
{ "id":"6003450277842",  "name": "Lutheranism"},
{ "id":"6003042965515",  "name": "Methodism"},
{ "id":"6003108539033",  "name": "Pentecostalism"},
{ "id":"6003280279759",  "name": "Presbyterianism"},
{ "id":"6003252221201",  "name": "Protestantism"},
{ "id":"6002893210222",  "name": "Seventh-day Adventist Church"},
{ "id":"6002868949222",  "name": "Universal Church of the Kingdom of God"},  
{ "id":"6003633771195",  "name": "Agnosticism"},
{ "id":"6003469024347",  "name": "Atheism"},
{ "id":"6003294073651",  "name": "Criticism of religion"},
{ "id":"6003521003970",  "name": "Irreligion"},
{ "id":"6003227576099",  "name": "Freethought"}           
              ],
"spiritism": [
{ "id":"6014466576902",  "name": "Catholic and Proud"},
{ "id":"6009835851982",  "name": "Catholic Bible"},
{ "id":"6003225407745",  "name": "Catholic Charismatic Renewal"},
{ "id":"6003021658693",  "name": "Catholic Church"},
{ "id":"6003009886419",  "name": "Catholic Online"},
{ "id":"6003178114366",  "name": "Catholicism"},
{ "id":"6003289528402",  "name": "Eucharist"},
{ "id":"6003321945297",  "name": "Hail Mary"},
{ "id":"6004026791506",  "name": "Immaculate Heart of Mary"},
{ "id":"6002911030679",  "name": "Mary (mother of Jesus)"},
{ "id":"6003491406547",  "name": "Mass (liturgy)"},
{ "id":"6002876800172",  "name": "Nossa Senhora Aparecida"},
{ "id":"6002958514650",  "name": "Our Lady of Aparecida"},
{ "id":"6003150781134",  "name": "Our Lady of Fátima"},
{ "id":"6003116458426",  "name": "Our Lady of Guadalupe"},
{ "id":"6003254600088",  "name": "Our Lady of Lourdes"},
{ "id":"6003098206258",  "name": "Our Lady of Perpetual Help"},
{ "id":"6003157806208",  "name": "Our Lady of Sorrows"},
{ "id":"6003157842084",  "name": "Our Lady of the Rosary"},
{ "id":"6003126096388",  "name": "Roman Catholic devotions"},
{ "id":"6003117116826",  "name": "Rosary"},
{ "id":"6003589124027",  "name": "Adventism"},
{ "id":"6003201144882",  "name": "Assembleias de Deus"},
{ "id":"6003593639487",  "name": "Assemblies of god church"},
{ "id":"6003338956996",  "name": "Baptist church"},
{ "id":"6003373700357",  "name": "Brazil for Christ Pentecostal Church"},
{ "id":"6003057442932",  "name": "Evangelicalism"},
{ "id":"6003667860620",  "name": "God is Love Pentecostal Church"},
{ "id":"1639220963012682",  "name": "Igreja Batista da  Lagoinha"},
{ "id":"6003259998688",  "name": "Igreja Renascer em Cristo"},
{ "id":"1587826828164693",  "name": "Igreja Universal"},
{ "id":"6003460212425",  "name": "International Church of God's Grace"},
{ "id":"6003393532763",  "name": "International Church of the Foursquare Gospel"},
{ "id":"6003450277842",  "name": "Lutheranism"},
{ "id":"6003042965515",  "name": "Methodism"},
{ "id":"6003108539033",  "name": "Pentecostalism"},
{ "id":"6003280279759",  "name": "Presbyterianism"},
{ "id":"6003252221201",  "name": "Protestantism"},
{ "id":"6002893210222",  "name": "Seventh-day Adventist Church"},
{ "id":"6002868949222",  "name": "Universal Church of the Kingdom of God"},
{ "id":"6003633771195",  "name": "Agnosticism"},
{ "id":"6003469024347",  "name": "Atheism"},
{ "id":"6003294073651",  "name": "Criticism of religion"},
{ "id":"6003521003970",  "name": "Irreligion"},
{ "id":"6003227576099",  "name": "Freethought"}
],
                        
"atheists": [
{ "id":"6003108495235",  "name": "Espiritismo"},{ "id":"6003554003103",  "name": "Mediumship"},{ "id":"6003222755698",  "name": "Spiritism"},{ "id":"6014466576902",  "name": "Catholic and Proud"},{ "id":"6009835851982",  "name": "Catholic Bible"},
{ "id":"6003225407745",  "name": "Catholic Charismatic Renewal"},{ "id":"6003021658693",  "name": "Catholic Church"},{ "id":"6003009886419",  "name": "Catholic Online"},{ "id":"6003178114366",  "name": "Catholicism"},{ "id":"6003289528402",  "name": "Eucharist"},
{ "id":"6003321945297",  "name": "Hail Mary"},{ "id":"6004026791506",  "name": "Immaculate Heart of Mary"},{ "id":"6002911030679",  "name": "Mary (mother of Jesus)"},{ "id":"6003491406547",  "name": "Mass (liturgy)"},{ "id":"6002876800172",  "name": "Nossa Senhora Aparecida"},{ "id":"6002958514650",  "name": "Our Lady of Aparecida"},
{ "id":"6003150781134",  "name": "Our Lady of Fátima"},{ "id":"6003116458426",  "name": "Our Lady of Guadalupe"},{ "id":"6003254600088",  "name": "Our Lady of Lourdes"},{ "id":"6003098206258",  "name": "Our Lady of Perpetual Help"},{ "id":"6003157806208",  "name": "Our Lady of Sorrows"},
{ "id":"6003157842084",  "name": "Our Lady of the Rosary"},{ "id":"6003126096388",  "name": "Roman Catholic devotions"}, { "id":"6003117116826",  "name": "Rosary"},
{ "id":"6003589124027",  "name": "Adventism"},{ "id":"6003201144882",  "name": "Assembleias de Deus"},{ "id":"6003593639487",  "name": "Assemblies of god church"},{ "id":"6003338956996",  "name": "Baptist church"},
{ "id":"6003373700357",  "name": "Brazil for Christ Pentecostal Church"},{ "id":"6003057442932",  "name": "Evangelicalism"},{ "id":"6003667860620",  "name": "God is Love Pentecostal Church"}, { "id":"6003505890395",  "name": ""},{ "id":"1639220963012682",  "name": "Igreja Batista da  Lagoinha"},
{ "id":"6003259998688",  "name": "Igreja Renascer em Cristo"},{ "id":"1587826828164693",  "name": "Igreja Universal"},{ "id":"6003460212425",  "name": "International Church of God's Grace"},{ "id":"6003393532763",  "name": "International Church of the Foursquare Gospel"},
{ "id":"6003450277842",  "name": "Lutheranism"},{ "id":"6003042965515",  "name": "Methodism"},{ "id":"6003108539033",  "name": "Pentecostalism"},{ "id":"6003280279759",  "name": "Presbyterianism"},{ "id":"6003252221201",  "name": "Protestantism"},
{ "id":"6002893210222",  "name": "Seventh-day Adventist Church"},{ "id":"6002868949222",  "name": "Universal Church of the Kingdom of God"},
{ "id":"6004099944209",  "name": "Jesus"},{ "id":"6003077008693",  "name": "God"},
# { "id":"6003505890395",  "name": "Gospel"},{ "id":"6004128067106",  "name": "Holy Spirit"},{ "id":"6004099944209",  "name": "Jesus"},{ "id":"6003077008693",  "name": "God"},{ "id":"6003644807546",  "name": "Worship"},
# { "id":"6003116800826",  "name": "Christian music"},{ "id":"6002900223962",  "name": "Christian ministry"},{ "id":"6003135047608",  "name": "Christian Church"},
{ "id":"6003198436882",  "name": "Pope"},{ "id":"6003073296797",  "name": "Sacred Heart"},
{ "id":"6003108495235",  "name": "Espiritismo"},{ "id":"6003554003103",  "name": "Mediumship"},{ "id":"6003222755698",  "name": "Spiritism"}, 
]
}

expats_new_brazil={
#     'all': '',
    'expats': [{"id":"6015559470583","name":"Expats (All)"}],
    'expats_mexico': [{"id":"6023676072183","name":"Expats (Mexico)"}],
    'expats_north_america': [{"id":"6019396649183","name":"Expats (US)"},{"id":"6019396764183","name":"Expats (Canada)"}],    
#     'expats_china': ,
#     'expats_india': ,
#     'expats_philippines': },
#     'expats_el_salvador': ,
#     'expats_vietnam': ,
#     'expats_cuba': ,

    'expats_europe': [ {"id":"6019367052983","name":"Expats (Germany)"}, {"id":"6019396657183","name":"Expats (Poland) "}, {"id":"6021354152983","name":"Expats (UK)"},
        {"id":"6021354857783","name":"Expats (Australia)"}, {"id":"6019396654583","name":"Expats (Italy)"}, {"id":"6019367014383","name":"Expats (France)"},{"id":"6027148962983","name":"Expats (Romania)"}, 
        {"id":"6021354882783","name":"Expats (Portugal)"},{"id":"6023676017583","name":"Expats (Greece)"},{"id":"6019396650783","name":"Expats (Ireland)"},{"id":"6019366943583","name":"Expats (Spain)"}],
    
    'expats_africa': [{"id":"6018797004183","name":"Expats (Nigeria)"},{"id":"6019564383383","name":"Expats (South Africa)"},{"id":"6018797165983","name":"Expats (Ethiopia)"},
        {"id":"6019673448383","name":"Expats (Ghana)"},{"id":"6018796980983","name":"Expats (Kenya)"}],

    'expats_south_asia': [{"id":"6016916298983","name":"Expats (India)"}, {"id":"6023356562783","name":"Expats (Bangladesh)"}, {"id":"6023356955383","name":"Expats (Nepal)"}],

    'expats_midle_east': [{"id":"6025000823583","name":"Expats (Israel)"}, {"id":"6025000813183","name":"Expats (Saudi Arabia)"}],

    'expats_asian': [{"id":"6018797091183","name":"Expats (Philippines)"}, {"id":"6027149006383","name":"Expats (Vietnam)"}, {"id":"6027148973583","name":"Expats (South Korea)"}, 
        {"id":"6019452369983","name":"Expats (China)"},{"id":"6023676028783","name":"Expats (Japan)"}],

    'expats_latin_america': [{"id":"6019673808383","name":"Expats (Guatemala)"},{"id":"6019673777983","name":"Expats (El Salvador)"}, {"id":"6019673762183","name":"Expats (Dominican Republic)"},
        {"id":"6018797127383","name":"Expats (Cuba)"}, {"id":"6019673525983","name":"Expats (Colombia)"}, {"id":"6018797373783","name":"Expats (Haiti)"}, {"id":"6059793664583","name":"Expats (Honduras)"},
        {"id":"6027149008183","name":"Expats (Peru)"},{"id":"6019564340583","name":"Expats (Brazil)"},{"id":"6026404871583","name":"Expats (Venezuela)"}, {"id":"6025000826583","name":"Expats (Argentina)"}],
            
    'expats_russia':[{"id":"6025000815983","name":"Expats (Russia)"}]
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

age_intervals_education_level = {
    'educational_age': {'age_min':25},
    'adolescent' :{'age_min': 13, 'age_max': 17},
    'young_1' :{'age_min': 18, 'age_max': 24},
    'young_2' :{'age_min': 25, 'age_max': 34},
    'mid_aged_1' :{'age_min': 35, 'age_max': 44},
    'mid_aged_2' :{'age_min': 45, 'age_max': 54},        
    'old_1': {'age_min': 55, 'age_max': 64},
    'old_2': {'age_min': 65}                               
}

age_intervals_expats = {         
    '13to17' :{'age_min': 13, 'age_max': 17},
    '18to34' :{'age_min': 18, 'age_max': 34},
    '35to50' :{'age_min': 35, 'age_max': 50},
    '51to64' :{'age_min': 51, 'age_max': 64},        
    '65_and_above': {'age_min': 65}                              
}

age_details = {         
    '13to14' :{'age_min': 13, 'age_max': 14},
    '15to19' :{'age_min': 15, 'age_max': 19},
    '20to24' :{'age_min': 20, 'age_max': 24},
    '25to29' :{'age_min': 25, 'age_max': 29},    
    '30to34' :{'age_min': 30, 'age_max': 34},
    '35to39' :{'age_min': 35, 'age_max': 39},
    '40to44' :{'age_min': 40, 'age_max': 44},  
    '45to49' :{'age_min': 45, 'age_max': 49},
    '50to54' :{'age_min': 50, 'age_max': 54},        
    '55to60' :{'age_min': 55, 'age_max': 60},
    '60to64' :{'age_min': 60, 'age_max': 64},
    '65_and_above': {'age_min': 65}                              
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
#     'college':[2,3,5,6],
#     "high_school":[1,4,13],
#     'grad_school':[7,8,9,10,11],                  
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
#         'hispanic_bilingual': [{"id":"6009609054383","name":"Hispanic (US - Bilingual)"}],
#         'hispanic_english': [{"id":"6009609045383","name":"Hispanic (US - English dominant)"}],
#         'hispanic_spanish':     [{"id":"6009609033583","name":"Hispanic (US - Spanish dominant)"}],
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

income_levels_brazil={
#         'all': [],
#         'all': [],
#     '30k_to_40k':[{"id": "6018510070532","name": "$30,000 - $40,000"}],
#     'other': 'dealt with specially',
    '2k_to_3k':[{"id": "6038940926682","name": "R$2.001 - R$3.000"}],
    '3k_to_4k':[{"id": "6038940928082","name": "R$3.001 - R$4.000"}],        
    '4k_to_5k':[{"id": "6038940928482","name": "R$4.001 - R$5.000"}],
    '5k_to_6k':[{"id": "6038940928882","name": "R$5.001 - R$6.000"}],
    '6k_to_8k':[{"id": "6038940929082","name": "R$6.001 - R$8.000"}],
    '8k_to_10k':[{"id": "6038940929482","name": "R$8.001 - R$10.000"}],
    '10k_to_15k':[{"id": "6038940929682","name": "R$10.001 - R$15.000"}], 
    '15k_to_20k':[{"id": "6038940929882","name": "R$15.001 - R$20.000"}],
    'over_20k':[{"id": "6038940930082","name": "Over R$20.001"}]                                                            
} 

income_levels_exclusions = {
    "income":[
        {"id": "6038940926682","name": "R$2.001 - R$3.000"},
        {"id": "6038940928082","name": "R$3.001 - R$4.000"},
        {"id": "6038940928482","name": "R$4.001 - R$5.000"},
        
        {"id": "6038940928882","name": "R$5.001 - R$6.000"},
        {"id": "6038940929082","name": "R$6.001 - R$8.000"},
        {"id": "6038940929482","name": "R$8.001 - R$10.000"},
        {"id": "6038940929682","name": "R$10.001 - R$15.000"},
        {"id": "6038940929882","name": "R$15.001 - R$20.000"},
        {"id": "6038940930082","name": "Over R$20.001"}                
    ]
} 


#     locales
#     https://developers.facebook.com/docs/marketing-api/targeting-search#locale
languages={
#         'all': [], 
    'english': [1001],
    'german': [5],
    'spanish': [1002],
    'french': [1003],
    'chinese' : [1004],
    'japanse' : [11],
    'portuguese': [1005],
    'arabic' : [28],
    'korean': [12],
    'hindi': [46]
}              