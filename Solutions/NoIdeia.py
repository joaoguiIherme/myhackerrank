"""nm = list(map(int, input().split()))
array = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
happiness = 0

for x in array:
    if x in a:
        happiness += 1
    elif x in b:
        happiness -= 1
print(happiness)"""

n, m = input().split()
sc_ar = input().split()
A = set(input().split())
B = set(input().split())

print(sum([(i in A) - (i in B) for i in sc_ar]))
