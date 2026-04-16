from prompts.score_prompt import score_prompt


def score(llm, match_result):
    response = llm.invoke(score_prompt.format(match_result=match_result))
    return response.content
