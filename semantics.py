import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("mokey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))

# What's interesting about the similarities between "cat," "monkey," and "banana" is how they connect in unexpected ways. While "cat" and "monkey" are animals, "banana" is a fruit. But sometimes, we see them together in stories or pictures.
#For example, in cartoons, monkeys often like bananas, and sometimes, cats are shown with bananas too. 
# This makes us think about how language and culture connect different things, even if they're not really related.
# In my own experience, when looking at social media posts about pets, I noticed people often talk about cats and monkeys with bananas, even though it's not something they do in real life. It shows how language and culture can make connections between things that might seem unrelated.#