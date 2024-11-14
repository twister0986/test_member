import requests
import zipfile
import os

# 定義資料庫壓縮檔的 GitHub URL
GITHUB_URL = ["https://github.com/twister0986/test_member/raw/main/member_data_v3.zip",
              "https://github.com/twister0986/test_member/raw/main/member_carrier_v3_lite.zip"]

# 定義下載和解壓的路徑
zip_path = ["member_data_v3.zip","member_carrier_v3_lite.zip"]
db_path = ["member_data_v3.db","member_carrier_v3_lite.db"]

# 檢查是否已經存在解壓縮的資料庫檔案
for index in range(2):
    if not os.path.exists(db_path[index]):
        # 從 GitHub 下載壓縮檔
        with requests.get(GITHUB_URL[index], stream=True) as r:
            with open(zip_path[index], "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    
        # 解壓縮檔案
        with zipfile.ZipFile(zip_path[index], 'r') as zip_ref:
            zip_ref.extractall()
    
        # 移除壓縮檔
        os.remove(zip_path)
    
conn = sqlite3.connect('member_data_v3.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM `UU-1001`;')

st.write(len(cursor.fetchall()))
tables=cursor.fetchall()

conn.close()
#-----------------------------------------------
conn = sqlite3.connect('member_carrier_v3_lite.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM `merge_area_store`;')

st.write(len(cursor.fetchall()))
tables=cursor.fetchall()

conn.close()
