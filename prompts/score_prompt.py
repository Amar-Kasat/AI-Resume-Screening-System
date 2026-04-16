from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_result"],
    template="""
Give score (0-100).

Rules:
- More matches → high score
- Missing important skills → reduce score

Match:
{match_result}

Return ONLY number.
""",
)
