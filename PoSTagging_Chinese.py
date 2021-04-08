import spacy
from spacy import displacy

nlp = spacy.load("zh_core_web_sm")
doc = nlp("你最近怎么样？")
doc1 = nlp("今天天氣很好。")
doc2 = nlp("你今天下午想跟我一起出去玩嗎?")

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