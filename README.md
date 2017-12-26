# Light-Oj-Solution-Scraper

To run this locally, we need to have a couple of things in our environment.

```
python 2
Scrapy==1.4.0
beautifulsoup4==4.6.0
```

Or after installing python 2, you can run only this command.

```
pip requirements.txt -r install
```

Then just run this command from the root of this project.
```
scrapy crawl loj
```

It will ask your LightOj ID/Email and Password. After that, it will create a LightOj-Solutions folder inside the project.

## Acknowledgments
All credit goes to this [blog](https://sjsakib.github.io/2017/scraping-lightoj-part-i/). It helps me to write this and download my own [lightoj solution](https://github.com/Kimbbakar/LightOj-Solutions)
