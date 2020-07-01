
## Setup

Recommand Python version: 3.8.3

### Install python dependencies

```shell
pip install -r requirements.txt
``` 
or
```shell
conda env create -f ./film_title_env.yml
conda activate film_title
```


## Generating new films data

```shell
python src/get_source_data.py
```

The new data file will be including the data in the filename, like `films-2020-07-01.json` .
