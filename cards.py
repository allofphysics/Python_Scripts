def CardsAndPero(S):
    hand=re.split('(\D\d{2})',S)[1::2]
    if len(hand)!=len(set(hand)):
        return [-1]*4
    return [13-re.split('(\D)',S).count(x) for x in ['P','K','H','T']]
