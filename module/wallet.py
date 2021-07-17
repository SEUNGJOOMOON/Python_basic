
balance = 0

#수입
def income(money):
    global balance
    balance += money

#현재 잔액 확인
def getBalance():
    global balance
    print("현재 남은 잔액은 " + str(balance) + "입니다.")

#지출
def spend(money):
    global balance
    balance -= money

