def word_count(sentences):
    words= sentences.split()
    return len(words)

#calling 
print(word_count('Hello World'))

size = word_count("Hello World of Pain")
print(size)

data = input('Enter a sentences')
size = word_count(data)
print(f'You entered {size} words')