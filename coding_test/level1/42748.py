# K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    for command in commands:
        cut_arr = sorted(array[command[0] - 1:command[1]])
        answer.append(cut_arr[command[2] - 1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
