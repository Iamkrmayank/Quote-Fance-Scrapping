import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("Quote Scraper")

user_input = st.text_input("Enter a string:")

if st.button("Scrape Quotes"):
    if user_input:
        # Normalize the input string: replace spaces and periods with hyphens, and convert to lowercase
        dashed_string = "-".join(user_input.replace(".", "").lower().split())
        quotes = []

        for i in range(1, 11):
            url = f"https://quotefancy.com/{dashed_string}/page/{i}"
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                quote_containers = soup.find_all('div', class_='q-wrapper')

                for container in quote_containers:
                    quote_link = container.find('a', class_='quote-a')
                    quote_text = quote_link.text if quote_link else 'No quote found'

                    author_paragraphs = container.find_all('p', class_='author-p')
                    categories = []
                    for author_paragraph in author_paragraphs:
                        category_elements = author_paragraph.find_all('a')
                        for category in category_elements:
                            categories.append(category.text)

                    # Each row is a quote followed by its categories
                    quotes.append([quote_text] + categories)

        # Displaying quotes and categories
        st.write("Quotes and Categories:")
        for quote_row in quotes:
            st.write(f"- *Quote:* {quote_row[0]}")
            st.write(f"  *Categories:* {', '.join(quote_row[1:])}")

        # Creating headers based on the maximum number of categories found
        max_categories = max(len(quote_row) - 1 for quote_row in quotes)
        headers = ["Quote"] + [f"Category {i+1}" for i in range(max_categories)]
        
        # Creating a DataFrame to handle variable-length categories
        df = pd.DataFrame(quotes, columns=headers)

        # Exporting DataFrame to CSV format
        csv_data = df.to_csv(index=False)

        # Providing a download button for the CSV file
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name=f"quotes_with_{user_input}.csv",
            mime="text/csv",
        )
    else:
        st.warning("Please enter a string to scrape quotes.")
