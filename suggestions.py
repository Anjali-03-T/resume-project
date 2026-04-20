def generate_suggestions(score):

    suggestions = []

    if score < 4:
        suggestions.append("Add more relevant skills from job description")
        suggestions.append("Include measurable achievements")
        suggestions.append("Improve ATS keywords")

    elif score < 7:
        suggestions.append("Add more technical keywords")
        suggestions.append("Improve project descriptions")

    else:
        suggestions.append("Resume is well optimized for ATS")

    return suggestions