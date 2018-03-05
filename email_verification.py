#connect
import json
from collections import defaultdict
import tldextract
import os
import re
import csv
import time
import neverbounce_sdk
import unidecode


input_filename = 'emails.csv'
if len(sys.argv) > 1:
    input_filename = sys.argv[1]

emails_to_check = []
with open(input_filename, 'r') as csvfile:
    csvreader = = csv.reader(csvfile)
    for row in csvreader:
        emails_to_check.append(row[0])




def check_domain(url):
    # Check if there is a mail server at the domain
    __query = 'nslookup -q=mx {0}'
    __pattern = '\*\*\sserver\scan\'t\sfind'

    def check_for_mx_record(domain):
        try:
            command = __query.format(domain)
            with os.popen(command) as response:
                result = response.readlines()
                return all(re.match(__pattern,l) == None for l in result)
        except Exception:
            return False
    clean = clean_domain(url)
    has_record = check_for_mx_record(clean)
    
    if has_record:
        return clean
    else:
        return False

def fix_utf8(s):
    if isinstance(s, unicode):
        return s.encode('utf8', 'replace')
    elif not isinstance(s, basestring):
        s = str(s)
    return s.decode('utf8', 'replace').encode('utf8')

email_results = []
for email in all_emails_to_check:
    try:
        parts = email.split('@')
        domain = parts[1]
    except:
        print 'Invalid email: ', email
        continue

    res = check_domain(domain)
    if res:
        email_results.append(parts[0] + '@' + domain)

with open('output.csv', 'w+') as csvfile:
    csvwriter = csv.writer(csvfile)
    for email in email_results:
        csvwriter.writerow(email)
