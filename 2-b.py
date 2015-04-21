def en_kucuk(tree):
    m=tree[1]
    for i in tree[2:]:
        if i<m:
            m=i
    return i
