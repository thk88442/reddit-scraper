import re
import scrapy
from reddit.items import RedditItem

class RedditCrawler(scrapy.Spider):
    name = 'redditSpider'
    allowed_domain = 'reddit.com'

    def start_requests(self):
        urls = [ #enter your subreddits as below ex. https://www.reddit.com/r/AskReddit/
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for main_div in response.css('div.s1us1wxs-0.iENbwa.s12rq52u-0.jNBfJm > div'):

            title = main_div.css("a[data-click-id='body'] > h2::text").extract_first()

            subreddit = response.css("button.h-jI8r2f9ozTNqu_2TBeY > span._1GieMuLljOrqnVpRAwz7VP::text").extract_first()

            comment_num = main_div.css('span.FHCV02u6Cp2zYL0fhQPsO::text').extract_first()

            upvotes = main_div.css('div._1rZYMD_4xY3gRcSS3p8ODO::text').extract_first()

            yield {
                'title': title,
                'subreddit': subreddit,
                'comment_num': comment_num,
                'upvotes': upvotes,
            }

    # next_page = response.css('span.next-button a::attr(href)').extract_first()
    # url = response.urljoin(next_page)
    # yield scrapy.Request(url=url, callback = self.parse)

