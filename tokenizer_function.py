# import libraries
import re

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def tokenize(text):
    '''Function to clean and tokenize text
    INPUT:
    text(str) - text message to be processed

    OUTPUT:
    clean_tokens(list) - text tokens list
    '''
    # check if there are urls within the text
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    detected_urls = re.findall(url_regex,text)
    for url in detected_urls:
        text = text.replace(url,"urlplaceholder")
    
    # remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]"," ",text)
    
    # tokenize the text
    tokens = word_tokenize(text)
    
    # remove stop words
    tokens = [tok for tok in tokens if tok not in stopwords.words("english")]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens