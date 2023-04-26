import streamlit as st
import authenticate as auth


def do_stuff_on_page_load():
    # To set the page layout to wide on page load
    st.set_page_config(layout="wide")


do_stuff_on_page_load()

name, authentication_status, username, authenticator = auth.authenticate()

if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif not authentication_status:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')


