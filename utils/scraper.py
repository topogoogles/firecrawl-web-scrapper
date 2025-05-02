# utils/scraper.py
from firecrawl import FirecrawlApp

def scrape_website(api_key: str, url: str, formats: list = ['markdown']) -> dict | None:
    """
    Scrapes a given URL using the Firecrawl API.

    Args:
        api_key: The Firecrawl API key.
        url: The URL to scrape.
        formats: A list of desired output formats (e.g., ['markdown', 'html']).

    Returns:
        A dictionary containing the scrape status and data, or None if an error occurs.
    """
    if not api_key:
        print("Error: Firecrawl API key not found.")
        return None
    if not url:
        print("Error: URL not provided.")
        return None

    try:
        app = FirecrawlApp(api_key=api_key)
        print(f"Scraping URL: {url} with formats: {formats}")
        scrape_result = app.scrape_url(url, params={'pageOptions': {'formats': formats}})
        # The SDK returns the data directly if successful, check if it's the expected dict
        if isinstance(scrape_result, dict) and 'markdown' in scrape_result or 'html' in scrape_result:
             return scrape_result
        else:
            print(f"Error: Unexpected response format from Firecrawl: {scrape_result}")
            return None
    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return None

# Example of how you might add the crawl functionality later
# from firecrawl import ScrapeOptions
# def crawl_website(api_key: str, url: str, limit: int = 10, formats: list = ['markdown']) -> dict | None:
#     """ Crawls a website starting from the given URL. """
#     # ... implementation ...

