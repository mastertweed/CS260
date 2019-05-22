# Dictionary of SMS slang to English
sms_trans = {'gr8': 'great', 'btw': 'by the way', 'imho': 'in my humble opinion', 'jk': 'just kidding', 'l8r': 'later',
             'np': 'no problem', 'r': 'are', 'u': 'you', 'y': 'why', 'ttyl': 'talk to you later', 'l8': 'late',
             'atm': 'at the moment', 'lmk': 'let me know', 'tia': 'thanks in advance', 'brb': 'br right back'}


def sms_english():

    sentence = input('Enter message to translate: ')

    # Check and set punctuation to value mark
    if sentence[-1] in ".?!,;:":
        mark = sentence[-1]
        sentence = sentence.rstrip(sentence[-1])

    # Create list of words and output list
    words = sentence.split()
    sentence_out = []

    # Check if object in dictionary, if so set it to new value, otherwise nothing
    for i in range(len(words)):
        if words[i] in sms_trans:
            words[i] = sms_trans[words[i]]
        sentence_out.append(words[i])

        # Create spaces between words until punctuation
        if i < len(words)-1:
            sentence_out.append(' ')

    # If mark initialized then add the sentence list
    if 'mark' in vars():
        sentence_out.append(mark)

    # Convert sentence_out from list to string
    sentence_out = ''.join(sentence_out)

    print('Message in the King’s English: ', sentence_out)

sms_english()