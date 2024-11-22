
def isComplementPair(ch1, ch2):
    """
    This method determines whether two given characters are valid pairs.

    :param ch1: an uppercase character
    :param ch2: an uppercase character
    :return: whether the two characters belong to one of the two possible pairs.
    """

    # Four difference combinations are possible for the two pairs.
    return ch1 + ch2 in ['AT', 'TA', 'CG', 'GC']


def findLRCS(str1, str2):
    """
    This method finds the LRCS of a given string via dynamic programming.

    :param str1: An uppercase string sequence
    :param str2: A reverse of the string sequence (i.e. str1)
    :return: The longest reverse complement sequence (LRCS) of the two given string sequences.
    """

    if len(str1) < 2:
        return ""

    N = len(str1)
    M = len(str2)

    # Create an empty table to record the results of sub-problems.
    table = [[None]*(N+1) for _ in range(M+1)]

    # Record the results (=length of LRCS) of sub-problems into the table.
    for i in range(N+1):
        for j in range(M+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif isComplementPair(str1[i-1:i], str2[j-1:j]):
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    # Create an empty list to store the resulting characters of the LRCS
    idx = table[N][M]
    LRCSArr = [''] * idx

    x = N
    y = M

    # Retrace the LRCS from the length table constructed above.
    while x > 0 and y > 0:
        if isComplementPair(str1[x-1:x], str2[y-1:y]):
            LRCSArr[idx - 1] = str1[x-1:x]
            x -= 1
            y -= 1
            idx -= 1
        elif table[x-1][y] > table[x][y-1]:
            x -= 1
        else:
            y -= 1
    return ''.join(LRCSArr)


if __name__ == '__main__':
    """
    This is the main function of the LRCS program.
    
    ## Execution
    - How to Run: `python LRCS.py`
    - How to Modify the Input: add or modify the `files` list in the first line of this scope.
    - Where to Find the Output: `{input file name}-output.txt` for each file in the current directory.
    
    This part of the program 
    1) reads the content (i.e. input string) of the input file,
    2) passes the string and its reverse to the `findLRCS` function, and
    3) writes the resulting LRCS of the given string into the output file.
    """

    # Please modify the line below to change the input test cases.
    files = ["seq1.txt", "seq2.txt", "test.txt"]

    for fileName in files:
        f = open(fileName, "r")
        s = f.read()

        result = findLRCS(s, s[::-1])
        f = open(f'{fileName.split(".")[0]}-output.txt', "w")
        f.write(result)
        f.close()
