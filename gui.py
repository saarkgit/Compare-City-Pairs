import tkinter as tk
from tkinter import messagebox
import pandas as pd
import plotly.graph_objects as go
from capital_pairs_compare import main
# Function to create and show the Plotly map for the first pair of cities
df_first_pair_of_cities, df_second_pair_of_cities, pair_one_dist, pair_two_dist = main("capital_cities_fixed.csv")


# Create the main application window
root = tk.Tk()
root.title("Compare City-Pairs")
root.geometry("600x400")

# Create a label
label = tk.Label(root, text="Compare City-Pairs", font=("Helvetica", 32))
label.pack(pady=20)

# Create the first button
button1 = tk.Button(root, text=f"{df_first_pair_of_cities.iloc[0]['city']} to {df_first_pair_of_cities.iloc[1]['city']}", font=("Helvetica", 22))#, command=show_first_pair_map)
button1.pack(pady=30)

# Create the second button
button2 = tk.Button(root, text=f"{df_second_pair_of_cities.iloc[0]['city']} to {df_second_pair_of_cities.iloc[1]['city']}", font=("Helvetica", 22))#, command=show_second_pair_map)
button2.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
