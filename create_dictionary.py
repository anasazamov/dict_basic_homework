def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    answer={}
    for i in range(len(key)):
        answer[key[i]]=value[i]

    return answer

print(create_dictionary([1, 2, 3],["one", "two", "three"]))