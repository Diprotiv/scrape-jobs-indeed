from angelScrap.angelScrap.spiders.job_spider import start_job_spider

if __name__ == "__main__":
    print("Starting to crawl...")
    start_job_spider("Java", "Kolkata")
    print("Contents saved to json file successfully.")

