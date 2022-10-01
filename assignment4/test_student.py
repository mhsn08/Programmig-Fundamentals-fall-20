try:
    from a05 import get_companies_names
except ImportError: pass
try:
    from a05 import get_countries
except ImportError: pass
try:
    from a05 import get_companies
except ImportError: pass


companyList = [ 
    {
        "Company Name": "Roshan",
        "Company Motto": "Roshan began operations in 2003 in an environment where there was virtually no telecommunications infrastructure.",
        "City": "Kabul",
        "Country": "Afghanistan",
        "Contact": {
            "Phone Number": "+93 79 997 1333",
            "Email": "roshanca@roshan.af",
            "Website": "http://www.roshan.af/"
        },
        "Social Accounts": {
            "Facebook": "https://www.facebook.com/RoshanConnects",
            "Twitter": "https://www.twitter.com/roshanconnects",
            "LinkedIn": "https://www.linkedin.com/company/roshan"
        }
    }, 
    {
        "Company Name": "Gjirafa",
        "Company Motto": "Gjirafa is a video content and e-commerce platform for the Balkans built on top of an Albanian language specialized search engine.",
        "City": "Tirana",
        "Country": "Albania",
        "Contact": {
            "Phone Number": "37744991206",
            "Email": "info@gjirafa.com",
            "Website": "http://www.gjirafa.com/"
        },
        "Social Accounts": {
            "Facebook": "http://www.facebook.com/gjirafa",
            "Twitter": "https://twitter.com/gjirafashqip",
            "LinkedIn": "https://www.linkedin.com/company/gjirafa-inc-"
        }
    },
    {
        "Company Name": "Shqiperia Com",
        "Company Motto": "ShqiperiaCom primarily provides web developing services and consultancy in the region of Balkan.",
        "City": "Tirana",
        "Country": "Albania",
        "Contact": {
            "Phone Number": "35542403910",
            "Email": "mandi@shqiperia.com",
            "Website": "http://www.shqiperiacom.info"
        },
        "Social Accounts": {
            "Facebook": "https://www.facebook.com/shqiperiacom",
            "Twitter": "http://twitter.com/ShqiperiaCom",
            "LinkedIn": "https://www.linkedin.com/company/shqiperiacom"
        }
    }
]



def test_get_companies_names_1():
    assert get_companies_names(companyList) == ['Roshan', 'Gjirafa', 'Shqiperia Com']
    
def test_get_companies_names_2():
    assert get_companies_names([]) == []

def test_get_companies_names_3():
    assert get_companies_names([companyList[0]]) == ['Roshan']

def test_get_countries_1():
    assert get_countries([companyList[0]]) == {'Afghanistan': 1}
    
def test_get_countries_2():
    assert get_countries([]) == {}

def test_get_countries_3():
    assert get_countries([companyList[1]]) == {'Albania': 1}

def test_get_countries_4():
    assert get_countries(companyList) == {'Afghanistan': 1, 'Albania': 2}
    
def test_get_companies_1():
    location = {'city': 'Tirana', 'country': 'Albania'}
    assert get_companies(companyList, location) == ['Gjirafa', 'Shqiperia Com']
    
def test_get_companies_2():
    location = {'city': 'Kabul', 'country': 'Afghanistan'}
    assert get_companies(companyList, location) == ['Roshan']

def test_get_companies_3():
    location = {'city': 'Peshawar', 'country': 'Pakistan'}
    assert get_companies(companyList, location) == None
    