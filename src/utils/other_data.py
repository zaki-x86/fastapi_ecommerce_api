from datetime import datetime
from decimal import Decimal

from src.config import settings


users_data = [
    {
        "email": "ffriedman0@oakley.com",
        "hashed_password": settings.USER_PASSWORD,
        "first_name": "Fanechka",
        "last_name": "Friedman",
    },
    {
        "email": "tweatherby1@quantcast.com",
        "first_name": "Tasha",
        "last_name": "Weatherby",
        "hashed_password": settings.USER_PASSWORD,
    },
    {
        "email": "jglassup2@jiathis.com",
        "first_name": "Joane",
        "last_name": "Glassup",
        "hashed_password": settings.USER_PASSWORD,
    },
    {
        "email": "cpoor3@wiley.com",
        "first_name": "Carmelia",
        "last_name": "Poor",
        "hashed_password": settings.USER_PASSWORD,
    },
    {
        "email": "bnapoleone4@cdbaby.com",
        "first_name": "Bernard",
        "last_name": "Napoleone",
        "hashed_password": settings.USER_PASSWORD,
    },
    {
        "email": "gromaint5@economist.com",
        "first_name": "Ginelle",
        "last_name": "Romaint",
        "hashed_password": settings.USER_PASSWORD,
    },
    {
        "email": "vbarrim6@google.es",
        "first_name": "Valle",
        "last_name": "Barrim",
        "hashed_password": settings.USER_PASSWORD,
    },
    {
        "email": "kwingeat7@miitbeian.gov.cn",
        "first_name": "Katusha",
        "last_name": "Wingeat",
        "hashed_password": settings.USER_PASSWORD,
    },
    {
        "email": "ycastleton8@1und1.de",
        "first_name": "Yolane",
        "last_name": "Castleton",
        "hashed_password": settings.USER_PASSWORD,
    },
    {
        "email": "amingame9@bravesites.com",
        "first_name": "Ashley",
        "last_name": "Mingame",
        "hashed_password": settings.USER_PASSWORD,
    },
]

address_data = [
    {
        "unit_number": "28809",
        "street_number": "42981",
        "address_line1": "73 Magdeline Trail",
        "address_line2": "15th Floor",
        "city": "Mobile",
        "region": "Alabama",
        "postal_code": "36610",
    },
    {
        "unit_number": "292",
        "street_number": "1",
        "address_line1": "3344 Northland Terrace",
        "address_line2": "8th Floor",
        "city": "Louisville",
        "region": "Kentucky",
        "postal_code": "40205",
    },
    {
        "unit_number": "2284",
        "street_number": "1361",
        "address_line1": "82548 Butterfield Plaza",
        "address_line2": "Room 448",
        "city": "Saint Cloud",
        "region": "Minnesota",
        "postal_code": "56372",
    },
    {
        "unit_number": "95",
        "street_number": "8517",
        "address_line1": "6473 High Crossing Point",
        "address_line2": "Apt 1811",
        "city": "Green Bay",
        "region": "Wisconsin",
        "postal_code": "54305",
    },
    {
        "unit_number": "0",
        "street_number": "5",
        "address_line1": "310 Everett Plaza",
        "address_line2": "Apt 1156",
        "city": "Tampa",
        "region": "Florida",
        "postal_code": "33673",
    },
    {
        "unit_number": "38718",
        "street_number": "20474",
        "address_line1": "3 Anniversary Point",
        "address_line2": "11th Floor",
        "city": "Atlanta",
        "region": "Georgia",
        "postal_code": "30301",
    },
    {
        "unit_number": "3",
        "street_number": "62970",
        "address_line1": "08 Division Court",
        "address_line2": "Room 1942",
        "city": "Oklahoma City",
        "region": "Oklahoma",
        "postal_code": "73135",
    },
    {
        "unit_number": "8572",
        "street_number": "77476",
        "address_line1": "9433 Shasta Road",
        "address_line2": "13th Floor",
        "city": "Columbia",
        "region": "South Carolina",
        "postal_code": "29215",
    },
    {
        "unit_number": "7",
        "street_number": "6473",
        "address_line1": "17676 Stone Corner Park",
        "address_line2": "Suite 64",
        "city": "Roanoke",
        "region": "Virginia",
        "postal_code": "24004",
    },
    {
        "unit_number": "0",
        "street_number": "396",
        "address_line1": "0242 Wayridge Avenue",
        "address_line2": "Apt 1208",
        "city": "Detroit",
        "region": "Michigan",
        "postal_code": "48217",
    },
    {
        "unit_number": "05837",
        "street_number": "0698",
        "address_line1": "75690 Gerald Pass",
        "address_line2": "Apt 1082",
        "city": "Fresno",
        "region": "California",
        "postal_code": "93750",
    },
    {
        "unit_number": "9",
        "street_number": "03",
        "address_line1": "13782 Karstens Road",
        "address_line2": "Suite 80",
        "city": "Atlanta",
        "region": "Georgia",
        "postal_code": "31136",
    },
    {
        "unit_number": "9800",
        "street_number": "210",
        "address_line1": "606 Sloan Trail",
        "address_line2": "Room 491",
        "city": "Hampton",
        "region": "Virginia",
        "postal_code": "23668",
    },
    {
        "unit_number": "68628",
        "street_number": "727",
        "address_line1": "02 Loftsgordon Plaza",
        "address_line2": "Room 1444",
        "city": "Minneapolis",
        "region": "Minnesota",
        "postal_code": "55480",
    },
    {
        "unit_number": "29",
        "street_number": "42253",
        "address_line1": "51 Monica Circle",
        "address_line2": "1st Floor",
        "city": "New York City",
        "region": "New York",
        "postal_code": "10105",
    },
    {
        "unit_number": "7926",
        "street_number": "254",
        "address_line1": "846 7th Circle",
        "address_line2": "Apt 1619",
        "city": "El Paso",
        "region": "Texas",
        "postal_code": "79905",
    },
    {
        "unit_number": "3",
        "street_number": "00353",
        "address_line1": "49 Westend Center",
        "address_line2": "Suite 26",
        "city": "Brooklyn",
        "region": "New York",
        "postal_code": "11254",
    },
    {
        "unit_number": "281",
        "street_number": "3",
        "address_line1": "286 Doe Crossing Plaza",
        "address_line2": "Apt 1213",
        "city": "Torrance",
        "region": "California",
        "postal_code": "90510",
    },
    {
        "unit_number": "63",
        "street_number": "19449",
        "address_line1": "5 1st Court",
        "address_line2": "Suite 81",
        "city": "Columbia",
        "region": "South Carolina",
        "postal_code": "29203",
    },
    {
        "unit_number": "8",
        "street_number": "32",
        "address_line1": "5177 Milwaukee Street",
        "address_line2": "PO Box 77721",
        "city": "Newark",
        "region": "New Jersey",
        "postal_code": "07112",
    },
]

