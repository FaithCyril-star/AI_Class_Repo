import datefinder
from datetime import datetime
from helpers import extract_skills, extract_text_from_pdf, get_match_score, preprocess_text,get_topk
import os
import re
import sys
sys.path.append('/Users/faithsobecyril/Desktop/Projects/AI/Midsem/AI_Class_Repo/Midsem_project/resumes')


def get_rankings(job_description,job_description_weights=None,k=None,exact_match=True):
    match_scores = {}
    resumes_path = r"resumes"

    job_description_tokens = preprocess_text(job_description)
    total_possible_match_score = len(job_description_tokens)
    if job_description_weights:
        for weight in job_description_weights.values():
            total_possible_match_score += (weight-1)
 
    for root,_,files in os.walk(resumes_path):
        for file in files:
            resume_text = extract_text_from_pdf(root+"/"+file)
            resume_tokens = preprocess_text(resume_text)
            found_skills = extract_skills(resume_tokens,job_description_tokens,exact_match)
            years_of_experience = get_years_of_experience(resume_text)
            match_scores[file] = (get_match_score(found_skills,job_description_weights)/total_possible_match_score,years_of_experience)
        
    if k is None:
        k = len(files)
    ranking = get_topk(match_scores,k)
    return ranking


def get_years_of_experience(resume_text):
    experience_titles = ['EXPERIENCE', 'WORK EXPERIENCE', 'PROFESSIONAL EXPERIENCE','EMPLOYMENT','EMPLOYMENT EXPERIENCE','WORK HISTORY']
    following_sections = ['EDUCATION', 'SKILLS', 'PROJECTS', 'CAMPUS INVOLVEMENT','EXTRACURRICULARS','LEADERSHIP & CO-CURRICULAR ACTIVITIES','VOLUNTEER WORK']
    experience_pattern = '|'.join(experience_titles)
    following_section_pattern = '|'.join(following_sections)
    experience_section = re.search(fr'({experience_pattern})(.*?)(?={following_section_pattern})', resume_text, re.DOTALL).group()
    if experience_section:
        matches = []
        full_numeric_dates = []
        full_numeric_date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b'
        full_numeric_dates.extend(re.findall(full_numeric_date_pattern, experience_section,re.IGNORECASE))

        partial_numeric_dates = []
        year_only_pattern = r'\b\d{4}\b'
        year_month_only_pattern = r'\b\d{1,2}/\d{4}\b'
        partial_numeric_date_pattern = f"{year_only_pattern}|{year_month_only_pattern}"
        partial_numeric_dates.extend(re.findall(partial_numeric_date_pattern, experience_section,re.IGNORECASE))

        text_dates = []
        text_date_pattern = r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}\b(?:\s*(?:to|-)\s*(?:PRESENT|\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}\b)?)?'
        text_dates.extend(re.findall(text_date_pattern, experience_section,re.IGNORECASE))

        # add all date matches
        matches.extend([date[date.index("/")+1:] for date in full_numeric_dates])
        matches.extend(partial_numeric_dates)
        for text_date in text_dates:
            date = re.split(r'[-to]',text_date) ##adding present as current time
            for d in date:
                matches.append(d)
            

        # convert matches to date objects
        dates = []
        for match in matches: 
            for date in datefinder.find_dates(match):
                dates.append(str(date))
        dates = sorted(dates)

        total_work_experience = 0
        dates = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in dates]
        for i in range(0, len(dates), 2):
            start_date = dates[i]
            end_date = dates[i + 1] if i + 1 < len(dates) else datetime.now()  # If end date is not provided, assume current date
            duration = end_date - start_date
            total_work_experience += duration.days

        return round(total_work_experience/365,2)
    return 0












