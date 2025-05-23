# Python doc reader

## Create virtual env

`python3 -m venv .venv`

## Activate virtual env

`source .venv/bin/activate`

## Deactivate virtual env

`deactivate`

## Install requirements

`pip install -r requirements.txt`

## Model for tokenizer

Clone Gemma 3 from https://huggingface.co/google/gemma-3-4b-it into the models folder

## Docs

Put docs to read into corresponding doc folders

## Run

`python3 server.py`

## API

http://localhost:8081/read
http://localhost:8081/readPDF

Send POST call with query text as body
