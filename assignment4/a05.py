# Your code for get_companies_names goes here


def get_companies_names(company_list):
    req_list = []
    for i in company_list:
        a = i["Company Name"]
        req_list.append(a)
    return req_list






# Your code for get_countries goes here

def get_countries(company_list):
    req_dict = {}
    for i in company_list:
        x = i["Country"]
        if x in req_dict:
            y = req_dict[x]
            y = y+1
            req_dict[x] = y
        else:
            req_dict[x] = 1
    return req_dict





# Your code for get_companies goes here

def get_companies(company_list,location):
    req_list = []
    for i in company_list:
        if i["Country"]== location["country"] and i["City"]== location["city"]:
            a = i["Company Name"]
            req_list.append(a)
    if req_list==[]:
        return None
    return req_list
    
    
    
    