payment_methods_data = [
    {
        "provider": "Master Card",
        "account_number": "6837536537771158",
        "expiry_date": datetime(2024, 11, 5),
        "is_default": True,
    },
    {
        "provider": "Master Card",
        "account_number": "2239045303432029",
        "expiry_date": datetime(2025, 4, 6),
        "is_default": True,
    },
    {
        "provider": "Visa",
        "account_number": "5829373658136293",
        "expiry_date": datetime(2025, 6, 26),
        "is_default": True,
    },
    {
        "provider": "Visa",
        "account_number": "8541919801138361",
        "expiry_date": datetime(2025, 1, 11),
        "is_default": True,
    },
    {
        "provider": "Visa",
        "account_number": "2206178905378059",
        "expiry_date": datetime(2025, 5, 9),
        "is_default": True,
    },
    {
        "provider": "Master Card",
        "account_number": "9712864412586547",
        "expiry_date": datetime(2024, 11, 28),
        "is_default": True,
    },
    {
        "provider": "Visa",
        "account_number": "3166250367651548",
        "expiry_date": datetime(2025, 2, 24),
        "is_default": True,
    },
    {
        "provider": "Master Card",
        "account_number": "1098426077427530",
        "expiry_date": datetime(2025, 9, 28),
        "is_default": True,
    },
    {
        "provider": "Master Card",
        "account_number": "5783906991081809",
        "expiry_date": datetime(2025, 4, 14),
        "is_default": True,
    },
    {
        "provider": "Visa",
        "account_number": "3755517087203477",
        "expiry_date": datetime(2025, 6, 1),
        "is_default": True,
    },
]

variations_data = [
    {"name": "Color", "category_id": 1},
    {"name": "Color", "category_id": 2},
    {"name": "Color", "category_id": 3},
    {"name": "Size", "category_id": 1},
    {"name": "Size", "category_id": 2},
]

variation_options_data = [
    {"value": "XS"},
    {"value": "S"},
    {"value": "M"},
    {"value": "L"},
    {"value": "XL"},
]

