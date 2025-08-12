import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import brown, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import Counter

# Ensure required resources are downloaded
nltk.download('brown')
nltk.download('punkt')
nltk.download('wordnet')

# Q1: Load and Tokenize Text
category = 'news'  # You can change to other categories
text = " ".join(brown.words(categories=category))
tokens = nltk.word_tokenize(text)

print(f"Total tokens: {len(tokens)}")
print("Sample tokens:", tokens[:20])

# Q2: Visualize Raw Word Frequencies
freq_dist = Counter(tokens)
top20 = freq_dist.most_common(20)

# Bar chart
words, counts = zip(*top20)
plt.figure(figsize=(10,5))
plt.bar(words, counts, color='skyblue')
plt.xticks(rotation=45)
plt.title("Top 20 Raw Word Frequencies")
plt.show()

# Word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(freq_dist)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Q3: Apply Stemming
ps = PorterStemmer()
stemmed_words = [ps.stem(w) for w in tokens]
stem_freq = Counter(stemmed_words)
print("Stemmed words sample:", list(stem_freq.items())[:20])

# Q4: Apply Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(w) for w in tokens]
lemma_freq = Counter(lemmatized_words)
print("Lemmatized words sample:", list(lemma_freq.items())[:20])

# Q5: Compare Stemming vs Lemmatization
common_words = list(set(stemmed_words) & set(lemmatized_words))
comparison_sample = common_words[:15]

print("\nComparison Table:")
print(f"{'Word':<15}{'Stemmed Count':<15}{'Lemma Count':<15}")
for word in comparison_sample:
    print(f"{word:<15}{stem_freq[word]:<15}{lemma_freq[word]:<15}")

# Bar chart comparison
stem_counts = [stem_freq[w] for w in comparison_sample]
lemma_counts = [lemma_freq[w] for w in comparison_sample]

x = range(len(comparison_sample))
plt.figure(figsize=(10,5))
plt.bar(x, stem_counts, width=0.4, label='Stemming', align='center')
plt.bar([i + 0.4 for i in x], lemma_counts, width=0.4, label='Lemmatization', align='center')
plt.xticks([i + 0.2 for i in x], comparison_sample, rotation=45)
plt.ylabel("Frequency")
plt.title("Stemming vs Lemmatization")
plt.legend()
plt.show()
