import heapq
from pypdf import PdfReader
import re
import spacy
from gensim.models import KeyedVectors

# Download this model
nlp = spacy.load("en_core_web_sm") 

# Load pre-trained Word2Vec model
filename = r'recommender/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(filename, binary=True)

SIMILARITY_THRESHOLD = 0.9

def deduplicate_tokens(tokens):
    return list(set(tokens))


def extract_skills(resume_tokens, job_description_tokens,exact_match):
    found_skills = set()
    job_description_tokens = set(job_description_tokens) ##remove this is you are using cosine similarity
    for token in resume_tokens:
        if exact_match:
             # direct comparision
             if token in job_description_tokens:
                found_skills.add(token)
        else:
            # semantic similarity
            for other_token in job_description_tokens:
                try:
                    if model.similarity(token,other_token) >= SIMILARITY_THRESHOLD:
                        found_skills.add(token)
                except KeyError:
                    if token == other_token:
                        found_skills.add(token)


    return found_skills


def extract_text_from_pdf(pdf_path):
    with open(pdf_path,'rb') as file:
        reader = PdfReader(file)
        pages = []
        for page in reader.pages:
            pages.append(page.extract_text(extraction_mode="layout"))

        text = join_string_from_list(pages)
        return text


def get_topk(match_scores,k):
    heap = []
    
    for candidate, score in match_scores.items():
        heapq.heappush(heap, (-score[0], score[1], candidate))
    
    ranking = []
    for _ in range(k):
        candidate = heapq.heappop(heap)[-1]
        ranking.append((candidate,match_scores[candidate][0],match_scores[candidate][1],match_scores[candidate][2]))

    ranking.sort(key = lambda candidate:(-candidate[1],-candidate[2]))
    return ranking


def get_match_score(found_skills,job_description_weights={}):
    score = len(found_skills)

    if job_description_weights == None:
        return score

    for skill in job_description_weights:
        if skill in found_skills:
            score += (job_description_weights[skill]-1)
    return score


def join_string_from_list(string_list):
    return "".join(string_list)


def preprocess_text(text):
    text = text.lower()
    text = remove_nonalphanumeric_characters(text)
    text = remove_whitespace(text)
    word_tokens = nlp(text)
    filtered_deduplicated_tokens = deduplicate_tokens([token.text for token in word_tokens if not token.is_stop])
    return filtered_deduplicated_tokens


def remove_nonalphanumeric_characters(text):
    return join_string_from_list(filter(lambda char: char.isalnum() or char.isspace(), text))


def remove_whitespace(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text



