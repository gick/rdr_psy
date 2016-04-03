from scrapy.loader import ItemLoader
from scrapy import exporters
import scrapy
import logging
import pickle
from operator import itemgetter




class RdrComment(scrapy.Item):
    mail =scrapy.Field()
    comment = scrapy.Field()
   
class RdrSpider(scrapy.Spider):
    name = "rdr"
    start_urls=[]
    allowed_domains = ["psychoactif.org"]
    postcodelist=pickle.load(open('/home/pgicquel/villeEx','rb'))
    for code in postcodelist :
        start_urls.append('https://www.psychoactif.org/forum/ou-trouver-des-seringues.php?a=' + code)
    print start_urls    

    def constructComment(self,sel):
        rdrComm=RdrComment()
        commentBind=[]     
        commentList = sel.xpath('./parent::*').css('.comment')
        for comment in commentList:
            commentArray=[]
            commentArray.append(comment.css('::text').extract());
            commentArray.append(comment.css('strong>a[href]').extract())
            commentArray.append(comment.css('strong>a[href]::text').extract())
            commentBind.append(commentArray)
        return commentBind    

    def parse(self, response):
        commentList=[]
        
        for sel in response.selector.css('div[itemtype]'):
            commentList.append(self.constructComment(sel))
        a=[]
      
        for index,sel in enumerate(response.selector.css('div[itemtype]')):       
           d=dict({	 
                'type' : sel.xpath('./parent::*/parent::*/parent::*').css('div>b::text').extract(),
            	'name' : sel.xpath('.//span/text()').extract_first(),
            	'position':sel.re(r'maps.?google.?[^>]+'),
            	'link' : sel.css('span[itemprop=url]').xpath('ancestor::a/@href').extract(),
            	'tel' :sel.css('span[itemprop=telephone]').xpath('.//text()').extract(),
                'mail': sel.css('span[itemprop=mail]').extract(),
                'streetAdress':sel.css('span[itemprop=streetAddress]').xpath('.//text()').extract(),
                'postalCode':sel.css('span[itemprop=postalCode]').xpath('.//text()').extract(),
                'locality':sel.css('span[itemprop=addressLocality]').xpath('.//text()').extract(),        
                })
           a.append(d)
        newlist = sorted(a, key=itemgetter('postalCode'))    
        return newlist