FROM python:3.9-buster

EXPOSE 8501

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm

COPY . .

CMD python -m streamlit run interface/main.py