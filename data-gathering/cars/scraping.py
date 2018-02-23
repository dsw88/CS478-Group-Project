import requests
from bs4 import BeautifulSoup
import re
import time

COOKIE = 'akaas_www-prod_instance=1519962497~rv=78~id=0130a3b56597937962cbb32a7e64411d; CarsSidCookie=5823934546642614739801633699380605406; affiliate=national; zipcode=84604; Registration=Registration=currentUserId:ktAQQz0eW0hqhAtTmwN6r+ClEsMF+NGi2An9Si60m0GH9TC3RGH+s//PAESbVdgraUBqI60Q1LrNa4jJI7kZ1wce/VW83XIN2gvctBi8FvI=; BIGipServercars_docker_rendering_prd=4198634668.15877.0000; rollout=85; TS019da928=01fce1e7c4e1623f48c0f0ef01b33d0b8b82458430c60d651fc568c5a5b9848e2e3e4c46e7c1a6d5eaa306445fe3a2c0001ea4ca93; bm_mi=DF79E1E43225EB31B59295DC49381A77~b+JC/FvyXL0N+yYKu0zjPVPHVeVLPzQkPiys0xJ5gmpR1Lkw0E0T63cGe42Ko2pUSDWsDMdl9dSERb1PG0277/gaqOvymaT2qMNyaAIKuPLsnD0+BgUscMJmypiPHUPY8dyoJcc0j16oF9b5vzt6r4xo6iWdUL8AxzW22olv5O37YCBebnWhj/3HSyKhgGp1kQsJlX81XQqLOp3peYUS6BG9ESYHEVcZqpkYHjcjZ1H7FLd9scyLMypoujfYA0uMJFEJfswpmpH0rRdjrzNCf9UbD4vpBFeIOx43xUm10BVB1zPjuHXk2Og2rxYD2aJv; _dtm=%7B%7D; optimizelyEndUserId=oeu1519357710266r0.9190418007411367; s_dfa=cvencars; BIGipServercars_composite=2604733612.23296.0000; returningUser=1519357708665; CarsVisitor=%7B%22pcid%22%3A%22null%22%2C%22pdid%22%3A%225824955393743377402391721255819024664%22%7D; BIGipServercars_docker_userprofiles_prd=4215411884.17439.0000; TS01952cdc=01fce1e7c498edd2f13a4e59918bca8c8bd520ef07bcc18f9f2e9e5bc7e9e6a0c76b03ffc5b627aa5eebe9104750a95f259da9415ebcd6d80d5b83ef9c37b03beb2ec055e8b8cb3ca41a60af1a2881feb31c4193456ec9b3c6c9a0e941cc6a9e20be530dfe65aeb866801e3632e2a87e4a7d8b6e7f273fc315c44f8b58b860bf000aa6fb863a9a071c203d397c255fbac9805f1efd; TS01bf77fc=01fce1e7c4f2293f6139ef9a559f5ab937d03b7f261b157b0926626926f15ac59e1321681ce65b1984dd7c07199bc5d27b7e87440e05b1415a2ff2514f41c828c8fb210439cd504ac70e4886fe373b6c923a7c9561; ak_bmsc=247AF4169A98AD24B391C052835D5399B819CC8E1C310000018F8F5AC293B172~plOVbuKqAWb+2a/XA2p3z5OwbO5LOvm2iJr4me141vwHZqVFx/8CxbHuoycBHfN4LvoemTeJCTK688hEvZDXVXfxEsc2h1V37qtAenN9HgS4i1aayjCJ7ankqF9ry1cb2aLCfCQo848hTj0QkGRohBIaBZ+58u0YYazvH/weoYxXuBOvB4Le7EmNbHUGqXYqmmeaYOGkGnmVzBkQhWX7b7BCkSAbH+wbC6fwzfFdn3ZPeIvIrZogL4d3TOu8cpqc1s; bm_sv=96FD26DC0B33A7458C2DE8B87A1D3120~m6A6CjkJ/dBlvXl82CstxAvJXfjy5YvtIJH+stbufl7oZoxFsbp6Qu2H7exkvSYqk3sDBZMpaWSBUR7+l1tMNlO4KpggrXrSlo4gsbslpOB19hmPEvBOdB5zGwr8oc0A+jkpwFnvPty+TEj+VboPNw==; __gads=ID=b3b6237e1fc7c4d9:T=1519357709:S=ALNI_MYncagpUfNpM4yOu80zJHqbsISoBA; stockCert=U|false; zipcode=84604; rd=99999; adZoneInfo=84604|saltlake_unzoned|saltlake; adCatInfo=All|All|DEFAULT_DEFAULT; s_cc=true; CarsComBridge=%7B%22evars%22%3A%7B%7D%2C%22events%22%3A%22%22%2C%22listvars%22%3A%7B%7D%2C%22props%22%3A%7B%22prop37%22%3A%22tablet%3Aportrait%3A862%7Ctablet%3Aportrait%3A862%22%7D%7D; s_lv=1519357711903; s_lv_s=First%20Visit; SC_LINKS=%5B%5BB%5D%5D; s_depth=1; s_uniSource=%5B%5B\'Typed%2FBookmarked\'%2C\'1519357711906\'%5D%5D; s_sq=%5B%5BB%5D%5D; s_vi=[CS]v1|2D47C786851D3699-60000134000058B2[CE]; _td=ef32e937-57e2-4e50-b1cf-4b0604019a73; btpdb.4IGCP5L.c2lnbmFsdWlk=NTc5NjI2Njk5NzYxODM0MDgyNQ; btpdb.4IGCP5L.dGZjLjUyNjM0OTg=U0VTU0lPTg; btpdb.4IGCP5L.dGZjLjU3MzA5MDI=TUlOVVRFUw; btpdb.4IGCP5L.cGFnZWNvdW50ZXI=MQ; btpdb.4IGCP5L.dGZjLjQxNDczMDM=TUlOVVRFUw; btpdb.4IGCP5L.dGZjLjMwMjc2ODk=TUlOVVRFUw; _ga=GA1.2.1672998214.1519357712; _gid=GA1.2.1419514857.1519357714; _gat_gtag_UA_50492232_1=1; __CT_Data=gpv=1&ckp=tld&dm=cars.com&apv_355_www06=1&cpv_355_www06=1; __sonar__se=80; __sonar=10082268943531320203; sonar_ume=1519962515057; sonar_ums=2796989132847456985; sonar_umn=11; QSI_HistorySession=https%3A%2F%2Fwww.cars.com%2Ffor-sale%2Fsearchresults.action%2F%3FldId%3D28882%26page%3D1%26perPage%3D100%26rd%3D99999%26searchSource%3DPAGINATION%26sort%3Drelevance%26stkTypId%3D28881%26zc%3D84604%26akamai-feo%3Doff~1519357715222; smtrrmkr=636549545155907181%5E2b0e5763-4c18-e811-8162-87f4b027e439%5E2c0e5763-4c18-e811-8162-87f4b027e439%5E0%5E10.0.10.140'
CARS_DETAIL_URL = 'https://www.cars.com/vehicledetail/detail/{}/overview/'
LISTINGS_URL = 'https://www.cars.com/for-sale/searchresults.action/?ldId=28882&page={}&perPage=100&rd=99999&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=84604'


