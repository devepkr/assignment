# StubHub Events Scraper Documentation

## Overview
This Scrapy project is designed to scrape sports event data from StubHub's explore page (specifically from the provided URL). The scraper extracts at least 5 events, each containing the event title, datetime, location, and image URL, and outputs the data in JSON format.

## Project Structure
The project follows a standard Scrapy structure:
- **stubhubs_spider.py**: Contains the `StubhubsSpider` class that defines the crawling logic.
- **items.py**: Defines the `StubhubsProjectsItem` class for structuring scraped data.
- **pipelines.py**: Implements a pipeline to validate and process scraped items.
- **settings.py**: Configures Scrapy settings, including JSON output and crawling behavior.

## Setup Instructions
1. **Install Scrapy**:
   pip install scrapy
   

2. **Create Project Directory**:
   Create a new Scrapy project or place the provided files in the appropriate directories:
   - Place `stubhubs_spider.py` in `stubhubs_projects/spiders/`.
   - Place `items.py`, `pipelines.py`, and `settings.py` in `stubhubs_projects/`.

3. **Directory Structure**:
   
   stubhubs_projects/
   ├── scrapy.cfg
   ├── stubhubs_projects/
   │   ├── __init__.py
   │   ├── items.py
   │   ├── pipelines.py
   │   ├── settings.py
   │   ├── spiders/
   │   │   ├── __init__.py
   │   │   ├── stubhubs_spider.py
   

4. **Run the Spider**:
   Navigate to the project directory and run:
   scrapy crawl stubhubs
   
   This will output the scraped data to `events.json`.

## Code Explanation
### stubhubs_spider.py
- **Purpose**: Defines the spider that sends HTTP requests and parses the JSON response.
- **Key Components**:
  - `name`: Set to `"stubhubs"` to identify the spider.
  - `allowed_domains`: Restricts crawling to `www.stubhub.com`.
  - `start_urls`: Contains the provided URL with encoded parameters.
  - `headers`: Mimics a browser to avoid being blocked.
  - `start_requests`: Generates requests with custom headers.
  - `parse_api`: Parses the JSON response, extracts event data, and yields `StubhubsProjectsItem` instances.
- **Error Handling**:
  - Checks for HTTP status code.
  - Handles JSON decoding errors and other exceptions with logging.

### items.py
- **Purpose**: Defines the `StubhubsProjectsItem` class with fields for `title`, `datetime`, `location`, and `images`.
- **Usage**: Used by the spider to structure scraped data.

### pipelines.py
- **Purpose**: Implements `StubhubsProjectsPipeline` to validate and clean scraped items.
- **Functionality**: Ensures all fields are non-empty, replacing missing values with `'N/A'`.

### settings.py
- **Purpose**: Configures Scrapy settings for optimal crawling and JSON output.
- **Key Settings**:
  - `FEED_FORMAT` and `FEED_URI`: Outputs scraped data to `events.json`.
  - `ROBOTSTXT_OBEY`: Ensures compliance with robots.txt.
  - `DOWNLOAD_DELAY`: Adds a 3-second delay to avoid server overload.
  - `ITEM_PIPELINES`: Enables the custom pipeline.

## Output
The scraper produces a JSON file (`events.json`) with at least 5 events, each containing:
- `title`: Event name.
- `datetime`: Combined time and date of the event.
- `location`: Venue name.
- `images`: URL to the event image.

Example output:
```json
[
  {
    "title": "Event Name 1",
    "datetime": "7:00 PM Jan 15",
    "location": "Venue Name 1",
    "images": "https://stubhub.com/image1.jpg"
  },
  ...
]
```

## Notes
- The provided URL uses encoded latitude and longitude parameters, which are preserved in the spider.
- The spider ensures at least 5 events are extracted (or all available if fewer than 5).
- The code includes robust error handling to manage network issues or malformed JSON.
- The project adheres to Scrapy best practices, including modularity, clear comments, and proper configuration.

## Troubleshooting
- **No data in output**: Verify the URL is accessible and returns valid JSON.
- **HTTP errors**: Check the `headers` configuration or try updating the user-agent.
- **Missing fields**: The pipeline ensures all fields have values, defaulting to `'N/A'` if missing.