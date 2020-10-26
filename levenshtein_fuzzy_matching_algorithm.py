"""Calculate the match ratio between two names using the levenshtein method"""

def levenshtein(string_1: str, string_2: str, return_match_ratio: bool = False):
    """
    Compare two names looking for the number of substitutions needed to make
    the two names match.  Both a count of those substitutions and a ratio,
    showing the difference between the two strings can be returned as a means
    of matching.

    A lower substitution count indicates a better match.

    A higher match ratio indicates a better match.

    :param string_1: str - one of the two names to compare

    :param string_2: str - the other of the two names you want to compare

    :param return_match_ratio: bool - Default False

    :return: float - 
        If a True value is passed to the return_match_ratio then both the
        number of substitutions and the match ratio will be return

        If a false value is passed then only the number of substitutions will
        be returned.
    """
    if len(string_1) < len(string_2):
        return levenshtein(string_2, string_1, return_match_ratio)
    else:
        pass

    if len(string_2) == 0:
        return len(string_1)
    else:
        pass

    previous_row = range(len(string_2) + 1)
    for i, char_1 in enumerate(string_1):
        current_row = [i + 1]
        for j, char_2 in enumerate(string_2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (char_1 != char_2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    if return_match_ratio:
        ratio = ((len(string_1) + len(string_2)) - previous_row[-1]) / (len(string_1) + len(string_2))
        return previous_row[-1], ratio
    else:
        return previous_row[-1]

