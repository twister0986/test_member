import requests
import zipfile
import os
import streamlit as st
import sqlite3

import zipfile
import os
import streamlit as st
import sqlite3

# 定義檔案的基本路徑與名稱
db_path = 'member_carrier_v3.db'
zip_path = 'member_carrier_v3.zip'

# 假設 GITHUB_URLS 包含四個分割檔案的 URL
GITHUB_URLS = [
    "https://github.com/twister0986/test_member/raw/main/member_carrier_v3.zip", 
    "https://github.com/twister0986/test_member/raw/main/member_carrier_v3.z01", 
    "https://github.com/twister0986/test_member/raw/main/member_carrier_v3.z02", 
    "https://github.com/twister0986/test_member/raw/main/member_carrier_v3.z03"
]
zip_parts = [f"member_carrier_v3.z{i:02}" for i in range(len(GITHUB_URLS))]

# 確認資料庫是否已存在
if not os.path.exists(db_path):
    st.write("Downloading and extracting database...")

    # 下載每個分割檔案
    for i, url in enumerate(GITHUB_URLS):
        with requests.get(url, stream=True) as r:
            with open(zip_parts[i], "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    # 合併分割檔案成一個完整的 ZIP 檔案
    with open(zip_path, "wb") as combined_zip:
        for part in zip_parts:
            with open(part, "rb") as f:
                combined_zip.write(f.read())

    # 解壓縮合併後的 ZIP 檔案
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()

    # 移除所有分割檔和合併後的 ZIP 檔
    for part in zip_parts:
        os.remove(part)
    os.remove(zip_path)
    st.write("Database downloaded and extracted successfully.")

# 連接到 SQLite 資料庫
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('SELECT * FROM `merge_area_store`;')

st.write(len(cursor.fetchall()))
tables=cursor.fetchall()

conn.close()
