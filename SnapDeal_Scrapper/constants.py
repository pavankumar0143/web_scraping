# Main website name
PROJECT_NAME = "SnapDeal"

# Domain name of website
PROJECT_DOMAIN = 'www.snapdeal.com'

# Root Url
ROOT_URL = 'https://www.snapdeal.com/page/sitemap'


# Categories available

MOBILES_AND_TABLETS                  =      'Mobiles_And_Tablets'
COMPUTERS_OFFICE_AND_GAMING          =      'Computers_Office_And_Gaming'
ELECTRONICS                          =      'Electronics'
HOME_AND_LIVING                      =      'Home_And_Living'
WOMENS_FASHION                       =      'Womens_Fashion'
MENS_FASHION                         =      'Mens_Fashion'
TOYS_KIDS_AND_BABIES                 =      'Toys_Kids_And_Babies'
DAILY_NEEDS                          =      'Daily_Needs'
SPORTS_FITNESS_AND_OUTDOOR           =      'Sports_Fitness_And_Outdoor'
MOTORS_ACCESSORIES                   =      'Motors_Accessories'
BOOKS_MUSIC_AND_GIFT_CARDS           =      'Books_Music_And_Gift_Cards'
REAL_ESTATE_AND_FINANCIAL_SERVICES   =      'Real_Estate_And_Financial_Services'


# max retires that are allowed
MAX_RETRIES = 5

# to compare with config.write_to value
WRITE_TO_DB = 1

# to compare with config.write_to value
WRITE_TO_FILE = 2

# to compare with config.url_flag value
URL_FLAG = 1


# to compare with config.info_flag value
PRODUCT_FlAG = 1

GOOD_STATUS = 200

# REquest headers to pass them in request.get arguments to look like request is comming from browser instead of script
REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",

    "User-Agent": "Chrome/51.0.2704.103 Safari/537.36",
}

