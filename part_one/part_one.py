"""
Given a CSV file, write a function that will open this file, validate the data and output a new file (good_data.csv).
"""
GOOD_DATA_FILE_NAME = "good_data.csv"


def validate_and_load_files(file_name):
    """
    Given a file name
    Open and validate this file based on the requirements given (see "Column validation" in part_one.txt)
    Save the good data to a new file
    """
    # Add your code here


if __name__ == "__main__":
    file_name = "mock_data_1000.csv"
    validate_and_load_files(file_name)
