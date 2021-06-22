Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Bank:
	def __init__(self,n,m,balance=0.0):
		self.acno=n
		self.name=m
		self.balance =balance
	def deposit(self,amnt):
		self.balance+=amnt
		return self.balance
	def withdrawal(self,amnt):
		if amnt>self.balance:
			print("balance amnt is less,so cannot with draw")
		else:
			self.balance=amnt
		return self.balance

	
>>> accno=input("Enter Acct no. : ")
Enter Acct no. : 8756365291
>>> name=input("Enter name :")
Enter name :Dharani
>>> b=Bank(accno,name)
>>> flag = 'yes'
>>> while flag=='yes':
	print('d - deposit, w - withdrawal')
	ch = input("Enter choice :")
	if ch== 'd':
		amnt=float(input("Enter amont to be deposited : "))
		print("Balance amount : ",b.deposit(amnt))
	else:
		amnt =float(input("Enter amont to be deposited : "))
		print("Balance amount : ",b.withdrawal(amnt))
	flag = input("do you want to continue yes/no :")

	
d - deposit, w - withdrawal
Enter choice :d
Enter amont to be deposited : 50000
Balance amount :  50000.0
do you want to continue yes/no :yes
d - deposit, w - withdrawal
Enter choice :w
Enter amont to be deposited : 25000
Balance amount :  25000.0
do you want to continue yes/no :no
>>> 
