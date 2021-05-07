import requests
import urllib.request
import json

''' This is a Python program to get the center details for the COVID-19 Vaccine program for any pincode in India 
    The output will show the details like Center Name, Timing, Fee type, Vaccine Capacity and Age limit.'''

pin = input('Enter your area Pincode - ')
id = str.strip(pin)
if len(id) == 6:
    date_id = input('Enter vaccination date in DD-MM-YYYY format year has to be 2021 - ')
    date = str.strip(date_id)
else:
    print('Not a valid Pincode:')
    exit()
url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={id}&date={date}'.format(id = id,date=date)

req_obj = urllib.request.urlopen(url)
content = req_obj.read()
content_json = json.loads(content)
if content_json['centers'] == []:
    print('Sorry! No center found for the given date, Try another date. ')
else:
    print('Details of Center:')
    print('------------------\n')
    for key in content_json:
        for child_key in content_json[key]:
            print('Center Name :',child_key["name"])
            print('District :',child_key["district_name"])
            print('Address :',child_key["address"])
            print('Timing from :',child_key["from"])
            print('Timing To :',child_key["to"])
            print('Fee type:',child_key["fee_type"])
            print('Vaccine Capacity:',child_key["sessions"][0]["available_capacity"])
            print('Minimum age limit:',child_key["sessions"][0]["min_age_limit"])
            print('Vaccine Type:',child_key["sessions"][0]["vaccine"])
            print('*************************************************\n')
