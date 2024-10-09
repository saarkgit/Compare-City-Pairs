import tkinter as tk
from capital_pairs_compare import main, check_for_answer, draw_connections

# Function to create and show the Plotly map for the first pair of cities
df_first_pair_of_cities, df_second_pair_of_cities, pair_one_dist, pair_two_dist = main(
    "capital_cities_fixed.csv"
)


def set_correct_value_label(correct):
    for widget in root.winfo_children():  # Remove previous widgets
        widget.destroy()

    if correct:
        label = tk.Label(
            root, text="You are correct!", font=("Helvetica", 26), fg="green"
        )
        label.pack(pady=50)
    else:
        label = tk.Label(
            root, text="Better luck next time!", font=("Helvetica", 26), fg="red"
        )
    
    label.pack(pady=50)

    button3 = tk.Button(
        root,
        text="See distances on a globe?",
        font=("Helvetica", 22),
        command=lambda: draw_connections(
            df_first_pair_of_cities,
            df_second_pair_of_cities,
            pair_one_dist,
            pair_two_dist,
        ),
    )
    button3.pack(pady=30)


def get_user_answer(answer):
    user_correct_bool = check_for_answer(
        df_first_pair_of_cities,
        df_second_pair_of_cities,
        pair_one_dist,
        pair_two_dist,
        answer,
    )

    set_correct_value_label(user_correct_bool)


# Create the main application window
root = tk.Tk()
root.title("Compare City-Pairs")
root.geometry("600x400")

# Create a label
label = tk.Label(root, text="Compare City-Pairs", font=("Helvetica", 32))
label.pack(pady=20)

# Create the first button
button1 = tk.Button(
    root,
    text=f"{df_first_pair_of_cities.iloc[0]['city']} to {df_first_pair_of_cities.iloc[1]['city']}",
    font=("Helvetica", 22),
    command=lambda: get_user_answer("a"),
)
button1.pack(pady=30)

# Create the second button
button2 = tk.Button(
    root,
    text=f"{df_second_pair_of_cities.iloc[0]['city']} to {df_second_pair_of_cities.iloc[1]['city']}",
    font=("Helvetica", 22),
    command=lambda: get_user_answer("b"),
)
button2.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
# RESET GAME
