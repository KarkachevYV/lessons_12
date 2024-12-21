import scrapy

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
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.q5Uds span::text').get(),
                'url': light.css('a').attrib['href']
            }

        # Проверка и извлечение всех ссылок пагинации
        pagination_links = response.css('a.PaginationLink::attr(href)').getall()
        for link in pagination_links:
            if link and response.urljoin(link) != response.url:
                yield response.follow(link, self.parse)
        
    def closed(self, reason):
        # Выводим общее количество после завершения работы паука
        self.log(f"Общее количество источников освещения: {self.total_lighting_sources}")