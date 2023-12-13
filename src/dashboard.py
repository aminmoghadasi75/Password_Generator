import streamlit as st
from src.main import RandomPassword,PinPassword,MemorablePassword
st.image('https://th.bing.com/th/id/OIP.UvLbU27o4w0CkWt2aROqLQHaHa?pid=ImgDet&rs=1',width=200)
st.title(':blue[_PasswordGenerator_]:red[_Project_]:lock::key:')
options = ['None', 'Random Password', 'PIN Password', 'Memorable Password']
option_pass = st.selectbox('Which Style want to generate the uniqe randomly password ? ',options)
if option_pass == 'Random Password':
    length = st.slider('The length of Password Characters',min_value=4, max_value=20,value=8)
    include_number = st.toggle('Include Numbers')
    include_symbol = st.toggle('Include Symbols')
    if st.button('Click To Generat a Random Password'):
        password = RandomPassword(length=length, include_numbers=include_number, include_symbols=include_symbol)
        st.write(f'Your Password : `{password.generate()}`')
if option_pass == 'PIN Password':
    length = st.slider('The length of Password Characters',min_value=4, max_value=20,value=8)
    if st.button('Click To Generat a Random Password'):
        password = PinPassword(length=length)
        st.write(f'Your Password : `{password.generate()}`')
if option_pass == 'Memorable Password':
    num_of_words = st.number_input('Number of Words',step=1)
    seperator_list = ['None','-','_','*','/','+','.',',',':',';']
    seperator = st.selectbox('Pick a Seperator you want',seperator_list)
    capitalization = st.toggle('Capitalize the words')
    if st.button('Click To Generat a Random Password'):
        password = MemorablePassword(num_of_words=num_of_words,separator=seperator,capitalization=capitalization)
        st.write(f'Your Password : `{password.generate()}`')



