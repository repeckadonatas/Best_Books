# Best Books


## Table of contents

<!-- TOC -->
* [Best Books](#best-books)
  * [About](#about)
  * [Tech stack used](#tech-stack-used)
  * [How to use the program](#how-to-use-the-program)
    * [**Important:**](#important)
  * [Input dataset cleaning](#input-dataset-cleaning)
  * [Exploratory data analysis](#exploratory-data-analysis)
<!-- TOC -->


## About

This project is created to clean and normalize a **[GoodReads Best Books](https://www.kaggle.com/datasets/thedevastator/comprehensive-overview-of-52478-goodreads-best-b?rvi=1)** dataset from kaggle. Once the dataset is cleaned and normalized, some exploratory analysis is done. The normalized datasets are loaded to a PostgreSQL database using Python code. The code also allows for some manipulation of the database using CLI commands.

**Note:** to run the program properly, install dependencies from `requirements.txt` file.

## Tech stack used

* Programing language - **Python**;
* Servers and load balancing - for this project, data is stored locally on the machine;
* Data storage and querying - **PostgreSQL**;
* For interactive data cleaning - **Jupyter Notebook**;
* Data cleaning normalization and analysis - **Pandas**, **Seaborn**;

## How to use the program

To use the program, run the _`main.py`_ file. You will then be greeted with a welcome message. 

To interact with the program use the built-in commands:

*     To test a connection with a database: test
*     To create a table: create
*     To truncate a table: trunc
*     To populate a table with data from a file: pop
*     To check on populated table data: if pop
*     To quit the program: exit

To see the commands at any time, pass an empty of wrong keyword and then type _**help**_ in the terminal window.


**Note:** 
- If while creating or populating a table an error occurs, the program has to be run again. To restart the program, run _`main.py`_.

### **Important:**

To connect to the database, the `db_config/get_config.py` file needs to read these values from `credentials.ini` file:

| Variable | Your value    |
|----------|---------------|
| database | database_name |
| host     | host_name     |
| user     | user_name     |
| password | user_password |
| port     | port          |

## Input dataset cleaning

Because no data is perfect, data cleaning and normalization was performed while keeping the context of data.

Following the cleaning procedure some columns were changed:

| Columns                                             | Change                                                                                                                                                                |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| genres, characters, awards, ratingsByStars, setting | These columns contained values that were **string representation of a list (<class 'numpy.ndarray'>)**. To perform normalization, data type was changed to list type. |
| publishDate and firstPublishDate                    | Dates in these columns had different formats. Dates were formatted to **[ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html)** format.                   |
| pages                                               | In some rows a page number was left as '**1 page**'. This was removed and left as a blank space for future update if needed.                                          |


Duplicate rows where all row values matched with previous row values were dropped before cleaning and during normalization.


Columns that contain empty values in Pandas show up as _**float**_ or _**string**_ data type. That is how Pandas treats empty values. NaN stands for **Not A Number** and is one of the common ways to represent the missing value in the data. It is a special **[floating-point](https://pandas.pydata.org/docs/user_guide/missing_data.html#integer-dtypes-and-missing-data)** value and cannot be converted to any other type than float.

For exploratory data analysis missing values can be ignored or changed to any other value if needed.


## Exploratory data analysis

Some exploration of data was performed. Explored book rating by language.