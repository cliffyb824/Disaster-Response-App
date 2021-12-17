# Disaster Response Pipeline Project

- [Description](#Description)
- [Dependencies](#Dependencies)
- [Project Components](#Components)
- [File Descriptions](#File-Descriptions)
- [Instructions](#How-To-Run-This-Project)
- [Discussion](#Discussion)
- [Licensing, Authors, Acknowledgements](#License)

## Description <a name="Description"></a>

The Disaster Response Pipeline Project is the data engineer project assigned by Udacity data scientist nanodegree. This project builds a machine learning pipeline to categorize emergency messages based on the needs communicated by the sender. 

## Dependencies <a name="Dependencies"></a>




## Project Components <a name="Components"></a>

1. ETL Pipeline
- 
2. ML Pipeline
- 
3. Web Deployment

## File Description <a name="File-Descriptions"></a>

```
├── app
│   ├── run.py--------------------------------# Flask file runs the web app
│   └── templates
│       ├── go.html---------------------------# Result page
│       └── master.html-----------------------# Main page
├── data
│   ├── DisasterResponse.db-------------------# *Database storing the processed data
│   ├── disaster_categories.csv---------------# Pre-labelled dataset
│   ├── disaster_messages.csv-----------------# Data
│   ├── process_data.py-----------------------# ETL pipeline processing the data
|   └── ETL Pipeline Preparation.ipynb-----# Jupyter notebook with details
├── models
|   ├── train_classifier.py-------------------# Machine learning pipeline
│   ├── ML Pipeline Preparation.ipynb------# Jupyter notebook with details
|   └── classifier.pkl------------------------# *Pickle file
*Files that will be generated when the python scripts .py are executed.
```

## Instructions <a name="How-To-Run-This-Project"></a>

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/ go to the website that is showed in your command line.

## Discussion <a name="Discussion"></a>



## Licensing, Authors, Acknowledgements <a name="License"></a>

