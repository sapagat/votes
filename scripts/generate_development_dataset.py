import csv
import os
import re
from utils import dataset
import pandas as pd

ROOT_PATH = os.getenv('PYTHONPATH')
INPUT_FOLDER = 'datasets/production/'
OUTPUT_FOLDER = 'datasets/development/'
DATASETS = [
    'DatasetCatSpa',
    'DatasetFavCon',
    'DatasetMaFe'
]
DEVELOPMENT_FRACTION = 0.1

for dataset_name in DATASETS:
    input_path = ROOT_PATH + INPUT_FOLDER + dataset_name
    output_path = ROOT_PATH + OUTPUT_FOLDER + dataset_name

    tweets = dataset.read_tweets_from(input_path)
    developement_tweets = pd.DataFrame(tweets).sample(frac=DEVELOPMENT_FRACTION).to_dict('records')
    dataset.write_tweets_to(output_path, developement_tweets)
