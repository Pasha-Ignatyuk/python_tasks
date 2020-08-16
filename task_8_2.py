lst = ['apple', 'level', 'android']


def palindroms():
    nlst = []
    for word in lst:
        length = len(word) - 1
        new_word = ''
        while length != -1:
            new_word += word[length]
            length -= 1
        if new_word == word:
            newer_word = new_word + '(palindrom)'
            nlst.append(newer_word)
        else:
            nlst.append(new_word)
    print(nlst)
    return nlst


palindroms()
