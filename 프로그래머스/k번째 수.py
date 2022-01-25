# solve 1

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command

        slice = array[i - 1:j]
        slice.sort()
        answer.append(slice[k - 1])

    return answer

# solve 2

def solution2(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))