import tkinter as tk
from capital_pairs_compare import main, check_for_answer, draw_connections

csv = "capital_cities_fixed.csv"


def restart_game():
    # global df_first_pair_of_cities, df_second_pair_of_cities, pair_one_dist, pair_two_dist

    # Clear the screen and reset the UI
    for widget in root.winfo_children():
        widget.destroy()

    # Rebuild the initial UI
    initialize_ui(csv)


def set_correct_value_label(correct):
    for widget in root.winfo_children():  # Remove previous widgets
        widget.destroy()

    if correct:
        correctness_label = tk.Label(
            root, text="You are correct!", font=("Helvetica", 26), fg="green"
        )
    else:
        correctness_label = tk.Label(
            root, text="Better luck next time!", font=("Helvetica", 26), fg="red"
        )
    correctness_label.pack(pady=20)

    info_text = (
        f"The capitals {df_first_pair_of_cities['city'].iloc[0]} and {df_first_pair_of_cities['city'].iloc[1]} are {pair_one_dist}km away."
        + f"\nWhilst {df_second_pair_of_cities['city'].iloc[0]} and {df_second_pair_of_cities['city'].iloc[1]} are {pair_two_dist}km away."
    )
    info_label = tk.Label(
        root, text=info_text, font=("Helvetica", 16), wraplength=550, justify="center"
    )
    info_label.pack()

    see_globe_button = tk.Button(
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
    see_globe_button.pack(pady=30)

    restart_button = tk.Button(
        root,
        text="Play Again",
        font=("Helvetica", 22),
        command=restart_game,  # Calls the restart function to reset the game. LAMBDA?
    )
    restart_button.pack(pady=30)


def get_user_answer(answer):
    user_correct_bool = check_for_answer(
        pair_one_dist,
        pair_two_dist,
        answer,
    )

    set_correct_value_label(user_correct_bool)


def initialize_ui(csv):
    global df_first_pair_of_cities, df_second_pair_of_cities, pair_one_dist, pair_two_dist
    df_first_pair_of_cities, df_second_pair_of_cities, pair_one_dist, pair_two_dist = (
        main(csv)
    )
    # Create a label
    label = tk.Label(root, text="Compare City-Pairs", font=("Helvetica", 32))
    label.pack(pady=20)

    desc_text = f"Select the pair of cities that is closest geographically."

    desc_label = tk.Label(
        root, text=desc_text, font=("Helvetica", 16), wraplength=550, justify="center", fg="blue"
    )

    desc_label.pack()

    # Create the first button
    first_pair_button = tk.Button(
        root,
        text=f"{df_first_pair_of_cities.iloc[0]['city']} to {df_first_pair_of_cities.iloc[1]['city']}",
        font=("Helvetica", 22),
        command=lambda: get_user_answer("a"),
    )
    first_pair_button.pack(pady=30)

    # Create the second button
    second_pair_button = tk.Button(
        root,
        text=f"{df_second_pair_of_cities.iloc[0]['city']} to {df_second_pair_of_cities.iloc[1]['city']}",
        font=("Helvetica", 22),
        command=lambda: get_user_answer("b"),
    )
    second_pair_button.pack(pady=10)


root = tk.Tk()
root.title("Compare City-Pairs")
root.geometry("600x400")

initialize_ui(csv)

root.mainloop()
