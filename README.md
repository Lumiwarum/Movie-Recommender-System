# Movie recommendation system

# Authors:

**Kirilin Anton - B20-RO** 

a.kirilin@innopolis.university

## Description 📔

In this project you can find .ipynb notebooks with code for training different models for collaborative filtering for recommendation system.  There are also reports of research work done during the assignment

## How to start 🚀

In order to run all the script you have to do the following procedure:

1.  Clone this git repo to your local machine

```bash
git clone https://github.com/Lumiwarum/Movie-Recommender-System/tree/main
```

1. Create a new python virtual environment and activate it

```bash
python3 -m venv /env
source ./env/bin/activate
```

1. Install all the requrements

```bash
pip install -r requirements.txt
```

Now you’re ready to run all python script in this repo.

## Structure  📦

```
detoxification
├── README.md # The top-level README
│
├── data
│   └── ml-100k     # The dataset to be processed
│
├── models       #  model checkpoints
│
├── notebooks    #  Jupyter notebooks.
│
├── references   # Data dictionaries, manuals, and all other explanatory materials.
│
├── reports      # Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures  # Generated graphics and figures to be used in reporting
│
├── requirements.txt # The requirements file for reproducing the analysis environment, e.g.
│                      generated with pip freeze › requirements. txt'
└── src                 # Source code for use in this assignment
    ├── prepare_data.py #script to prepare the movielens-100k dataset
    │
    └── evaluate.py #script to run SVD model for movie recomendation
```

The structure was taken from [here](https://github.com/Lumiwarum/Movie-Recommender-System/blob/main/TASK_DESCRIPTION.md)

[Notebooks](https://github.com/Lumiwarum/Movie-Recommender-System/tree/main/notebooks) folder contains all the .ipynb file that I used during the research process

[The report](https://github.com/Lumiwarum/Movie-Recommender-System/blob/main/reports/Report.pdf) about searching for the solution and  the final result

## Usage:

### Data processing:

1. [benchmark/prepare_data.py](https://github.com/Lumiwarum/Movie-Recommender-System/blob/main/benchmark/prepare_data.py) - downloads the dataset and extracts it into `data/raw` directory.

### Suggest films:

[benchmark/evaluate.py](https://github.com/Lumiwarum/Movie-Recommender-System/blob/main/benchmark/evaluate.py) - allows you to run the model for suggesting similar films to a film in the database.

[Solution Building](https://www.notion.so/Solution-Building-6d2179d9f6b449c693e6195c8eadaa3f?pvs=21)

[Task description](https://www.notion.so/Task-description-5e4030a0bfd24766b02870b42635373a?pvs=21)

[Final Solution](https://www.notion.so/Final-Solution-ace688180ab74348851d9548f48f6622?pvs=21)