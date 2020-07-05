def ordered_list_query(search_terms,lst):
    """
    ordered_list_query([1,2],[1,2,3,4]) -> True
    ordered_list_query([1,5],[1,2,3,4]) -> False
    ordered_list_query([2,1],[1,2,3,4]) -> False
    """
    temp_lst = lst.copy()
    if search_terms[0] in temp_lst:
        indx = temp_lst.index(search_terms[0])
        temp_lst = temp_lst[indx:]
        search_terms.pop(0)
        print(temp_lst,search_terms)
        if search_terms:
            ordered_list_query(search_terms,temp_lst)
    if not search_terms:
        return True
    return False
