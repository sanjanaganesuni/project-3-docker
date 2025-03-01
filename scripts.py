import os
import re
import collections
import socket

# File paths
data_dir = "/home/data"
output_file = "/home/data/output/result.txt"
file1_path = os.path.join(data_dir, "IF-1.txt")
file2_path = os.path.join(data_dir, "AlwaysRememberUsThisWay-1.txt")

# Ensure output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Function to read and clean text
def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read().lower()
    return text

# Function to split contractions
def expand_contractions(text):
    contractions = {
        "i'm": "i am", "can't": "cannot", "don't": "do not", "it's": "it is",
        "won't": "will not", "you're": "you are", "isn't": "is not"
    }
    for contraction, expansion in contractions.items():
        text = text.replace(contraction, expansion)
    return text

# Function to count words
def count_words(text):
    words = re.findall(r"\b\w+\b", text)
    return len(words), collections.Counter(words)

# Read files
text1 = read_file(file1_path)
text2 = read_file(file2_path)

# Count words
count1, freq1 = count_words(text1)
count2, freq2 = count_words(expand_contractions(text2))

# Grand total
grand_total = count1 + count2

# Top 3 words in each file
top3_file1 = freq1.most_common(3)
top3_file2 = freq2.most_common(3)

# Get container IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Prepare output
output_text = (
    f"Total words in IF-1.txt: {count1}\n"
    f"Total words in AlwaysRememberUsThisWay-1.txt: {count2}\n"
    f"Grand total words: {grand_total}\n\n"
    f"Top 3 words in IF-1.txt: {top3_file1}\n"
    f"Top 3 words in AlwaysRememberUsThisWay-1.txt: {top3_file2}\n\n"
    f"Container IP Address: {ip_address}\n"
)

# Write results to file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(output_text)

# Print results
print(output_text)
