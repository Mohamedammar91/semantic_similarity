# import spacy
import spacy
nlp = spacy.load("en_core_web_md")
nlp2 = spacy.load("en_core_web_sm")

word1_sm = nlp2("cat")
word2_sm = nlp2("monkey")
word3_sm = nlp2("banana")
word1_md = nlp("house")
word2_md = nlp("flat")
word3_md = nlp("door")

print("small model")
print(word1_sm.similarity(word2_sm))
print(word3_sm.similarity(word2_sm))
print(word3_sm.similarity(word1_sm))
#  The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
#   print(word3_md.similarity(word1_md))
print("md model ")
print(word1_md.similarity(word2_md))
print(word3_md.similarity(word2_md))
print(word3_md.similarity(word1_md))
