from download_data import download_url
import zipfile

url = 'http://files.grouplens.org/datasets/movielens/ml-100k.zip'
output_path = "../data/ml-100k.zip"
output_tsv = "../data/"

download_url(url, output_path)

with zipfile.ZipFile(output_path, "r") as zip_ref:
    zip_ref.extractall(output_tsv)

# remove the zip file
import os

os.remove(output_path)

