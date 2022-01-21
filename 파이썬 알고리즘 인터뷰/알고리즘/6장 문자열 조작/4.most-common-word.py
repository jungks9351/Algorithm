# 가장 흔한 단어

# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표) 또한 무시한다.
import collections
import re

pragraph = "Bob hit a ball ball ball, bob the the the hit BALL flew far after it was hit."
banned = ["hit"]

# ball 출력

# 리스트 컴프리헨션, Counter 객체 사용
def solve(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]',' ',pragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)

    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    # most_common(갯수)
    print(counts)
    print(counts.most_common())
    return counts.most_common(1)[0][0]

print(solve(pragraph, banned))