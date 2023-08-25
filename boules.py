import sys
import math


def main():
    lines = sys.stdin.readlines()
    my_dict = {}
    my_list = []
    for i in range(1, len(lines)):
        el = lines[i].strip().split(" ")
        my_dict[math.sqrt(((int(el[1]) - 0) * (int(el[1]) - 0)) + ((int(el[2]) - 0) * (int(el[2]) - 0)))] = el[0]
        my_list.append(math.sqrt(((int(el[1]) - 0) * (int(el[1]) - 0)) + ((int(el[2]) - 0) * (int(el[2]) - 0))))
    final = sort_scores(my_list)
    for i in final:
        print(my_dict[i])
    
        

def sort_scores(my_list):
    if len(my_list) > 1:
        middle = len(my_list) // 2
        right = my_list[middle:]
        left = my_list[:middle]
        sort_scores(right)
        sort_scores(left)

        i = 0
        j = 0
        x = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                my_list[x] = left[i]
                i += 1
            else:
                my_list[x] = right[j]
                j += 1
            x += 1
        

        while i < len(left):
            my_list[x] = left[i]
            i += 1
            x += 1
        
        while j < len(right):
            my_list[x] = right[j]
            j += 1
            x += 1
        
    return my_list 
                        


main()
