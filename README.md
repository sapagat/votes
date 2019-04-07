# Votes

This repository contains some analysis and datasets related to the competition "Stance and Gender Detection in Tweets
on Catalan Independence@Ibereval 2017". You can find more details [here](http://stel.ub.edu/Stance-IberEval2017/index.html).

## Requirements

- Docker + docker compose
- Makefile

## Development

- `make jupyter`: a Jupyter Notebook server will be available in the prompted URL.
- `make check`: run a check that all the notebooks execute without errors. Useful for refactoring into functions.

## Datasets

The datasets have the following structure:

```
<tweet_id> <category>  <text>
```

Datasets:

- `DatasetCatSpa`: categories CAT => catalan, SPA => spanish.
- `DatasetFavCon`: categories FAVOR, NEUTRAL, AGAINST
- `DatasetMaFe`: categories FEMALE, MALE

They can be found in `datasets` directory and `fixtures` contain the light representation for running checks.
