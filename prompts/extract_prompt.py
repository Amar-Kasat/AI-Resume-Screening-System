from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract:
- Skills
- Experience
- Tools

Rules:
- Do NOT assume anything not present

Resume:
{resume}

Return in JSON format.
""",
)
