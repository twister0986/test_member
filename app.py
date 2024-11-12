import requests
import zipfile
import os

# 定義資料庫壓縮檔的 GitHub URL
GITHUB_URL = "https://github.com/twister0986/test_member/raw/main/Car_Database.rar"

# 定義下載和解壓的路徑
zip_path = "Car_Database.rar"
db_path = "Car_Database.db"

# 檢查是否已經存在解壓縮的資料庫檔案
if not os.path.exists(db_path):
    # 從 GitHub 下載壓縮檔
    with requests.get(GITHUB_URL, stream=True) as r:
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    # 解壓縮檔案
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()

    # 移除壓縮檔
    os.remove(zip_path)

import streamlit as st
import sqlite3

conn = sqlite3.connect('Car_Database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM `Brands`;')

st.write(len(cursor.fetchall()))
tables=cursor.fetchall()



