r = []
while True:
    temp = 0
    temp_i = 0
    for i in range(8):
        mountain_h = int(input())
        if mountain_h > temp:
            temp = mountain_h
            temp_i = i
    print(temp_i)

