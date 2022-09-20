# ClickUp Batch Worklog

Save time log entries into ClickUp, read data from CSV file.

!ALERT! Use the script on your own risk! There is no adequate error handling in the script!

## Prerequisites

* ClickUp account
* python3

## Setup

* Copy .env.template file to .env
* Create az API Token in ClickUp (Settings / App)
* Copy & paste the token into the .env file
* Get the Team ID: go to the ClickUp Home page, the number in the path before /home is the Team ID
* Put the Team ID into the .env file
* Get your User ID:
  * Run: 
    ``` python3 ./get_team_data.py ```
  * In the output, you can find your user and User ID
  * Use grep to search for your user if the output is too verbose:
    ``` python3 ./get_team_data.py | grep 'YOUR NAME' -B 10```
* Put your User ID into the .env file

## Prepare CSV file

The script reads data from times.csv file. Copy the ```times.csv.example``` file as ```times.csv``` and update the data in it as follows:

* The CSV file doesn't have any header, the first row is the first valid data
* The separator is ;
* Columns:
  * Start time (Date and time) in the following format: 2022-06-29 9:00:00
  * Duration hours
  * Duration minutes
  * Description
  * Task ID (Check the URL or task's details page)
  * Unused fields: you can write here additional informations about task, if the Task ID is confusing
    (for example: ```2022-06-29 9:00:00;15;Daily standup;2ar5n1m;Meetings```)

## Run the script

!ALERT! There is no decent error handling in the script and you can't revert easily what you have done with it! So, be on the watch! ;-)

``` python3 ./time_logger_from_csv.py```



