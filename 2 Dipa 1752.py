# Given sentence
sentence = "Learning Python is fun and rewarding."

# a. Extract the substring "Python is fun" using negative slicing
# Counting backwards, "Python is fun" starts from -27 and ends at -13
substring = sentence[-28:-14]
print("Extracted Substring:", substring)

# b. Modify the original string by replacing "rewarding" with "exciting"
modified_sentence = sentence.replace("rewarding", "exciting")
print("Modified Sentence:", modified_sentence)

# c. Insert the phrase " Keep practicing!" after "exciting"
insert_phrase = " Keep practicing!"
# Find the position where "exciting" ends
position = modified_sentence.find("exciting") + len("exciting")
# Insert " Keep practicing!" at the correct position
final_sentence = modified_sentence[:position] + insert_phrase + modified_sentence[position:]
print("Final Sentence after insertion:", final_sentence)

# d. Capitalize the first letter of each word in the final output
capitalized_sentence = final_sentence.title()
print("Final Capitalized Output:", capitalized_sentence)