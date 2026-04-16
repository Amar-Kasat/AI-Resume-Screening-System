from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["score", "match_result"],
    template="""
Explain the score.

Score:
{score}

Match:
{match_result}

Give 3-4 lines explanation.
""",
)
