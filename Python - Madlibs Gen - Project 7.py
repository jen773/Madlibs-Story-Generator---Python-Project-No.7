## Python Project:: Madlibs Generator ##

with open("story.txt"), "r" as f:
    story = f.read()

## 'with' supports context for this file ##
    
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumarate(story):
    if char == target_start:
        start_of_word = 1
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: ; + 1]
        words.add(word)
        start_of_word = -1
        
answers = {}

for word in words: 
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer
    
for word in words: 
    story = story.replace(word, snswers[word])
    
print(story)
