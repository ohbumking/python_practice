import random
i= range(1,46)
a=sorted(random.sample(i,6))
#b_n은 사용자가 n번째에 선택한 번호
print('로또번호 5개를 골라주시면 나머지 한 개는 임의로 골라드려요')
for b_1 in i:
    b_1 = input('첫번째 번호입력해줘')
    try:
        int(b_1)
    except ValueError:
        print('1-45사이의 정수만 입력하세요')
        continue
    if  int(b_1)>int(45):
        print('1-45사이의 정수만 입력하세요')
    elif int(b_1)>=int(1) and int(b_1)<=int(45):
        print("**현재까지 선택하신 번호는",int(b_1),"입니다.**")
        break
for b_2 in i:
    b_2=input('두번째 번호입력해줘')
    try:
        int(b_2)
    except ValueError:
        print('1-45사이의 정수만 입력하세요')
        continue
    if int(b_2)>int(45):
        print('1-45사이의 정수만 입력하세요')
    elif int(b_2)==int(b_1):
        print('이미 선택한 번호입니다')
    elif int(b_2)>=int(1) and int(b_2)<=int(45) and int(b_2) != int(b_1):
        print("**현재까지 선택하신 번호는",int(b_1),'/',int(b_2),"입니다.**")
        break
for b_3 in i:
    b_3=input('세번째 번호입력해줘')
    try:
        int(b_3)
    except ValueError:
        print('1-45사이의 정수만 입력하세요')
        continue
    if int(b_3)>int(45):
        print('1-45사이의 정수만 입력하세요')
    elif b_3 in list((b_1,b_2)):
        print('이미 선택한 번호입니다')
    elif int(b_3)>=int(1) and int(b_3)<=int(45) and b_3 not in list((b_1,b_2)):
        print("**현재까지 선택하신 번호는",int(b_1),'/',int(b_2),'/',int(b_3),"입니다.**")
        break
for b_4 in i:
    b_4=input('네번째 번호입력해줘')
    try:
        int(b_4)
    except ValueError:
        print('1-45사이의 정수만 입력하세요')
        continue
    if int(b_4)>int(45):
        print('1-45사이의 정수만 입력하세요')
    elif b_4 in list((b_1,b_2,b_3)):
        print('이미 선택한 번호입니다')
    elif int(b_4)>=int(1) and int(b_4)<=int(45) and b_4 not in list((b_1,b_2,b_3)):
        print("**현재까지 선택하신 번호는",int(b_1),'/',int(b_2),'/',int(b_3),'/',int(b_4),"입니다.**")
        break
for b_5 in i:
    b_5=input('다섯번째 번호입력해줘')
    try:
        int(b_5)
    except ValueError:
        print('1-45사이의 정수만 입력하세요')
        continue
    if int(b_5)>int(45):
        print('1-45사이의 정수만 입력하세요')
    elif b_5 in list((b_1,b_2,b_3,b_4)):
        print('이미 선택한 번호입니다')
    elif int(b_5)>=int(1) and int(b_5)<=int(45) and b_5 not in list((b_1,b_2,b_3,b_4)):
        print("**현재까지 선택하신 번호는",int(b_1),'/',int(b_2),'/',int(b_3),'/',int(b_4),'/',int(b_5),"입니다.**")
        break
c=int(b_1), int(b_2), int(b_3), int(b_4), int(b_5)
d=list(c)
print('최종 선택 번호는', sorted(d))

def difference(j,k): #차집합
    _k=set(k)
    return [item for item in j if item not in _k]
print('로또 번호는',sorted(d+random.sample(difference(a,d),len(a)-len(d))))#사용자선택n개+차집합선택6-n개
