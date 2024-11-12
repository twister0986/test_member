import streamlit as st
import sqlite3

conn = sqlite3.connect('Car_Database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM `Brands`;')

st.write(len(cursor.fetchall()))
tables=cursor.fetchall()



