# reverses words in a sentence only if they have more than four letters
def spin_words(sentence):
    return ' '.join([word[::-1] if len(word) > 4 else word for word in sentence.split(' ')])
