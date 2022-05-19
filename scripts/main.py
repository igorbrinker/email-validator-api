import sys
import re
import json
from datetime import datetime

def raw_data():
    now = datetime.now()

    raw_email = input('Insert yout e-mail address: ')
    # print(raw_email)
    domain = raw_email.split('@')[1]
    domain = re.sub(r'<(.*?)>', '', domain)
    print(domain)

    subdomain = raw_email.split('@')[0]
    # print(subdomain)

    mail_treatment = re.sub(r'<(.*?)>', '', subdomain)
    mail_treatment = re.sub(r'\s*\(([^)]*)\)', '', mail_treatment).replace(' ', '')

    if domain.split('.')[0].lower() == 'gmail' or domain.split('.')[0].lower() == 'outlook':
        mail_treatment = mail_treatment.split('+')[0]

    if domain.split('.')[0].lower() == 'gmail':
        mail_treatment = mail_treatment.replace('.', '')
    cleansed_email = mail_treatment + '@' + domain
    
    print(cleansed_email)

    time = datetime.timestamp(now)
    timestamp = datetime.fromtimestamp(time).isoformat()
    print(timestamp)

    if len(domain.split('.')[1]) >= 2:
        domain_valid_indicator = True
    else: domain_valid_indicator = False

    print(domain_valid_indicator)

    # if 

    result = [{
        'raw_email': raw_email,
        'domain': domain,
        'doman_valid_indicator': domain_valid_indicator,
        'validation_timestamp': timestamp,
        'username_valid_indicator': 'true',
        'cleansed_email': cleansed_email
    }]

    with open('../data/output.json', 'w') as f:
        json.dump(result, f)



raw_data()