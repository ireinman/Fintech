# Methods in Prediction in Fintech - Final Project
Submitted by Itamar Reinman, Ben Eliav and Eyal El Ani

## Overview
This repository contains all the code and data we used to conduct our experiments. The general pipeline of our project starts from the data, downloaded from AHDB. Afterwards, we process the data to make it suitable for learning tasks and finally try different tasks using the processed model.

### data
The data folder contains the raw data as downloaded from online, of the futures and of the prime interest rate. The data engineering pipeline to get datasets that we can work with is summarized in the files check_good_years.ipynb, preprocess_comm.ipynb, and adjust_prime.ipynb.

### processed_data
This is the folder of the data after preprocessing that was generated via the data engineering pipeline.

### check_good_years.ipynb
This notebook reads over the raw data and looks for any problematic rows (with missing values). We used this file to find any bad rows and manually deleted them from the raw data.

### adjust_prime.ipynb
This file performs the necessary data engineering to cause the integration of the prime data in the data process file (preprocess_comm.ipynb) to go more smoothly.

### preprocess_comm.ipynb
This notebook is responsible for extracting the important information (get next year for every row in data) from the raw excel files and the results of the adjust_prime notebbok. For every row in the raw files, we save the future prices for next year in the months March, May, July and September. We save the results of every day in a new dataframe, one with different columns (date/march/may/july/september). This was for all the data to be in the same format and make it more comfortable for performing tasks. Then, it adds the prime and date difference as additional columns, for reasons explained in the written report. The file continues to save a number of csv files:
1. For each commodity, saves the entire dataframe,
2. For each commodity and each year, saves the dataframe for the relevant year.
3. Saves a single dataframe which is the join of all the dataframes created in (1).

### regression.ipynb
This notebook presents an experiment using linear regression models for the task of predicting futures contract prices, as mentioned in the report.

### predict_average.ipynb
This notebook presents a baseline model for predicting the prices of futures contracts using the mean of the previous values, as mentioned in the report.

### ar.ipynb
This notebook presents a model for predicting the prices of futures contracts using auto-regressive models, as mentioned in the report.

### ma.ipynb
This notebook presents a model for predicting the prices of futures contracts using moving-average models, as mentioned in the report.

### sarima.ipynb
This notebook presents a model for predicting the prices of futures contracts using SARIMA models which have auto-regressive and moving-average components alongside a seasonality component, as mentioned in the report.

### sarimax.ipynb
This notebook presents a model for predicting the prices of futures contracts using SARIMA models incorporated with an exogenous variable of the "prime", called SARIMAX , as mentioned in the report.

### kalman-filters-holt-winters.ipynb
This notebook presents a model for predicting the prices of futures contracts using the Holt-Winters model with additive seasonality, implemented via the Kalman Filters Equations, as mentioned in the report.

### deep_sequential.ipynb
This notebook presents a model for predicting the prices of futures contracts using deep learning and sequential models like RNN and LSTM, as mentioned in the report.

### sharpe_index.ipynb
This notebook presents a model for predicting the quarterly of the Sharpe Ratio of the following quarter, as mentioned in the report. We did not end up using this code as predicting the Sharpe Ratio is not a common task.

### economic_statistics.ipynb
This notebook provides various statistics for all futures being measured. This will be used to measure the general success of each future in the bonus section.

### commodities_tickers.json
JSON file that contains codes of popularly traded commodities in the futures market. The commodities are divided by category (grains / metals / etc.).

### ar-predictions.ipynb
This notebook presents a trial of forecasting the time series with AR(p) models, which appear to be the best models in our task. The notebook contains also discussion about the validity of the results, and when it would be a good idea to use such models

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
