import requests
from bs4 import BeautifulSoup
import re

COOKIE = 'BIGipServercars_docker_rendering_prd=4248966316.17157.0000; rollout=20; optimizelyEndUserId=oeu1519094414906r0.7661190246916298; s_dfa=cvencars; BIGipServercars_composite=2621510828.23296.0000; ak_bmsc=6850FEE3FFD448E30ECF631BEF46424CB819CC8E8D0400008A8A8B5A9381BA18~plEolk1hsv4X0TDc8hlian3EnX5vl3iuLVMGLvzaTZ85b6RSnEJRQwsXhAgAHU8PcE+Xfug3Ot14cXUQLEN/7rz7jhsTSLaONbaPFNcBLWNcUNeJHrALlYXfHE6oTKEGm/vrXxEgotOOkUTgbKhFV2cgFN/9PSqONB4WMX2Dln9iNbcIFmwSomF7X1NIhg3rEofggKkV5yElBd1oYXIsNDcN3YMV20/JBYg27q2XKQNJk=; _dtm=%7B%7D; Registration=currentUserId:7nu61vFBOYY67eDhpNGucBDC55GJ10J0BUjigrUkJRV4jqHWXQZ5ZGvUwplS+Tx3K4nOegM+Q1h7vtrlkpEXY6hcJ0n71e01; returningUser=1519094411090; CarsVisitor=%7B%22pcid%22%3A%22null%22%2C%22pdid%22%3A%221356228113506240907491318191396470%22%7D; BIGipServercars_docker_userprofiles_prd=4198634668.18463.0000; TS01952cdc=01fce1e7c4774c8422f33214af3705ce11436bc4df082557b5bfcb447b64a6c6e563066703fe85530bf64796ce0913d403c24dac6bf31d6138db2961fefdadadf059965ada3f1ed910d7cc9eab6c9b02303ac2098cfd6980245b508cde926cfab3c3bb8597bd8dd77034b864fb462e6ca11a9774363b12304598ef81f0b490b434b79bf119532ce0ce1536aad13838ccce37742310; TS01bf77fc=01fce1e7c4414d7cbeac9bbd861901e59a3aa25f91a1e8844597389f7a36eb15f15b8d674c4914807d027097a94f30695b522fb16da1f91cb70bc52401fc19a07024b49184c912e6531c812e70b4c2b43842ae8ff8; stockCert=U|false; zipcode=84097; adZoneInfo=84097|saltlake_unzoned|saltlake; adCatInfo=All|All|DEFAULT_DEFAULT; s_cc=true; s_lv_s=First%20Visit; SC_LINKS=%5B%5BB%5D%5D; s_uniSource=%5B%5B\'Typed%2FBookmarked\'%2C\'1519094416304\'%5D%5D; s_sq=%5B%5BB%5D%5D; __gads=ID=d3ab4e7c773aea13:T=1519094411:S=ALNI_MYqGwTiHjuWhzKvxm8wb58L7Xy_Ow; s_vi=[CS]v1|2D45C54585033641-600011868000BFC0[CE]; btpdb.4IGCP5L.c2lnbmFsdWlk=ODkzOTQyNTEyNTc0Mzk1NzQy; btpdb.4IGCP5L.dGZjLjUyNjM0OTg=U0VTU0lPTg; btpdb.4IGCP5L.dGZjLjU3MzA5MDI=TUlOVVRFUw; btpdb.4IGCP5L.dGZjLjQxNDczMDM=TUlOVVRFUw; btpdb.4IGCP5L.dGZjLjMwMjc2ODk=TUlOVVRFUw; _ga=GA1.2.504614395.1519094416; _gid=GA1.2.1010903952.1519094418; __sonar__se=97; __sonar=8314454990548995489; sonar_ume=1519699218005; sonar_ums=2796989132847456985; akaas_www-prod_instance=1519699288~rv=15~id=9248f6624d59976054847590bd3f4b59; bm_mi=BCDCA2946A97D3FC6638DA919147E42E~K1Eo63dm5xrOj+sAI5pMTkpDqB+dPzbAK9RqvYSvmVxYLX7yR/Ytfhw+hu9PY0y/a4LUfdpUlgo6Xt/xP86Idndw8zImHQP4+QVZV7VArlYqMcV8bmbES/0oeB0s107ykbAqD6oURn/bnoBfPnHQVk2ENPuxSpt1E/fT+lX3uraMCGkxXqlTWrmOtpcu5Udy65o/unhjtoerAOldqF4gp6ZJRE0fJab/DKq4q4vdWzXYi40JxZIOPQ4d07zK8g4290/wRqB9Ut940iehbxL/JA==; CarsSidCookie=1356307341668778671815725348771605; TS019da928=01fce1e7c446a63e99ad4c6fd2b12764fb7554d1721fad27605790dc4740375812c3e049b38effa0478809d0e98172b88e1719c930; rd=99999; s_lv=1519094504244; s_depth=2; CarsComBridge=%7B%22evars%22%3A%7B%7D%2C%22events%22%3A%22%22%2C%22listvars%22%3A%7B%7D%2C%22props%22%3A%7B%22prop37%22%3A%22large-desktop%3Alandscape%3A1918%7Clarge-desktop%3Alandscape%3A1918%22%7D%7D; bm_sv=3DEE8526021092F45E3494CF74D36DE9~4OIOpdxKcPMklijdirY2AqgrkOkfl1xjCgMKYEHO4oBAX6XurPgqYWzBZ3EZkG17Z6PFXsO2K9KfUH2HlRcfOYx+4XceJE9LFuzldNmuVwfhiIzryT0nhd0JSFg+KME7c30QMT7XRPGvRflFuV1bCQ==; btpdb.4IGCP5L.cGFnZWNvdW50ZXI=Mg; _td=da44fb11-fc24-4c76-ba1f-c57eaf1faad5; _gat_gtag_UA_50492232_1=1; __CT_Data=gpv=2&ckp=tld&dm=cars.com&apv_355_www06=2&cpv_355_www06=2; sonar_umn=17; QSI_HistorySession=https%3A%2F%2Fwww.cars.com%2Ffor-sale%2Fsearchresults.action%2F%3FldId%3D28882%26page%3D2%26perPage%3D20%26rd%3D20%26searchSource%3DPAGINATION%26sort%3Drelevance%26stkTypId%3D28881%26zc%3D84097~1519094418315%7Chttps%3A%2F%2Fwww.cars.com%2Ffor-sale%2Fsearchresults.action%2F%3FldId%3D28882%26page%3D2%26perPage%3D100%26rd%3D99999%26searchSource%3DPAGINATION%26sort%3Drelevance%26stkTypId%3D28881%26zc%3D84097~1519094505413; smtrrmkr=636546913061291236%5E3af4d759-e715-e811-815f-bbe134565254%5E3bf4d759-e715-e811-815f-bbe134565254%5E0%5E10.0.20.87'
CARS_DETAIL_URL = 'https://www.cars.com/vehicledetail/detail/{}/overview/'
LISTINGS_URL = 'https://www.cars.com/for-sale/searchresults.action/?ldId=28882&page={}&perPage=100&rd=99999&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=84604'


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