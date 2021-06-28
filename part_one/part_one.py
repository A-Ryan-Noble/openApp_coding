import csv

"""
Given a CSV file, write a function that will open this file, validate the data and output a new file (good_data.csv).
"""
GOOD_DATA_FILE_NAME = "good_data.csv"


def write_to_file(row, column_names):
    import os

    # if the file exists and is empty then open and write into the file
    if os.path.exists(GOOD_DATA_FILE_NAME) and os.path.getsize(GOOD_DATA_FILE_NAME) == 0:
        with open(file=GOOD_DATA_FILE_NAME, mode='w', encoding="utf8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=column_names)
            writer.writeheader()
            writer.writerow(row)

    # Append the existing file by opening and appending it with the given row
    else:
        with open(file=GOOD_DATA_FILE_NAME, mode='a', encoding="utf8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=column_names)
            writer.writerow(row)


def validate_and_load_files(file_name):
    """
    Given a file name
    Open and validate this file based on the requirements given (see "Column validation" in part_one.txt)
    Save the good data to a new file
    """
    # Add your code here

    # Opens the file in readable mode and decoded into utf8
    with open(file=file_name, mode='r', encoding="utf8") as file:
        # Converts the file into a dictionary reader
        csv_reader = csv.DictReader(file)

        fieldnames = csv_reader.fieldnames # Gets the list of column names
        #  Iterate through each row of the dictionary
        for row in csv_reader:

            # if fieldnames is None and :

            # Defaults variables to not valid
            valid_id = False
            valid_first_name = False
            valid_last_name = False
            valid_email = False
            valid_eircode = False

            # Id column validation:
            #     - Must be integer and not empty
            if row["id"] and row["id"].isdecimal():
                valid_id = True

            # First name column validation:
            #     - Must be string and not empty
            if row["first_name"].isascii():
                valid_first_name = True

            # Last name Column validation:
            #     - Must be string and not empty
            if row["last_name"].isascii():
                valid_last_name = True

            # Email Column validation:
            #     - Must be string, not empty and contain '@'
            if row["email"] and row["email"].isascii() and row["email"].__contains__("@"):
                valid_email = True

            # Eircode Column validation:
            #     - Must be string, not empty, contain only alphanumeric characters and 7 characters long
            if row["eircode"] and row["eircode"].isalnum() and len(row["eircode"]) is 7:
                valid_eircode = True

            # If the current row is considered valid, the row written to file
            if valid_id and valid_first_name and valid_last_name and valid_email and valid_eircode:
                write_to_file(row, fieldnames)


if __name__ == "__main__":
    file_name = "mock_data_1000.csv"
    validate_and_load_files(file_name)