def get_listing_details_from_soup(soup):
    listing_details = {}
    # See if the listing exists
    listing_not_exists = soup.find('div', class_='vdp__no-listing__alert')
    if listing_not_exists:
        print("  Listing didn't exist on details page!!!!!!")
        return None


    # Get price
    price = soup.find_all('cars-monthly-payment-detail')[0].get('price')
    if price == "" or price == 'Not Priced': # Don't want the data if there's no label
        return None

    listing_details['price'] =  float(price)

    # Get basic details
    basic_details = soup.find_all('li', class_='vdp-details-basics__item')
    for detail in basic_details:
        detail_name = detail.find('strong').get_text().rsplit(':',1)[0]
        detail_value = detail.find('span').get_text().lstrip()

        # TODO - NEED TO ACCOUNT FOR OPTIONAL VARS LIKE INTERIOR_COLOR AND TRANSMISSION

        if detail_name == 'FuelType':
            listing_details['fuel_type'] = detail_value
        elif detail_name == 'MPG':
            mpg_parts = detail_value.split('-')
            listing_details['mpg_city'] = mpg_parts[0]
            listing_details['mpg_highway'] = mpg_parts[1]
        elif detail_name == 'Exterior Color':
            listing_details['exterior_color'] = detail_value
        elif detail_name == 'Interior Color':
            listing_details['interior_color'] = detail_value
        elif detail_name == 'Engine':
            listing_details['engine'] = detail_value
        elif detail_name == 'Vin':
            listing_details['vin'] = detail_value
        elif detail_name == 'Mileage':
            listing_details['mileage'] = int(detail_value.replace(',', ''))

    # Get all advanced details
    advanced_details = soup.find('div', class_='standard-feature').find('div', class_='accordion__section-body').find('ul').find_all('li')
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