# Chat Message Analyzer

messages = [
    "hello how are you",
    "i am fine thank you",
    "python programming is fun",
    "have a great day",
    "learning coding is useful",
    "good morning everyone",
    "welcome to the chat group",
    "practice makes perfect",
    "keep working hard",
    "success comes with effort",
    "enjoy your studies",
    "artificial intelligence is amazing",
    "data science is interesting",
    "machine learning is powerful",
    "communication improves skills",
    "team work brings success",
    "reading books increases knowledge",
    "coding challenges improve logic",
    "never stop learning",
    "stay positive and motivated"
]

total_words_all = 0
longest_message = messages[0]
shortest_message = messages[0]

all_words = {}

for msg in messages:
    print("\nMessage:", msg)

    words = msg.split()

    # Total words
    print("Total Words:", len(words))
    total_words_all += len(words)

    # Total characters
    print("Total Characters:", len(msg))

    # Vowels and Consonants
    vowels = 0
    consonants = 0

    for ch in msg.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

    # Longest and shortest word
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    print("Longest Word:", longest_word)
    print("Shortest Word:", shortest_word)

    # Word frequencies in current message
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        all_words[word] = all_words.get(word, 0) + 1

    print("Word Frequencies:", freq)

    # Repeated words
    repeated = [word for word in freq if freq[word] > 1]
    print("Repeated Words:", repeated)

    # Words starting with vowels
    vowel_words = [word for word in words if word[0].lower() in "aeiou"]
    print("Words Starting with Vowels:", vowel_words)

    # Words longer than 5 characters
    long_words = [word for word in words if len(word) > 5]
    print("Words Longer than 5 Characters:", long_words)

    # Longest and shortest message
    if len(msg) > len(longest_message):
        longest_message = msg

    if len(msg) < len(shortest_message):
        shortest_message = msg

# Most frequently used word
most_word = max(all_words, key=all_words.get)

# Average words per message
average_words = total_words_all / len(messages)

print("\n===== CHAT REPORT =====")
print("Most Frequently Used Word:", most_word)
print("Longest Message:", longest_message)
print("Shortest Message:", shortest_message)
print("Average Words Per Message:", round(average_words, 2))
print("\nDictionary of Word Frequencies:")
print(all_words)
