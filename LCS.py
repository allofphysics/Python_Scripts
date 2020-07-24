def largest_substring_match(string1, string2):
    match = ""
    lst = []
    for letter in string1:
        match += letter
        if match in string2:
            lst.append(match)
        else:
            lst.append("")
            match = ""
    return max(lst, key=len)


print(largest_substring_match("hellothisisatest", "hellothis"))
