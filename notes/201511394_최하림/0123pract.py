# #펠린드롬
# def is_pal(string):
# 	for i in range(len(string)+1):
# 		if(string[i]!=string[len(string)-i-1]):
# 			return False
# 		else:
# 			return True
# 	return True #참값인지 아닌지 판별하는 함수


# str1 = input("글자를 입력하세요.")
# a = is_pal(str1)
# if(a==True):
# 	print("입력하신 문자는 팰린드롬입니다")
# else:
# 	print("팰린드롬이 아닙니다")

# def is_pal(string)
# string2 = string2
# string2.reverse()
# return string == string2

# return string == string[::-1]


#array에서 근접한 두 개의 원소를 뽑아서 만들수 있는 제일 큰 값을 리턴하시오 

# inputArr = [3, 6, -2, -5, 7, 3]
# Cmpar1 = inputArr[0]*inputArr[len(inputArr)-1]
# Cmpar2 = 0

# for i in range(len(inputArr)):
# 	if(i+1==len(inputArr)):
# 		break
# 	Cmpar2 = inputArr[i]*inputArr[i+1]
# 	if(Cmpar2 > Cmpar1):
# 		Cmpar1 = Cmpar2

# print(inputArr)
# print("인접한 수들의 곱 중 가장 큰 값은=", end= '')
# print(Cmpar1)

# Sum=0

# for i in range(1000):
# 	if(i%3==0):
# 		Sum+=i
# 	elif(i%5==0):
# 		Sum+=i
# 	elif(i%15==0):
# 		Sum-=i

# print("1000미만의 자연수 중 3,5로 나누었을때 나머지가 0인 수의 합은="+str(Sum)+"입니다")

#정수의 값이 있는 리스트가 있습니다 최소 몇 번을 바꿔서
 #정렬된 리스트로 바꿀 수 있는지 출력하는 함수를 구하시오

input_arr = [3,5,7,1,2]

def cnt_chart(input_arr):
	Cnt=0
	temp=0
	for i in range(len(input_arr)):
		for j in range(len(intput_arr)):
			if(input_arr[i]<input_arr[j]):
				temp = input_arr[j]
				input_arr[j] = input_arr[i]
				input_arr[i] = temp
				Cnt +=1
	return Cnt


print(cnt_chart(input_arr))
				

