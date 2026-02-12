n = 120 #구하고 싶은 약수의 숫자 입력

i = 1
count = 0
while i<=n:
    if n%i == 0:
        print(i)
        count += 1
    i += 1
    
print(f"{n}의 약수는 총 {count}개 입니다")

