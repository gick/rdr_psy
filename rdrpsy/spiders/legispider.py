import scrapy
import pickle

class RdrSpider(scrapy.Spider):
    name = "rdrspi"
    allowed_domains = ["psychoactif.org"]
    startList=
    start_urls = [
        "https://www.psychoactif.org/forum/ou-trouver-des-seringues.php?a=75000",
    ]

    def parse(self, response):
        for sel in response.selector.css('div[itemtype]'):
	    yield{	 
            	'name' : sel.xpath('.//span/text()').extract_first(),
            	'position':sel.re(r'maps.?google.?[^>]+'),
            	'link' : sel.css('span[itemprop=url]').xpath('ancestor::a/@href').extract(),
            	'tel' :sel.css('span[itemprop=telephone]').xpath('.//text()').extract(),
                'mail': sel.css('span[itemprop=mail]').extract(),
                'streetAdress':sel.css('span[itemprop=streetAddress]').xpath('.//text()').extract(),
                'postalCode':sel.css('span[itemprop=postalCode]').xpath('.//text()').extract(),
                'locality':sel.css('span[itemprop=addressLocality]').xpath('.//text()').extract(),

           	}
            
