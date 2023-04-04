def convert_score(grade):
    match grade:
        case 'A+':
            return 4.5
        case 'A':
            return 4.0
        case 'B+':
            return 3.5
        case 'B':
            return 3.0
        case 'C+':
            return 2.5
        case 'C':
            return 2.0
        case 'D+':
            return 1.5
        case 'D':
            return 1.0
        case 'F':
            return 0.0


submitcredit, readcredit = 0, 0
submitgpa, readgpa = 0.0, 0.0

while True:
    print("작업을 선택하세요")
    print("1. 입력")
    print("2. 계산")

    user_value = input()
    value = int(user_value)

    match value:
        case 1:
            user_value = input("학점을 입력하세요: \n")
            credit = int(user_value)

            user_value = input("평점을 입력하세요: \n")
            gpa = convert_score(user_value)

            if gpa > 0:
                submitcredit += credit
                submitgpa += gpa * credit
            readcredit += credit
            readgpa += gpa * credit 

            print("입력되었습니다.\n")

        case 2:
        
            submitgpa /= submitcredit
            readgpa /= readcredit

            print('제출용: ' + str(submitcredit) + '학점 (GPA: ' + str(round(submitgpa, 2)) + ')')
            print('열람용: ' + str(readcredit) + '학점 (GPA: ' + str(round(readgpa, 2)) + ')')

            break
    
        case _:
            print("잘못입력하셨습니다. \n")

