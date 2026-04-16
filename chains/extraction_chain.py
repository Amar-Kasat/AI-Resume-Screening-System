from prompts.extract_prompt import extract_prompt


def extract(llm, resume):
    response = llm.invoke(extract_prompt.format(resume=resume))
    return response.content
