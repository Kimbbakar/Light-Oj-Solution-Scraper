# -*- coding: utf-8 -*-
import scrapy


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


