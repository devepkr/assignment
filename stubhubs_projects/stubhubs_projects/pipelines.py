# pipelines.py
# Pipeline to process and validate scraped items

class StubhubsProjectsPipeline:
    def process_item(self, item, spider):
        """
        Validate and process each scraped item.
        """
        # Ensure all fields are present and not empty
        for field in ['title', 'datetime', 'location', 'images']:
            if not item.get(field):
                item[field] = 'N/A'
        return item