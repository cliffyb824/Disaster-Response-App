# Disaster Response Pipeline Project

- [Project Overview](#Project-Overview)
- [Installation](#Installation)
- [Project Components](#Components)
- [File Descriptions](#File-Descriptions)
- [Instructions](#How-To-Run-This-Project)
- [Discussion](#Discussion)
- [Licensing, Authors, Acknowledgements](#License)

## Project Overview <a name="Project-Overview"></a>
The Disaster Response Pipeline Project is the data engineer project assigned by Udacity data scientist nanodegree.

## Installation <a name="Installation"></a>

## Project Components <a name="Components"></a>

## File Description <a name="File-Descriptions"></a>

## Instructions <a name="How-To-Run-This-Project"></a>

## Discussion <a name="Discussion"></a>

## Licensing, Authors, Acknowledgements <a name="License"></a>


















### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
