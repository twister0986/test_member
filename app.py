import sqlite3
import streamlit as st
import pandas as pd
import random


def member_question():
    #按照順序:['UU_與你的距離','GMO']，此為第1個
    def question_class1():
        #連接到 SQLite 資料庫，之後決定問卷選項後要查詢
        conn = sqlite3.connect('member_data_v3.db')
        cursor = conn.cursor()
        # 你的選項列表
        select_item_list=[
            [('Q3-興趣-家居和園藝',),('Q3-興趣-寵物及動物',), ('Q3-興趣-房地產',), ('Q3-興趣-旅遊',), ('Q3-興趣-書籍和文學',), ('Q3-興趣-汽車及交通工具',), ('Q3-興趣-網上社群',), ('Q3-興趣-美容和健身',), ('Q3-興趣-藝術和娛樂',), ('Q3-興趣-購物',), ('Q3-興趣-遊戲',), ('Q3-興趣-運動',), ('Q3-興趣-金融',), ('Q3-興趣-電腦和電子產品',), ('Q3-興趣-餐飲',), ('Q3-興趣-其他',)],
            [('Q3-青中老年成員-青老人(65至74歲)',), ('Q3-青中老年成員-中老人(75至84歲)',), ('Q3-青中老年成員-老老人(85歲以上)',), ('Q3-青中老年成員-以上都沒有',),('Q4-寵物成員-狗毛孩',), ('Q4-寵物成員-貓大人',), ('Q4-寵物成員-兔子',), ('Q4-寵物成員-鼠類',), ('Q4-寵物成員-爬蟲類',), ('Q4-寵物成員-其他',), ('Q4-寵物成員-沒有寵物',)],
            [('Q1-身體健康-運動健身',), ('Q1-身體健康-保健食品',), ('Q1-身體健康-健康飲食',), ('Q1-身體健康-規律作息',), ('Q1-身體健康-其他',),('Q2-心靈健康-朋友傾訴',), ('Q2-心靈健康-休閒娛樂',), ('Q2-心靈健康-醫師諮詢',), ('Q2-心靈健康-其他',),('Q4-保健議題-網路搜尋文章、新聞',), ('Q4-保健議題-社群論壇討論',), ('Q4-保健議題-健康雜誌、書籍',), ('Q4-保健議題-專業醫師、藥師',), ('Q4-保健議題-親朋好友',), ('Q4-保健議題-其他',),('Q5-擔心面臨-糖尿病',), ('Q5-擔心面臨-腎臟病',), ('Q5-擔心面臨-心臟病',), ('Q5-擔心面臨-肝臟病',), ('Q5-擔心面臨-肺部疾病',), ('Q5-擔心面臨-高血壓',), ('Q5-擔心面臨-腫瘤癌症',), ('Q5-擔心面臨-呼吸道相關疾病',), ('Q5-擔心面臨-牙齒、口腔相關疾病',), ('Q5-擔心面臨-心理疾病',), ('Q5-擔心面臨-流行感冒、疾病',), ('Q5-擔心面臨-其他',),('Q3-孕期關心-孕期營養保健品',), ('Q3-孕期關心-嬰兒車',), ('Q3-孕期關心-嬰兒床',), ('Q3-孕期關心-汽車座椅',), ('Q3-孕期關心-奶粉',), ('Q3-孕期關心-副食品',), ('Q3-孕期關心-尿布',), ('Q3-孕期關心-保險',), ('Q3-孕期關心-其他',)],
            [('Q1-出遊交通工具-自行駕車',), ('Q1-出遊交通工具-自行騎車',), ('Q1-出遊交通工具-自行車',), ('Q1-出遊交通工具-公車',), ('Q1-出遊交通工具-火車',), ('Q1-出遊交通工具-高鐵',), ('Q1-出遊交通工具-捷運',), ('Q1-出遊交通工具-客運',), ('Q1-出遊交通工具-走路',),('Q3-國內旅遊-海邊、離島',), ('Q3-國內旅遊-山上、風景區',), ('Q3-國內旅遊-老街、古蹟',), ('Q3-國內旅遊-農場、觀光工廠',), ('Q3-國內旅遊-城市市區',), ('Q3-國內旅遊-其他',),('Q4-出國地區-東南亞',), ('Q4-出國地區-日本、韓國',), ('Q4-出國地區-中國大陸',), ('Q4-出國地區-歐洲',), ('Q4-出國地區-美國',), ('Q4-出國地區-澳洲',), ('Q4-出國地區-其他',)],
            [('Q2-上班交通工具-自行駕車',), ('Q2-上班交通工具-自行騎車',), ('Q2-上班交通工具-自行車',), ('Q2-上班交通工具-公車',), ('Q2-上班交通工具-火車',), ('Q2-上班交通工具-高鐵',), ('Q2-上班交通工具-捷運',), ('Q2-上班交通工具-客運',), ('Q2-上班交通工具-走路',),('Q3-採購項目-文具用品',), ('Q3-採購項目-辦公用品',), ('Q3-採購項目-印表機、影印機',), ('Q3-採購項目-電腦設備（硬體）',), ('Q3-採購項目-電腦軟體',), ('Q3-採購項目-其他',), ('Q3-採購項目-都無法建議或決定購買',)],
            [('Q1-喜歡的茶類-煎茶',), ('Q1-喜歡的茶類-玄米茶',), ('Q1-喜歡的茶類-綠茶',), ('Q1-喜歡的茶類-包種茶',), ('Q1-喜歡的茶類-高山烏龍茶',), ('Q1-喜歡的茶類-東方美人茶',), ('Q1-喜歡的茶類-鐵觀音',), ('Q1-喜歡的茶類-紅茶',), ('Q1-喜歡的茶類-英式紅茶',), ('Q1-喜歡的茶類-普洱茶',), ('Q1-喜歡的茶類-水果茶',), ('Q1-喜歡的茶類-花草茶',), ('Q1-喜歡的茶類-其他',),('Q1-喜歡的茶類-我不喜歡喝茶',),('Q2-喜歡的咖啡-美式咖啡',), ('Q2-喜歡的咖啡-義式濃縮咖啡',), ('Q2-喜歡的咖啡-拿鐵',), ('Q2-喜歡的咖啡-卡布其諾',), ('Q2-喜歡的咖啡-瑪奇朵',), ('Q2-喜歡的咖啡-其他',), ('Q2-喜歡的咖啡-我不喜歡喝咖啡',),('Q3-喜歡的咖啡包裝-即溶式(三合一)',), ('Q3-喜歡的咖啡包裝-濾掛式',), ('Q3-喜歡的咖啡包裝-膠囊',), ('Q3-喜歡的咖啡包裝-罐裝',), ('Q3-喜歡的咖啡包裝-超商、咖啡店等現沖',), ('Q3-喜歡的咖啡包裝-自己選購咖啡豆沖泡',), ('Q3-喜歡的咖啡包裝-其他',),('Q4-喜歡的酒類-水果酒',), ('Q4-喜歡的酒類-紅酒',), ('Q4-喜歡的酒類-啤酒',), ('Q4-喜歡的酒類-威士忌',), ('Q4-喜歡的酒類-白酒',), ('Q4-喜歡的酒類-其他',), ('Q4-喜歡的酒類-我不喜歡喝酒',),],
            [('Q3-喜歡的食物-台式小吃',), ('Q3-喜歡的食物-中式菜肴',), ('Q3-喜歡的食物-義式料理',), ('Q3-喜歡的食物-美式速食',), ('Q3-喜歡的食物-泰式酸辣',), ('Q3-喜歡的食物-川味麻辣',), ('Q3-喜歡的食物-日式料理',), ('Q3-喜歡的食物-蔬食主義',), ('Q3-喜歡的食物-其他',)],
            [('Q1-擁有的汽車-本田（Honda）',), ('Q1-擁有的汽車-豐田（Toyota）',), ('Q1-擁有的汽車-凌志（Lexus）',), ('Q1-擁有的汽車-納智捷（LUXGEN）',), ('Q1-擁有的汽車-三菱（Mitsubishi）',), ('Q1-擁有的汽車-裕隆（Nissan）',), ('Q1-擁有的汽車-馬自達（Mazda）',), ('Q1-擁有的汽車-福特（Ford）',), ('Q1-擁有的汽車-奧迪（Audi）',), ('Q1-擁有的汽車-富豪（VOLVO）',), ('Q1-擁有的汽車-賓士（Mercedes Benz）',), ('Q1-擁有的汽車-寶馬（BMW）',), ('Q1-擁有的汽車-特斯拉（Tesla）',), ('Q1-擁有的汽車-其他',), ('Q1-擁有的汽車-我沒有汽車',),('Q3-擁有機車-一般機車(50cc)',), ('Q3-擁有機車-一般機車(100cc)',), ('Q3-擁有機車-一般機車(150cc)',), ('Q3-擁有機車-一般機車(250cc)',), ('Q3-擁有機車-重型機車',), ('Q3-擁有機車-電動機車',), ('Q3-擁有機車-我沒有機車',)],
            [('Q1-靜態休閒娛樂-閱讀看書',), ('Q1-靜態休閒娛樂-聽音樂會',), ('Q1-靜態休閒娛樂-看電影',), ('Q1-靜態休閒娛樂-看電視',), ('Q1-靜態休閒娛樂-看線上影音',), ('Q1-靜態休閒娛樂-玩遊戲',), ('Q1-靜態休閒娛樂-朋友聚會',), ('Q1-靜態休閒娛樂-其他',),('Q1-喜歡的遊戲類型-動作（ACT）',), ('Q1-喜歡的遊戲類型-冒險（AVG）',), ('Q1-喜歡的遊戲類型-角色扮演（RPG）',), ('Q1-喜歡的遊戲類型-第一人稱射擊（FPS）',), ('Q1-喜歡的遊戲類型-策略（SLG）',), ('Q1-喜歡的遊戲類型-音樂（MUG）',), ('Q1-喜歡的遊戲類型-格鬥（FTG）',), ('Q1-喜歡的遊戲類型-益智休閒（PUZ）',), ('Q1-喜歡的遊戲類型-我不喜歡玩遊戲',),('Q2-常用的遊戲裝置-智慧型手機/平版',), ('Q2-常用的遊戲裝置-筆記型電腦',), ('Q2-常用的遊戲裝置-桌上型電腦',), ('Q2-常用的遊戲裝置-SNOY Play Station',), ('Q2-常用的遊戲裝置-微軟 XBOX',), ('Q2-常用的遊戲裝置-任天堂 Switch',), ('Q2-常用的遊戲裝置-其他',),('Q3-喜歡的影視類型-動作、冒險片',), ('Q3-喜歡的影視類型-喜劇片',), ('Q3-喜歡的影視類型-愛情片',), ('Q3-喜歡的影視類型-恐怖、驚悚、懸疑片',), ('Q3-喜歡的影視類型-奇幻片、科幻片',), ('Q3-喜歡的影視類型-歌舞劇、音樂片',), ('Q3-喜歡的影視類型-戰爭片',), ('Q3-喜歡的影視類型-歷史電影',), ('Q3-喜歡的影視類型-動畫片',), ('Q3-喜歡的影視類型-其他',),('Q4-常用的影視裝置-第四台',), ('Q4-常用的影視裝置-中華電信 MOD',), ('Q4-常用的影視裝置-Netflix',), ('Q4-常用的影視裝置-friDay影音',), ('Q4-常用的影視裝置-LINE TV',), ('Q4-常用的影視裝置-KKTV',), ('Q4-常用的影視裝置-WeTV',), ('Q4-常用的影視裝置-Amazon Prime Video',), ('Q4-常用的影視裝置-Apple TV+',), ('Q4-常用的影視裝置-其他',)],
            [('Q2-動態休閒娛樂-健身房健身',), ('Q2-動態休閒娛樂-球場打球',), ('Q2-動態休閒娛樂-慢跑健走',), ('Q2-動態休閒娛樂-爬山',), ('Q2-動態休閒娛樂-逛街購物',), ('Q2-動態休閒娛樂-逛展覽',), ('Q2-動態休閒娛樂-其他',),],
            [('Q3-提神方法-喝茶類飲品',), ('Q3-提神方法-喝咖啡',), ('Q3-提神方法-喝提神飲料',), ('Q3-提神方法-抽菸／電子菸',), ('Q3-提神方法-以上皆非',),],
            ]
        #標準答案表格獲取過程
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables=cursor.fetchall()
        #先把資料庫中的資料表名稱及欄位匯入
        answer_data={}
        #用於比對找出資料表
        for table_index in range(1,len(tables)):
            single_col_total=[]
            cursor.execute(f"PRAGMA table_info(`{tables[table_index][0]}`);")
            columns = cursor.fetchall()
            for single_col in columns:
                if single_col[2]=='TEXT':
                    continue
                single_col_total.append(single_col[1])
            answer_data[tables[table_index][0]]=single_col_total
        # 創建一個列表來保存所有選擇
        selected_items_all = []
        #儲存要搜尋的欄位
        target_select=[]
        # 定義列和標題的映射
        columns = st.columns(3)
        #精簡版
        group_titles = ['興趣','家庭成員','身心靈議題',
                        '旅遊相關','工作相關','飲品議題',
                        '喜歡的食物','擁有車型','靜態休閒娛樂',
                        '動態休閒娛樂','提神方法']
        #原版
        # group_titles = ['Q3-興趣', 'Q3-青中老年成員', 'Q4-寵物成員', 
        #                 'Q1-身體健康', 'Q2-心靈健康', 'Q3-提神方法',
        #                 'Q4-保健議題', 'Q1-出遊交通工具', 'Q2-上班交通工具',
        #                 'Q3-國內旅遊', 'Q4-出國地區', 'Q1-靜態休閒娛樂',
        #                 'Q2-動態休閒娛樂', 'Q3-喜歡的食物', 'Q3-採購項目',
        #                 'Q3-孕期關心', 'Q1-喜歡的茶類', 'Q2-喜歡的咖啡',
        #                 'Q3-喜歡的咖啡包裝', 'Q4-喜歡的酒類', 'Q5-擔心面臨',
        #                 'Q1-擁有的汽車', 'Q3-擁有機車', 'Q1-喜歡的遊戲類型',
        #                 'Q2-常用的遊戲裝置', 'Q3-喜歡的影視類型', 'Q4-常用的影視裝置',]
        # 使用循環來創建多選框
        for i in range(11):
            with columns[i%3]:
                select_list = st.multiselect(group_titles[i], [single_var[0] for single_var in select_item_list[i]], [])
                st.write(select_list)
                selected_items_all.append(select_list)
        

        count=0
        colqu1,colqu2,colqu3 = st.columns(3)
        with colqu2:
            select_sub=st.button('下一步',on_click=lock_fun4,disabled=st.session_state.lock4)


        if st.session_state.lock4:
            for single_list in selected_items_all:
                if len(single_list)==0:
                    count+=1
            if count==11:
                st.markdown("**無選取項目，請刷新網頁後重新選擇**")
            if count<11:
                for i, selected_items in enumerate(selected_items_all):
                    if selected_items:  # 只顯示有選擇的項目
                        st.markdown(f"**{group_titles[i]}:**")
                        select_item_view=st.write(f"{','.join(selected_items)}")
                #按下進行篩選      
                if st.session_state.lock3:
                    question_select_date=[]
                    colqu4,colqu5=st.columns(2)
                    with colqu4:
                        start_date_select=st.date_input('請選擇問卷填寫起始時間')    
                        question_select_date.append(int(str(start_date_select).replace('-','')))

                    with colqu5:
                        end_date_select=st.date_input('請選擇問卷填寫結束時間')
                        question_select_date.append(int(str(end_date_select).replace('-','')))

                    
                    colqu6,colqu7,colqu8=st.columns(3)
                    with colqu7:
                        filter_go=st.button('進行篩選',on_click=lock_fun5,disabled=st.session_state.lock5)
                        if filter_go:
                            
                            if start_date_select>end_date_select:
                                st.write('開始日期大於結束日期，請刷新頁面重新選擇')
                            
                            else:
                                #把儲存在不同 list 的選擇改放到同一個 list
                                for single_select_group in selected_items_all:
                                    if len(single_select_group)==0:
                                        continue
                                    for single_select in single_select_group:
                                        target_select.append(single_select)
                                #把要進行搜尋的欄位與資料表結合成字典
                                find_dict={}
                                for key,value in answer_data.items():
                                    tmp_list=[]
                                    for single_col in target_select:
                                        if single_col in value:
                                            tmp_list.append(single_col)
                                    if len(tmp_list)==0:
                                        continue
                                    find_dict[key]=tmp_list
                                #輸出查詢結果合併表格
                                result_table=[]
                                for single_table,table_col in find_dict.items():
                                    
                                    for single_col in table_col:
                                        query=f'''
                                        SELECT `memberNo` FROM `{single_table}`
                                        WHERE `{single_col}` = 1.0
                                        AND `logTime` BETWEEN {question_select_date[-2]} AND {question_select_date[-1]};'''
                                        #print(question_select_date[-2],question_select_date[-1])
                                        #防止SQL注入攻擊，避免把數值寫在原始SQL語句內，至少要傳入兩個參數
                                        #params=(1.0,1.0)
                                        cursor.execute(query)
                                        result_table.append(cursor.fetchall())
                                        print(result_table)
                                #進行交集運算，找出共有元素
                                
                                finally_result=[]
                                member_cal_result=set.intersection(*map(set,result_table))
                                #print(member_cal_result)
                                for member_filter in member_cal_result:
                                    finally_result.append(member_filter[0])
                                #print(finally_result)
                                #找出符合條件之會員的基本資料
                                #用於儲存從資料庫查詢後再準備要顯示dataframe的數據
                                df_data=[]
                                for single_member in finally_result:
                                    query=f'''
                                    SELECT `memberNo`,`性別`,`年紀`,`所在直轄市及縣`,`婚姻`,`薪資水平`,`職業別`
                                    FROM UU_member_data
                                    WHERE `memberNo` IN ("{single_member}");'''
                                    df_data.append(list((cursor.execute(query))))
                                #print(df_data)
                                #顯示dataframe
                                member_df=pd.DataFrame(columns=['memberNo','性別','年紀','所在直轄市及縣','婚姻','薪資水平','職業別'])
                                for single_df in df_data:
                                    try:
                                        member_df.loc[len(member_df)]=single_df[0]
                                    except:
                                        continue
                                st.write(f"會員筆數 : {member_df.shape[0]}")
                                st.dataframe(member_df,use_container_width=True)
                                
                            
                            
        # 關閉連接
        conn.close()
    #按照順序:['UU_與你的距離','GMO']，此為第2個    
    def question_class2():
        #資料表對照欄位
        answer_data_colqu={}
        
        conn = sqlite3.connect('member_data_v3.db')
        cursor = conn.cursor()
        
        cursor.execute(f"PRAGMA table_info(`GMO202408`);")
        tables=cursor.fetchall()
        
        select_item_list1=[]
        select_item_list2=[]
        select_item_list3=[]
        select_item_list4=[]
        #gmo_item_all=[select_item_list1,select_item_list2,select_item_list3,select_item_list4]

        for item_var in tables:
            if 'Q10' in item_var[1]:
                select_item_list1.append(item_var[1])
            elif '持有所有資產' in item_var[1]:
                select_item_list2.append(item_var[1])
            elif '遊戲設備' in item_var[1]:
                select_item_list3.append(item_var[1])
            elif 'Q14' in item_var[1]:
                select_item_list4.append(item_var[1])
                
        finally_select=[]
        
        colqu9,colqu10,colqu11=st.columns(3)
        with colqu9:
            gmo_item1=st.multiselect("參與的採購或引進決策的所有方面",select_item_list1)
            st.write('選擇的是 :',gmo_item1)
            finally_select.append(gmo_item1)
        with colqu10:
            gmo_item2=st.multiselect("目前持有所有資產",select_item_list2)
            st.write('選擇的是 :',gmo_item2)
            finally_select.append(gmo_item2)
        with colqu11:
            gmo_item3=st.multiselect("平時使用的遊戲設備",select_item_list3)
            st.write('選擇的是 :',gmo_item3)
            finally_select.append(gmo_item3)
        #------------------------------------------
        colqu12,colqu13,colqu14=st.columns(3)
        with colqu12:
            gmo_item4=st.multiselect("經歷過以下症狀？或者目前有在接受以下症狀的治療？",select_item_list4)
            st.write('選擇的是 :',gmo_item4)
            finally_select.append(gmo_item4)
        #欄位是文字，不是有填有勾就是1.0，做另一種處理
        #採購/引進的決策權
        with colqu13:
            colqu13_item=[]
            #取得欄位選項
            query=f'''
            SELECT `採購/引進的決策權` FROM `GMO202408`'''
            
            cursor.execute(query)
            for single_item in list(set(cursor.fetchall())):
                if single_item[0]==None:
                    continue
                colqu13_item.append(single_item[0])

            gmo_item13=st.multiselect("採購/引進的決策權",colqu13_item)
            st.write('選擇的是 :',gmo_item13)
            finally_select.append(gmo_item13)
        #最高學歷
        with colqu14:
            colqu14_item=[]
            #取得欄位選項
            query=f'''
            SELECT `最高學歷` FROM `GMO202408`'''
            
            cursor.execute(query)
            for single_item in list(set(cursor.fetchall())):
                if single_item[0]==None:
                    continue
                colqu14_item.append(single_item[0])

            gmo_item14=st.multiselect("最高學歷",colqu14_item)
            st.write('選擇的是 :',gmo_item14)
            finally_select.append(gmo_item14)
        #---------------------------------------------
        colqu15,colqu16,colqu17=st.columns(3)
        #您平時吸菸嗎？
        with colqu15:
            colqu15_item=[]
            #取得欄位選項
            query=f'''
            SELECT `您平時吸菸嗎？` FROM `GMO202408`'''
            
            cursor.execute(query)
            for single_item in list(set(cursor.fetchall())):
                if single_item[0]==None:
                    continue
                colqu15_item.append(single_item[0])

            gmo_item15=st.multiselect("您平時吸菸嗎？",colqu15_item)
            st.write('選擇的是 :',gmo_item15)
            finally_select.append(gmo_item15)
        #平時有開車嗎?
        with colqu16:
            colqu16_item=[]
            #取得欄位選項
            query=f'''
            SELECT `平時有開車嗎?` FROM `GMO202408`'''
            
            cursor.execute(query)
            for single_item in list(set(cursor.fetchall())):
                if single_item[0]==None:
                    continue
                colqu16_item.append(single_item[0])

            gmo_item16=st.multiselect("平時有開車嗎?",colqu16_item)
            st.write('選擇的是 :',gmo_item16)
            finally_select.append(gmo_item16)
        #汽車車型
        with colqu17:
            colqu17_item=[]
            #取得欄位選項
            query=f'''
            SELECT `汽車車型` FROM `GMO202408`'''
            
            cursor.execute(query)
            for single_item in list(set(cursor.fetchall())):
                if single_item[0]==None:
                    continue
                colqu17_item.append(single_item[0])

            gmo_item17=st.multiselect("汽車車型",colqu17_item)
            st.write('選擇的是 :',gmo_item17)
            finally_select.append(gmo_item17)
        #---------------------------------------------
        colqu18,colqu19,colqu20=st.columns(3)
        #汽車品牌
        with colqu18:
            colqu18_item=[]
            #取得欄位選項
            query=f'''
            SELECT `汽車品牌` FROM `GMO202408`'''
            
            cursor.execute(query)
            for single_item in list(set(cursor.fetchall())):
                if single_item[0]==None:
                    continue
                colqu18_item.append(single_item[0])

            gmo_item18=st.multiselect("汽車品牌",colqu18_item)
            st.write('選擇的是 :',gmo_item18)
            finally_select.append(gmo_item18)
        #家庭年收
        with colqu19:
            colqu19_item=[]
            #取得欄位選項
            query=f'''
            SELECT `家庭年收` FROM `GMO202408`'''
            
            cursor.execute(query)
            for single_item in list(set(cursor.fetchall())):
                if single_item[0]==None:
                    continue
                colqu19_item.append(single_item[0])

            gmo_item19=st.multiselect("家庭年收入",colqu19_item)
            st.write('選擇的是 :',gmo_item19)
            finally_select.append(gmo_item19)
        #個人年收入
        with colqu20:
            colqu20_item=[]
            #取得欄位選項
            query=f'''
            SELECT `個人年收入` FROM `GMO202408`'''
            
            cursor.execute(query)
            for single_item in list(set(cursor.fetchall())):
                if single_item[0]==None:
                    continue
                colqu20_item.append(single_item[0])

            gmo_item20=st.multiselect("個人年收入",colqu20_item)
            st.write('選擇的是 :',gmo_item20)
            finally_select.append(gmo_item20)
        #---------------------------------------------
        #從colqu13為文字答案
        col_var_all=['colqu13_item','colqu14_item','colqu15_item',
                     'colqu16_item','colqu17_item','colqu18_item',
                     'colqu19_item','colqu20_item']
        #從colqu13為文字答案的答案清單
        col_text_answer=['gmo_item13','gmo_item14','gmo_item15',
                         'gmo_item16','gmo_item17','gmo_item18',
                         'gmo_item19','gmo_item20']
        #文字答案欄位名稱
        text_col_name=['採購/引進的決策權','最高學歷','您平時吸菸嗎？','平時有開車嗎?','汽車車型',
                       '汽車品牌','家庭年收','個人年收入']
        
        gmo_result=[]
        print(finally_select)
        for check_index in range(len(finally_select)):
            
            if finally_select[check_index]==0:
                continue
            
            elif check_index < 4:
                for check_item in finally_select[check_index]:
                    query=f'''
                    SELECT `Uupon_User_ID` FROM `GMO202408`
                    WHERE `{check_item}` = 1.0'''
                    #print(question_select_date[-2],question_select_date[-1])
                    #防止SQL注入攻擊，避免把數值寫在原始SQL語句內，至少要傳入兩個參數
                    #params=(1.0,1.0)
                    cursor.execute(query)
                    gmo_result.append(cursor.fetchall())
                    
            else:
                for check_item in finally_select[check_index]:
                    # " "與` `兩個符號非常有差，差一點點就錯誤
                    query=f'''
                    SELECT "Uupon_User_ID" FROM "GMO202408"
                    WHERE "{text_col_name[int(check_index-4)]}"="{check_item}";'''

                    cursor.execute(query)
                    gmo_result.append(cursor.fetchall())
        
        colqu21,colqu22,colqu23=st.columns(3)
        with colqu22:
            gmo_item_sub=st.button('進行篩選',on_click=lock_fun6,disabled=st.session_state.lock6)
        
        q2_df_data=[]
        
        if st.session_state.lock6:
            member_cal_result=set.intersection(*map(set,gmo_result))
            member_cal_result=[var_filter[0] for var_filter in member_cal_result]
           
            for single_member in member_cal_result:
                query=f'''
                SELECT `Uupon_User_ID`,`GMOR_monitor_ID`,`性別`,`年齡`,`居住地`,`婚姻狀態`,`職業`,`職位`,`專業領域`,`職業領域`
                FROM `GMO202408`
                WHERE `Uupon_User_ID` IN ("{single_member}");'''
                q2_df_data.append(list((cursor.execute(query))))

            #顯示dataframe
            gmo_member_df=pd.DataFrame(columns=['Uupon_User_ID','GMOR_monitor_ID','性別','年齡','居住地','婚姻狀態','職業','職位','專業領域','職業領域'])
            for q2_df_data_item in q2_df_data:
                try:
                    gmo_member_df.loc[len(gmo_member_df)]=q2_df_data_item[0]
                except:
                    continue
            st.write(f"會員筆數 : {gmo_member_df.shape[0]}")
            st.dataframe(gmo_member_df,use_container_width=True)

        # 關閉連接
        conn.close()
    
    question_class=['UU_與你的距離','GMO']
    question_type=st.selectbox("請選擇問卷類別",question_class)
    st.write('您選擇的是 :',question_type)
    
    colqu1,colqu2,colqu3 = st.columns(3)
    with colqu2:
        select_sub=st.button('確定送出',on_click=lock_fun3,disabled=st.session_state.lock3,key='btn1')
    if st.session_state.lock3:
        if question_type==question_class[0]:
            question_class1()
        elif question_type==question_class[1]:
            question_class2()
    
    
    
    # 連接到 SQLite 資料庫，之後決定問卷選項後要查詢
    # conn = sqlite3.connect('member_data_v3.db')
    # cursor = conn.cursor()
    # # 你的選項列表
    # select_item_list=[
    #     [('Q3-興趣-家居和園藝',),('Q3-興趣-寵物及動物',), ('Q3-興趣-房地產',), ('Q3-興趣-旅遊',), ('Q3-興趣-書籍和文學',), ('Q3-興趣-汽車及交通工具',), ('Q3-興趣-網上社群',), ('Q3-興趣-美容和健身',), ('Q3-興趣-藝術和娛樂',), ('Q3-興趣-購物',), ('Q3-興趣-遊戲',), ('Q3-興趣-運動',), ('Q3-興趣-金融',), ('Q3-興趣-電腦和電子產品',), ('Q3-興趣-餐飲',), ('Q3-興趣-其他',)],
    #     [('Q3-青中老年成員-青老人(65至74歲)',), ('Q3-青中老年成員-中老人(75至84歲)',), ('Q3-青中老年成員-老老人(85歲以上)',), ('Q3-青中老年成員-以上都沒有',),('Q4-寵物成員-狗毛孩',), ('Q4-寵物成員-貓大人',), ('Q4-寵物成員-兔子',), ('Q4-寵物成員-鼠類',), ('Q4-寵物成員-爬蟲類',), ('Q4-寵物成員-其他',), ('Q4-寵物成員-沒有寵物',)],
    #     [('Q1-身體健康-運動健身',), ('Q1-身體健康-保健食品',), ('Q1-身體健康-健康飲食',), ('Q1-身體健康-規律作息',), ('Q1-身體健康-其他',),('Q2-心靈健康-朋友傾訴',), ('Q2-心靈健康-休閒娛樂',), ('Q2-心靈健康-醫師諮詢',), ('Q2-心靈健康-其他',),('Q4-保健議題-網路搜尋文章、新聞',), ('Q4-保健議題-社群論壇討論',), ('Q4-保健議題-健康雜誌、書籍',), ('Q4-保健議題-專業醫師、藥師',), ('Q4-保健議題-親朋好友',), ('Q4-保健議題-其他',),('Q5-擔心面臨-糖尿病',), ('Q5-擔心面臨-腎臟病',), ('Q5-擔心面臨-心臟病',), ('Q5-擔心面臨-肝臟病',), ('Q5-擔心面臨-肺部疾病',), ('Q5-擔心面臨-高血壓',), ('Q5-擔心面臨-腫瘤癌症',), ('Q5-擔心面臨-呼吸道相關疾病',), ('Q5-擔心面臨-牙齒、口腔相關疾病',), ('Q5-擔心面臨-心理疾病',), ('Q5-擔心面臨-流行感冒、疾病',), ('Q5-擔心面臨-其他',),('Q3-孕期關心-孕期營養保健品',), ('Q3-孕期關心-嬰兒車',), ('Q3-孕期關心-嬰兒床',), ('Q3-孕期關心-汽車座椅',), ('Q3-孕期關心-奶粉',), ('Q3-孕期關心-副食品',), ('Q3-孕期關心-尿布',), ('Q3-孕期關心-保險',), ('Q3-孕期關心-其他',)],
    #     [('Q1-出遊交通工具-自行駕車',), ('Q1-出遊交通工具-自行騎車',), ('Q1-出遊交通工具-自行車',), ('Q1-出遊交通工具-公車',), ('Q1-出遊交通工具-火車',), ('Q1-出遊交通工具-高鐵',), ('Q1-出遊交通工具-捷運',), ('Q1-出遊交通工具-客運',), ('Q1-出遊交通工具-走路',),('Q3-國內旅遊-海邊、離島',), ('Q3-國內旅遊-山上、風景區',), ('Q3-國內旅遊-老街、古蹟',), ('Q3-國內旅遊-農場、觀光工廠',), ('Q3-國內旅遊-城市市區',), ('Q3-國內旅遊-其他',),('Q4-出國地區-東南亞',), ('Q4-出國地區-日本、韓國',), ('Q4-出國地區-中國大陸',), ('Q4-出國地區-歐洲',), ('Q4-出國地區-美國',), ('Q4-出國地區-澳洲',), ('Q4-出國地區-其他',)],
    #     [('Q2-上班交通工具-自行駕車',), ('Q2-上班交通工具-自行騎車',), ('Q2-上班交通工具-自行車',), ('Q2-上班交通工具-公車',), ('Q2-上班交通工具-火車',), ('Q2-上班交通工具-高鐵',), ('Q2-上班交通工具-捷運',), ('Q2-上班交通工具-客運',), ('Q2-上班交通工具-走路',),('Q3-採購項目-文具用品',), ('Q3-採購項目-辦公用品',), ('Q3-採購項目-印表機、影印機',), ('Q3-採購項目-電腦設備（硬體）',), ('Q3-採購項目-電腦軟體',), ('Q3-採購項目-其他',), ('Q3-採購項目-都無法建議或決定購買',)],
    #     [('Q1-喜歡的茶類-煎茶',), ('Q1-喜歡的茶類-玄米茶',), ('Q1-喜歡的茶類-綠茶',), ('Q1-喜歡的茶類-包種茶',), ('Q1-喜歡的茶類-高山烏龍茶',), ('Q1-喜歡的茶類-東方美人茶',), ('Q1-喜歡的茶類-鐵觀音',), ('Q1-喜歡的茶類-紅茶',), ('Q1-喜歡的茶類-英式紅茶',), ('Q1-喜歡的茶類-普洱茶',), ('Q1-喜歡的茶類-水果茶',), ('Q1-喜歡的茶類-花草茶',), ('Q1-喜歡的茶類-其他',),('Q1-喜歡的茶類-我不喜歡喝茶',),('Q2-喜歡的咖啡-美式咖啡',), ('Q2-喜歡的咖啡-義式濃縮咖啡',), ('Q2-喜歡的咖啡-拿鐵',), ('Q2-喜歡的咖啡-卡布其諾',), ('Q2-喜歡的咖啡-瑪奇朵',), ('Q2-喜歡的咖啡-其他',), ('Q2-喜歡的咖啡-我不喜歡喝咖啡',),('Q3-喜歡的咖啡包裝-即溶式(三合一)',), ('Q3-喜歡的咖啡包裝-濾掛式',), ('Q3-喜歡的咖啡包裝-膠囊',), ('Q3-喜歡的咖啡包裝-罐裝',), ('Q3-喜歡的咖啡包裝-超商、咖啡店等現沖',), ('Q3-喜歡的咖啡包裝-自己選購咖啡豆沖泡',), ('Q3-喜歡的咖啡包裝-其他',),('Q4-喜歡的酒類-水果酒',), ('Q4-喜歡的酒類-紅酒',), ('Q4-喜歡的酒類-啤酒',), ('Q4-喜歡的酒類-威士忌',), ('Q4-喜歡的酒類-白酒',), ('Q4-喜歡的酒類-其他',), ('Q4-喜歡的酒類-我不喜歡喝酒',),],
    #     [('Q3-喜歡的食物-台式小吃',), ('Q3-喜歡的食物-中式菜肴',), ('Q3-喜歡的食物-義式料理',), ('Q3-喜歡的食物-美式速食',), ('Q3-喜歡的食物-泰式酸辣',), ('Q3-喜歡的食物-川味麻辣',), ('Q3-喜歡的食物-日式料理',), ('Q3-喜歡的食物-蔬食主義',), ('Q3-喜歡的食物-其他',)],
    #     [('Q1-擁有的汽車-本田（Honda）',), ('Q1-擁有的汽車-豐田（Toyota）',), ('Q1-擁有的汽車-凌志（Lexus）',), ('Q1-擁有的汽車-納智捷（LUXGEN）',), ('Q1-擁有的汽車-三菱（Mitsubishi）',), ('Q1-擁有的汽車-裕隆（Nissan）',), ('Q1-擁有的汽車-馬自達（Mazda）',), ('Q1-擁有的汽車-福特（Ford）',), ('Q1-擁有的汽車-奧迪（Audi）',), ('Q1-擁有的汽車-富豪（VOLVO）',), ('Q1-擁有的汽車-賓士（Mercedes Benz）',), ('Q1-擁有的汽車-寶馬（BMW）',), ('Q1-擁有的汽車-特斯拉（Tesla）',), ('Q1-擁有的汽車-其他',), ('Q1-擁有的汽車-我沒有汽車',),('Q3-擁有機車-一般機車(50cc)',), ('Q3-擁有機車-一般機車(100cc)',), ('Q3-擁有機車-一般機車(150cc)',), ('Q3-擁有機車-一般機車(250cc)',), ('Q3-擁有機車-重型機車',), ('Q3-擁有機車-電動機車',), ('Q3-擁有機車-我沒有機車',)],
    #     [('Q1-靜態休閒娛樂-閱讀看書',), ('Q1-靜態休閒娛樂-聽音樂會',), ('Q1-靜態休閒娛樂-看電影',), ('Q1-靜態休閒娛樂-看電視',), ('Q1-靜態休閒娛樂-看線上影音',), ('Q1-靜態休閒娛樂-玩遊戲',), ('Q1-靜態休閒娛樂-朋友聚會',), ('Q1-靜態休閒娛樂-其他',),('Q1-喜歡的遊戲類型-動作（ACT）',), ('Q1-喜歡的遊戲類型-冒險（AVG）',), ('Q1-喜歡的遊戲類型-角色扮演（RPG）',), ('Q1-喜歡的遊戲類型-第一人稱射擊（FPS）',), ('Q1-喜歡的遊戲類型-策略（SLG）',), ('Q1-喜歡的遊戲類型-音樂（MUG）',), ('Q1-喜歡的遊戲類型-格鬥（FTG）',), ('Q1-喜歡的遊戲類型-益智休閒（PUZ）',), ('Q1-喜歡的遊戲類型-我不喜歡玩遊戲',),('Q2-常用的遊戲裝置-智慧型手機/平版',), ('Q2-常用的遊戲裝置-筆記型電腦',), ('Q2-常用的遊戲裝置-桌上型電腦',), ('Q2-常用的遊戲裝置-SNOY Play Station',), ('Q2-常用的遊戲裝置-微軟 XBOX',), ('Q2-常用的遊戲裝置-任天堂 Switch',), ('Q2-常用的遊戲裝置-其他',),('Q3-喜歡的影視類型-動作、冒險片',), ('Q3-喜歡的影視類型-喜劇片',), ('Q3-喜歡的影視類型-愛情片',), ('Q3-喜歡的影視類型-恐怖、驚悚、懸疑片',), ('Q3-喜歡的影視類型-奇幻片、科幻片',), ('Q3-喜歡的影視類型-歌舞劇、音樂片',), ('Q3-喜歡的影視類型-戰爭片',), ('Q3-喜歡的影視類型-歷史電影',), ('Q3-喜歡的影視類型-動畫片',), ('Q3-喜歡的影視類型-其他',),('Q4-常用的影視裝置-第四台',), ('Q4-常用的影視裝置-中華電信 MOD',), ('Q4-常用的影視裝置-Netflix',), ('Q4-常用的影視裝置-friDay影音',), ('Q4-常用的影視裝置-LINE TV',), ('Q4-常用的影視裝置-KKTV',), ('Q4-常用的影視裝置-WeTV',), ('Q4-常用的影視裝置-Amazon Prime Video',), ('Q4-常用的影視裝置-Apple TV+',), ('Q4-常用的影視裝置-其他',)],
    #     [('Q2-動態休閒娛樂-健身房健身',), ('Q2-動態休閒娛樂-球場打球',), ('Q2-動態休閒娛樂-慢跑健走',), ('Q2-動態休閒娛樂-爬山',), ('Q2-動態休閒娛樂-逛街購物',), ('Q2-動態休閒娛樂-逛展覽',), ('Q2-動態休閒娛樂-其他',),],
    #     [('Q3-提神方法-喝茶類飲品',), ('Q3-提神方法-喝咖啡',), ('Q3-提神方法-喝提神飲料',), ('Q3-提神方法-抽菸／電子菸',), ('Q3-提神方法-以上皆非',),],
    #     ]
    # #標準答案表格獲取過程
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # tables=cursor.fetchall()
    # #先把資料庫中的資料表名稱及欄位匯入
    # answer_data={}
    # #用於比對找出資料表
    # for table_index in range(1,len(tables)):
    #     single_col_total=[]
    #     cursor.execute(f"PRAGMA table_info(`{tables[table_index][0]}`);")
    #     columns = cursor.fetchall()
    #     for single_col in columns:
    #         if single_col[2]=='TEXT':
    #             continue
    #         single_col_total.append(single_col[1])
    #     answer_data[tables[table_index][0]]=single_col_total
    # # 創建一個列表來保存所有選擇
    # selected_items_all = []
    # #儲存要搜尋的欄位
    # target_select=[]
    # # 定義列和標題的映射
    # columns = st.columns(3)
    # #精簡版
    # group_titles = ['興趣','家庭成員','身心靈議題',
    #                 '旅遊相關','工作相關','飲品議題',
    #                 '喜歡的食物','擁有車型','靜態休閒娛樂',
    #                 '動態休閒娛樂','提神方法']
    # #原版
    # # group_titles = ['Q3-興趣', 'Q3-青中老年成員', 'Q4-寵物成員', 
    # #                 'Q1-身體健康', 'Q2-心靈健康', 'Q3-提神方法',
    # #                 'Q4-保健議題', 'Q1-出遊交通工具', 'Q2-上班交通工具',
    # #                 'Q3-國內旅遊', 'Q4-出國地區', 'Q1-靜態休閒娛樂',
    # #                 'Q2-動態休閒娛樂', 'Q3-喜歡的食物', 'Q3-採購項目',
    # #                 'Q3-孕期關心', 'Q1-喜歡的茶類', 'Q2-喜歡的咖啡',
    # #                 'Q3-喜歡的咖啡包裝', 'Q4-喜歡的酒類', 'Q5-擔心面臨',
    # #                 'Q1-擁有的汽車', 'Q3-擁有機車', 'Q1-喜歡的遊戲類型',
    # #                 'Q2-常用的遊戲裝置', 'Q3-喜歡的影視類型', 'Q4-常用的影視裝置',]
    # # 使用循環來創建多選框
    # for i in range(11):
    #     with columns[i%3]:
    #         select_list = st.multiselect(group_titles[i], [single_var[0] for single_var in select_item_list[i]], [])
    #         st.write(select_list)
    #         selected_items_all.append(select_list)
    

    # count=0
    # colqu1,colqu2,colqu3 = st.columns(3)
    # with colqu2:
    #     select_sub=st.button('確定送出',on_click=lock_fun3,disabled=st.session_state.lock3,key='btn1')


    # if st.session_state.lock3:
    #     for single_list in selected_items_all:
    #         if len(single_list)==0:
    #             count+=1
    #     if count==11:
    #         st.markdown("**無選取項目，請刷新網頁後重新選擇**")
    #     if count<11:
    #         for i, selected_items in enumerate(selected_items_all):
    #             if selected_items:  # 只顯示有選擇的項目
    #                 st.markdown(f"**{group_titles[i]}:**")
    #                 select_item_view=st.write(f"{','.join(selected_items)}")
    #         #按下進行篩選      
    #         if st.session_state.lock3:
    #             question_select_date=[]
    #             col10,col11= st.columns(2)
    #             with col10:
    #                 start_date_select=st.date_input('請選擇問卷填寫起始時間')    
    #                 question_select_date.append(int(str(start_date_select).replace('-','')))

    #             with col11:
    #                 end_date_select=st.date_input('請選擇問卷填寫結束時間')
    #                 question_select_date.append(int(str(end_date_select).replace('-','')))

                
    #             col12,col13,col14 = st.columns(3)
    #             with col13:
    #                 filter_go=st.button('進行篩選',on_click=lock_fun4,disabled=st.session_state.lock4,key='btn2')
    #                 if filter_go:
                        
    #                     if start_date_select>end_date_select:
    #                         st.write('開始日期大於結束日期，請刷新頁面重新選擇')
                        
    #                     else:
    #                         #把儲存在不同 list 的選擇改放到同一個 list
    #                         for single_select_group in selected_items_all:
    #                             if len(single_select_group)==0:
    #                                 continue
    #                             for single_select in single_select_group:
    #                                 target_select.append(single_select)
    #                         #把要進行搜尋的欄位與資料表結合成字典
    #                         find_dict={}
    #                         for key,value in answer_data.items():
    #                             tmp_list=[]
    #                             for single_col in target_select:
    #                                 if single_col in value:
    #                                     tmp_list.append(single_col)
    #                             if len(tmp_list)==0:
    #                                 continue
    #                             find_dict[key]=tmp_list
    #                         #輸出查詢結果合併表格
    #                         result_table=[]
    #                         for single_table,table_col in find_dict.items():
                                
    #                             for single_col in table_col:
    #                                 query=f'''
    #                                 SELECT `memberNo` FROM `{single_table}`
    #                                 WHERE `{single_col}` = 1.0
    #                                 AND `logTime` BETWEEN {question_select_date[-2]} AND {question_select_date[-1]};'''
    #                                 #print(question_select_date[-2],question_select_date[-1])
    #                                 #防止SQL注入攻擊，避免把數值寫在原始SQL語句內，至少要傳入兩個參數
    #                                 #params=(1.0,1.0)
    #                                 cursor.execute(query)
    #                                 result_table.append(cursor.fetchall())
    #                         #進行交集運算，找出共有元素
                            
    #                         finally_result=[]
    #                         member_cal_result=set.intersection(*map(set,result_table))
    #                         #print(member_cal_result)
    #                         for member_filter in member_cal_result:
    #                             finally_result.append(member_filter[0])
    #                         #print(finally_result)
    #                         #找出符合條件之會員的基本資料
    #                         #用於儲存從資料庫查詢後再準備要顯示dataframe的數據
    #                         df_data=[]
    #                         for single_member in finally_result:
    #                             query=f'''
    #                             SELECT `memberNo`,`性別`,`年紀`,`所在直轄市及縣`,`婚姻`,`薪資水平`,`職業別`
    #                             FROM UU_member_data
    #                             WHERE `memberNo` IN ("{single_member}");'''
    #                             df_data.append(list((cursor.execute(query))))
    #                         #print(df_data)
    #                         #顯示dataframe
    #                         member_df=pd.DataFrame(columns=['memberNo','性別','年紀','所在直轄市及縣','婚姻','薪資水平','職業別'])
    #                         for single_df in df_data:
    #                             try:
    #                                 member_df.loc[len(member_df)]=single_df[0]
    #                             except:
    #                                 continue
    #                         st.write(f"會員筆數 : {member_df.shape[0]}")
    #                         st.dataframe(member_df,use_container_width=True)
                            
                        
                        
    # # 關閉連接
    # conn.close()

