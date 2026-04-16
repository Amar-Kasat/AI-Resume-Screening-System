from prompts.explain_prompt import explain_prompt


def explain(llm, score_val, match_result):
    response = llm.invoke(
        explain_prompt.format(score=score_val, match_result=match_result)
    )
    return response.content
