# Firecrawl Web Scrapper CLI 🔥   
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Unleash the power of Firecrawl directly from your terminal! This Python script leverages the `firecrawl-py` SDK to effortlessly scrape web pages, extracting clean Markdown or raw HTML content. 
Built with modern tooling (`uv` for environment/package management) and best practices (`.env` for API keys, modular structure). 
Just provide a URL and go!   

## ✨ Features   
* Scrape content from any public URL using the Firecrawl API.
* Specify desired output formats: `markdown` and/or `html`. 
* Simple Command-Line Interface (CLI).
* Uses `uv` for fast and efficient virtual environment and package management.
* Securely manages your Firecrawl API key using a `.env` file.
* Modular code structure using a `utils` package.
* Includes `.gitignore` configured for Python projects and sensitive files.

## 📋 Prerequisites 
* Python 3.8+
* [uv](https://github.com/astral-sh/uv) (Python package installer and virtual environment manager)
 * Installation instructions are on the `uv` GitHub page (often `pipx install uv` or `pip install uv`).
 * A Firecrawl API Key (Get yours from [firecrawl.dev](https://firecrawl.dev/))

## 🚀 Installation & Setup
1.  **Clone the repository:**

```bash
git clone
https://github.com/topogoogles/firecrawl-web-scrapper.git
cd firecrawl-web-scrapper
 ```

2. **Create and activate the virtual environment using `uv`**:
```bash
# Create the environment (in a .venv directory)
uv venv
# Activate the environment
# Linux/macOS:
source .venv/bin/activate
# Windows (Git Bash):
source .venv/Scripts/activate
# Windows (Command Prompt):
.venv\Scripts\activate.bat 
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
```
3.  **Install dependencies using `uv`:**
```bash
uv pip install -r requirements.txt
```
 ## ⚙️ Configuration
 1.  **Create a `.env` file** in the project root directory:
```
touch .env
```
2.  **Add your Firecrawl API key** to the `.env` file:
``` 
 FIRECRAWL_API_KEY="fc-YOUR_API_KEY"
```
Replace `fc-YOUR_API_KEY` with your actual Firecrawl API key.   **Important:** The `.env` file is listed in `.gitignore` and should **never** be committed to version control.

## ▶️ Usage
Make sure your virtual environment is activated before running the script.   The script requires one positional argument: the `url` to scrape. You can optionally specify the output `formats`.
1. **Basic Scrape (Default format: Markdown):**
    ```
    python app.py https://example.com
   ```

2. **Scrape with Specific Formats:**
Use the `--formats` flag followed by one or more format choices (`markdown`, `html`).
   ```bash
   python app.py https://firecrawl.dev      --formats markdown html
   ```
3. **Getting Help:**
To see the available options, arguments, and usage examples, use the `-h` or `--help` flag:
   ```
   python app.py --help
   ```
   This will display output similar to:
   Usage:
   ```bash
   app.py [-h] [--formats FORMATS [FORMATS ...]] url # Scrape a website using the Firecrawl API via its Python SDK.
   ```
   Positional arguments:
   ```bash
   url # The mandatory URL of the website to scrape.   
   ```
   Options:
   ```bash
   -h, --help # Show this help message and exit 
   --formats FORMATS [FORMATS ...] #    Specify desired output formats (space-separated list, e.g., markdown html). Default: ['markdown']
   ```
   Examples:
   ```bash
   # Scrape a single URL (default format: markdown)
   python app.py https://example.com

   # Scrape a URL and request both markdown    and HTML formats
   python app.py https://firecrawl.dev --formats markdown html
   ```

## 📂 Project Structure
```bash
firecrawl-web-scrapper/   
  ├── .env # Stores API keys (DO NOT COMMIT)  
  ├── .gitignore # Specifies intentionally untracked files for Git  
  ├── .venv/ # Virtual environment directory (created by uv)  
  ├── app.py # Main application script (entry point)  
  ├── requirements.txt # Project dependencies  
  └── utils/  
     ├── __init__.py # Makes 'utils' a Python package  
     └── scraper.py # Module containing the Firecrawl interaction logic
```

# Module containing the Firecrawl interaction logic

## 📦 Version Control 

This project is set up with Git. The `.gitignore` file ensures that sensitive information (`.env`) and unnecessary files (`.venv`, `__pycache__`) are not tracked. Remember to commit your changes and push them to your GitHub repository.

## 🤝 Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue. If you'd like to contribute code, please open a pull request.   

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

