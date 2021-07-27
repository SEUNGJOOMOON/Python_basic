from openpyxl import Workbook

#기본 사용하기
#workbook 생성하기
workbook = Workbook()

#현재 workbook의 활성화 된 Sheet 가져오기
sheet = workbook.active

# cell에 직접 데이터 입력하기
sheet['A1'] = "이름"
sheet['B1'] = "나이"
sheet['C1'] = "성별"
sheet['D1'] = "주소"

# row 단위로 데이터 입력하기
sheet.append(['홍길동', 20, '남자', '서울'])
sheet.append(['춘향이', 25, '여자', '경기'])
sheet.append(['이몽룡', 30, '남자', '충청도'])


# 파일 저장하기
workbook.save("C:/Users/nick9/OneDrive/바탕 화면/sample.xlsx")