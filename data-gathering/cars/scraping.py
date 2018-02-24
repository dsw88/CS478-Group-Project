import requests
from bs4 import BeautifulSoup
import re
import json

COOKIE = '_dtm=%7B%7D; optimizelyEndUserId=oeu1517888019690r0.08582387089030452; BIGipServercars_composite=2671842476.23296.0000; rollout=41; s_cc=true; s_fid=7F950673AF3F3744-2EFD8E01761F0615; Registration=currentUserId:IfNdi0siDBMUCE68Pt+EdHoDIpwdj1vVHEbvwrvNICYvFXqsWIU/Wp19EDlQsJjkBUZJe4DYlQ27apWjNn9rDjjfBgKhEM4Q2gvctBi8FvI=; returningUser=1517888014664; CarsVisitor=%7B%22pcid%22%3A%22null%22%2C%22pdid%22%3A%225823934544865873988895810493417232294%22%7D; s_vi=[CS]v1|2D3C9107051D0D6D-60000170800005F9[CE]; btpdb.4IGCP5L.c2lnbmFsdWlk=NDQzOTg0MTE5ODc2NTA0MTU1Mg; btpdb.4IGCP5L.dGZjLjUyNjM0OTg=U0VTU0lPTg; _ga=GA1.2.1111185128.1517888022; rd=20; TS01bf77fc=01fce1e7c4c6235142d0bc5fccb426ffff7978189979f14f7cd353e1e44ee4fd42ca27217f436213bf46d519089794f5e4d88742e34cf193b30766393be449b2ccf40b161a8dee8178dc7233666bff392bc2e52d829946a41a6069830fd712277788f659dfaaa503688c8983a6850d169f588b91c2d3308e84864a17488e6b9a1c172cce52; zipcode=84097; BIGipServercars_services_85x=2604733612.20736.0000; stockCert=U|false; affiliate=national; affiliate=national; catRetarget=suv_midsize; s_sv_sid=1247136766296; BIGipServercars_sites_www=541136044.21791.0000; akaas_www-prod_instance=1519698035~rv=37~id=9748c8de3fdf5d4f4c6c7ce94e11738b; BIGipServercars_docker_userprofiles_prd=4215411884.17439.0000; _gid=GA1.2.1925398884.1519359145; BIGipServercars_docker_rendering_prd=4215411884.16901.0000; SessionInfo=mkid%3D0%7Cmknm%3DKia%7Cmdid%3D0%7Cmdnm%3DStinger%7C; BIGipServercars_dockercomposite_price_advisor_api_prd=339874988.12579.0000; BIGipServercars_webstatic_85x=2671842476.21248.0000; s_dfa=cvencars; s_lv_s=Less%20than%201%20day; rd=20; zipcode=84097; btpdb.4IGCP5L.dGZjLjU3MzA5MDI=TUlOVVRFUw; btpdb.4IGCP5L.dGZjLjQxNDczMDM=TUlOVVRFUw; btpdb.4IGCP5L.dGZjLjMwMjc2ODk=TUlOVVRFUw; BIGipServercars_docker_vertical_vdp_prd=4248966316.20511.0000; bm_mi=0EE941693546E7D5CA900125AC072F43~b+JC/FvyXL0N+yYKu0zjPVagpaZdDjuWN7uH9qzHzpqLjP11DRCSnTDwwk1XlK1y1gFNRS1f4fKUWmJbQFY96m0PsMHkHlSmrEBbhtfykIJDkNodx/ci5coIwRGjmuuRZQPuATirqrlm3J/YhoQ5BQ/wazm63oEE6EzliCpnlp2qlWY38BVlBauxHrpCZs39y0//mCVjmIVAW6pON8NowUeQf0PB8wL2wWoJRxFpbn1o+l4l0oTHALQmFC6WopIyKd8BpdymmocRTr8T7sC86frXSSAaz74T/HyQZmToWqaDomc1a7EiJ0JHJD98DGzXMS508LwEgIX6D+PbMJRtIw==; ak_bmsc=9D017CCA8090B0CCEF1F53AC1ACE3847B819CC8E1C31000026DA905A26D0197A~plMPCNuRJGxMFx7Xvu6yeWGcm5VMmxsp3bG93AzFN0hv+arSRz7yJyCFfrMxTj22vjcFVBI8PDkEOvqME1QAD673dG+BZcnpledtZehY/DkZB7aUAZBOHblG58E9CjNzs2pttOUejRcJibj+ufJVP0j3RDrVZN3u5ZGYN+xrjx8ypMMqaBOKs1KiVxU3tmVnT8dDjq7nBLY8MYpF/Mfbutxhsdm7BYRzqNO+DBFMQiWeC3WLddUEzf8NCpvO+o7L1J; btpdb.4IGCP5L.dGZjLjMwMjc3MzE=TUlOVVRFUw; BIGipServercars_dockerapp_swarm_prd=2369918124.20480.0000; btpdb.4IGCP5L.dGZjLjQ5MTU5MjM=TUlOVVRFUw; btpdb.4IGCP5L.dGZjLjM3MzQzMDQ=TUlOVVRFUw; ae-sessionId=1180223l3cbvr1yocos0ek; ae-visitorId=1180223u8950aj9j7riyeu; SC_LINKS=%5B%5BB%5D%5D; TS01952cdc=01fce1e7c4579807dab1ab434816de5b567469288160fd4d8d7b3becc9ff03160dd9c667315cbfb3a2c64eb986de35964fad446f4c80395d6bb4919762e74390c18fc93a351b4e99e01478c9468a2e3b75d9238909e988c163bb1641f1d6b201327710f01062294e035a4c0067f05621dcf22bd479a5d36070a99078fb82c22fe070507f2e9c84e1432b496a2220522bf5447abed229a157cf0e9283e03d729f8667066d1e266672268d0a502f97eb009b69ef075ec327c23a781b53fada84548ede3f5e956c28d3726ee23e1746bcf1951517ff72aa982265629dfd3e540b378c8647f4282382a276b02d8e0c61a6a234b807d0a550b229d637611cc2f233428c3775c291fef0970eae5aa551e16ef3041e479489; SessionInfo=mkid%253D0%257Cmknm%253DKia%257Cmdid%253D0%257Cmdnm%253DStinger%257C; _gat_gtag_UA_50492232_1=1; s_sq=cvencarsdtm%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.cars.com%25252F%2526link%253DSearch%2526region%253DsearchWidgetForm%2526.activitymap%2526.a%2526.c; stockCert=N|false|all; CarsSidCookie=1356228113604667332975050736217407; TS019da928=01fce1e7c40d4902ba761875c664eb9638afa4b1af415cc4fe3ab93a15cb4588f7c40f2c02ba66d947f4afffb2d3c95daf65f788691ff1febe14f2da6d4761172d0b221c64274d267939c2a58fb8e4141c45a8fd1810e38e9fe1feb8868226d2339aad2b4c426488f5186b4ce5af6699c1fc0ef5115cda7f103ec204caeeebfa5543a4a71b; bm_sv=2296B10D80FEABEE816850E932ACA8D0~m6A6CjkJ/dBlvXl82CstxAsX4aHSL/D4WRMmXO1sXc0BUyp6UCZe1V9mRYZqzX3QsuwwuqbAO2WoTxpdt8sW3/6zFXCiaCBqdiOlmsQKbwIGEw7FGPYXo/uxz3ZCc+UEiGKpwBMGTU638R8rVxHA/xWIiZuUANvc2eKG4+dwu3Q=; _td=291df3e5-f629-409b-bbff-40c334b767e5; btpdb.4IGCP5L.cGFnZWNvdW50ZXI=ODg; __CT_Data=gpv=80&ckp=tld&dm=cars.com&apv_355_www06=80&cpv_355_www06=80; QSI_HistorySession=https%3A%2F%2Fwww.cars.com%2Fvehicledetail%2Fdetail%2F728303873%2Foverview%2F~1519442990878%7Chttps%3A%2F%2Fwww.cars.com%2Fresearch%2Fdodge-dakota-2011%2Ftrims%2F~1519443016123%7Chttps%3A%2F%2Fwww.cars.com%2Fresearch%2Fdodge-dakota-2011%2F~1519443030203%7Chttps%3A%2F%2Fwww.cars.com%2Fresearch%2Fdodge-dakota-2011%2Fspecs%2F~1519443051364%7Chttps%3A%2F%2Fwww.cars.com%2Fresearch%2Fdodge-dakota-2011%2F~1519443069910%7Chttps%3A%2F%2Fwww.cars.com%2Fresearch%2Fdodge-dakota-2011%2Fconsumer-reviews%2F~1519443079817%7Chttps%3A%2F%2Fwww.cars.com%2Fvehicledetail%2Fdetail%2F728249658%2Foverview%2F~1519443241091%7Chttps%3A%2F%2Fwww.cars.com%2F~1519444093239%7Chttps%3A%2F%2Fwww.cars.com%2Ffor-sale%2Fsearchresults.action%2F%3FmkId%3D20068%26mdId%3D36293408%26rd%3D20%26zc%3D84097%26searchSource%3DQUICK_FORM~1519444100924; adZoneInfo=84097|saltlake_unzoned|saltlake; adCatInfo=Kia|Stinger|sedan_midsize; s_lv=1519444101811; s_depth=27; CarsComBridge=%7B%22evars%22%3A%7B%7D%2C%22events%22%3A%22%22%2C%22listvars%22%3A%7B%7D%2C%22props%22%3A%7B%22prop37%22%3A%22tablet%3Aportrait%3A862%7Ctablet%3Aportrait%3A862%22%7D%7D; catRetarget=suv_midsize; smtrrmkr=636550409024087646%5E28877c81-ee0a-e811-8163-d91eb79d529c%5E7b22fcc1-1119-e811-8163-dddb49dd7f71%5E0%5E24.10.218.40'
CARS_DETAIL_URL = 'https://www.cars.com/vehicledetail/detail/{}/overview/'
LISTINGS_URL = 'https://www.cars.com/for-sale/searchresults.action/?ldId=28882&page={}&perPage=100&rd=99999&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=84604'


# TODO - Might need to make this fancier
def get_value_for_db(valueToGet):
    return valueToGet if valueToGet else None


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
    listing_details['vin'] = get_value_for_db(car_attributes['vehicleIdentificationNumber'])
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