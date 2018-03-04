import requests
from bs4 import BeautifulSoup
import re
import json

COOKIE = '_dtm=%7B%7D; optimizelyEndUserId=oeu1517888019690r0.08582387089030452; BIGipServercars_composite=2671842476.23296.0000; rollout=41; s_cc=true; s_fid=7F950673AF3F3744-2EFD8E01761F0615; Registration=currentUserId:IfNdi0siDBMUCE68Pt+EdHoDIpwdj1vVHEbvwrvNICYvFXqsWIU/Wp19EDlQsJjkBUZJe4DYlQ27apWjNn9rDjjfBgKhEM4Q2gvctBi8FvI=; returningUser=1517888014664; CarsVisitor=%7B%22pcid%22%3A%22null%22%2C%22pdid%22%3A%225823934544865873988895810493417232294%22%7D; s_vi=[CS]v1|2D3C9107051D0D6D-60000170800005F9[CE]; btpdb.4IGCP5L.c2lnbmFsdWlk=NDQzOTg0MTE5ODc2NTA0MTU1Mg; btpdb.4IGCP5L.dGZjLjUyNjM0OTg=U0VTU0lPTg; _ga=GA1.2.1111185128.1517888022; rd=20; TS01bf77fc=01fce1e7c4c6235142d0bc5fccb426ffff7978189979f14f7cd353e1e44ee4fd42ca27217f436213bf46d519089794f5e4d88742e34cf193b30766393be449b2ccf40b161a8dee8178dc7233666bff392bc2e52d829946a41a6069830fd712277788f659dfaaa503688c8983a6850d169f588b91c2d3308e84864a17488e6b9a1c172cce52; zipcode=84097; BIGipServercars_services_85x=2604733612.20736.0000; affiliate=national; affiliate=national; s_sv_sid=1247136766296; BIGipServercars_sites_www=541136044.21791.0000; BIGipServercars_dockercomposite_price_advisor_api_prd=339874988.12579.0000; BIGipServercars_webstatic_85x=2671842476.21248.0000; BIGipServercars_dockerapp_swarm_prd=2369918124.20480.0000; ae-visitorId=1180223u8950aj9j7riyeu; catRetarget=sedan_midsize|suv_midsize; catRetarget=sedan_midsize%7Csuv_midsize; stockCert=U%7Cfalse; __gads=ID=ed81e58d5d9bcfdf:T=1519683835:S=ALNI_Ma7D0MkesoBAz3jc27m5BxMx-TRjg; zipcode=84604; adZoneInfo=84604|saltlake_unzoned|saltlake; adCatInfo=All|All|DEFAULT_DEFAULT; akaas_www-prod_instance=1520303870~rv=47~id=bc4cf080c36e7f55aa3f5143bb007359; SC_LINKS=%5B%5BB%5D%5D; stockCert=U|false; SessionInfo=mkid%253D0%257Cmknm%253DKia%257Cmdid%253D0%257Cmdnm%253DStinger%257C; BIGipServercars_docker_userprofiles_prd=4198634668.19487.0000; _gid=GA1.2.2076741410.1519886096; s_sq=cvencarsdtm%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.cars.com%25252F%2526link%253DUsed%252520All%252520Vehicles%252520%252528all%252520mi%252529%25252084604_1%2526region%253Dinventory%2526.activitymap%2526.a%2526.c; SessionInfo=mkid%3D0%7Cmknm%3DKia%7Cmdid%3D0%7Cmdnm%3DStinger%7C; akaas_vdp_instance=2147483647~rv=37~id=bf0c5e93c22f22e331e9d2203b646a51~rn=; BIGipServercars_docker_vertical_vdp_prd=4232189100.24095.0000; BIGipServercars_docker_rendering_prd=4248966316.16389.0000; s_dfa=cvencars; ak_bmsc=2932BFB83626A0F55E76C2C93BA6D290B819CC8ED7280000B8109A5A8215F533~plMIfm6BQmzuOzM5u9WYDXTWX+704H2aAYzSzYNAQRXTlqcq/kvN8BUZlglcqHogQWO3R/xCl0IL0G57fSNfcCXx5MZyk9anGY2WMS7GEsRbWhq+RV7mabXwbT5ccoerBjJZ5Bq1n4lcV++0bPUepSS6ZAFI2rh/NOfgoUcEoNNOj+niKdn/IS8IpoeN544fKZCPLLfGEQD2srb2yNZ/XaLisJ9/hu+J2ndfCxqw9E5tI=; s_lv_s=Less%20than%201%20day; s_uniSource=%5B%5B\'Session%2520Refresh\'%2C\'1520046269272\'%5D%5D; btpdb.4IGCP5L.dGZjLjQxNDczMDM=TUlOVVRFUw; btpdb.4IGCP5L.dGZjLjMwMjc2ODk=TUlOVVRFUw; QSI_HistorySession=https%3A%2F%2Fwww.cars.com%2Fvehicledetail%2Fdetail%2F728817780%2Foverview%2F~1519973502930%7Chttps%3A%2F%2Fwww.cars.com%2Fvehicledetail%2Fdetail%2F728681358%2Foverview%2F~1519973810407%7Chttps%3A%2F%2Fwww.cars.com%2Ffor-sale%2Fsearchresults.action%2F%3FldId%3D28882%26page%3D1%26perPage%3D20%26rd%3D99999%26searchSource%3DGN_REFINEMENT%26sort%3Drelevance%26stkTypId%3D28881%26zc%3D84604~1520046299941; TS01952cdc=01fce1e7c41dafc0864e1d381cc3f3d8293f32bc629742f2d9917a8f07dbed84b303beed29ace14819558ab950975ddb48c278d2000a6abe142c4b1ac630538fb4f7c772809689b0be96b95204c3926c217d4be37cc1b5f764f6f4a862b2526722f19123ab4d6ecb1efe5873f79454ec2ca06d85c6705184b8f5bea77abc0f31217ebf929007f987d54168ef772d40dc511dd13f3f97a0d68d83a752e32c2859b8cd0f2d2d5daf588b16a91c91173d23199b1ad26f043fd9c27a40a14c018b8c66485072a48160c0c92cb92431c15e04d09d49c1b4c06deb8082095fcb2afd01c5acae92fc50e9effd0d5d3b2117038bf759acf278b850bfe79612cc90e1e6b82787b99088f390eaefbc629b53246850266894aac1; CarsSidCookie=1356307341936868559883823067896600; TS019da928=01fce1e7c45b083939eb5cc7db2b0d7173c14115cb415cc4fe3ab93a15cb4588f7c40f2c02ba66d947f4afffb2d3c95daf65f788691ff1febe14f2da6d4761172d0b221c64274d267939c2a58fb8e4141c45a8fd1810e38e9fe1feb8868226d2339aad2b4c426488f5186b4ce5af6699c1fc0ef51117b4297e3954d403b99e2a3310bce3ca; bm_sv=02237F70FA0D60AE26EF8D96413C7DAB~rW41D9hVZ4tEdgVINRzK+5zgqStNW63OZChNCR3p8ZzzWvcW63vwoibCadEaxhdQbGm4PCQ/ni7yYTQXh9gMh+ozDlOObDh3S/5yN/CT6U6wjk8wZ9e+FVw2RAb4bGxb0S7R9yrbqNcMTyYaBfcsoQ==; _td=291df3e5-f629-409b-bbff-40c334b767e5; btpdb.4IGCP5L.cGFnZWNvdW50ZXI=MTM1; _gat_gtag_UA_50492232_1=1; rd=20; __CT_Data=gpv=125&ckp=tld&dm=cars.com&apv_355_www06=125&cpv_355_www06=125; s_lv=1520046952523; s_depth=2; CarsComBridge=%7B%22evars%22%3A%7B%7D%2C%22events%22%3A%22%22%2C%22listvars%22%3A%7B%7D%2C%22props%22%3A%7B%22prop37%22%3A%22large-desktop%3Alandscape%3A1889%7Clarge-desktop%3Alandscape%3A1889%22%7D%7D; smtrrmkr=636556437549518429%5E28877c81-ee0a-e811-8163-d91eb79d529c%5E2c3388a4-8f1e-e811-8176-9cd3eac60d16%5E0%5E24.10.218.40'
CARS_DETAIL_URL = 'https://www.cars.com/vehicledetail/detail/{}/overview/'
VIN_DETAIL_URL = 'https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/{}?format=json'
LISTINGS_URL = 'https://www.cars.com/for-sale/searchresults.action/?ldId=28882&page={}&perPage=100&rd=99999&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=84604'


