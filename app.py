# app.py (Modified with argument parser, description and epilog)
import os
import argparse
from dotenv import load_dotenv
from utils.scraper import scrape_website

def main():
    # Load environment variables (code unchanged)
    load_dotenv()
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY not found...")
        return

    # Set up argument parser with description and epilog
    parser = argparse.ArgumentParser(
        description="Scrape a website using the Firecrawl API via its Python SDK.",
        epilog="""
Examples:
  # Scrape a single URL (default format: markdown)
  python %(prog)s https://example.com

  # Scrape a URL and request both markdown and HTML formats
  python %(prog)s https://firecrawl.dev --formats markdown html
""",
        formatter_class=argparse.RawTextHelpFormatter # Preserves formatting in epilog
    )

    # Positional argument: URL (Refined help text)
    parser.add_argument(
        "url",
        help="The mandatory URL of the website to scrape."
    )

    # Optional argument: Formats (Refined help text, using %(default)s)
    parser.add_argument(
        "--formats",
        nargs='+',  # Allows one or more values [5]
        default=['markdown'],
        choices=['markdown', 'html'],
        help="Specify desired output formats (space-separated list, e.g., markdown html). Default: %(default)s" # Use specifier [3]
    )

    # Parse arguments (code unchanged)
    args = parser.parse_args()
    target_url = args.url
    output_formats = args.formats

    # Call the scraping function (code unchanged)
    scrape_result = scrape_website(api_key=api_key, url=target_url, formats=output_formats)

    # Print the result (code unchanged)
    if scrape_result:
        print("\n--- Scrape Result ---")
        if 'markdown' in scrape_result:
            print("\n## Markdown Content:\n")
            print(scrape_result['markdown'])
        if 'html' in scrape_result:
            print("\n## HTML Content:\n")
            print(scrape_result['html'])
        print("\n---------------------\n")
    else:
        print("Scraping failed.")

if __name__ == "__main__":
    main()
