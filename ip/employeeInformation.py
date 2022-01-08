import calculateTax

# backend for maritial status checking
def checkStatus(isMarried, isInsurance, isDisability, isDiplomat, yearlyIncome):
          if isMarried.upper() == "Y":
                    minimum_taxable = float(input("Enter the minimum taxable amount::"))
                    maximum_taxable = float(input("Enter the maximum taxable amount::"))
                    return calculateTax.taxForMarried(yearlyIncome, minimum_taxable, maximum_taxable)
          elif isMarried.upper() == "N":
                    minimum_taxable = float(input("Enter the minimum taxable amount::"))
                    maximum_taxable = float(input("Enter the maximum taxable amount::"))
                    return calculateTax.taxForUnmarried(yearlyIncome, minimum_taxable, maximum_taxable)
          else:
                    print("Oops! Something went wrong.\nThank you for using our service!!!\nSee you next time")
          


def employeeInfo(numberOfUsers):
          # ask for the number of users
          for i in range(numberOfUsers):
                    yourname = input("Customer[{}]:: Enter your name::".format(i+1))
                    yournameList.append(yourname)
                    address = input("Customer[{}]:: Enter your address::".format(i+1))
                    addressList.append(address)
                    contact = input("Customer[{}]:: Enter your contact number::".format(i+1))
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
                    isDiplomatList.append(isDiplomat)
                    yearlyIncome = float(input("Customer[{}]:: Enter your yearly income:: ".format(i+1)))
                    yearlyIncomeList.append(yearlyIncome)
                    taxAmount = checkStatus(isMarried, isInsurance isDisability, isDiplomat, yearlyIncome)
                    taxAmountList.append(taxAmount)


def displayInfoWithResult(numberOfUsers):
          for i in range(numberOfUsers):
                    print("For Customer[{}]\nCustomer Name::", yournameList[i], "Address::", addressList[i],"Contact::", contactList[i],"Age::",ageList[i],"Gender::",genderList[i],"Current Date of Registration::",currentDORList[i],"Marital Status::",isMarriedList[i],"Insurance::", isInsuranceList[i],"Disability::",isDisabilityList[i],"Diplomat::",isDiplomatList,"Yearly Income::", yearlyIncomeList[i],"Taxable Amount::",taxAmountList[i],"\nThis is computer generated tax amount to be paid.\n".format(i))

                    




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
isDiplomatList = []
yearlyIncomeList = []
taxAmountList = []



if __name__ == '__main__':
          # get the number of user for the system to calculate the tax amount
          numberOfUsers = int(input("Enter the number of users::"))
          print("Enter the details of", numberOfUsers, "users::")
          # call above function here
          employeeInfo(numberOfUsers)
          displayInfoWithResult(numberOfUsers)