import streamlit as st

value = 0
btn = st.button('+1する')
if 'increment' not in st.session_state: # 初期化
    st.session_state['increment'] = 0
    st.subheader(f"初期値は{st.session_state['increment']}です。")
     
if btn:
    st.subheader(f'初期値は{value}です。')
    st.session_state['increment'] += 1 # 値を増やす
    st.write(f"{st.session_state['increment']}になりました。")
