def checkletter(s, t):
    """
    base case is the check if one or both of the inputs is empty
    after that we will check if a spesific letter is the other other input
    if that is the case we will keep going until we have the letters that are in both strings
    """
    if len(s) == 0 or len(t) == 0:
        return ''
    if s[0] == t[0]:
        return s[0] + checkletter(s[1:], t[1:])
    else:
        lose_s = lcs(s[1:], t)
        lose_t = lcs(s, t[1:])
        if len(lose_s) > len(lose_t):
            return lose_s
        else:
            return lose_t
assert lcs('gattaca', 'tacgaacta') == "gaaca"
assert lcs('abcdefgh', 'efghabcd') == "abcd"
