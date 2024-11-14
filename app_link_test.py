import requests
import zipfile
import os
import streamlit as st
import sqlite3

# 定義資料庫壓縮檔的 GitHub URL
GITHUB_URL = "https://github.com/twister0986/test_member/raw/main/member_carrier_v3.db.zip"

# 定義下載和解壓的路徑
zip_path = ["member_carrier_v3.zip",]
db_path = ["member_carrier_v3.db",]

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

conn = sqlite3.connect('member_carrier_v3.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM `merge_area_store`;')

st.write(len(cursor.fetchall()))
tables=cursor.fetchall()

conn.close()
