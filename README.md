# GLAB 927.2.1 — Text Analysis Using NLP Techniques

**Student:** Amira Lions  
**Course:** Per Scholas CAX 215

## Project Overview

This project demonstrates how Python and the Natural Language Toolkit (NLTK) can analyze a business document using Named Entity Recognition (NER) and Part-of-Speech (POS) tagging.

The sample document discusses customer feedback, shipping delays, company leadership, and a product.

## Technologies Used

- Python 3.14.7
- NLTK 3.10.4
- NumPy 2.5.4
- uv for dependency management
- Visual Studio Code

## Assignment Tasks

**Task 1 — Named Entity Recognition**

Tokenized the business document, assigned POS tags, and used NLTK to identify named entities such as people, organizations, and locations.

**Task 2 — Entity Classification**

Displayed each named entity alongside the category assigned by NLTK.

**Task 3 — Part-of-Speech Tagging**

Displayed each token alongside its grammatical classification, including nouns, verbs, adjectives, and proper nouns.

## Testing Results

All three tasks executed successfully without runtime errors.

The program successfully produced named entities, entity categories, and POS tags.

### NER Classification Findings

Testing revealed several inaccurate classifications:

| Named Entity | NLTK Classification | More Appropriate Interpretation |
|---|---|---|
| Acme Corp | PERSON | ORGANIZATION |
| Omega | GPE | Product name |
| New York | GPE | Correct |
| San Francisco | PERSON | GPE |
| CEO of Acme Corp | ORGANIZATION | Role combined with organization |
| Jane Doe | PERSON | Correct |

These findings demonstrate that statistical NLP models can produce inaccurate classifications, even when the Python program runs correctly.

Automated results should be reviewed before being used for business decisions.

## Running the Program

From the project directory, install the required dependencies:

```powershell
uv sync
```

Then execute the Python script:

```powershell
uv run python glab_927_2_1.py
```

The program displays tokenization results, named entities, entity classifications, and POS tags.

NLTK language resources must also be installed before the first run.

## Conclusion

This lab demonstrated how NLP techniques can extract structured information from unstructured business text.

It also highlighted the importance of evaluating AI-generated classifications for accuracy rather than assuming that successful execution guarantees correct results.

**Submission file:** `glab_927_2_1.py`