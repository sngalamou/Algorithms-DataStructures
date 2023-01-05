words = input('Enter words:\n')
words=words.split(' ')

words_list = set(words)
words_count={}
for word in words_list:
    if word != '':
        words_count[word]=words.count(word)

print(words_count)
