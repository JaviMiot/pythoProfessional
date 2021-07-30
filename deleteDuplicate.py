def deleteDuplicate(elements):
    del_duplicates = set(elements)
    return list(del_duplicates)


if __name__ == '__main__':
    list_with_Duplicate = [1,2,34,2,3,1,5,6,3,1,2,6,5,4,3]
    print(deleteDuplicate(list_with_Duplicate))