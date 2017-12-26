import scrapy
from bs4 import BeautifulSoup
import html5lib
import os

class LojSpider(scrapy.Spider):
    name = 'loj'
    allowed_domains = ['lightoj.com']
    start_urls = ['http://lightoj.com/login_main.php']
    submission_url = 'http://lightoj.com/volume_usersubmissions.php'
    f = open ('E:\Project\Light Oj Solution Scraper\LightOj\done_solution.txt','r') 

    file_list = list()

    for i in f:
        file_list.append(i.strip() )

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

        for idx, tr in enumerate(reversed(trs[1:])): 
            verdict = tr.css('div::text').extract_first().strip()   
            link = tr.css('a')[0] 
 
            if verdict == 'Accepted': 
                yield response.follow(link, callback=self.parse_submission ) 
                
    def parse_submission(self,response):
        soup = BeautifulSoup(response.text,'html5lib' )
 
        code = soup.find('textarea').text
         
        tr = soup.find('table', id='mytable3').find_all('tr')[1]
        tds = tr.find_all('td')
        subid = tr.find('th').text.strip()
        name = tds[2].text.strip()
        pid = name.split('-')[0].strip()

        file_name = 'LightOj '+str(pid)+'.cpp' 


        if pid in self.file_list:
            return
        else:
            print file_name
 
 
        if os.path.isfile('LightOj_Solutions/' + file_name )==False:
            w = open ('E:\Project\Light Oj Solution Scraper\LightOj\done_solution.txt','a') 
            w.write(pid + '\n')
            w.close()
            f = open('LightOj_Solutions/' + file_name,'w' );
            f.write(code)
            f.close()
        else:
            print '--------------------------- Code ID: ' + str(pid) + '-------------------------\n'  + code


            ok = raw_input('This proble\'s code already exist. Want to overwrite? Y/N: ')

            if ok == 'Y':
                f = open('LightOj_Solutions/' + file_name,'w' );
                f.write(code)
                f.close()        