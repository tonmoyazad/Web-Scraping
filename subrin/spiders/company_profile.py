import scrapy

#   open every company
#    open each department departments 
#     Grab contacts data with department_name they belong

class CompaniesBasicInfoSpider(scrapy.Spider):
    name = 'company_profile'
    allowed_domains = ['www.adapt.io']
    start_urls = ['https://www.adapt.io/directory/industry/telecommunications/A-1']

    def parse(self, response):

        companies= response.xpath("/html/body/div[1]/div/main/div[2]/div[2]/div[1]/div/div/a")
        for company in companies:
            link = company.xpath(".//@href").get()
            yield scrapy.Request(link, callback = self.parse_company)

    def parse_company(self, response):
        
#Grabing company data 

        company_name = response.xpath("//*[@id='__next']/div/main/div[2]/div[1]/div/div[1]/div[1]/h1/text()").get()
        company_location = response.xpath("//span[@class= 'CompanyTopInfo_infoValue__27_Yo' and @itemprop='address']/span/span[@itemprop='addressRegion']/text()").get() + ", " + response.xpath("//span[@class= 'CompanyTopInfo_infoValue__27_Yo' and @itemprop='address']/span/span[@itemprop='addressCountry']/text()").get()
        company_website = response.xpath("//div[@class='CompanyTopInfo_websiteUrl__13kpn']/text()").get()
        company_webdomain = company_website.split('.',1)[1]
        company_industry = response.xpath("//div[@class='CompanyTopInfo_infoItem__2Ufq5'][3]/div[2]/span[@class='CompanyTopInfo_infoValue__27_Yo']/text()").get()
        if company_industry:
            company_employee_size = response.xpath("//div[@class='CompanyTopInfo_infoItem__2Ufq5'][2]/div[2]/span[@class='CompanyTopInfo_infoValue__27_Yo']/text()").get()
            company_revenue = response.xpath("//div[@class='CompanyTopInfo_infoItem__2Ufq5'][1]/div[2]/span[@class='CompanyTopInfo_infoValue__27_Yo']/text()").get()
            pass
        else:
            company_industry = response.xpath("//div[@class='CompanyTopInfo_infoItem__2Ufq5'][2]/div[2]/span[@class='CompanyTopInfo_infoValue__27_Yo']/text()").get()
            company_revenue = None
            company_employee_size = response.xpath("//div[@class='CompanyTopInfo_infoItem__2Ufq5'][1]/div[2]/span[@class='CompanyTopInfo_infoValue__27_Yo']/text()").get()
        
        

# declearing empty list which will hold every employee's data in dict         
        contact_person_list = []
        contacts_dict = {}

# Grabing employee data 
        persons = response.xpath("//div[@class='TopContacts_roundedBorder__1a3yB undefined']")
        for person in persons:
            contact_name = person.xpath(".//div/a/text()").get()
            contact_jobtitle = person.xpath("./p[@class='TopContacts_jobTitle__3M7A2' and @itemprop='jobTitle']/text()").get()

# Asserting employee detail in contacts_dict            
            contacts_dict['contact_name'] = contact_name
            contacts_dict['contact_jobtitle'] = contact_jobtitle
            contacts_dict['Contact_email_domain'] = company_webdomain

# employee info dict transfered into the list 
            contact_person_list.append(contacts_dict.copy())

        yield {
            'company_name': company_name,
            'company_location': company_location,
            'company_website': company_website,
            'company_webdomain': company_webdomain,
            'company_industry': company_industry,
            'company_employee_size': company_employee_size,
            'company_revenue': company_revenue,
            'contact_details': contact_person_list
            } 

        next_page = response.xpath("//div[@class='DirectoryList_actionBtnLink__Seqhh undefined']/a/@href").get()
        if next_page:
            yield scrapy.Request(url = next_page, callback=self.parse)


#Company's Departments & next page have contacts list for each department
  
        #departments = response.xpath("//div[@class='ContactsByDepartment_departmentListWrapper__3o6jX']/div/a")
        #for department in departments:
            #department_name = department.xpath(".//span/text()").get()
            #department_link = department.xpath(".//@href").get()
            #yield scrapy.Request(department_link, callback = self.parse_contacts, meta={'d_name':department_name,'c_name':company_name,'contacts_list':contact_person_list})


# After this loop yield company infos and nested list->dict hold employee info
         
       #yield {
       #     'company_name': company_name,

        #HAVING PROBLEM HERE: getting empty list here
        #    'contact_details': contact_person_list
        #    } 
        
    #def parse_contacts(self, response):
        #department_name = response.request.meta['d_name']
        #company_name = response.request.meta['c_name']
        #contact_person_list = response.request.meta['contacts_list']
        

        #contacts_dict = {}
        #persons = response.xpath("//div[@class='TopContacts_roundedBorder__1lCWH undefined']")
        #for person in persons:

            #contact_name = person.xpath(".//div/a/text()").get()
            #contact_jobtitle = person.xpath("./p[@class='TopContacts_jobTitle__1HIPn' and @itemprop='jobTitle']/text()").get()
            
            #contacts_dict['contact_name'] = contact_name
            #contacts_dict['contact_jobtitle'] = contact_jobtitle
            #contacts_dict['department_name'] = department_name

            #contact_person_list.append(contacts_dict.copy())



       