def binary_search(list, item):
    low = 0                        # lowとhighを使ってリストの検索部分を追跡
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]          # 真ん中の要素を調べる
        if guess == item:
            return mid
        if guess > item:           
            high = mid - 1         # -1は下から数えているから
        else:                      
            low = mid + 1          # +1は上から数えているから
    return None                    # アイテムが存在しない
my_list = [1, 3, 5, 7, 9]          
print(binary_search(my_list, 3))    

print(binary_search(my_list, -1))
