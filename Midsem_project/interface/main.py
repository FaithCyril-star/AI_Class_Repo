import sys
sys.path.append('/Users/faithsobecyril/Desktop/Projects/AI/Midsem/AI_Class_Repo/Midsem_project/recommender')

import model


job_description = """
Basic Qualifications

 Currently enrolled in a Bachelor’s or Master’s Degree in Computer Science, Computer Engineering, or related fields at time of application
 Although no specific programming language is required – you should be familiar with the syntax of languages such as Java, C/C++, or Python
 Knowledge of Computer Science fundamentals such as object-oriented design, algorithm design, data structures, problem solving and complexity analysis.

Preferred Qualifications

 Previous technical internship(s) if applicable
 Experience with distributed, multi-tiered systems, algorithms, and relational databases
 Experience in optimization mathematics such as linear programming and nonlinear optimisation
 Ability to effectively articulate technical challenges and solutions
 Adept at handling ambiguous or undefined problems as well as ability to think abstractly
"""
print("candidate | score | YOE")
print(model.get_rankings(job_description,job_description_weights={"python":5,"git":3},exact_match=True))
