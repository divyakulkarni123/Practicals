
# Practical 2: Implement Inverted Index

# Collection of documents
documents = {
    1: "Information retrieval is the process of retrieving relevant documents",
    2: "An inverted index maps each term to the documents containing it",
    3: "Python is a popular programming language for data science",
    4: "Search engines use inverted indexes for fast retrieval",
    5: "Machine learning models learn patterns from data"
}

# Step 1: Build Inverted Index
inverted = {}

for doc_id, text in documents.items():
    for term in text.lower().split():
        inverted.setdefault(term, set()).add(doc_id)

# Step 2: Display Inverted Index
print("Inverted Index:")
for term in sorted(inverted):
    print(f"{term}: {sorted(inverted[term])}")

# Step 3: Search Queries
queries = ["inverted index", "data", "retrieval python"]

print("\nSearch Results:")

for q in queries:
    results = set(documents)

    for t in q.lower().split():
        results = results.intersection(inverted.get(t, set()))

    print(f"Query '{q}' -> Documents: {sorted(results)}")




'''## Theory: Implementation of Inverted Index for Document Retrieval

**Aim:** To implement a program that builds an inverted index over a collection of documents and uses it to retrieve the documents containing all the terms of a query.

**Theory:**

An inverted index is a data structure used in Information Retrieval (IR) systems to store and search documents efficiently. It maps each unique word (term) to the list of document IDs in which that word appears.

It helps search engines retrieve relevant documents quickly without scanning every document individually.

**Working of Inverted Index:**

1. Document Collection: A collection of text documents is stored, and each document is assigned a unique ID.
2. Tokenization: Each document is split into individual words called tokens.
3. Index Creation: A dictionary is created where each word is stored as a key and its corresponding document IDs are stored as values.
4. Searching: When a user enters a query, the query is split into individual terms.
5. Document Retrieval: The inverted index is searched for each query term. Set intersection is performed to retrieve only those documents that contain all the query terms.

**Example:**

Consider three documents:

D1: Python is a programming language.

D2: Python is easy to learn.

D3: Java is a programming language.

The inverted index will be:

- Python: D1, D2
- Programming: D1, D3
- Language: D1, D3
- Java: D3
- Easy: D2
- Learn: D2

If the search query is "Python programming", the system checks both terms and returns documents containing both terms.

**Advantages:**

1. Provides faster document searching.
2. Reduces the time required for information retrieval.
3. Avoids scanning all documents for every search query.
4. Efficiently handles large collections of documents.
5. Forms the foundation of search engines.

**Applications:**

1. Google and other search engines.
2. Digital libraries.
3. Document management systems.
4. Information retrieval systems.
5. Search functionality in databases.

**Conclusion:**

Thus, the inverted index is successfully implemented using Python dictionaries and sets. It efficiently maps words to their corresponding document IDs and retrieves documents based on user search queries.
'''
