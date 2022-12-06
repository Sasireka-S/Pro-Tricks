import streamlit as st
import base64
import pandas as pd
import sqlite3
from collections import defaultdict as dd
def text_field(label, columns=None, **input_params):
    c1, c2 = st.columns(columns or [1, 4])
    c1.markdown("##")
    c1.markdown(label)
    input_params.setdefault("key", label)
    return c2.text_input("", **input_params)
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.jpg')
sqliteConnection = sqlite3.connect('gamedb.db')
cursor = sqliteConnection.cursor()
sql_command = """CREATE TABLE IF NOT EXISTS gam (
    name VARCHAR(50),
    trick1 VARCHAR(50),
    trick2 VARCHAR(50),
    trick3 VARCHAR(50),
    trick4 VARCHAR(50),
    trick5 VARCHAR(50)
);"""
cursor.execute(sql_command)
original_title = '<p style="font-family:Georgia; color:white; font-size: 60px;">Want to Play well? See Tips !!!</p>'
st.markdown(original_title, unsafe_allow_html=True)
with st.form("my_form"):
    options = [" ","PUBG", "League of Legends", "Call of Duty", "Brawl Stars", "Track Mania", "Clash Royale", "Fortnite", "Team Fortress", "Paladins"]
    comp = (st.selectbox('Select your game of interest : ',(options)))
    submit = st.form_submit_button(label="Submit")
if comp != " ":
    if(comp == options[1]):
        add_bg_from_local('bg3.jpg')
    elif(comp == options[2]):
        add_bg_from_local('bg4.jpg')
    elif(comp == options[3]):
        add_bg_from_local('bg5.jpg')
    elif(comp == options[4]):
        add_bg_from_local('bg6.jpg')
    elif(comp == options[5]):
        add_bg_from_local('bg7.png')
    elif(comp == options[6]):
        add_bg_from_local('bg8.jpg')
    elif(comp == options[7]):
        add_bg_from_local('bg9.jpg')
    elif(comp == options[8]):
        add_bg_from_local('bg2.jpg')
    elif(comp == options[9]):
        add_bg_from_local('bg3.jpg')
    cursor.execute("SELECT * FROM gam WHERE name = (?)", (comp,))
    ans = cursor.fetchall() 
    dicti = dd(list)
    with st.expander('', expanded=True):
        for x in ans:
            for i in range(1,6):
                t = '<p style = "color:white; font-size: 20px;">{code}</p>'.format(code = x[i])
                st.markdown(t, unsafe_allow_html=True)
sqliteConnection.commit()
sqliteConnection.close()