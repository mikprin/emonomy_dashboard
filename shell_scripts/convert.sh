#!/bin/bash
# Convert a file to a different format

target_dir=$1


# Convert all files in the target directory

for file in $target_dir/*
do
    # Get the file extension
    extension="${file##*.}"

    # Convert the file to a different format
    case $extension in
        "xls" | "XLS" | "xlsx" | "XLSX")
            ssconvert $file ./${file%.*}.csv
            ;;
        # "png")
        #     convert $file ./${file%.*}.jpg
        #     ;;
        *)
            # If file is a directory, enter it
            if [ -d $file ]
            then
                echo "Entering directory $file"
                SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
                ( mkdir -p $(basename ${file}) && cd $(basename ${file}) && $SCRIPTPATH/convert.sh $file )
            else
                echo "File $file is not an xls or xlsx file"
            fi
            ;;
    esac
done

# ssconvert $1/emotions_data.xlsx ./emotions_data.csv
# ssconvert $1/emotions_metrics.xlsx ./emotions_metrics.csv
# ssconvert $1/statement_irt_result.xlsx ./statement_irt_result.csv