# TODO - Might need to make this fancier
def get_value_for_db(valueToGet):
    return valueToGet if valueToGet else None


def get_attributes_from_vin(vin):
    page_url = VIN_DETAIL_URL.format(vin)
    page_response = requests.get(page_url)
    if page_response.status_code != 200:
        return {}
    vin_attributes = json.loads(page_response.text)
    if len(vin_attributes['Results']) != 1:
        raise RuntimeError('Too many results returned from VIN service')
    return vin_attributes['Results'][0]


def get_listing_details_from_soup(soup):
    listing_details = {}
    # See if the listing exists
    listing_not_exists = soup.find('div', class_='vdp__no-listing__alert')
    if listing_not_exists:
        print("  Listing didn't exist on details page!!!!!!")
        return None

    # Get primary car attributes
    primary_car_attributes_json = soup.find('script', {'type': 'application/ld+json'}).get_text()
    primary_attributes = json.loads(primary_car_attributes_json)
    car_attributes = None
    for attribute in primary_attributes:
        if attribute['@type'] == 'Car':
            car_attributes = attribute

    if not car_attributes:
        raise RuntimeError('Listing didnt have core attributes!')

    # Require price
    price = get_value_for_db(car_attributes['offers']['price'])
    if not price or price == 'Not Priced': # Don't want the data if there's no label
        print("  Price didn't exist on details page!!!!!")
        return None

    listing_details['price'] = float(price)
    vin = get_value_for_db(car_attributes['vehicleIdentificationNumber'])
    listing_details['vin'] = vin
    listing_details['make'] = get_value_for_db(car_attributes['manufacturer']['name'])
    listing_details['model'] = get_value_for_db(car_attributes['model']['name'])
    listing_details['year'] = get_value_for_db(car_attributes['vehicleModelDate'])
    listing_details['condition'] = get_value_for_db(car_attributes['itemCondition']['name'])
    mpg = get_value_for_db(car_attributes['fuelEfficiency']['value'])
    if mpg:
        mpg_parts = mpg.split('-')
        listing_details['mpg_city'] = mpg_parts[0]
        listing_details['mpg_highway'] = mpg_parts[1]
    listing_details['fuel_type'] = get_value_for_db(car_attributes['fuelType'])
    listing_details['mileage'] = get_value_for_db(car_attributes['mileageFromOdometer']['value'])
    listing_details['number_of_doors'] = get_value_for_db(car_attributes['numberOfDoors'])
    listing_details['engine'] = get_value_for_db(car_attributes['vehicleEngine']['name'])
    listing_details['interior_color'] = get_value_for_db(car_attributes['vehicleInteriorColor'])
    # listing_details['seating_capacity'] = get_value_for_db(car_attributes['vehicleSeatingCapacity'])
    listing_details['transmission'] = get_value_for_db(car_attributes['vehicleTransmission'])
    if car_attributes.get('aggregateRating'):
        listing_details['cars_rating'] = get_value_for_db(car_attributes['aggregateRating']['ratingValue'])
    listing_details['exterior_color'] = get_value_for_db(car_attributes['color'])
    listing_details['city'] = get_value_for_db(car_attributes['offers']['seller']['address']['addressLocality'])
    listing_details['state'] = get_value_for_db(car_attributes['offers']['seller']['address']['addressRegion'])

    # Get model from vin (if it exists)
    if vin:
        vin_attributes = get_attributes_from_vin(vin)
        if vin_attributes.get('Model'):
            listing_details['model'] = vin_attributes['Model']

    # Get zip code if exists
    address_el = soup.find('p', class_='vdp-dealer-location__address')
    if address_el:
        address = address_el.get_text()
        zip_code = re.search('.*(\d{5})', address, re.IGNORECASE).group(1)
        if zip_code:
            listing_details['zip_code'] = zip_code

    # REPLACED BY CAR ATTRIBUTES ABOVE
    # # Get basic details
    # basic_details = soup.find_all('li', class_='vdp-details-basics__item')
    # for detail in basic_details:
    #     detail_name = detail.find('strong').get_text().rsplit(':',1)[0]
    #     detail_value = detail.find('span').get_text().lstrip()
    #     if detail_name == 'FuelType':
    #         listing_details['fuel_type'] = detail_value
    #     elif detail_name == 'MPG':

    #     elif detail_name == 'Exterior Color':
    #         listing_details['exterior_color'] = detail_value
    #     elif detail_name == 'Interior Color':
    #         listing_details['interior_color'] = detail_value
    #     elif detail_name == 'Transmission':
    #         listing_details['transmission'] = detail_value
    #     elif detail_name == 'Engine':
    #         listing_details['engine'] = detail_value
    #     elif detail_name == 'Vin':
    #         listing_details['vin'] = detail_value
    #     elif detail_name == 'Mileage':
    #         listing_details['mileage'] = int(detail_value.replace(',', ''))

    # Get all advanced details (if exist)
    standard_features_el = soup.find('div', class_='standard-feature')
    if standard_features_el:
        advanced_details_el = standard_features_el.find('div', class_='accordion__section-body')
        if advanced_details_el:
            advanced_details = advanced_details_el.find('ul').find_all('li')
            listing_details['advanced_details'] = list(map(lambda list_item: list_item.get_text(), advanced_details))

    return listing_details


