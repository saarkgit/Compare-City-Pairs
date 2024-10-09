import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from geopy.distance import distance
import random


def distance_finder(df, city_one, city_two):
    city_one_coords = (df.loc[city_one]["lat"], df.loc[city_one]["lng"])
    city_two_coords = (df.loc[city_two]["lat"], df.loc[city_two]["lng"])
    return distance(city_one_coords, city_two_coords)  # distance(lat, lon)


def gen_rand_pairs(df):
    # Generate a random sample of 4 unique indices from the DataFrame
    rand_sample = random.sample(range(len(df.index)), 4)

    # Split the sample into two pairs
    pair_one = rand_sample[:2]
    pair_two = rand_sample[2:]

    # Extract the DataFrames for each pair of cities
    df_first_pair_of_cities = df.iloc[pair_one]
    df_second_pair_of_cities = df.iloc[pair_two]

    # Calculate the distances between the cities in each pair
    pair_one_dist = int(
        distance_finder(df_first_pair_of_cities, pair_one[0], pair_one[1]).km
    )
    pair_two_dist = int(
        distance_finder(df_second_pair_of_cities, pair_two[0], pair_two[1]).km
    )

    return (
        df_first_pair_of_cities,
        df_second_pair_of_cities,
        pair_one_dist,
        pair_two_dist,
    )


def check_for_answer(
    df_first_pair_of_cities, df_second_pair_of_cities, pair_one_dist, pair_two_dist
):
    print(f"Which capital cities are closer together? (a or b)")
    user_answer = input(
        f"a: ({df_first_pair_of_cities['city'].iloc[0]}, {df_first_pair_of_cities['city'].iloc[1]})"
        + f" or b: ({df_second_pair_of_cities['city'].iloc[0]}, {df_second_pair_of_cities['city'].iloc[1]})\n"
    )

    invalid_answer = True
    while invalid_answer:
        if user_answer == "a" or user_answer == "b":
            invalid_answer = False
        else:
            user_answer = input("Please input a valid response.")

    user_correct = False
    if user_answer == "a":
        user_correct = pair_one_dist < pair_two_dist
    else:
        user_correct = pair_two_dist < pair_one_dist

    if user_correct:
        print("You are correct!")
    else:
        print("Better luck next time!")

    print(
        f"The capitals {df_first_pair_of_cities['city'].iloc[0]} and {df_first_pair_of_cities['city'].iloc[1]} are {pair_one_dist} away."
        + f"\nWhilst {df_second_pair_of_cities['city'].iloc[0]} and {df_second_pair_of_cities['city'].iloc[1]} are {pair_two_dist} away."
    )


df = pd.read_csv("capital_cities_fixed.csv")
df_first_pair_of_cities, df_second_pair_of_cities, pair_one_dist, pair_two_dist = (
    gen_rand_pairs(df)
)

check_for_answer(
    df_first_pair_of_cities, df_second_pair_of_cities, pair_one_dist, pair_two_dist
)

# VISUALS 2
fig = go.Figure()

city_pairs = [
    (df_first_pair_of_cities, "blue", (pair_one_dist)),
    (df_second_pair_of_cities, "red", (pair_two_dist)),
]

for df_pair, color, dist in city_pairs:
    # Extract latitudes and longitudes
    lats = df_pair["lat"]
    lons = df_pair["lng"]
    cities = df_pair["city"]
    countries = df_pair["country"]

    # Add line trace connecting the two cities
    fig.add_trace(
        go.Scattergeo(
            lon=lons,
            lat=lats,
            mode="lines",
            line=dict(width=2, color=color),
            name=f"{cities.iloc[0]}, {countries.iloc[0]} to {cities.iloc[1]}, {countries.iloc[1]}, {dist}",
        )
    )

    # Add marker trace for the cities with labels
    fig.add_trace(
        go.Scattergeo(
            lon=lons,
            lat=lats,
            mode="markers+text",
            text=cities,
            textposition="top center",
            marker=dict(size=5, color=color),
            showlegend=False,  # Hide individual city markers from the legend
        )
    )

# Update the layout of the figure
fig.update_layout(
    title_text="Capital City Connections",
    showlegend=True,
    legend=dict(title="Routes", x=0.75, y=0.95),
    geo=dict(
        projection_type="orthographic",
        showland=True,
        landcolor="rgb(243, 243, 243)",
        # oceancolor="rgb(0, 0, 243)",
        # countrycolor="rgb(204, 204, 204)",
        showcountries=True,
        # showocean = True,
    ),
    height=800,
)

# Display the figure
fig.show()
