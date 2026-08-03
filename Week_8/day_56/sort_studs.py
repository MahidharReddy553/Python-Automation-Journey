li = [89, 76, 23, 56, 90]
# li = []
def sort_stud(li):
    if len(li) == 0:
        return "Students marks list is empty"
    li.sort()
    return li

print(sort_stud(li))