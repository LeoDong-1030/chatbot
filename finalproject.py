import streamlit as st
from PIL import Image
from openai import OpenAI
import json

# Idea - Informational Website About Roblox (Blox Fruit):
# - how game is made
# - how to play the game(gameplay)
# - types of fruits 
# - number of active players
# - number of visits
# - information about the creator of the game
# - information about each island inside the game
# - backstories/history about this game
active_players_img = Image.open("Blox fruit active player graph image.png")
blox_creator_img = Image.open("Blox Fruit creator.png")
blox_piece_logo = Image.open("Blox_Piece_Logo_29.webp")
Blox_fruit_fruits = Image.open("Blox fruit fruits.jpeg")
if "info" not in st.session_state:
    st.session_state.info = {}

client = OpenAI(
    api_key = st.secrets["API_KEY"]
)

system_prompt = "You should make a JSON response and maintain the informations in order as what I asked in user_prompt."
user_prompt = '''Make a JSON response with information of this games in Roblox, Blox Fruit, for the game you need to give me how the game is made, how to play the game, types of fruits inside the game, number of active players, number of visits, information about the creator of the game, history about the game."

Heres how I want my JSON to be formated
{
    "Blox Fruit":
    {
        "how the game is made":str,
        "how to play the game":str,
        "types of fruits inside the game":str
        "number of active players":str
        "number of visits":str
        "information about the creator of the game":str
        "history about the game":str
    }
}

do not add any markdown symbols. Format it in a way where json.loads can decode it
'''

if not st.session_state.info:
    with st.spinner("🍎 Loading Blox Fruit info..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        print(response.choices[0].message.content)
        st.session_state.info = json.loads(response.choices[0].message.content)
        
# =====================================================
st.title("Blox Fruit")

st.header("How the game is made")

st.write(st.session_state.info["Blox Fruit"]["how the game is made"])

st.header("How to play the game")

st.write(st.session_state.info["Blox Fruit"]["how to play the game"])

st.header("Types of fruits inside the game")

st.write(st.session_state.info["Blox Fruit"]["types of fruits inside the game"])

st.header("Number of active players")

col1, col2 = st.columns(2)
with col1:
    st.write(st.session_state.info["Blox Fruit"]["number of active players"])
with col2: 
    st.image(active_players_img, width = 400)

st.header("Number of visits")
st.write(st.session_state.info["Blox Fruit"]["number of visits"])


st.header("Information about the creator of the game")
st.write(st.session_state.info["Blox Fruit"]["information about the creator of the game"])

crt1, crt2 = st.columns(2)
with crt1:
    st.write(st.session_state.info["Blox Fruit"]["information about the creator of the game"])
with crt2: 
    st.image(active_players_img, width = 400)



st.header("History about the game")
st.write(st.session_state.info["Blox Fruit"]["history about the game"])


