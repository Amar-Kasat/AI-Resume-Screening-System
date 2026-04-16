from prompts.match_prompt import match_prompt


def match(llm, resume_data, job_description):
    response = llm.invoke(
        match_prompt.format(resume_data=resume_data, job_description=job_description)
    )
    return response.content
