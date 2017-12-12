# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import html5lib

class LojSpider(scrapy.Spider):
    name = 'loj'
    allowed_domains = ['lightoj.com']
    start_urls = ['http://lightoj.com/login_main.php']
    submission_url = 'http://lightoj.com/volume_usersubmissions.php'

    def parse(self, response):

        self.username = raw_input("Username/Email : ")
        self.userpass = raw_input("Password: ")
 

        return scrapy.FormRequest.from_response(
            response,
            formdata = {
                'myuserid':self.username,
                'mypassword':self.userpass,
            },
            callback = self.after_login

        )

    def after_login(self,response):
        
        if 'login_main.php' in response.text:
            print "Login failed!!!"
            return  

        print "Login Successful !!!"


        yield scrapy.Request(self.submission_url,callback = self.submission )

    def submission(self,response):
        
        return scrapy.FormRequest.from_response(
            response,
            formdata = {'user_password':self.userpass},
            callback = self.all_sub

        )

    def all_sub(self, response):
        

        trs = response.css('#mytable3 tr')  
        for tr in trs[1:]: 
            verdict = tr.css('div::text').extract_first().strip()   
            link = tr.css('a')[0] 
            print (link) 
            if verdict == 'Accepted': 
                print (verdict,link)
                yield response.follow(link, callback=self.parse_submission )
                break
    def parse_submission(self,response):
        soup = BeautifulSoup(response.text,'html5lib' )

        print soup.find('textarea').text