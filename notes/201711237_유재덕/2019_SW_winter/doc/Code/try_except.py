try:
    t=4/0
    a = [1,2]
    print(a[2])

except ZeroDivisionError as e:
    print(e)
except IndexError:
    print('해당 리스트에 내용이 없습니다.')
