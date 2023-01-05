def is_sorted(my_list):
    sort = 0
    x = 1
    while x < len(my_list):
        if(my_list[x] < my_list[x - 1]):
            sort = 1
        x += 1
    if (not sort) :
        print("YES")
    else :
        print("NO")
