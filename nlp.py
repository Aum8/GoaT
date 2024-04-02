import spacy

# Load the English language model (change 'en_core_web_sm' for other languages/models)
nlp = spacy.load("en_core_web_sm")

def spacy_processing(text):
  # Process the text with spaCy
  doc = nlp(text)
  # Extract tokens, lemmas, and POS tags
  tokens = [token.text for token in doc]
  lemmas = [token.lemma_ for token in doc]
  pos_tags = [(token.text, token.pos_) for token in doc]
  return tokens, lemmas, pos_tags
