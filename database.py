from deta import Deta
import streamlit as st

deta = Deta(st.secrets["deta_key"])
db = deta.Base("users")


def insert_user(username, name, password, role):
    return db.put({"key": username, "name": name, "password": password, "role": role})


def fetch_all_users():
    res = db.fetch()
    return res.items


def get_user(username):
    return db.get(username)


def update_user(username, updates):
    return db.update(updates, username)


def delete_user(username):
    return db.delete(username)
