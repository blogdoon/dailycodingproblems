def make_suggestion(q, list):
    suggestions = []

    for item in list:
        if len(item) >= len(q) and item[:len(q)] == q:
            suggestions.append(item)

    return suggestions


print(make_suggestion("de", ["deed", "dog","deuch"]))