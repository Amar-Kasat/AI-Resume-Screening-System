import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from chains.extraction_chain import extract
from chains.matching_chain import match
from chains.scoring_chain import score
from chains.explanation_chain import explain

# Load .env
load_dotenv()

# Initialize LLM
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

# Job Description
job_description = """
Python, Machine Learning, SQL, Data Visualization
"""

# Resumes
strong_resume = "Python, ML, SQL, Deep Learning, 3 years experience"
average_resume = "Python, SQL, basic ML"
weak_resume = "HTML, CSS, Excel"


def pipeline(resume):
    extracted = extract(llm, resume)
    matched = match(llm, extracted, job_description)
    score_val = score(llm, matched)
    explanation = explain(llm, score_val, matched)

    print("\nScore:", score_val)
    print("Explanation:", explanation)


# Run all
print("===== STRONG =====")
pipeline(strong_resume)

print("\n===== AVERAGE =====")
pipeline(average_resume)

print("\n===== WEAK =====")
pipeline(weak_resume)
