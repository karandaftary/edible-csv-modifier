import pandas as pd

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    print("Data processing finished.")
    return modified_data

def main():
    # read csv file if it exists
    df = pd.read_csv(r'11-04-21 Kirkland.csv', error_bad_lines=False)
    print(df)
    # extract fields that are necessary
    
    # add message

    # create new csv file with extracted fields

# entry point
if __name__ == "__main__":
    main()