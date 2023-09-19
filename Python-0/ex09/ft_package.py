def count_in_list(lst, to_match):
    """Count matching word in list"""
    count = 0
    for item in lst:
        if (item == to_match):
            count += 1
    return count
