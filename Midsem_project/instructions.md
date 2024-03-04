Resume Parsing and Recommendation System
Objective:
Develop a Python application that automates the process of parsing resumes (CVs) from PDF format, extracts relevant information using OCR (Optical Character Recognition) and NLP (Natural Language Processing) techniques, and recommends candidates based on specific job requirements and years of experience.
Tools and Libraries:
  - Python 3.x
  - OCR libraries (e.g., PyMuPDF, pytesseract)
  - Spacy for NLP tasks
  - Pandas for data manipulation
  - Any other library you find necessary

Requirements:\
1 . PDF Resume Parsing:
  Implement a function to read resumes in PDF format and convert them to text using OCR techniques. Consider edge cases where resumes have complex layouts or include images.

2 . Information Extraction:
  Use Spacy and regular expressions to extract structured information from the resume texts, including but not limited to:
  - Candidate's Name
  - Contact Information
  - Skills
  - Educational Background
  - Professional Experience (including job titles, companies, and duration)

3 . Experience Calculation:
  Develop a method to calculate the total years of professional experience for each candidate based on their resume's professional experience section.

4 . Job Requirement Matching:
  Allow the input of job requirements, including required skills and minimum years of experience. Implement a matching algorithm to filter candidates who meet the job requirements based on their skills and experience.

5 . Recommendation System:
  Create a system to rank and recommend the top N candidates for a given job posting based on the match score of skills and years of experience.

6 . User Interface (Optional):
  Develop a simple user interface (can be CLI, web, or GUI) where a user can upload PDF resumes, input job requirements, and view the list of recommended candidates.

Deliverables:
  - Source code for the resume parsing and recommendation system.
  - A detailed report explaining your methodology, challenges faced, and how they were overcome. Include screenshots or a video demo if a user interface is developed.
  - A set of test resumes (in PDF format) and a test job requirement to demonstrate the functionality of your system.

Evaluation Criteria:
  - Accuracy of information extraction from resumes.
  - Effectiveness of the matching algorithm in identifying suitable candidates based on job requirements.
  - Code quality, including readability, comments, and adherence to best practices.
  - Innovation in handling edge cases and improving the user experience.
  
Submission Guidelines:
  - Submit your source code and report as a compressed archive (ZIP or RAR) to the designated submission portal by [insert due date].
  - Ensure your submission includes a README file with instructions on how to run your application, along with any necessary installation steps for dependencies.
  - This assignment not only tests your programming skills but also your ability to apply machine learning and NLP concepts in a practical scenario.
