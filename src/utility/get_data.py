import pandas as pd
import os
import urllib.request


def download_project_maslow_files():
    """The purpose of this function is to handle getting the nonprofit.txt and nonprofit_text.txt
    files.  This functin will create a data directory, add a .gitignore file so
    source control does not pick up the txt files, and then check to see
    if either nonprofit.txt and nonprofit_text.txt have been downloaded yet.
    If not, it will proceed to download the files.
    """

    if os.path.isfile("data/nonprofit.txt") is False:
        print("Downloading nonprofit.txt...")
        urllib.request.urlretrieve("https://mtsu-dsi-non-profit-categorization.s3.amazonaws.com/tax-data-descriptions/nonprofit.txt", 'data/nonprofit.txt')

    if os.path.isfile("data/nonprofit_text.txt") is False:
        print("Downloading nonprofit_text.txt...")
        urllib.request.urlretrieve("https://mtsu-dsi-non-profit-categorization.s3.amazonaws.com/tax-data-descriptions/nonprofit_text.txt", 'data/nonprofit_text.txt')


def get_non_profit_df():
    """This function will first run the download_project_maslow_files() to check to
    see if the files have been downloaded to the `data/` folder.  If not,
    it will download the files.
    Then, it will read in the file and return a dataframe with the nonprofit
    """

    download_project_maslow_files()

    col_types = {
        "nonprofit_id": "Int64",
        "reporting_year": "Int64",
        "ein": "Int64",
        "businessname": "str",
        "phone": "str",
        "address1": "str",
        "address2": "str",
        "city": "str",
        "stabbrv": "str",
        "zip": "str"
      }

    df = pd.read_csv("data/nonprofit.txt", sep = "|", dtype=col_types)

    return df

def get_non_profit_text_df():
    """This function will first run the download_project_maslow_files() to check to
    see if the files have been downloaded to the `data/` folder.  If not,
    it will download the files.
    Then, it will read in the file and return a dataframe with the nonprofit_text
    """

    download_project_maslow_files()

    col_types = {
        "nonprofit_text_id": "Int64",
        "reporting_year": "Int64",
        "nonprofit_id": "Int64",
        "grouptype": "str",
        "description": "str"
    }

    df = pd.read_csv("data/nonprofit_text.txt", sep = "|", encoding="cp1252", dtype=col_types)

    return df