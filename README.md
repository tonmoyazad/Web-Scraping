# Subrin Al Azad

This scripts was developed for the lead book and it was build with python with scrapy frame work. 
You can find my code in spiders folder. 
file name "companies_basic_info" is for the first task and "company_profile" for the second task. 

Output are in json files.
For the first task's output can be found as 'company index'
and Second task's json output as 'company_profiles'

Architecture is of the first task's script:
1. Looping through every companies that holds the url as href & name of the company as text 
2. Scraping them in two variables name & url for each company
3. After going through each company check if there a next page 
4. If there is a next page go to that page and repeat 1 

Architecture is of the second task's script:
1. Looping through every companies that holds the url as href & name of the company as text 
2. Open each url and get information of the company
3. There need to be implement some checks because on some company profile some datas are missing 
    and this creates tourble to store the data in the correct key
4. They it's time to get data of company's contacts the trickest part of this project starts here
5. Under every company there will be a nest list which will hold dicts of contacts 
