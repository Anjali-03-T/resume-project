def score_resume(similarity):

    score = round(similarity * 10, 2)

    if score > 10:
        score = 10

    return score