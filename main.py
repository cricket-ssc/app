import streamlit as st
import authenticate as auth

admin_sidebar_list = ["Create Practice"]
player_sidebar_list = ["Match Availability", "Practice Availability"]


def do_stuff_on_page_load():
    # To set the page layout to wide on page load
    st.set_page_config(layout="wide")


do_stuff_on_page_load()

name, authentication_status, username, authenticator = auth.authenticate()

if authentication_status is not None:
    if authentication_status:
        if username in ["dheeren"]:
            admin_sidebar_list = admin_sidebar_list + ["Create Match", "Create Inventory"]
            player_sidebar_list = player_sidebar_list + ["Finance Management", "Invoice Management", "Inventory Management"]
        authenticator.logout('Logout', 'sidebar')

        admin_functionalities = st.sidebar.radio(
            "Admin Roles",
            tuple(admin_sidebar_list),
        )

        st.sidebar.markdown("---")

        player_functionalities = st.sidebar.radio(
            "Player Roles",
            tuple(player_sidebar_list)
        )

        st.subheader(f'Welcome *{name}*')
        st.title('Some content')
    else:
        st.error('Username/password is incorrect')
