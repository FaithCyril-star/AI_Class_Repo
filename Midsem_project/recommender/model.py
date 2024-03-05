from helpers import extract_skills, extract_text_from_pdf, get_match_score, preprocess_text,get_topk
import os
import sys
sys.path.append('/Users/faithsobecyril/Desktop/Projects/AI/Midsem/AI_Class_Repo/Midsem_project/resumes')


def get_rankings(job_description,job_description_weights=None,k=None):
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
            found_skills = extract_skills(resume_tokens,job_description_tokens)
            match_scores[file] = get_match_score(found_skills,job_description_weights)/total_possible_match_score
    ranking = get_topk(match_scores,k)
    return ranking












