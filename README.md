# Quote Scraper Streamlit App

This is a simple web scraping app built using Streamlit that scrapes quotes and their associated categories from [QuoteFancy](https://quotefancy.com/). Users can input a string, and the app will scrape relevant quotes from the website. Additionally, users can download the scraped data as a CSV file.

## Features

- Input any string to search for quotes.
- Scrape quotes from multiple pages (up to 10 pages).
- Display quotes along with their categories.
- Download the scraped quotes and categories as a CSV file.

## How It Works

1. Enter a search string (for example, `motivation`, `life`, etc.).
2. Click the **Scrape Quotes** button to fetch quotes and their categories.
3. View the scraped quotes and categories in the Streamlit app.
4. Optionally, download the results as a CSV file.

## Installation

To run this project locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/quote-scraper-streamlit.git
cd quote-scraper-streamlit
```
### 2.Create a virtual environment (optional but recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3.Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4.Run the Streamlit app

```bash
streamlit run app.py
```
