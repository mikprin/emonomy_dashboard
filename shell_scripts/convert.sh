#!/bin/bash
# Convert a file to a different format

target_dir=$1

ssconvert $1/emotions_data.xlsx ./emotions_data.csv
ssconvert $1/emotions_metrics.xlsx ./emotions_metrics.csv
ssconvert $1/statement_irt_result.xlsx ./statement_irt_result.csv

