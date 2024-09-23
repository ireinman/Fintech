# Methods in Prediction in Fintech - Final Project
Submitted by Itamar Reinman, Ben Eliav and Eyal El Ani

## Overview
This repository contains all the code and data we used to conduct our experiments. The general pipeline of our project starts from the data, downloaded from AHDB. Afterwards, we process the data to make it suitable for learning tasks and finally try different tasks using the processed model.

### data
The data folder contains the raw data as downloaded from online, of the futures and of the prime interest rate. The data engineering pipeline to get datasets that we can work with is summarized in the files check_good_years.ipynb, preprocess_comm.ipynb, and adjust_prime.ipynb.

### check_good_years.ipynb
This notebook reads over the raw data and looks for any problematic rows (with missing values). We used this file to find any bad rows and manually deleted them from the raw data.

### adjust_prime.ipynb
We will want to add the prime as a feature to the final dataset. This file performs the necessary data engineering to cause the integration to go more smoothly.

### preprocess_comm.ipynb
This notebook is responsible for extracting the important information (get next year for every row in data) from the raw excel files. For every row in the raw files, we save the future prices for next year in the months March, May, July and September. We save the results of every day in a new dataframe, one with different columns (date/march/may/july/september). This was for all the data to be in the same format and make it more comfortable for performing tasks. Then, it adds the prime and date difference as additional columns, for reasons explained in the written report. The file continues to save a number of csv files:
1. For each commodity, saves the entire dataframe,
2. For each commodity and each year, saves the dataframe for the relevant year.
3. Saves a single dataframe which is the join of all the dataframes created in (1).

### data_processed
This is the folder of the data after preprocessing that was generated via the data engineering pipeline.

### commodities_tickers.json
JSON file that contains codes of popularly traded commodities in the futures market. The commodities are divided by category (grains / metals / etc.).

### regression.ipynb
Does first task in the written report.

### sarima.ipynb
Does second task in the written report

### kalman-filters-holt-winters.ipynb
Does second task in the written report using a different model - Holt Winters using Kalman filters.

### deep_sequential.ipynb
Does third task in the written report.

### sharpe_index.ipynb
Does fourth task in the written report.

## Requirements
To run the code in this repository, the following prerequisites are required:
1. Python 3.9+
2. Jupyter
3. NumPy
4. Pandas
5. PyTorch
6. Matplotlib
7. Sklearn
8. PyKalman
9. Statsmodels
10. yFinance
11. gensim
