def count_distinct_words_and_a_occurrences(text):
    words = text.split()
    distinct_words = set(words)
    num_distinct_words = len(distinct_words)
    count_a = sum(1 for word in distinct_words if 'a' in word)
    
    print("Distinct words: " + num_distinct_words)
    print("Number of a: " + count_a)

text =input("What's your sentence? ")
count_distinct_words_and_a_occurrences(text)