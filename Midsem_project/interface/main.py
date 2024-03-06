import streamlit as st
from streamlit_tags import st_tags
import time
import sys
sys.path.append('/Users/faithsobecyril/Desktop/Projects/AI/Midsem/AI_Class_Repo/Midsem_project/recommender')
import model
import numpy as np
import pandas as pd
from utils import save_uploadedfile,clear_success_mesages

KEY_SKILLS_WEIGHT = 3


def main():
    st.title("Resume Parsing and Recommendation System")
    st.divider()
    st.caption("A Python application that automates the process of parsing resumes (CVs) from PDF format, extracts relevant information and recommends candidates based on specific job requirements and years of experience.")
    job_description = st.text_area("Enter your job description",height=150)
    key_skills = st_tags(
        label='Enter most important skills:',
        text='Press enter to add more',
        maxtags = -1)
    match_type = st.checkbox("Exact token match")
    st.markdown('##')
    resumes = st.file_uploader("Upload your resumes", type=['pdf'], accept_multiple_files=True, label_visibility="visible")
    for resume in resumes:
        save_uploadedfile(resume)

    _, _, col3 , _, _ = st.columns(5)
    with col3 :
        submit = st.button("Submit")

    if submit:
        clear_success_mesages()
        if key_skills:
            key_skills = {skill.lower():KEY_SKILLS_WEIGHT for skill in key_skills}
        with st.spinner('Analyzing resumes...'):
            candidates,match_scores,years_of_experience = model.get_rankings(job_description,job_description_weights=key_skills,exact_match=match_type)
        data_frame = pd.DataFrame(zip(candidates,match_scores,years_of_experience),columns=['candidates','match_scores','years_of_experience'])
        st.write("Results:")
        st.table(data_frame)


if __name__=='__main__':
    main()