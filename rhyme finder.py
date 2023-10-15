def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

user_word = input("Enter a word: ").strip()

word_list = ["apple", "banana", "cherry", "orange", "strawberry"]

most_similar_word = min(word_list, key=lambda word: levenshtein_distance(user_word, word))

print(f"The word most similar to '{user_word}' is '{most_similar_word}'")
