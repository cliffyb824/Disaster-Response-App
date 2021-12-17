# **Disaster Response Pipeline Project**

- [Description](#Description)
- [Dependencies](#Dependencies)
- [Project Components](#Components)
- [File Descriptions](#File-Descriptions)
- [Instructions](#How-To-Run-This-Project)
- [Licensing, Authors, Acknowledgements](#License)

## Description <a name="Description"></a>

The Disaster Response Pipeline Project is the data engineer project assigned by Udacity data scientist nanodegree. This project builds a **Machine Learning Natural Language Processing pipeline** to categorize emergency messages based on the needs communicated by the sender. 

## Dependencies <a name="Dependencies"></a>




## Project Components <a name="Components"></a>

1. **ETL Pipeline**
    1. Disaster_categories.csv and disater_messages.csv is imported as dataframe.
    2. Perform extract, transform and load to clean the dataset and save the dataset to SQL database.
2. **ML Pipeline**
    1. Load dataframe from database.
    2. Split the dataset into training and testing set.
    3. Train the model on training set and test the model on testing set, the model first tokenize, normalize, and lemmatize the dataset then apply Random Forest Classifier to do classification.
    4. Try grid search for best parameters and also try other model(such as Support Vector Machine, Adaboost, kNN, Decision Tree).
    5. Compare the models by looking at their precision, recall, and accuracy. Choose a model that have relative higher of these attributes.
    6. Export the model as a pickle file.
3. **Web Deployment**
    1. Create a html website and link to Github database
    2. Deploy app on Heroku so that everyone can view it.

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


## Licensing, Authors, Acknowledgements <a name="License"></a>
**Licensing**
Begin license text.
Copyright <2021> <COPYRIGHT Yuan Qiu>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

End license text.

**Authors** [Yuan Qiu](https://github.com/cliffyb824)

**Acknowledgements** Nguyen Pam,