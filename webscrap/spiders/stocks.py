import scrapy
import csv
from ..items import WebscrapItem
from scrapy.http import FormRequest

opt1,opt2,opt3,opt4,opt5,opt6,opt7='trending-stocks','52-week-low','52-week-high','most-active-stocks','top-stock-gainers','top-stock-losers','All'
n = int('1')

class QuoteSpider(scrapy.Spider):
    name = 'info'
    
    print(f"1-{opt1.upper()}\n2-{opt2.upper()}\n3-{opt3.upper()}\n4-{opt4.upper()}\n5-{opt5.upper()}\n6-{opt6.upper()}\n7-{opt7}")
    cini = "opt"+input("\nEnter Your Choice: ")
    c = eval(f'{cini} ')   
    if c.lower()=='all' or c=='opt7':
        url = [f'https://in.investing.com/equities/{it}' for it in (opt1,opt2,opt3,opt4,opt5,opt6)]
        start_urls = url
    else:
        url = f'https://in.investing.com/equities/{c}'
        start_urls = [url]
    n=int('1')
    def start_requests(self):
        for url in QuoteSpider.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
            
    def parse(self, response):
        items = WebscrapItem()
        global n
        block = response.css('.js-section-content')
        items['name'] = block.css('.medium .js-instrument-page-link::text').extract()
        items['last'] = block.css('.medium .u-clickable .col-last .text::text').extract() 
        items['high'] = block.css('.u-clickable .col-high .text::text').extract() 
        items['low'] = block.css('.u-clickable .col-low .text::text').extract()
        items['chg'] = block.css('.medium .u-clickable .col-chg .text::text').extract()
        items['chgper'] = block.css('.medium .u-clickable .col-chg_pct .text::text').extract()
        items['volume'] = block.css('.u-clickable .col-volume .text::text').extract()
        yield items
        
        #file_name = input("Enter file name")+'.csv'
        self.opt1,self.opt2,self.opt3,self.opt4,self.opt5,self.opt6=opt1,opt2,opt3,opt4,opt5,opt6
        if QuoteSpider.c.lower()=='all' or QuoteSpider.c=='opt7':
            self.file_name = eval('opt{}'.format(n))+".csv"
        else:
            self.file_name = eval('{}'.format(QuoteSpider.cini))+".csv"
        n+=1
        with open(self.file_name,'w') as f:
            #ieldnames = ['change','change%','high','last','low','name','volume']
            writer = csv.DictWriter(f,items.keys())
            writer.writeheader()
            w=csv.writer(f)
            data = zip(items['name'],items['last'],items['high'],items['low'],items['chg'],items['chgper'],items['volume'])
            w.writerows(data)
        print("\n*******Stock Data Has Been Downloaded********")    
            
            #for k,v in items.items():
                #for val in v:
                    #writer.writerow({k:val})
            #f=f.dropna()
        
        #next_page = response.css('li.next a::attr(href)').get()
        #if next_page is not None:
            #yield response.follow(next_page,callback=self.parse)
        