products_data = [
    {
        "name": "Belt",
        "description": "It will always hold your pants",
        "product_image": "belt",
    },
    {
        "name": "Men T-Shirt",
        "description": "Very comfortable t-shirt. 100% cotton.",
        "product_image": "men_t_shirt",
    },
    {
        "name": "Men Sweater",
        "description": "Very comfortable sweater. 100% cotton.",
        "product_image": "men_sweater",
    },
    {
        "name": "Men Jeans",
        "description": "Very comfortable jeans.",
        "product_image": "men_jeans",
    },
    {
        "name": "Men Pants",
        "description": "Very comfortable pants",
        "product_image": "men_pants",
    },
    {
        "name": "Men Shorts",
        "description": "Very comfortable shorts",
        "product_image": "men_shorts",
    },
    {
        "name": "Men Sweatpants",
        "description": "Very comfortable sweatpants.",
        "product_image": "men_sweatpants",
    },
    {
        "name": "Men Jacket",
        "description": "Very comfortable jacket.",
        "product_image": "men_jacket",
    },
    {
        "name": "Men Coat",
        "description": "Very comfortable coat",
        "product_image": "men_coat",
    },
    {
        "name": "Men Blazer",
        "description": "Very comfortable blazer.",
        "product_image": "men_blazer",
    },
    {
        "name": "Women Blouse",
        "description": "Very comfortable blouse.",
        "product_image": "women_blouse",
    },
    {
        "name": "Women T-Shirt",
        "description": "Very comfortable t-shirt.",
        "product_image": "women_t_shirt",
    },
    {
        "name": "Women Sweater",
        "description": "Very comfortable sweater.",
        "product_image": "women_sweater",
    },
    {
        "name": "Women Jeans",
        "description": "Very comfortable jeans.",
        "product_image": "women_jeans",
    },
    {
        "name": "Women Pants",
        "description": "Very comfortable pants",
        "product_image": "women_pants",
    },
    {
        "name": "Women Skirt",
        "description": "Very comfortable skirt.",
        "product_image": "women_skirt",
    },
    {
        "name": "Baseball Cap",
        "description": "Very comfortable baseball_cap.",
        "product_image": "baseball_cap",
    },
    {
        "name": "Beanie",
        "description": "Very comfortable beanie.",
        "product_image": "beanie",
    },
    {
        "name": "Sun Hat",
        "description": "Very comfortable sun hat.",
        "product_image": "sun_hat",
    },
    {
        "name": "Backpack",
        "description": "Very comfortable backpack",
        "product_image": "backpack",
    },
    {
        "name": "Handback",
        "description": "Very comfortable handback.",
        "product_image": "handback",
    },
]

product_items_data = [
    {"SKU": "999_JRZ_682", "quantity_in_stock": 4, "price": Decimal("6.99")},
    {"SKU": "473_JHI_115", "quantity_in_stock": 5, "price": Decimal("7.99")},
    {"SKU": "010_RNK_498", "quantity_in_stock": 3, "price": Decimal("10.99")},
    {"SKU": "533_DOH_461", "quantity_in_stock": 2, "price": Decimal("12.99")},
    {"SKU": "364_GNJ_157", "quantity_in_stock": 3, "price": Decimal("9.99")},
    {"SKU": "190_ILR_299", "quantity_in_stock": 1, "price": Decimal("8.99")},
    {"SKU": "351_FMA_897", "quantity_in_stock": 4, "price": Decimal("4.99")},
    {"SKU": "652_XFD_829", "quantity_in_stock": 8, "price": Decimal("13.99")},
    {"SKU": "289_XTV_984", "quantity_in_stock": 5, "price": Decimal("8.99")},
    {"SKU": "140_EJL_189", "quantity_in_stock": 1, "price": Decimal("4.99")},
    {"SKU": "438_XEA_781", "quantity_in_stock": 3, "price": Decimal("12.99")},
    {"SKU": "429_UAG_536", "quantity_in_stock": 4, "price": Decimal("17.99")},
    {"SKU": "835_IGY_289", "quantity_in_stock": 2, "price": Decimal("5.99")},
    {"SKU": "655_SWX_813", "quantity_in_stock": 3, "price": Decimal("9.99")},
    {"SKU": "722_JIB_059", "quantity_in_stock": 7, "price": Decimal("8.99")},
    {"SKU": "075_XZC_445", "quantity_in_stock": 6, "price": Decimal("4.99")},
    {"SKU": "608_KCD_726", "quantity_in_stock": 5, "price": Decimal("12.99")},
    {"SKU": "989_USO_636", "quantity_in_stock": 1, "price": Decimal("3.99")},
    {"SKU": "422_VRR_938", "quantity_in_stock": 2, "price": Decimal("10.99")},
    {"SKU": "744_IVJ_876", "quantity_in_stock": 3, "price": Decimal("9.99")},
    {"SKU": "958_VQN_926", "quantity_in_stock": 2, "price": Decimal("4.99")},
]

user_reviews_data = [
    {
        "rating_value": 4,
        "comment": "Amazing product, but was very expensive for me",
    },
    {
        "rating_value": 1,
        "comment": "There was a spider in the box. Disgusting",
    },
    {
        "rating_value": 5,
        "comment": "The delivery came 2 days before the expected date, nice!",
    },
    {"rating_value": 3, "comment": "Okay, but expensive."},
    {
        "rating_value": 4,
        "comment": "The delivery was too long, but the product is awesome",
    },
    {"rating_value": 5, "comment": "Nice product, everything nice."},
    {"rating_value": 3, "comment": "The size does not fit me"},
    {"rating_value": 1, "comment": "It was ordered with stains on it"},
    {"rating_value": 5, "comment": "Wonderful product, it fits me!"},
    {"rating_value": 2, "comment": "It was awful, but the price is too good."},
]
