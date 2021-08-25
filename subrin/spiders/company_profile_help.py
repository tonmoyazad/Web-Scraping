import scrapy


class CompaniesBasicInfoSpider(scrapy.Spider):
    name = 'company_profile_help'
    allowed_domains = ['www.adapt.io']
    start_urls = ['https://www.adapt.io/directory/industry/telecommunications/A-1']

    def parse(self, response):

#   open every company
#    open each department departments 
#     Grab contacts data with department_name they belong

#Looping through companies
        companies= response.xpath("/html/body/div[1]/div/main/div[2]/div[2]/div[1]/div/div/a")
        for company in companies:
            link = company.xpath(".//@href").get()
            yield scrapy.Request(link, callback = self.parse_company)

    def parse_company(self, response):
        
#Grabing company data but this page don't have employee's department info

        company_name = response.xpath("//*[@id='__next']/div/main/div[2]/div[1]/div/div[1]/div[1]/h1/text()").get()
        
#List of employee & must have everyone's department info
        contact_person_list = []


#Company's Departments & next page have contacts list for each department
        departments = response.xpath("//div[@class='ContactsByDepartment_departmentListWrapper__3o6jX']/div/a")
        for department in departments:
            department_name = department.xpath(".//span/text()").get()
            department_link = department.xpath(".//@href").get()
            yield scrapy.Request(department_link, callback = self.parse_contacts, 
                meta={'d_name':department_name,'contacts_list':contact_person_list})


# After this loop yield company infos and nested list->dict hold employee info
         
        yield {
            'company_name': company_name,

        #HAVING PROBLEM HERE: getting empty list here
        # HOW TO GET THE LIST FROM NEXT def parse_contacts??
            'contact_details': contact_person_list
            } 
        
    def parse_contacts(self, response):
        
    #getting data from previous function
        department_name = response.request.meta['d_name']
        contact_person_list = response.request.meta['contacts_list']
        
    #creating emtpy dict for each employee & appending the list contact_person_list
        contacts_dict = {}
        
    # going through each employee from the current department
        persons = response.xpath("//div[@class='TopContacts_roundedBorder__1lCWH undefined']")
        for person in persons:

            contact_name = person.xpath(".//div/a/text()").get()
            
            contacts_dict['contact_name'] = contact_name
            contacts_dict['department_name'] = department_name

            contact_person_list.append(contacts_dict.copy())

        print(contact_person_list)
        
               