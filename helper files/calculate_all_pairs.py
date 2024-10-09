import pandas as pd

from geopy.distance import distance, geodesic

df = pd.read_csv("capital_cities_fixed.csv")


def distance_finder(df, city_one, city_two):
    city_one_coords = (df.loc[city_one]["lat"], df.loc[city_one]["lng"])
    city_two_coords = (df.loc[city_two]["lat"], df.loc[city_two]["lng"])
    return geodesic(city_one_coords, city_two_coords).km  # distance(lat, lon)


try:
    all_pairs = pd.read_csv("all_city_pairs.csv")
except FileNotFoundError:
    data = {
        "city1": [],
        "city2": [],
        "distance_between": [],
    }

    i = 0
    for city_index_1 in range(len(df)):
        for city_index_2 in range(city_index_1 + 1, (len(df))):
            data["city1"].append(df["city"][city_index_1])
            data["city2"].append(df["city"][city_index_2])
            dist_btwn = distance_finder(df, city_index_1, city_index_2)
            data["distance_between"].append(dist_btwn)
        print(i)
        i += 1

    all_pairs = pd.DataFrame(data)
    all_pairs.to_csv("all_city_pairs.csv", encoding="utf-8", index=False)

sorted_df = all_pairs.sort_values(by=["distance_between"])
sorted_df.to_csv("sorted_city_pairs.csv", encoding="utf-8", index=False)
print(sorted_df)

import numpy as np
np.set_printoptions(suppress=True)
print(sorted_df['distance_between'].values)
distances = np.sort(sorted_df['distance_between'].values)
print(distances)
distances_compared = np.diff(distances)
np.savetxt("distances.txt", distances)
print(distances_compared)
sorted_compared = np.sort(distances_compared)
print(sorted_compared)
np.savetxt("distances_diff_sorted.txt", sorted_compared)
all_distances_valid = np.all(distances_compared >= 1)

print(all_distances_valid)

"""
import pandas as pd
from geopy.distance import geodesic

# Load the CSV file into a DataFrame
df = pd.read_csv("capital_cities_fixed.csv")

# Initialize an empty list to store distance information
distance_data = []

# Iterate through each city pair
for i in range(len(df)):
    for j in range(i + 1, len(df)):  # Avoid duplicate pairs and self-pairs
        city_one = df.iloc[i]
        city_two = df.iloc[j]
        
        # Calculate the distance between the two cities
        coords_1 = (city_one['lat'], city_one['lng'])
        coords_2 = (city_two['lat'], city_two['lng'])
        distance_km = geodesic(coords_1, coords_2).kilometers
        
        # Append the information to the list
        distance_data.append({
            'City 1': city_one['city'],
            'City 2': city_two['city'],
            'Country 1': city_one['country'],
            'Country 2': city_two['country'],
            'Distance (km)': distance_km
        })

# Convert the list into a DataFrame
distance_df = pd.DataFrame(distance_data)

# Save the DataFrame to a new CSV file
distance_df.to_csv("city_distances.csv", index=False)

print("Distance calculation complete. Results saved to 'city_distances.csv'.")

"""
