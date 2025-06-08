from collections import Counter
import string

# Step 1: Read and clean the file
with open("Day7.txt", "r") as file:
    text = file.read().lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

# Step 2: Count word frequencies
word_counts = Counter(text.split())

# Step 3: Print top 10 most common words
print("Top 10 words:\n")
for word, freq in word_counts.most_common(10):
    print(f"{word}: {freq}")

# Step 4: (Optional) Write results to CSV
import csv
with open("word_count.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Word", "Frequency"])
    for word, freq in word_counts.items():
        writer.writerow([word, freq])
