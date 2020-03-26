# For each word in words, add ‘d’ to the end of the word
# if the word ends in “e” to make it past tense. 
# Otherwise, add ‘ed’ to make it past tense. 
# Save these past tense words to a list called past_tense

# *************************** PROGRAM **************************

# list of words
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

# init new list
past_tense = []

# iterate
for word in words :
    if word.endswith('e') :
        past_tense.append(word + 'd')
    else :
        past_tense.append(word + 'ed')

# print the words list
print(words)

print("******************************************************************************")

# print new list containing past tense
print(past_tense)