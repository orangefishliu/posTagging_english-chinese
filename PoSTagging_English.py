import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("How are you doing?")
doc1 = nlp("The weather is nice today.")
doc2 = nlp("Do you want to hang out with me this afternoon?")

for token in doc:
    print(token.text, ":", token.lemma_, token.pos_, token.tag_, token.dep_)
print("\n")

for token in doc1:
    print(token.text, ":", token.lemma_, token.pos_, token.tag_, token.dep_)
print("\n")

for token in doc2:
    print(token.text, ":", token.lemma_, token.pos_, token.tag_, token.dep_)

displacy.serve(doc, style="dep")
displacy.serve(doc1, style="dep")
displacy.serve(doc2, style="dep")