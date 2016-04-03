import scrapy

class RdrItem(scrapy.Item):
    organisation_type =scrapy.Field()
    organisation_name = scrapy.Field()
    geo_position = scrapy.Field()
    link = scrapy.Field()
    tel = scrapy.Field()    
    mail = scrapy.Field()
    street_adress = scrapy.Field()
    postal_code=scrapy.Field()
    locality=scrapy.Field()


class RdrComment(scrapy.Item):
    mail =scrapy.Field()
    comment = scrapy.Field()
   