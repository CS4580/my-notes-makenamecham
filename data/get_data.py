
"""Download data from out server
"""
import urllib.request
import zipfile
import os
import shutil


SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/pandas02Data.zip'

# TODO: Create a function to download files from Kaggle directly by passing the dataset name

def download_file(url, file_name):
    # TODO: Download to pwd
    full_url = url + file_name
    urllib.request.urlretrieve(full_url, file_name)
    print(f"'{file_name}' has been downloaded.")

    if file_name.endswith('.zip'):   # TODO: Check extension, if it is zip
            print(f"'{file_name}' is a zip file. Unzipping...")
            unzip_file(file_name) # Call unzip_file()
    else:
        print(f"'{file_name}' is not a zip file. No unzipping necessary.")

def extract_zip_file(file_name):
    # TODO: Unzip file
    """
    Unzip the file in the current working directory
    """
    if zipfile.is_zipfile(file_name):
          os.getcwd()
          with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())
            os.path.join(os.getcwd, file_name)

    else:
        print(f"'{file_name}' is not a valid zip file or it may be corrupted.")

def main():
    """Driven Function
    """
    data02 = 'hotel-booking-demand.zip'
    download_file(SERVER_URL, data02)
    extract_zip_file(data02) # unzip_file(data01)
    # TODO: Set input user options to extract files 



    print('Main Function')

if __name__ == '__main__':
    main()