def member_carrier():
    
    
    test_fre=[]
    
    
    # 連接到另一個載具 SQLite 資料庫
    conn = sqlite3.connect('member_carrier_v3.db')
    cursor = conn.cursor()
    
    area_name=['台北市','台南市','高雄市','新北市','桃園市',
               '台中市','基隆市','新竹市','新竹縣','台東縣',
               '花蓮縣','南投縣','彰化縣','雲林縣','宜蘭縣',
               '苗栗縣','嘉義縣','嘉義市','屏東縣','金門縣',
               '澎湖縣','連江縣',]
    
    #取得商家名稱
    query='''
    SELECT `消費地點` FROM `einvoice_header`;
    '''
    cursor.execute(query)
    store_list=[]
    
    for area_var in cursor.fetchall():
        store_list.append(area_var[0])
    store_list=list(set(store_list))
    
    carr_col1,carr_col2=st.columns(2)
    with carr_col1:
        area_select=st.selectbox('選擇消費地區',area_name)
    with carr_col2:
        store_select=st.selectbox('選擇消費地點',store_list)
    print(area_select)
    print(store_select)
    #消費金額加總
    carr_col3,carr_col4,carr_col5=st.columns(3)
    with carr_col4:
        pay_total=st.button('進行計算',on_click=lock_fun7,disabled=st.session_state.lock7)
    
    if st.session_state.lock7:
        
        #找出消費地區、消費地點、商品項目、單價，再從中計算出商品購買次數
        query=f'''SELECT "merge_area_store"."消費地區", 
                   "merge_area_store"."消費地點", 
                   "merge_area_store"."商品項目", 
            	   "merge_area_store"."單價", 
                  COUNT("merge_area_store"."商品項目") AS "消費次數"
                  FROM "merge_area_store"
                  WHERE "消費地區" = '{area_select}' 
                  AND "消費地點" = '{store_select}'
                  GROUP BY "merge_area_store"."消費地區", 
                           "merge_area_store"."消費地點", 
                           "merge_area_store"."商品項目";'''
        
        
        cursor.execute(query)
        commodity_data=cursor.fetchall()
        #顯示dataframe
        commodity_view=pd.DataFrame(columns=['消費地區','消費地點','消費商品','商品單價','消費次數'])
        for single_commodity_data in commodity_data:
            try:
                commodity_view.loc[len(commodity_view)]=single_commodity_data
            except:
                continue
        st.write(f"會員筆數 : {commodity_view.shape[0]}")
        st.dataframe(commodity_view,use_container_width=True)
            
    # #------------------------------
    # col7,col8,col9 = st.columns(3)
    # with col8:
    #     select_sub=st.button('確定送出',on_click=lock_fun3,disabled=st.session_state.lock3,key='btn1')
    #     if select_sub:
    #         member_list=[]
    
    # #------------------------------
    # # 關閉連接
    # cursor.close()
    conn.close()

