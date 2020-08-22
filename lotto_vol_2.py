import random
i= range(1,46)
a=sorted(random.sample(i,6))
def difference(j,k): #차집합
    _k=set(k)
    return [item for item in j if item not in _k]
while True:
    first_Question = input('모든 번호를 자동 추첨 하실겁니까?[y/n]')
    if first_Question !='y' and first_Question !='n':
        print('[y/n]중에서 골라주세요.')
    elif first_Question == 'y':
        print('자동 추첨 결과 번호는', sorted(random.sample(range(1,46),6)), '입니다.')
    elif first_Question == 'n':
        while True:
            select_manual_num = input('몇 개의 번호를 임의 선택 하실 겁니까?[1~5]')
            if select_manual_num not in ['1','2','3','4','5']:
                print('[1~5]중에서 입력해주세요')
            elif select_manual_num == '1':
                for b_1 in i:
                    b_1 = input('첫번째 번호입력해주세요')
                    try:
                        int(b_1)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_1) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif int(b_1) >= int(1) and int(b_1) <= int(45):
                        b_1_list=list(b_1)
                        print("**현재까지 선택하신 번호는", int(b_1), "입니다.**")
                        print('로또번호는', sorted(list([int(b_1)])
                                              + random.sample(difference(a, list([int(b_1)])),
                                                              len(a) - len(b_1))),'입니다')
                        break
                break
            elif select_manual_num == '2':
                for b_1 in i:
                    b_1 = input('첫번째 번호입력해주세요')
                    try:
                        int(b_1)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_1) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif int(b_1) >= int(1) and int(b_1) <= int(45):
                        b_1_list=list(b_1)
                        print("**현재까지 선택하신 번호는", int(b_1), "입니다.**")
                        break
                for b_2 in i:
                    b_2 = input('두번째 번호입력해줘')
                    try:
                        int(b_2)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_2) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif int(b_2) == int(b_1):
                        print('이미 선택한 번호입니다')
                    elif int(b_2) >= int(1) and int(b_2) <= int(45) and int(b_2) != int(b_1):
                        print("**현재까지 선택하신 번호는", int(b_1), '/', int(b_2), "입니다.**")
                        print('로또번호는', sorted(list([int(b_1),int(b_2)])
                                              + random.sample(difference(a, list([int(b_1),int(b_2)])),
                                                              len(a) - len(list([int(b_1),int(b_2)])))),'입니다.')
                        break
                break
            elif select_manual_num == '3':
                for b_1 in i:
                    b_1 = input('첫번째 번호입력해주세요')
                    try:
                        int(b_1)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_1) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif int(b_1) >= int(1) and int(b_1) <= int(45):
                        b_1_list=list(b_1)
                        print("**현재까지 선택하신 번호는", int(b_1), "입니다.**")
                        break
                for b_2 in i:
                    b_2 = input('두번째 번호입력해줘')
                    try:
                        int(b_2)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_2) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif int(b_2) == int(b_1):
                        print('이미 선택한 번호입니다')
                    elif int(b_2) >= int(1) and int(b_2) <= int(45) and int(b_2) != int(b_1):
                        print("**현재까지 선택하신 번호는", int(b_1), '/', int(b_2), "입니다.**")
                        break
                for b_3 in i:
                    b_3 = input('세번째 번호입력해줘')
                    try:
                        int(b_3)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_3) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif b_3 in list((b_1, b_2)):
                        print('이미 선택한 번호입니다')
                    elif int(b_3) >= int(1) and int(b_3) <= int(45) and b_3 not in list((b_1, b_2)):
                        print("**현재까지 선택하신 번호는", int(b_1), '/', int(b_2), '/', int(b_3), "입니다.**")
                        print('로또번호는', sorted(list([int(b_1),int(b_2),int(b_3)])
                                              + random.sample(difference(a, list([int(b_1),int(b_2),int(b_3)])),
                                                              len(a) - len(list([int(b_1),int(b_2),int(b_3)])))),'입니다.')
                        break
                break
            elif select_manual_num == '4':
                for b_1 in i:
                    b_1 = input('첫번째 번호입력해주세요')
                    try:
                        int(b_1)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_1) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif int(b_1) >= int(1) and int(b_1) <= int(45):
                        b_1_list=list(b_1)
                        print("**현재까지 선택하신 번호는", int(b_1), "입니다.**")
                        break
                for b_2 in i:
                    b_2 = input('두번째 번호입력해줘')
                    try:
                        int(b_2)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_2) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif int(b_2) == int(b_1):
                        print('이미 선택한 번호입니다')
                    elif int(b_2) >= int(1) and int(b_2) <= int(45) and int(b_2) != int(b_1):
                        print("**현재까지 선택하신 번호는", int(b_1), '/', int(b_2), "입니다.**")
                        break
                for b_3 in i:
                    b_3 = input('세번째 번호입력해줘')
                    try:
                        int(b_3)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_3) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif b_3 in list((b_1, b_2)):
                        print('이미 선택한 번호입니다')
                    elif int(b_3) >= int(1) and int(b_3) <= int(45) and b_3 not in list((b_1, b_2)):
                        print("**현재까지 선택하신 번호는", int(b_1), '/', int(b_2), '/', int(b_3), "입니다.**")
                        break
                for b_4 in i:
                    b_4 = input('네번째 번호입력해줘')
                    try:
                        int(b_4)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_4) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif b_4 in list((b_1, b_2, b_3)):
                        print('이미 선택한 번호입니다')
                    elif int(b_4) >= int(1) and int(b_4) <= int(45) and b_4 not in list((b_1, b_2, b_3)):
                        print("**현재까지 선택하신 번호는", int(b_1), '/', int(b_2), '/', int(b_3), '/', int(b_4), "입니다.**")
                        print('로또번호는', sorted(list([int(b_1), int(b_2), int(b_3),int(b_4)]) + random.sample(
                            difference(a, list([int(b_1), int(b_2), int(b_3),int(b_4)])),
                            len(a) - len(list([int(b_1), int(b_2), int(b_3),int(b_4)])))),'입니다')
                        break
                break
            elif select_manual_num == '5':
                for b_1 in i:
                    b_1 = input('첫번째 번호입력해줘')
                    try:
                        int(b_1)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_1) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif int(b_1) >= int(1) and int(b_1) <= int(45):
                        print("**현재까지 선택하신 번호는", int(b_1), "입니다.**")
                        break
                for b_2 in i:
                    b_2 = input('두번째 번호입력해줘')
                    try:
                        int(b_2)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_2) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif int(b_2) == int(b_1):
                        print('이미 선택한 번호입니다')
                    elif int(b_2) >= int(1) and int(b_2) <= int(45) and int(b_2) != int(b_1):
                        print("**현재까지 선택하신 번호는", int(b_1), '/', int(b_2), "입니다.**")
                        break
                for b_3 in i:
                    b_3 = input('세번째 번호입력해줘')
                    try:
                        int(b_3)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_3) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif b_3 in list((b_1, b_2)):
                        print('이미 선택한 번호입니다')
                    elif int(b_3) >= int(1) and int(b_3) <= int(45) and b_3 not in list((b_1, b_2)):
                        print("**현재까지 선택하신 번호는", int(b_1), '/', int(b_2), '/', int(b_3), "입니다.**")
                        break
                for b_4 in i:
                    b_4 = input('네번째 번호입력해줘')
                    try:
                        int(b_4)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_4) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif b_4 in list((b_1, b_2, b_3)):
                        print('이미 선택한 번호입니다')
                    elif int(b_4) >= int(1) and int(b_4) <= int(45) and b_4 not in list((b_1, b_2, b_3)):
                        print("**현재까지 선택하신 번호는", int(b_1), '/', int(b_2), '/', int(b_3), '/', int(b_4), "입니다.**")
                        break
                for b_5 in i:
                    b_5 = input('다섯번째 번호입력해줘')
                    try:
                        int(b_5)
                    except ValueError:
                        print('1-45사이의 정수만 입력하세요')
                        continue
                    if int(b_5) > int(45):
                        print('1-45사이의 정수만 입력하세요')
                    elif b_5 in list((b_1, b_2, b_3, b_4)):
                        print('이미 선택한 번호입니다')
                    elif int(b_5) >= int(1) and int(b_5) <= int(45) and b_5 not in list((b_1, b_2, b_3, b_4)):
                        print("**현재까지 선택하신 번호는", int(b_1), '/', int(b_2), '/', int(b_3), '/', int(b_4), '/', int(b_5),
                              "입니다.**")
                        print('로또번호는', sorted(list([int(b_1), int(b_2), int(b_3), int(b_4),int(b_5)]) + random.sample(
                            difference(a, list([int(b_1), int(b_2), int(b_3), int(b_4),int(b_5)])),
                            len(a) - len(list([int(b_1), int(b_2), int(b_3), int(b_4),int(b_5)])))), '입니다')
                        break
                break