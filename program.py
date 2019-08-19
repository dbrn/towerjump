# Jack is playing a 2D game. In that, there are N towers aligned in a straight 
# horizontal line from left to right. Jack has to move from right to left 
# by jumping. He can jump over K towers provided they all are shorter than or 
# equal to the current tower. Find the value of K for each tower.
test_cases = int(input())
for case in range(test_cases):
    answers_array = []
    array_length = int(input())
    towers_array = tuple(map(lambda x: int(x), input().split()))
    for i in range(array_length - 1, -1, -1):
        counter = 0
        start = i -1
        for j in range(start, -1, -1):
            if towers_array[j] <= towers_array[i]:
                counter += 1
            else:
                break
        answers_array.append(counter)
    answers_array.reverse()
    for answer in answers_array:
        print(answer, end=" ")
