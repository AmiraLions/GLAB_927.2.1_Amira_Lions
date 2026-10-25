
# GLAB 927.2.1 - Text Analysis Using NLP Techniques
# Task 1: Named Entity Recognition (NER)

import nltk


# Sample business document for NLP analysis
business_document = """
The recent feedback from Acme Corp highlighted issues with the new model of the Omega widget.
Customers from New York and San Francisco have reported delays in shipping.
The CEO of Acme Corp, Jane Doe, mentioned plans to address these concerns by Q3.
"""


# Task 1: Break the business document into individual tokens
# Tokenization separates the text into words and punctuation marks.
tokens = nltk.word_tokenize(business_document)


# Display the tokens to verify that tokenization works
print("\n--- Tokenization Test (Preparation for Task 1) ---")
print(tokens)


# Task 1: Apply Named Entity Recognition (NER)

# Identify the grammatical role of each token.
# POS tagging helps NLTK recognize named entities.
pos_tags = nltk.pos_tag(tokens)

# Use the POS tags to identify people, organizations, and locations.
ner_result = nltk.ne_chunk(pos_tags)


# Display the named entities found in the business document
print("\n--- Task 1: Named Entities ---")

# Examine each item in the NER results.
for entity in ner_result:

    # Named entities are represented as NLTK Tree objects.
    if isinstance(entity, nltk.Tree):

        # Extract the words and combine them into readable names.
        entity_name = " ".join(
            word for word, tag in entity.leaves()
        )

        # Print the recognized entity.
        print(entity_name)


# Task 2: Print Named Entities with Their Categories
# NLTK uses a statistical model to classify named entities.
# Some classifications may be inaccurate because the model
# relies on learned language patterns rather than human understanding.
# For example, Acme Corp may be classified as PERSON instead of
# ORGANIZATION, and San Francisco as PERSON instead of GPE.
# These results demonstrate a limitation of automated NER.
# Display a heading for Task 2.
print("\n--- Task 2: Named Entities with Categories ---")

# Examine the named entities identified in Task 1.
for entity in ner_result:

    # Check whether the item is a named entity.
    if isinstance(entity, nltk.Tree):

        # Combine the entity's words into a readable name.
        entity_name = " ".join(
            word for word, tag in entity.leaves()
        )

        # Retrieve the entity's classification.
        entity_category = entity.label()

        # Display the entity name and its category.
        print(f"{entity_name}: {entity_category}")


        # Task 3: Part-of-Speech (POS) Tagging

# Display a heading for Task 3.
print("\n--- Task 3: Words and POS Tags ---")

# Reuse the POS tags created during Task 1.
# Each item contains a word and its grammatical classification.
for word, tag in pos_tags:

    # Display each word alongside its POS tag.
    print(f"{word}: {tag}")