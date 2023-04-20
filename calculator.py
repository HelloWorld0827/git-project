def convert_score(grade):
    scores = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}
    return scores[grade]

def get_code(course_name, course_map):
    if course_name not in course_map:
        course_map[course_name] = course_map['base_id']
        course_map['base_id'] += 1
    return course_map[course_name]

course_map = {'base_id': 12345}
course_grade_list = []
submitcredit, readcredit = 0, 0
submitgpa, readgpa = 0.0, 0.0

while True:
    print("작업을 선택하세요")
    print("1. 입력")
    print("2. 출력")
    print("3. 계산")
    user_value = input()
    value = int(user_value)

    if value == 1:
        course_name = input("과목명을 입력하세요: ")
        credit = int(input("학점을 입력하세요: "))
        grade = input("평점을 입력하세요: ")

        # 기존에 수강한 과목인지 확인
        found = False
        for i, (code, _, _) in enumerate(course_grade_list):
            if code == get_code(course_name, course_map):
                found = True
                if convert_score(grade) > convert_score(course_grade_list[i][2]):
                    course_grade_list[i] = (get_code(course_name, course_map), credit, grade)
                break
        
        if not found:
            course_grade_list.append((get_code(course_name, course_map), credit, grade))

        print("입력되었습니다.")

    elif value == 2:
        for code, credit, grade in course_grade_list:
            course_name = [k for k, v in course_map.items() if v == code][0]
            print(f"[{course_name}] {credit}학점: {grade}")
        print("")
    
    elif value == 3:
        # 제출용 계산
        for code, credit, grade in course_grade_list:
            if grade != 'F':
                submitcredit += credit
                submitgpa += convert_score(grade) * credit
        submitgpa /= submitcredit

        # 열람용 계산
        for code, credit, grade in course_grade_list:
            readcredit += credit
            readgpa += convert_score(grade) * credit
        readgpa /= readcredit

        print(f"제출용: {submitcredit}학점 (GPA: {submitgpa:.2f})")
        print(f"열람용: {readcredit}학점 (GPA: {readgpa:.2f})")
        print("프로그램을 종료합니다.")
        break