import streamlit as st

# Function to show the selection page
def select_num_players():
    st.sidebar.title("Select Number of Players")
    num_players = st.sidebar.radio("Number of Players", [2, 3, 4])
    if st.sidebar.button("Start Game"):
        return num_players

# Function to show the main game page
def main_game(num_players):
    st.title("All or Nothing Game")
    # Your main game logic here
    st.write(f"Number of players selected: {num_players}")

def main():
    st.set_page_config(layout="wide")
    num_players = select_num_players()
    if num_players:
        main_game(num_players)

if __name__ == "__main__":
    main()

