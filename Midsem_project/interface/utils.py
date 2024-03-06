import os
import streamlit as st
import time

success_messages = []


def save_uploadedfile(uploadedfile):
    with open(os.path.join("/Users/faithsobecyril/Desktop/Projects/AI/Midsem/AI_Class_Repo/Midsem_project/resumes",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
    return show_upload_success_message(uploadedfile.name)


def show_upload_success_message(file_name):
    success = st.success(f"{file_name} saved to resumes")
    success_messages.append(success)


def clear_success_mesages():
    for success in success_messages:
        success.empty()
    success_messages.clear()