import streamlit as st
# https://blox-fruits.fandom.com/wiki/Blox_Fruits
# https://st-styled.evo-byte.com/
import st_yled
from PIL import Image
from openai import OpenAI
import json

st_yled.init()
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
BloxFruitTittle = Image.open("The_Blox_Bulletin_003.webp")
if "info" not in st.session_state:
    st.session_state.info = {}

client = OpenAI(
    api_key = st.secrets["API_KEY"]
)

system_prompt = "You should make a JSON response and maintain the informations in order as what I asked in user_prompt."
user_prompt = '''Make a JSON response with information of this games in Roblox, Blox Fruit, for the game you need to give me how the game is made, how to play the game, most recent types of fruits inside the game, most recent number of active players, most recent number of visits, information about the creator of the game, history about the game."

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

def set_background(image_path: str):
    """Set a local image as the full-page background."""
    import base64

    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)

# Sets background of website 
set_background("BloxFruitsforproject.jpg")

# =====================================================
st.image(BloxFruitTittle, width = 300)

with st_yled.container(
    background_color="#b4af96",
    border_color="#dee2e6",
    padding="20px"
):
    st.header("How the game is made")
    st.write(st.session_state.info["Blox Fruit"]["how the game is made"])

with st_yled.container(
    background_color="#b4af96",
    border_color="#dee2e6",
    padding="20px"
):
    st.header("How to play the game")
    st.write(st.session_state.info["Blox Fruit"]["how to play the game"])

# color this purple only the text 

with st_yled.container(
    background_color="#b4af96",
    border_color="#dee2e6",
    padding="20px"
):
    st.header("Types of fruits inside the game")

    frs1, frs2 = st.columns(2)
    with frs1:
        st.write(st.session_state.info["Blox Fruit"]["types of fruits inside the game"])
    with frs2: 
        st.image(Blox_fruit_fruits, width = 400)

# color this yellow as only the tittle

with st_yled.container(
    background_color="#b4af96",
    border_color="#dee2e6",
    padding="20px"
):
    st.header("Number of active players")

    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.info["Blox Fruit"]["number of active players"])
    with col2: 
        st.image(active_players_img, width = 400)

# color this red only the title

with st_yled.container(
    background_color="#b4af96",
    border_color="#dee2e6",
    padding="20px"
):
    st.header("Number of visits")
    st.write(st.session_state.info["Blox Fruit"]["number of visits"])

# color this blue only the title
with st_yled.container(
    background_color="#b4af96",
    border_color="#dee2e6",
    padding="20px"
):
    st.header("Information about the creator of the game")

    crt1, crt2 = st.columns(2)
    with crt1:
        st.write(st.session_state.info["Blox Fruit"]["information about the creator of the game"])
    with crt2: 
        st.image(blox_creator_img, width = 400)

# this should be colored as green title only

with st_yled.container(
    background_color="#b4af96",
    border_color="#dee2e6",
    padding="20px"
):
    st.header("History about the game")

    inf1, inf2 = st.columns(2)
    with inf1:
        st.write(st.session_state.info["Blox Fruit"]["history about the game"])
    with inf2: 
        st.image(blox_piece_logo, width = 400)

# color this brown title only