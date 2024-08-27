import pandas as pd

def filter_csv(input_file, output_file, filter_function):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Apply the filtering criteria
    filtered_df = df[filter_function(df)]

    # Save the filtered DataFrame to a new CSV file
    filtered_df.to_csv(output_file, index=False)

# Define your filtering function
def filter_capitals(df):
    return df['capital'] == 'primary' # and df['population'] > 500

# Example usage
input_file = 'worldcities.csv'
output_file = 'capital_cities.csv'
filter_csv(input_file, output_file, filter_capitals)



# def find_duplicates(input_list):
#     seen = set()
#     duplicates = set()

#     for item in input_list:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)

#     return list(duplicates)

# duplicates = find_duplicates(country)
# print(duplicates)
