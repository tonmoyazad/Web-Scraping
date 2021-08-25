import scrapy

#   Go through each company
#   get name & href

class CompaniesBasicInfoSpider(scrapy.Spider):
    name = 'companies_basic_info'
    allowed_domains = ['www.adapt.io']
    start_urls = ['https://www.adapt.io/directory/industry/telecommunications/A-1']

    def parse(self, response):
# All the companies         
        companies= response.xpath("/html/body/div[1]/div/main/div[2]/div[2]/div[1]/div/div/a")

# Going through every company & getting name & gref
        for company in companies:
            name = company.xpath(".//text()").get()
            url = company.xpath(".//@href").get()

            yield{
                'company_name': name,
                'source_url': url
                }

# Checking if there is a next page
# if yes entering it and starting calling parse function
 
        next_page = response.xpath("//div[@class='DirectoryList_actionBtnLink__Seqhh undefined']/a/@href").get()
        if next:
            yield scrapy.Request(url = next_page, callback=self.parse)