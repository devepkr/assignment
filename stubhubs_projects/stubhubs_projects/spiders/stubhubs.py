# stubhubs_spider.py
# Scrapy spider to extract sports event data from StubHub's explore page

import scrapy
import json
from stubhubs_projects.items import StubhubsProjectsItem

class StubhubsSpider(scrapy.Spider):
    name = "stubhubs"
    allowed_domains = ["www.stubhub.com"]
    start_urls = [
        "https://www.stubhub.com/explore?method=getExploreEvents&lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&tlcId=2"
    ]

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        """
        Generate initial requests for the start URLs with custom headers.
        """
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, callback=self.parse_api)

    def parse_api(self, response):
        """
        Parse the JSON response and extract event data.
        """
        if response.status != 200:
            self.logger.error(f"Failed to fetch data: HTTP {response.status}")
            return

        try:
            data = json.loads(response.body)
            events = data.get('events', [])
            n = len(events)
            print(n)
            # Ensure at least 5 events are processed (or all available if fewer)
            for item in events[:5]:
                stub_item = StubhubsProjectsItem()
                
                stub_item['title'] = item.get('name', 'N/A')
                formatted_date = item.get('formattedDateWithoutYear', '')
                formatted_time = item.get('formattedTime', '')
                stub_item['datetime'] = f"{formatted_time} {formatted_date}".strip() or 'N/A'
                stub_item['location'] = item.get('venueName', 'N/A')
                stub_item['images'] = item.get('imageUrl', 'N/A')
                yield stub_item

        except json.JSONDecodeError:
            self.logger.error("Failed to parse JSON response")
        except Exception as e:
            self.logger.error(f"Error processing response: {str(e)}")