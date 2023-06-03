from practice_05 import CourseRecord, CourseHistory

# 실행 코드
course_history = CourseHistory()

# 무한 루프
while True:
    # 출력
    print('작업을 선택하세요')
    print('    1. 입력')
    print('    2. 출력')
    print('    3. 조회')
    print('    4. 계산')
    print('    5. 파일 저장')
    print('    6. 파일 불러오기')
    print('    7. 종료')

    # 사용자 입력
    user_input = input()
    
    # 입력값별 작업
    if user_input == '1':
        course_history.input_process()
        
    elif user_input == '2':
        course_history.print_process()
        
    elif user_input == '3':
        course_history.query_process()

    elif user_input == '4':
        course_history.calculate_process()
    
    elif user_input == '5':
        course_history.savefile()

    elif user_input == '6':
        course_history.loadfile()

    elif user_input == '7':
        break

    elif not user_input:
        print('잘못된 입력입니다.')

    else:
        continue
        
print('프로그램을 종료합니다.')