#介面按鈕鎖定項
#會員問卷
def lock_fun1():
    st.session_state.lock1=True
#會員載具
def lock_fun2():
    st.session_state.lock2=True
#會員問卷->確定送出
def lock_fun3():
    st.session_state.lock3=True
#會員問卷->確定送出->下一步
def lock_fun4():
    st.session_state.lock4=True
#會員問卷->確定送出(UU與你的距離)->下一步->進行篩選
def lock_fun5():
    st.session_state.lock5=True
#會員問卷->確定送出(GMO)->下一步->進行篩選
def lock_fun6():
    st.session_state.lock6=True
#會員載具->開始計算
def lock_fun7():
    st.session_state.lock7=True
    

if 'lock1' not in st.session_state:
    st.session_state.lock1=False
if 'lock2' not in st.session_state:
    st.session_state.lock2=False
#會員問卷按鈕變數------------------------
if 'lock3' not in st.session_state:
    st.session_state.lock3=False
if 'lock4' not in st.session_state:
    st.session_state.lock4=False
if 'lock5' not in st.session_state:
    st.session_state.lock5=False
if 'lock6' not in st.session_state:
    st.session_state.lock6=False
#會員載具按鈕變數-------------------------------------
if 'lock7' not in st.session_state:
    st.session_state.lock7=False    


#介面放寬
st.set_page_config(layout="wide")
#開頭標題引導
st.markdown("""
         <h3 style='text-align:center;
             font-weight:bold;'>
             會員輪廓查詢系統</h3>"""
             ,unsafe_allow_html=True)
#定義 CSS 樣式，將按鈕寬度設為 100%
st.markdown("""
    <style>
    .stButton button {
        width: 95.5%;  /* 按鈕寬度拉到佔據欄位的100% */
    }
    </style>
    """, unsafe_allow_html=True)

# 使用 columns 方法將按鈕居中
col1, col2, col3 = st.columns([1, 1, 1])  # 左右佔2，中間佔1
with col2:  # 將按鈕放置在中間欄位
    first_bt1_sub = st.button('會員問卷', on_click=lock_fun1, disabled=st.session_state.lock1)
if st.session_state.lock1:
    member_question()
#加一條線分開
st.divider()

col4, col5, col6 = st.columns([1, 1, 1])  # 左右佔2，中間佔1
with col5:
    first_bt2_sub = st.button('會員載具', on_click=lock_fun2, disabled=st.session_state.lock2)
if st.session_state.lock2:
    member_carrier()
