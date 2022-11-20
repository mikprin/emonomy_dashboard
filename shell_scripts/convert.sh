#!/bin/bash
# Convert a file to a different format

target_dir=$1
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# Convert all files in the target directory

for file in $target_dir/*
do
    # Get the file extension
    extension="${file##*.}"

    # Convert the file to a different format
    case $extension in
        "xls" | "XLS" | "xlsx" | "XLSX")
            short_filename="$(basename "$file")"
           echo 'Converting file: ' "$short_filename"
            ssconvert "$file" ./"$(echo "$short_filename" | cut -f1 -d'.').csv"
            echo ssconvert "$file" "./$(echo "$short_filename" | cut -f1 -d'.').csv"
            ;;
        *)
            # If file is a directory, enter it
            if [ -d $file ]
            then
                new_path=$(realpath $file)
                echo "Entering directory $new_path"
                ( mkdir -p "$(basename ${file})" && cd "$(basename ${file})" && "$SCRIPTPATH/convert.sh" "$new_path" )
            else
                echo "File $file is not an xls or xlsx file"
            fi
            ;;
    esac
done

# Old format:
# ssconvert $1/emotions_data.xlsx ./emotions_data.csv
# ssconvert $1/emotions_metrics.xlsx ./emotions_metrics.csv
# ssconvert $1/statement_irt_result.xlsx ./statement_irt_result.csv

