import streamlit_authenticator as stauth
import database as deta_db


def authenticate():
    credentials_main = {}
    credentials_temp = {}
    usernames = []
    names = []
    passwords = []
    roles = []
    users = deta_db.fetch_all_users()
    for user in users:
        usernames.append(user['key'])
        names.append(user['name'])
        passwords.append(user['password'])
        roles.append(user['role'])
    for username, name, password, role in zip(usernames, names, passwords, roles):
        credentials_temp[username] = {"name": name, "password": password, "role": role}
    credentials_main["usernames"] = credentials_temp
    authenticator = stauth.Authenticate(
        credentials_main,
        "cricket_cookie",
        "cricket_dashboard",
        1,
    )
    name, authentication_status, username = authenticator.login('Login', 'main')
    return name, authentication_status, username, authenticator



