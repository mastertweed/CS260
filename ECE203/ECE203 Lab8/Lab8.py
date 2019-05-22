import string

def punc_strip(sentence):
    words_out = []
    for w in sentence:
        for [character] in w:
            if character in string.punctuation:
                w = w.strip(character)
        words_out.append(w)
    return words_out

# --------------------
marytext = open('mary.txt', 'r')
words_ls = marytext.read().split()
words_d = {}

words_new = punc_strip(words_ls)
words_new = punc_strip(words_new)

for word in words_new:
    if word not in words_d:
        words_d[word] = 1
    else:
        words_d[word] = words_d[word] + 1
    print(word, ':', words_d[word])

# --------------------

spell_file = open('misspell.txt', 'r')
english_words = open('american-english', 'r')
missing_words = open('missing_words.log', 'w')

english_words = english_words.read().split()
words_ls = spell_file.read().split()

words_new = punc_strip(words_ls)

for word in words_new:
    if word not in english_words:
        missing_words.write(word + '\n')

# --------------------
