#general imports
import sys
import re
import json
from datetime import datetime

def raw_data():

    #picking timestamp
    now = datetime.now()
    
    #raw input for emails
    raw_email = input('Insert yout e-mail address: ')
    # print(raw_email)

    #selecting domain and cleaning comments between '<>'
    domain = raw_email.split('@')[1]
    domain = re.sub(r'<(.*?)>', '', domain)
    # print(domain)

    #picking username befor '@'
    subdomain = raw_email.split('@')[0]
    # print(subdomain)

    mail_treatment = re.sub(r'<(.*?)>', '', subdomain)
    mail_treatment = re.sub(r'\s*\(([^)]*)\)', '', mail_treatment).replace(' ', '')

    if domain.split('.')[0].lower() == 'gmail' or domain.split('.')[0].lower() == 'outlook':
        mail_treatment = mail_treatment.split('+')[0]

    if domain.split('.')[0].lower() == 'gmail':
        mail_treatment = mail_treatment.replace('.', '')
    cleansed_email = mail_treatment + '@' + domain
    
    # print(cleansed_email)

    #catching timestamp and using isoformat to be accepted by json file
    time = datetime.timestamp(now)
    timestamp = datetime.fromtimestamp(time).isoformat()
    # print(timestamp)

    #validating if domain length domain is equal or greator to 2 after '.'
    if len(domain.split('.')[1]) >= 2:
        domain_valid_indicator = True
    else: domain_valid_indicator = False

    # print(domain_valid_indicator)

    #validating username (subdomain)
    if mail_treatment.find('__') or mail_treatment.find(',,') or mail_treatment.find('--'):
        username_valid_indicator = False
    else: username_valid_indicator = True

    #creating dict of results
    result = [{
        'raw_email': raw_email,
        'domain': domain,
        'validation_timestamp': timestamp,
        'doman_valid_indicator': domain_valid_indicator,
        'username_valid_indicator': username_valid_indicator,
        'cleansed_email': cleansed_email
    }]

    #tranforming dict to json
    with open('../data/output.json', 'w') as f:
        json.dump(result, f)



raw_data()