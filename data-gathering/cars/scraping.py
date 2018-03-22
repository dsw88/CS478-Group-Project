import requests
from bs4 import BeautifulSoup
import re
import json

COOKIE = 'optimizelyEndUserId=oeu1517888019690r0.08582387089030452; BIGipServercars_composite=2671842476.23296.0000; rollout=41; s_cc=true; s_fid=7F950673AF3F3744-2EFD8E01761F0615; Registration=currentUserId:IfNdi0siDBMUCE68Pt+EdHoDIpwdj1vVHEbvwrvNICYvFXqsWIU/Wp19EDlQsJjkBUZJe4DYlQ27apWjNn9rDjjfBgKhEM4Q2gvctBi8FvI=; returningUser=1517888014664; CarsVisitor=%7B%22pcid%22%3A%22null%22%2C%22pdid%22%3A%225823934544865873988895810493417232294%22%7D; s_vi=[CS]v1|2D3C9107051D0D6D-60000170800005F9[CE]; btpdb.4IGCP5L.c2lnbmFsdWlk=NDQzOTg0MTE5ODc2NTA0MTU1Mg; btpdb.4IGCP5L.dGZjLjUyNjM0OTg=U0VTU0lPTg; _ga=GA1.2.1111185128.1517888022; TS01bf77fc=01fce1e7c4c6235142d0bc5fccb426ffff7978189979f14f7cd353e1e44ee4fd42ca27217f436213bf46d519089794f5e4d88742e34cf193b30766393be449b2ccf40b161a8dee8178dc7233666bff392bc2e52d829946a41a6069830fd712277788f659dfaaa503688c8983a6850d169f588b91c2d3308e84864a17488e6b9a1c172cce52; BIGipServercars_services_85x=2604733612.20736.0000; affiliate=national; affiliate=national; s_sv_sid=1247136766296; BIGipServercars_sites_www=541136044.21791.0000; BIGipServercars_dockercomposite_price_advisor_api_prd=339874988.12579.0000; BIGipServercars_webstatic_85x=2671842476.21248.0000; BIGipServercars_dockerapp_swarm_prd=2369918124.20480.0000; ae-visitorId=1180223u8950aj9j7riyeu; catRetarget=sedan_midsize|suv_midsize; catRetarget=sedan_midsize%7Csuv_midsize; __gads=ID=ed81e58d5d9bcfdf:T=1519683835:S=ALNI_Ma7D0MkesoBAz3jc27m5BxMx-TRjg; zipcode=84604; adZoneInfo=84604|saltlake_unzoned|saltlake; stockCert=U|false; akaas_vdp_instance=2147483647~rv=37~id=bf0c5e93c22f22e331e9d2203b646a51~rn=; zipcode=84604; BIGipServercars_docker_userprofiles_prd=4215411884.18207.0000; SC_LINKS=%5B%5BB%5D%5D; rd=99999; rd=99999; stockCert=U%7Cfalse; adCatInfo=All|All|DEFAULT_DEFAULT; BIGipServercars_docker_rendering_prd=4198634668.16645.0000; SessionInfo=mkid%3D0%7Cmknm%3DYugo%7Cmdid%3D0%7Cmdnm%3DStinger%7C; BIGipServercars_docker_vertical_vdp_prd=4232189100.19231.0000; akaas_hp_abtest=1521868921~rv=69~id=d420161026a118437b2148f069c8cb15~rn=; s_lv_s=Less%20than%207%20days; _dtm=%7B%22_sdsat_days%20since%20last%20visit%22%3A%22Less%20than%207%20days%22%7D; ak_bmsc=D59126DAA636EDCB04E8D7C6BC42232A423DA54473420000F9A5AC5A7C7DD861~plZHk44OorfZYYeUMZLCmKZiuU5MFlOz2NNk10zZwSF/2cFdLEBvwO8ShCQVmscqAS66q437JUdj7QA0YqPNAXD9Gadv+8JiaxWykLo3V1jmSUoE/9iCwGfxHif3fvjAlkvxo2XJCln2Oy6xmNP5ufAdtvFvuxl5GYFVLX5lRglj3LF7zbeo3UJInDi/rkwltYHkJei7OCJWGMHLH8NokP5JWXfUk3qbJsetrnadWfEVby1pq5vBykeQkiYMYf6uED; s_dfa=cvencars; SessionInfo=mkid%253D0%257Cmknm%253DYugo%257Cmdid%253D0%257Cmdnm%253DStinger%257C; btpdb.4IGCP5L.dGZjLjQxNDczMDM=TUlOVVRFUw; _gid=GA1.2.316469215.1521264124; _gat_gtag_UA_50492232_1=1; s_uniSource=%5B%5B%27Session%2520Refresh%27%2C%271520622371427%27%5D%2C%5B%27Typed%2FBookmarked%27%2C%271521264130076%27%5D%5D; akaas_srp_abtest=1521868930~rv=4~id=6772d68cc04143f75fd73b56cb9eb134~rn=hotCar1; QSI_HistorySession=https%3A%2F%2Fwww.cars.com%2F~1520918672038%7Chttps%3A%2F%2Fwww.cars.com%2Ffor-sale%2Fsearchresults.action%2F%3FmkId%3D20045%26rd%3D99999%26zc%3D84604%26stkTypId%3D28881%26searchSource%3DQUICK_FORM~1520918676710%7Chttps%3A%2F%2Fwww.cars.com%2Ffor-sale%2Fsearchresults.action%2F%3Fpage%3D1%26perPage%3D20%26rd%3D99999%26searchSource%3DGN_BREADCRUMB%26showMore%3Dtrue%26sort%3Drelevance%26stkTypId%3D28881%26zc%3D84604~1520918694134%7Chttps%3A%2F%2Fwww.cars.com%2F~1521001289930%7Chttps%3A%2F%2Fwww.cars.com%2Ffor-sale%2Fsearchresults.action%2F%3Fpage%3D1%26perPage%3D20%26rd%3D99999%26searchSource%3DGN_BREADCRUMB%26showMore%3Dtrue%26sort%3Drelevance%26stkTypId%3D28881%26zc%3D84604~1521001297934%7Chttps%3A%2F%2Fwww.cars.com%2Fvehicledetail%2Fdetail%2F726630335%2Foverview%2F~1521001315239%7Chttps%3A%2F%2Fwww.cars.com%2F~1521264124397%7Chttps%3A%2F%2Fwww.cars.com%2Ffor-sale%2Fadvanced-search%2F~1521264132699; smtrrmkr=636568609365449952%5E28877c81-ee0a-e811-8163-d91eb79d529c%5E9513871b-a329-e811-8165-e1052edeefc5%5E0%5E24.10.218.40; CarsSidCookie=1355990429629421557828445529670163; akaas_srp_instance=hotCar1; TS01952cdc=01fce1e7c404554c48ce3bb060c174f9af89627d9e16f22b05b731b966ca846d6de460969ac80fde009e68c44326d245653d80eadda8e40eaceb35d472511751c3ef9098b1d604fb673caaabd422d5788691c0a8fdc820b620ade1a48659f0e15f7652d67b9dfced9b1bc29ed017279fcff211113917325e65ba1f8d1e20ce9d153a3ce46b058a1e1d28ab404a51be9af72bcaa08ee01300d962458fb1343a7c7d87d8e52771007ca18a0bada00820b9125ac6907f04a74fd00e7b7c073764220bab900fd0b0ca8c590c49b33431710f539ab6e467cbb57fc5659a355b3656e4b44364a7574e55f1607670ff15f35cb5dd99da9c10857e78d946e6dcecbec05900dfd1c8c63faf582272b180652c3755a64a52e2bc327e1be8bc61b207ca1e779a23493991; TS019da928=01fce1e7c40650cf0e881f5f87855ac76b76117fb0415cc4fe3ab93a15cb4588f7c40f2c02ba66d947f4afffb2d3c95daf65f788691ff1febe14f2da6d4761172d0b221c64274d267939c2a58fb8e4141c45a8fd1810e38e9fe1feb8868226d2339aad2b4c426488f5186b4ce5af6699c1fc0ef5113343cc403106b2827a043dd1fde99e86; CarsComBridge=%7B%22evars%22%3A%7B%22eVar37%22%3A%22desktop%3Alandscape%3A1083%7Cdesktop%3Alandscape%3A1083%22%7D%2C%22events%22%3A%22%22%2C%22listvars%22%3A%7B%7D%2C%22props%22%3A%7B%22prop37%22%3A%22desktop%3Alandscape%3A1083%7Cdesktop%3Alandscape%3A1083%22%7D%7D; bm_sv=ABE882D4D3173F177346D9B1E111BF2C~4k1EdlK++ec1+HAEB0FtBdi1p1xX7OAm8/8p8EhapGoePcOmU/kiJUgMB+BolhipNhcv9GNa+18oyTMsmA127vUNKuhttvs8xalncNzk2v4FF+uWbEI79eZ93HbDw1e0N94CcCXbO4NPs+4Dr+pYow==; _td=291df3e5-f629-409b-bbff-40c334b767e5; btpdb.4IGCP5L.cGFnZWNvdW50ZXI=MTY4; btpdb.4IGCP5L.dGZjLjMwMjc2ODk=TUlOVVRFUw; _dtmp=%7B%22_sdsat_pcid%22%3A%7B%22v%22%3A%22null%22%2C%22t%22%3A1584336142287%7D%7D; s_lv=1521264142293; s_depth=5; s_sq=%5B%5BB%5D%5D; __CT_Data=gpv=159&ckp=tld&dm=cars.com&apv_355_www06=159&cpv_355_www06=159'
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