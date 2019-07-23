student=[]
student.append((90, 80))
student.append((85, 75))
student.append((90, 100))



for i in range(len(student)):
	print(f"{i+1}번 학생의 총점은 {sum(student[i])}점이고, 평균은 {sum(student[i])/2}입니다.")
