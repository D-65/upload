import streamlit as st
import webbrowser

st.title('-----テストページ-----')
st.subheader('内見形式を選択してください')
uri1 = 'file:///' + 'Users/komakoma/Desktop/github/upload/test.html'

# 内見方式
view = st.button('3D')
if view == True:
     webbrowser.open_new_tab(uri1)
view = st.button('2D')
if view == True:
     webbrowser.open_new_tab(uri2)

#アンケート
st.write("アンケートに答える")
q =  st.checkbox('Yes', value=False) # valueは初期状態
if q == True:
    q = ['すごく良い', '良い', 'どちらとも言えない','悪い','すごく悪い']
    ans = []
    q1 = st.radio("Q1",q)
    ans.append(q1)
    q2 = st.radio("Q2",q)
    ans.append(q2)
    q3 = st.radio("Q3",q)
    ans.append(q3)
    q4 = st.radio("Q4",q)
    ans.append(q4)
    st.text_input('その他')
    
    send = st.button('アンケートを送信')
    if send == True:
        
# 選択肢
st.selectbox('ラベル',('選択肢1', '選択肢2', '選択肢3'))

