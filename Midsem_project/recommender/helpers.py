import heapq
from pypdf import PdfReader
import re
import spacy
import gensim.downloader as api
from sklearn.metrics.pairwise import cosine_similarity

# Download this model
nlp = spacy.load("en_core_web_sm") 

# # Load pre-trained Word2Vec model
# word_vectors = api.load("word2vec-google-news-300")

SIMILARITY_THRESHOLD = 0.9

def deduplicate_tokens(tokens):
    return list(set(tokens))


def extract_skills(resume_tokens, job_description_tokens):
    found_skills = set()
    job_description_tokens = set(job_description_tokens) ##remove this is you are using cosine similarity
    for token in resume_tokens:
        # resume_token_vector = word_vectors[token]
        # for other_token in job_description_tokens:
        #     job_description_token_vector = word_vectors[other_token]
            ## semantic similarity
            # if cosine_similarity([resume_token_vector], [job_description_token_vector])[0][0] >= SIMILARITY_THRESHOLD:
            #     found_skills.add(token)

            # direct comparision
        if token in job_description_tokens:
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


def get_match_score(found_skills,job_description_weights={}):
    score = len(found_skills)

    if job_description_weights == {}:
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


def get_topk(match_scores,k):
    heap = []
    
    for candidate, score in match_scores.items():
        heapq.heappush(heap, (-score, candidate))
    
    ranking = []
    for _ in range(k):
        candidate = heapq.heappop(heap)[1]
        ranking.append((candidate,match_scores[candidate]))
    
    return ranking
