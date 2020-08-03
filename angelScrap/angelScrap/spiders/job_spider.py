import scrapy
from scrapy.crawler import CrawlerProcess

from angelScrap.angelScrap import settings
from angelScrap.angelScrap.items import JobItem


class JobSpider(scrapy.Spider):
    name = "job"

    base_url = "https://www.indeed.co.in"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        job_type = kwargs["job_type"]
        location = kwargs["location"]
        self.start_urls = [f"{self.base_url}/jobs?q={job_type}&l={location}"]

    def parse(self, response):
        for job in response.css("div.jobsearch-SerpJobCard"):
            item = JobItem()
            item["title"] = job.css("h2.title a::attr(title)").get().strip()
            item["company"] = job.css(".company::text").get()
            item["location"] = job.css("div.location::text").get()
            item["remote"] = job.css("span.remote::text").get()
            item["job_link"] = f"{self.base_url}{job.css('h2.title a::attr(href)').get()}"
            item["salary"] = job.css("span.salaryText::text").get()
            item["summary"] = " ".join(job.css("div.summary li::text").getall())
            item["date"] = job.css("span.date::text").get().strip()
            yield item
        next_page = response.css("ul.pagination-list li")[-1].css("a::attr(href)").get()
        if next_page is not None:
            print("Extracting next page...")
            yield response.follow(f"{self.base_url}{next_page}", callback=self.parse)

def start_job_spider(job_type="Python", location="Mumbai"):
    process = CrawlerProcess()
    process.settings.setmodule(settings)
    process.crawl(JobSpider, job_type=job_type, location=location)
    process.start()

