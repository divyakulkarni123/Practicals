# Practical 1: Text Pre-processing
# Stop Word Removal and Stemming

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download required datasets (only needed once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Original text
text = "The quick brown foxes are jumping over the lazy dogs while the children are playing happily in the beautiful green garden near their houses."

print("Original Text:\n", text)

# Step 1: Tokenization
tokens = word_tokenize(text)
print("\nTokens:\n", tokens)

# Step 2: Stop Word Removal
stop_words = set(stopwords.words('english'))

filtered = [w for w in tokens if w.lower() not in stop_words]

print("\nAfter Stop Word Removal:\n", filtered)

# Step 3: Stemming
stemmer = PorterStemmer()

stemmed = [stemmer.stem(w) for w in filtered]

print("\nAfter Stemming:\n", stemmed)




















'''## Theory: Text Pre-processing – Stop Word Removal and Stemming

### 1. Introduction
Text pre-processing is an important step in Natural Language Processing (NLP). It involves cleaning and transforming raw text into a structured format so that machines can understand and process it easily.

In this practical, we perform three main operations: Tokenization, Stop Word Removal, and Stemming using the NLTK library in Python.

### 2. Objectives
- To understand text pre-processing in NLP.
- To divide a given sentence into individual words using tokenization.
- To remove commonly occurring words using stop word removal.
- To reduce words to their root form using stemming.

### 3. Explanation of Libraries Used

1. **NLTK (Natural Language Toolkit):** A Python library used for text processing and Natural Language Processing tasks.
2. **PorterStemmer:** A stemming algorithm provided by NLTK that reduces words to their root-like form.
3. **Stopwords:** A collection of commonly occurring words such as 'the', 'is', 'are', and 'while' that are generally removed during text processing.
4. **word_tokenize():** A function used to split a sentence into individual words and punctuation marks.

### 4. Explanation of Code

**Step 1: Import Libraries**

The NLTK library and its modules are imported for performing text processing operations. PorterStemmer is used for stemming, stopwords provides a list of common English words, and word_tokenize() is used for tokenization.

**Step 2: Download Required Datasets**

The nltk.download() function downloads the required resources:
- punkt: Used for tokenization.
- punkt_tab: Additional tokenizer data required by some NLTK versions.
- stopwords: Contains a list of English stop words.

These resources generally need to be downloaded only once.

**Step 3: Define Original Text**

A sample English sentence is stored in a variable named `text`. This sentence is used as input for the pre-processing operations.

**Step 4: Tokenization**

The word_tokenize() function divides the original sentence into individual words and punctuation marks. These individual elements are called tokens.

Example:  
"The quick brown foxes" becomes `['The', 'quick', 'brown', 'foxes']`.

**Step 5: Stop Word Removal**

Stop words are commonly occurring words that usually provide less meaningful information for certain NLP tasks. The stopwords.words('english') function provides a list of English stop words.

A list comprehension is used to remove words that appear in the stop-word list. The `lower()` function ensures that words are checked without considering uppercase or lowercase differences.

**Step 6: Stemming**

Stemming is the process of reducing words to their root-like base form by removing prefixes or suffixes using predefined rules.

The PorterStemmer() function creates a stemmer object, and the stem() function converts each filtered word into its stem.

Examples:
- foxes → fox
- jumping → jump
- playing → play
- happily → happili
- beautiful → beauti

The resulting words may not always be grammatically correct English words, but they represent simplified word forms.

**Step 7: Display the Output**

The print() function displays the original text, tokens, text after stop word removal, and text after stemming.

### 5. Advantages
1. Reduces unnecessary words in text.
2. Helps reduce the size of text data.
3. Improves the efficiency of NLP applications.
4. Helps in text classification, sentiment analysis, and information retrieval.
5. Makes text data easier to process and analyze.

### 6. Applications
- Search engines
- Spam email detection
- Sentiment analysis
- Text classification
- Chatbots
- Document processing

### 7. Conclusion
Thus, we successfully implemented text pre-processing using Python and the NLTK library. We performed tokenization to split the text into individual tokens, stop word removal to eliminate commonly occurring words, and stemming to convert words into their root-like forms. These operations help prepare raw text for further Natural Language Processing tasks.
'''