# 일일 온도

# 매일의 화씨 온도 리스트 T를 입력 받아서
# 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라

# T = [73, 74, 75,71, 69,72,76,73]

# [1,1,4,2,1,1,0,0]

def daily_temperature(T):

    # answer = [0, 0, 0, 0, 0, 0, 0, 0]
    answer = [0]*len(T)
    # print(answer)
    stack = []
    for i, temp in enumerate(T):
        # print(i)
        # 스택에서 원소를 제거하지 않고 가져오기만 할 때에는
        # [-1]을 이용하도록 한다.
        # top = stack[-1]

        while stack and temp > T[stack[-1]]:
            last = stack.pop()
            print(last)
            answer[last] = i - last;
        stack.append(i)
    return answer

if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    # 0 73 -> 1 74 -> 1
    # 1 74 -> 2 75 -> 1
    # 2 75 -> 3 71 -> 6 76 -> 4
    # 3 71 -> 4 69 -> 5 72 -> 2
    # 4 69 -> 5 72 -> 1
    # 5 72 -> 6 76 -> 1
    # 6 76 -> 7 73 -> 0
    # 7 73 -> 0 모름
    print(daily_temperature(T))
    # daily_temperature(T)

