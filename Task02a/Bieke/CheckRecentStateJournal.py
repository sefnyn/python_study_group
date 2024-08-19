import os # For removing the temp.pdf file after browsing through it
import requests # For interacting with the web
from datetime import datetime, timedelta # For getting current date and calculating the date of X days ago 
from PyPDF2 import PdfReader # For reading a downloaded pdf
import argparse # For interpreting command line arguments
import re # For several string modifications


# Helper function to convert date in string format to actual date object
def get_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        exit()


# Helper function to get today's date in the format YYYY-MM-DD
def get_today_date():
    return datetime.now().strftime("%Y-%m-%d")


# Helper function to get a list of the sentences within a text that contain a specific keyword
def find_sentences_with_keyword(text, keyword):
    sentences = text.split(". ")
    result = []
    for sentence in sentences:
        if keyword.lower() in sentence.lower():
            result.append(sentence.strip())
    return result


# Function that checks for particular keywords in the pdf behind a given url
def check_keywords_in_edition(url):

    # Download the PDF file (will be removed later)
    response = requests.get(url)
    with open("temp.pdf", "wb") as f:
        f.write(response.content)

    # Open the PDF file
    with open("temp.pdf", "rb") as f:
        pdf_reader = PdfReader(f)

        # Define the list of keywords to search for
        keywords = ["Rijksarchief", "archieven", "bewaartermijn"]

        keyword_found = False

        # Loop through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):

            # Load the text on the page to a string variable
            page_text = pdf_reader.pages[page_num].extract_text()

            keyword_no = 0

            # Check if any of the keywords exist in the text (case-insensitive)
            for keyword in keywords:
                keyword_no += 1

                # If a keyword is found at least once on a page, print out a line that says to, and on which page. Also give a url directly to that page online. (The local pdf will already be gone by the time of consulting the output of the script).
                if keyword.lower() in page_text.lower():
                    keyword_found = True
                    print(f"    Keyword '{keyword}' found in the PDF on page {page_num + 1}: {url}#page={page_num+1}\n")
                    sentences_with_keyword = find_sentences_with_keyword(page_text, keyword)

                    # Print each sentence containing the keyword (in original case), highlighting the keyword in a unique color proper (except for keywords after the 7th place, in keys there are more than 7 keywords).
                    for sentence in sentences_with_keyword:
                        if keyword_no <= 7:
                            indented_sentence = "        " + re.sub(re.escape(keyword), f"\033[9{keyword_no}m{keyword}\033[0m", sentence, flags=re.IGNORECASE)
                        else:
                            indented_sentence = "        " + re.sub(re.escape(keyword), f"\033[90m{keyword}\033[0m", sentence, flags=re.IGNORECASE)
                        indented_sentence = indented_sentence.replace('\n', '\n        ')
                        print(f"{indented_sentence}\n")

        # Display a message if no keyword matches are found for the edition
        if not keyword_found:
            print(f"    No keyword matches found for this edition.\n")

    # Clean up the temporary PDF file
    os.remove("temp.pdf")


# Function that constructs the urls to search, and feeds them to the keyword checking function
def main(date):

    # Construct the URLs using a specified date (1st and 2nd edition)
    url_1 = f"https://www.ejustice.just.fgov.be/mopdf/{date.strftime('%Y/%m/%d')}_1.pdf"
    url_2 = f"https://www.ejustice.just.fgov.be/mopdf/{date.strftime('%Y/%m/%d')}_2.pdf"

    # Check for the first edition
    response_1 = requests.head(url_1)
    if response_1.status_code == 200:
        # First edition found, download and search for keywords
        print(f"Checking PDF for {date.strftime('%Y-%m-%d')} (1st edition)...\n")
        check_keywords_in_edition(url_1)

        # Check for the second edition
        response_2 = requests.head(url_2)
        if response_2.status_code == 200:
            # Second edition found, download and search for keywords
            print(f"Checking PDF for {date.strftime('%Y-%m-%d')} (2nd edition)...\n")
            check_keywords_in_edition(url_2)


""" Actual script """

# Create an argument handler to accept inputs from the command line
parser = argparse.ArgumentParser(description="Check PDF for keywords")

# Add an optional argument '-d' or '--days-back' to accept an integer input. This indicates how many days back from today to check. The default value is 1 day
parser.add_argument("-d", "--days-back", type=int, default=1, help="Number of days back from today")

# Add another optional argument '-s' or '--specific-date' to accept a string input. This specifies a particular date (in YYYY-MM-DD format) to check instead of the current date
parser.add_argument("-s", "--specific-date", type=str, help="Specific date to check (format: YYYY-MM-DD)")

# Capture the values passed by the user into 'args'
args = parser.parse_args()

try:
    # If the user provides a specific date with the '--specific-date' option, convert that string into a date object
    if args.specific_date:
        specific_date = get_date(args.specific_date)
    else:
        # If no specific date is given, use today's date
        specific_date = datetime.now().date()

    # Calculate the start date by subtracting the 'days-back' value from the specific date. This gives the first day to start checking
    start_date = specific_date - timedelta(days=args.days_back)

    # Go through each day starting from the 'start_date' and ending at the 'specific_date'
    for i in range(args.days_back + 1):
        
        # Calculate the exact date to check by adding 'i' days to the start date
        date_to_check = start_date + timedelta(days=i)
        
        # Call the main function for the given date
        main(date_to_check)

except Exception as e:
    print(f"An error occurred: {e}")

# Pause to prevent the console from closing immediately
input("Press Enter to exit...")
