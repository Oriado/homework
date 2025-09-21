#task №5
def filter_words_by_length(words, min_length=3):
    
    filter = []
    
    for word in words:
        if len(word) > min_length:
            filter.append(word)
    return filter            

words = ["flowers", "kitchen", "dog", "mouse"]
result = filter_words_by_length(words, 4)
print(result)      