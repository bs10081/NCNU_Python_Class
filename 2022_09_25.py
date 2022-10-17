def main():
	Passwd = input("Input Password: ")
	findSol(Passwd)

def findSol(data):
	if (data == 1234):
		print("歡迎光臨")
	else:
		print("密碼錯誤")
if __name__ == "__main__":
	main()