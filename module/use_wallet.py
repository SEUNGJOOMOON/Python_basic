#use_wallet.py
import wallet

wallet.getBalance() # 잔액확인
wallet.income(10000) # 10000원 추가
wallet.getBalance() # 잔액 확인
wallet.spend(5000) # 5000원 사용
wallet.getBalance() # 잔액 확인