def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    alpha=0
    digit=0
    for i in txt:
        if i.isalpha():
            alpha+=1
        elif i.isdigit():
            digit+=1
        answer={"LETTERS":alpha,"DIGITS":digit}

    return answer
print(count_all("python foundations 2022"))