class Course:
    course_map = {'base_id': 12345}
    course_grade_list = []

    @classmethod
    def convert_score(cls, grade):
        scores = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}
        return scores[grade]

    @classmethod
    def get_code(cls, course_name):
        if course_name not in cls.course_map:
            cls.course_map[course_name] = cls.course_map['base_id']
            cls.course_map['base_id'] += 1
        return cls.course_map[course_name]

    @classmethod
    def input_course_grade(cls):
        course_name = input("과목명을 입력하세요: ")
        credit = int(input("학점을 입력하세요: "))
        grade = input("평점을 입력하세요: ")

        # 기존에 수강한 과목인지 확인
        found = False
        for i, (code, _, _) in enumerate(cls.course_grade_list):
            if code == cls.get_code(course_name):
                found = True
                if cls.convert_score(grade) > cls.convert_score(cls.course_grade_list[i][2]):
                    cls.course_grade_list[i] = (cls.get_code(course_name), credit, grade)
                break

        if not found:
            cls.course_grade_list.append((cls.get_code(course_name), credit, grade))

        print("입력되었습니다.")

    @classmethod
    def print_course_grade(cls):
        for code, credit, grade in cls.course_grade_list:
            course_name = [k for k, v in cls.course_map.items() if v == code][0]
            print(f"[{course_name}] {credit}학점: {grade}")
        print("")

    @classmethod
    def calculate_gpa(cls, for_submission=False):
        total_credit, total_gpa = 0, 0.0
        for code, credit, grade in cls.course_grade_list:
            if grade != 'F' or for_submission:
                total_credit += credit
                total_gpa += cls.convert_score(grade) * credit
        gpa = total_gpa / total_credit if total_credit > 0 else 0.0
        return total_credit, gpa

while True:
    print("작업을 선택하세요.")
    print("1. 입력")
    print("2. 출력")
    print("3. 조회")
    print("4. 계산")
    print("5. 종료")
    user_value = input()
    value = int(user_value)

    if value == 1:
        Course.input_course_grade()

    elif value == 2:
        Course.print_course_grade()

    elif value == 3:
        courseselect = input("과목명을 입력하세요: ")
        if courseselect in Course.course_map:
            found = False
            for code, credit, grade in Course.course_grade_list:
                if code == Course.get_code(courseselect):
                    print(f"[{courseselect}] {credit}학점: {grade}")
                    found = True
                    break
        else:
            print(f"{courseselect}해당하는 과목이 없습니다.")

    elif value == 4:
        submit_credit, submit_gpa = Course.calculate_gpa(for_submission=True)
        read_credit, read_gpa = Course.calculate_gpa()
        print(f"제출용: {submit_credit}학점 (GPA: {submit_gpa:.2f})")
        print(f"열람용: {read_credit}학점 (GPA: {read_gpa:.2f})")
    elif value == 5:
        break
