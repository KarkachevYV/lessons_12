import scrapy
from myproject.items import LightingSourceItem

class LightingSourcesSpider(scrapy.Spider):
    name = "lighting_sources"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/tver/category/svet"]

    # Инициализация счетчика
    total_lighting_sources = 0

    def parse(self, response):
        # Извлечение информации об источниках света
        lighting_sources = response.css('div._Ud0k')
        for light in lighting_sources:
            self.total_lighting_sources += 1  # Увеличиваем счетчик
            item = LightingSourceItem()
            item['name'] = light.css('div.lsooF span::text').get()
            item['price'] = light.css('div.q5Uds span::text').get()
            item['url'] = response.urljoin(light.css('a::attr(href)').get())
            yield item

        # Проверка и извлечение всех ссылок пагинации
        pagination_links = response.css('a.PaginationLink::attr(href)').getall()
        for link in pagination_links:
            yield response.follow(link, self.parse)

