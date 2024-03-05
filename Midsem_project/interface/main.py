import sys
sys.path.append('/Users/faithsobecyril/Desktop/Projects/AI/Midsem/AI_Class_Repo/Midsem_project/recommender')

import model


job_description = """
Requirements:
Bachelor's degree in Computer Science, Engineering, or related field.
 years of professional experience as a Software Engineer or related role.
Proficiency in [programming languages, frameworks, and technologies relevant to the role, e.g., Python, Java, JavaScript, etc.].
Strong understanding of software development principles, design patterns, and best practices.
Experience with version control systems (e.g., Git) and agile development methodologies.
Excellent problem-solving skills and attention to detail.
Strong communication and collaboration skills, with the ability to work effectively in a team environment.
"""
print(model.get_rankings(job_description,{"python":5,"git":3,"computer":5},k=2))
