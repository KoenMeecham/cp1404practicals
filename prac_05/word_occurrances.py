"""Word occurrences Question"""
"""
Expected = 20 mins
Actual = 24 mins
"""
#Take the input and count the word occurrences
word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

#Turn te dict to a list and sort it
words = list(word_to_count.keys())
words.sort()

#format the print based of the longest word in the string
max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")