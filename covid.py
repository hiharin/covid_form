# Autofill Google Form
import requests
from datetime import date

# URL to the form you want to fill. formResponse should be used instead of viewform
#urlView = 'https://docs.google.com/forms/d/e/1FAIpQLSfyS8JR7COVkiu3T6qbFfefyAmwBx55h0xRgx_wuXyxeXo2YQ/viewform'
#urlRes = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfyS8JR7COVkiu3T6qbFfefyAmwBx55h0xRgx_wuXyxeXo2YQ/formResponse"

#test urls
urlView = "https://docs.google.com/forms/d/e/1FAIpQLSeQPXSFj5Zqe2866YAtiVv14wWKYY1GB9PV6fjnwv85TbFtGw/viewform"
urlRes = "https://docs.google.com/forms/d/e/1FAIpQLSeQPXSFj5Zqe2866YAtiVv14wWKYY1GB9PV6fjnwv85TbFtGw/formResponse"

def send_covid_screen(id, firstName, lastName, school):

    values = {
        # student id
        "entry.600030874": id,
        # first name
        "entry.1039936616": firstName,
        # last name
        "entry.332004738": lastName,
        # school
        "entry.1281858889": school,
        # magic answers.....
        "entry.862559759": "No",
        "entry.2066453226": "No",
        "entry.1792770653": "No",
        "entry.1935346097": "No",
        "entry.1935346097_sentinel": "",
        "entry.1792770653_sentinel": "",
        "entry.2066453226_sentinel": "",
        "entry.862559759_sentinel": ""
    }
    today = date.today()
    session = requests.Session()
    
    r = session.get(urlView)
    #print(r.text)

    r = session.post(urlRes, data=values)

    if r.status_code == requests.codes.ok:
        print(values)
        print( "Yippi ", today)
    else:
        print("error occured ", today)


send_covid_screen("2028020061", "Duncan", "West", "MLS")
send_covid_screen("2026020075", "Isabella", "West", "FMS")