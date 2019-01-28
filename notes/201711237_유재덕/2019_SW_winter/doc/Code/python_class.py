class Human:
    def __init__(self):		#디폴트 생성자
        self.name = '홍길동'
        self.age = 22
        self.major = '전자공학과'

    def set_name(self, name):	#쓰기 전용 함수	
        self.name = name
    
    def get_name(self):		#읽기 전용 함수
        return self.name


student = Human()
print(student.get_name())
student.set_name('유재덕')
print(student.get_name())