# Generate Parenthesis
def printParenthesis(n):
    def _printParenthesis(str, pos, n, open, close):
        if close == n:
            print("".join(str))
            return
        else:
            if open > close:
                str[pos] = '}'
                _printParenthesis(str, pos + 1, n, open, close + 1)
            if open < n:
                str[pos] = '{'
                _printParenthesis(str, pos + 1, n, open + 1, close)

    if n > 0:
        str = [""] * 2 * n
        _printParenthesis(str, 0, n, 0, 0)

# Driver Code
n = 3
printParenthesis(n)

