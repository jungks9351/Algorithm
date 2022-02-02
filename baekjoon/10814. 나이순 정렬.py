import sys

sys.stdin = open('input.text')

n = int(input())
persons = []

for _ in range(n):
    age, name = input().split()
    person = (int(age), name)
    persons.append(person)

persons.sort(key = lambda x : (x[0]))
for person in persons:
    print(person[0],person[1])

