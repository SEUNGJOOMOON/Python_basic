from openpyxl import Workbook

#workbook 생성하기(1개의 시트가 생성된 상태)
workbook = Workbook()

#현재 workbook의 활성화 된 Sheet 가져오기
sheet = workbook.active
sheet.title = "학생정보" #해당 sheet의 sheet명 변경하기

# cell에 직접 데이터 입력하기
sheet['A1'] = "이름"
sheet['B1'] = "나이"
sheet['C1'] = "성별"
sheet['D1'] = "주소"
sheet['E1'] = "학년"

# row 단위로 데이터 입력하기
sheet.append(['홍길동', 20, '남자', '서울', '1학년'])
sheet.append(['춘향이', 25, '여자', '경기', '2학년'])
sheet.append(['이몽룡', 30, '남자', '충청도', '2학년'])

#시트 추가하기
workbook.create_sheet("성적정보", 1)
sheet2 = workbook['성적정보'] #생성한 시트 접근
sheet2.append(['홍길동', '국어', 100])
sheet2.append(['춘향이', '수학', 90])
sheet2.append(['이몽룡', '사회', 85])


# 파일 저장하기
workbook.save("C:/Users/nick9/OneDrive/바탕 화면/sample2.xlsx")