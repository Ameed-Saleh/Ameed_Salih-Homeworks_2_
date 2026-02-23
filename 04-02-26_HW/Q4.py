'''
Question 4 – Post office delivery (f-string)
For a post office delivery, input the following details from the user:

last name
first name
country
city address
zipcode
Fixes & Requirements
The last name string must be uppercase
-- Use a while loop and isupper to validate the last name input
The first name string must be lowercase
-- Use a while loop and islower to validate the first name input
The country string length must be at most 3 letters (for example: US, IL)
-- Use a while loop and isalpha len to validate the country input
The zipcode must contain digits only and be at least 4 digits
-- Use a while loop and isdigit len to validate the zipcode input
Output Format
FOR: COHEN, danny
COUNTRY: IL
ADDRESS: Tel Aviv
ZIPCODE: 12345

Use print(f"...")

FOR: {last-name}, {first-name}
COUNTRY: {country}
ADDRESS: {city address}
ZIPCODE: {zipcode}
'''

import time

last_name = str("PErETZ")
while True:
    if last_name.isupper():
        print("valid")
        break
    else:
        last_name = last_name.upper()
        break

first_name= str("daNny")
while True:
    if first_name.islower():
        print("valid")
        break
    else:
        first_name = first_name.lower()
        break

country = str("IL58")
while True:
    if country.isalpha() and len(country) <= 3 and country.isupper():
        break
    else:
        country = str(input("enter country (capital only, max letters 3): "))
        continue

city_address = str(" tEL aviV ")
while True:
    city_address = city_address.title()
    break

zipcode = str("  20128  ")
while True:
    zipcode = zipcode.strip()
    if zipcode.isdigit() and len(zipcode) >= 4:
        break
    else:
        zipcode = str(input("enter zipcode (digit only, at least 4): "))
        continue
time.sleep(2)
print(" - "*20)
print("details of post office delivery")
print(f"FOR : {last_name},{first_name}")
print(f"COUNTRY : {country}")
print(f"ADDRESS : {city_address}")
print(f"ZIPCODE :{zipcode}")