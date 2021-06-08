import streamlit as st
import webbrowser
import pandas as pd
import datetime

#アンケート数値化
ans_output = []
q_nums = ['Q1','Q2','Q3','Q4','その他']
def val(q):
    if q == 'すごく良い':
        ans_output.append(5)
    elif q == '良い':
        ans_output.append(4)
    elif q == 'どちらとも言えない':
        ans_output.append(3)
    elif q == '悪い':
        ans_output.append(2)
    elif q == 'すごく悪い':
        ans_output.append(1)
    else:
        ans_output.append(q)


st.title('Welcome to 3D room tour!!!')
#st.subheader('内見形式を選択してください')
url1 = 'file:///' + 'Users/komakoma/Desktop/github/upload/test.html'

# 内見
view = st.button('3Dモデルを見る')
if view == True:
    webbrowser.open_new_tab(url1)

#アンケート
st.write("アンケートに答える")
q =  st.checkbox('Yes', value=False) # valueは初期状態
if q == True:
    q = ['すごく良い', '良い', 'どちらとも言えない','悪い','すごく悪い']
    ans = []
    q1 = st.radio("Q1",q)
    ans.append(q1)
    val(q1)
    q2 = st.radio("Q2",q)
    ans.append(q2)
    val(q2)
    q3 = st.radio("Q3",q)
    ans.append(q3)
    val(q3)
    q4 = st.radio("Q4",q)
    ans.append(q4)
    val(q4)
    qf = st.text_input('その他')
    ans.append(qf)
    val(qf)
    #print(ans_output)
    
    #アンケート送信
    send = st.button('アンケートを送信')
    if send == True:
        # データフレームを作成
        df = pd.DataFrame([ans_output], columns=q_nums)
        path = '/Users/komakoma/Box/test/'
        # CSV ファイル出力
        now = datetime.datetime.now()
                    #ここのパスをbox契約後変更#
        df.to_csv('/Users/komakoma/Box/test/answers' + now.strftime('%Y_%m_%d_%H_%M') + '.csv',encoding='utf_8_sig')
        #表示
        #df