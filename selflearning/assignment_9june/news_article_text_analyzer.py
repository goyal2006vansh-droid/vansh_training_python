# News Article Analyzer

paragraph = """
Technology is changing the world rapidly. People use smartphones,
computers, and the internet every day. Technology helps students learn,
businesses grow, and governments provide better services. Many companies
invest in artificial intelligence and data science. These technologies
improve efficiency and reduce manual work. Education is becoming more
accessible because online platforms provide learning opportunities to
millions of people. Healthcare services are also improving with the help
of modern machines and digital records. Scientists continue to develop
new solutions for environmental problems. Renewable energy sources such
as solar and wind power are becoming more popular. Governments encourage
citizens to use clean energy and reduce pollution. Social media connects
people across different countries and cultures. Communication is faster
than ever before. Businesses use digital marketing to reach customers.
The growth of technology creates new jobs and industries. However,
technology also brings challenges such as cybersecurity threats and data
privacy concerns. Experts work continuously to improve security systems.
People must learn how to use technology responsibly. Innovation remains
an important factor in economic growth. Researchers and engineers work
together to create better products and services. The future of technology
looks promising as new discoveries continue to improve daily life.
"""

# Total characters
total_characters = len(paragraph)

# Words
words = paragraph.lower().split()
total_words = len(words)

# Sentences
total_sentences = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")

# Vowels and consonants
vowels = 0
consonants = 0

for ch in paragraph.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Longest and shortest word
clean_words = [word.strip(".,!?") for word in words]

longest_word = max(clean_words, key=len)
shortest_word = min(clean_words, key=len)

# Word frequency dictionary
freq = {}
for word in clean_words:
    freq[word] = freq.get(word, 0) + 1

# Most frequent word
most_frequent_word = max(freq, key=freq.get)

# Words appearing only once
once_words = [word for word in freq if freq[word] == 1]

# Words appearing more than 5 times
more_than_5 = [word for word in freq if freq[word] > 5]

# Words starting with each alphabet
alphabet_count = {}
for word in clean_words:
    first = word[0]
    alphabet_count[first] = alphabet_count.get(first, 0) + 1

# Unique words
unique_words = set(clean_words)

# Average word length
total_letters = sum(len(word) for word in clean_words)
average_word_length = total_letters / total_words

# Display Results
print("Total Characters:", total_characters)
print("Total Words:", total_words)
print("Total Sentences:", total_sentences)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Most Frequent Word:", most_frequent_word)

print("\nWords Appearing Once:")
print(once_words)

print("\nWords Appearing More Than 5 Times:")
print(more_than_5)

print("\nWord Frequencies:")
print(freq)

print("\nWords Starting With Each Alphabet:")
print(alphabet_count)

print("\nUnique Words:")
print(unique_words)

# Summary Report
print("\n===== TEXT SUMMARY =====")
print("Total Words:", total_words)
print("Total Sentences:", total_sentences)
print("Average Word Length:", round(average_word_length, 2))
print("Most Frequent Word:", most_frequent_word)
print("Vocabulary Size:", len(unique_words))
