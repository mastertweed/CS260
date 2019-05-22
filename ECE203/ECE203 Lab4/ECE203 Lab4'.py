from random import randrange

def dollar(a):
    b = '$' + str(round(a,2))
    return b
print(dollar(1.2342))

# -----


def lens(n, R1, R2, d):
    f = ((n-1) * ((1/R1) - (1/R2) + ((n-1)*d) / (n*R1*R2)))**-1
    return round(f,2)

print(lens(1.2, 10, 10, .2))

# -----


def scramble(word):

    if len(word) > 3:
        rand_letter_1 = randrange(1, len(word)-1)
        rand_letter_2 = randrange(1, len(word)-1)

        while rand_letter_2 == rand_letter_1:
            rand_letter_2 = randrange(1, len(word)-1)

        word_str = list(word)
        word_str[rand_letter_2], word_str[rand_letter_1] = word_str[rand_letter_1], word_str[rand_letter_2]
        word = ''.join(word_str)

    return word

print(scramble('hello'))

# -----


def build_sentence(sentence):

    words = sentence.split()
    sentence_out = []

    for i in words:
        sentence_out.append(scramble(i))
        sentence_out.append(' ')

    sentence_out = ''.join(sentence_out)
    return sentence_out

a = build_sentence('yes I would like that')
print(a)