def load_listing_detail_page(listing_id):
    print("  Loading details page")
    page_url = CARS_DETAIL_URL.format(listing_id)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
        'cache-control': 'max-age=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    page_response = requests.get(page_url, headers=headers)
    if page_response.status_code != 200:
        print("Error loading details page {}. Status code: {}".format(listing_id, page_response.status_code))
    else:
        soup = BeautifulSoup(page_response.text, 'html.parser')
        return get_listing_details_from_soup(soup)


def load_listings_page(page_num):
    print("Loading page {}".format(page_num))
    listing_ids = []

    page_url = LISTINGS_URL.format(page_num)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': COOKIE,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    page_response = requests.get(page_url, headers=headers)
    if page_response.status_code != 200:
        print("Error loading page {}. Status code: {}".format(page_num, page_response.status_code))
    else:
        print("Loaded page {}".format(page_num))
        soup = BeautifulSoup(page_response.text, 'html.parser')
        listings = soup.find(id='listings')
        for listing_container in listings.find_all('div', class_='shop-srp-listings__listing'):
            for link in listing_container.find_all('a', class_='listing-row__link'):
                detail_link = link['href']
                listing_ids.append(re.search('vehicledetail/detail/(.*)/overview', detail_link, re.IGNORECASE).group(1))

    return listing_ids