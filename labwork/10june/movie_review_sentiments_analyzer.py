reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# 1. Count sentiments
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for review in reviews:
        if "excellent" in review:
            excellent += 1
        elif "good" in review:
            good += 1
        elif "average" in review:
            average += 1
        elif "poor" in review:
            poor += 1

    print("Excellent Reviews:", excellent)
    print("Good Reviews:", good)
    print("Average Reviews:", average)
    print("Poor Reviews:", poor)


# 2. Most common word
def most_common_word(reviews):
    word_count = {}

    for review in reviews:
        words = review.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    max_word = ""
    max_count = 0

    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            max_word = word

    return max_word


# 3. Longest review
def longest_review(reviews):
    longest = reviews[0]

    for review in reviews:
        if len(review) > len(longest):
            longest = review

    return longest


# 4. Reviews with keyword
def reviews_with_keyword(reviews, keyword):
    print("Reviews containing", keyword, ":")

    for review in reviews:
        if keyword.lower() in review.lower():
            print(review)


# Function Calls
count_sentiments(reviews)

print("\nMost Common Word:", most_common_word(reviews))

print("\nLongest Review:", longest_review(reviews))

keyword = input("\nEnter keyword to search: ")
reviews_with_keyword(reviews, keyword)
