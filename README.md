# Subrin Al Azad

Scripts were developed for the lead book and it was built with python with scrapy framework. 
You can find my code in the spiders folder. 
filename "companies_basic_info" is for the first task and "company_profile" is for the second task. 

Outputs are in JSON files.
For the first task's output can be found as 'company index'
and Second task's JSON output as 'company_profiles'

Architecture is of the first task's script:
1. Looping through every company that holds the url as href & name of the company as text 
2. Scraping them in two variables name & url for each company
3. After going through each company check if there a next page 
4. If there is a next page go to that page and repeat 1 

Architecture is of the second task's script:
1. Looping through every company that holds the URL as href & name of the company as text 
2. Open each URL and get information about the company
3. There need to implement some checks because on some company profiles some data are missing 
    and this creates trouble to store the data in the correct key
4. Then it's time to get data of company's contacts the trickest part of this project starts here
5. Under every company there will be a nest list which will hold dicts of contacts 


# This wasn't loaded to database yet.

