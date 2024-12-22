import csv

class MyprojectPipeline:
    def open_spider(self, spider):
        self.file = open('lighting_sources.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['name', 'price', 'url'])
    
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow([item['name'], item['price'], item['url']])
        return item
