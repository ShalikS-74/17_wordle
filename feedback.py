def evaluate(target, guess):
    """Return Wordle-style feedback for a guess against a target word.

    Exact matches are claimed first.  The remaining target letters can then
    satisfy at most one non-exact occurrence in the guess.
    """
    result = ["gray"] * len(guess)
    remaining = list(target)

    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
            remaining[i] = None

    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue
        if ch in remaining:
            result[i] = "yellow"
            remaining[remaining.index(ch)] = None

    return result
