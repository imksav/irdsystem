# initalize the variable
yournameList = []
addressList = []
contactList = []
ageList = []
genderList = []
currentDORList = []
isMarriedList = []
isInsuranceList = []
isDisabilityList = []
isDiplomat = []
monthlyIncomeList = []
taxAmountList = []

# ask for the number of users
numberOfUsers = int(input("Enter the number of users::"))
print("Enter the details of", numberOfUsers, "users::")

for i in range(numberOfUsers):
              yourname = input("Customer[{}]:: Enter your name::".format(i+1))
              yournameList.append(yourname)
              address = input("Customer[{}]:: Enter your address::".format(i+1))
              addressList.append(address)
              contact = input("Customer[{}]:: Enter your contact number[{}]::".format(i+1))
              contactList.append(contact)
              age = int(input("Customer[{}]:: Enter your age::".format(i+1)))
              ageList.append(age)
              gender = input("Customer[{}]:: Enter your gender::".format(i+1))
              genderList.append(gender)
              currentDOR = input("Customer[{}]:: Enter current date of registartion::".format(i+1))
              currentDORList.append(currentDOR)
              isMarried = input("Customer[{}]:: Are you married?(Y/N)::")
              isMarriedList.append(isMarried)
              isInsurance = input("Customer[{}]:: Did you insurance?(Y/N)::".format(i+1))
              isInsuranceList.append(isInsurance)
              isDisability = input("Customer[{}]:: Do you have any disability?(Y/N)::".format(i+1))
              isDisabilityList.append(isDisability)
              isDiplomat = input("Customer[{}]:: Do you have diplomat job?(Y/N)::".format(i+1))
              isDisabilityList.append(isDiplomat)


