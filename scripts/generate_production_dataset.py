import csv
import os
import re

ROOT_PATH = os.getenv('PYTHONPATH')
INPUT_FOLDER = 'datasets/raw'
OUTPUT_FOLDER = 'datasets/production/'
DATASETS = [
    'DatasetCatSpa',
    'DatasetFavCon',
    'DatasetMaFe'
]

for dataset in DATASETS:
    input_path = ROOT_PATH + INPUT_FOLDER + dataset
    output_path = ROOT_PATH + OUTPUT_FOLDER + dataset

    with open(output_path, 'w') as out_file:
        writer = csv.writer(out_file, delimiter=';')
        with open(input_path, 'r') as in_file:
            for i, line in enumerate(in_file):
                tweet_id = re.search(r'^\d+', line).group()
                category = re.search(r'^\d+\s(\w+)\s', line).group(1)
                text = re.search(r'^\d+\s\w+\s{2}(.+)', line).group(1)
                writer.writerow([tweet_id, category, text])
