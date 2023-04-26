import database as deta_db
import streamlit_authenticator as stauth

# hashed_passwords = stauth.Hasher(['...', '...', '...']).generate()
# print(hashed_passwords)

usernames = ["bhargav", "chaitanya", "dheeren"]
names = ["Bhargav Muktevi", "Chaitanya Sankaramanchi", "Dheeren Pawar"]
passwords = ["....", "....", "...."]
roles = ["basic", "basic", "admin"]

# for (username, name, password, role) in zip(usernames, names, passwords, roles):
# deta_db.insert_user(username, name, password, role)
