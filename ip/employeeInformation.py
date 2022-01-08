import calculateTax
import calculateDiscountRate

def checkStatus(isMarried, gender, isInsurance, isDisability, isDiplomat, yearlyIncome):
          if isMarried.upper() == "Y":
                    # minimum_taxable = float(input("Enter the minimum taxable amount::"))
                    # maximum_taxable = float(input("Enter the maximum taxable amount::"))
                    minimum_taxable = 450000
                    maximum_taxable = 2000000
                    discount = calculateDiscountRate.calculateDiscountRate(gender, isDisability, isDiplomat)
                    return calculateTax.taxForMaritalStatus(yearlyIncome, minimum_taxable, maximum_taxable, discount)
          elif isMarried.upper() == "N":
                    # minimum_taxable = float(input("Enter the minimum taxable amount::"))
                    # maximum_taxable = float(input("Enter the maximum taxable amount::"))
                    minimum_taxable = 400000
                    maximum_taxable = 2000000
                    discount = calculateDiscountRate.calculateDiscountRate(gender, isDisability, isDiplomat)
                    return calculateTax.taxForMaritalStatus(yearlyIncome, minimum_taxable, maximum_taxable, discount)
                    # print(discount)
          else:
                    print("Oops! Something went wrong.\nThank you for using our service!!!\nSee you next time")
          


def employeeInfo(numberOfUsers):
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
                    taxAmount = checkStatus(isMarried, gender, isInsurance, isDisability, isDiplomat, yearlyIncome)
                    taxAmountList.append(taxAmount)

# display output
def displayInfoWithResult(numberOfUsers):
          for i in range(numberOfUsers):
                    print("For Customer[{}]\nCustomer Name::", yournameList[i], "\tAddress::", addressList[i],"\tContact::", contactList[i],"\nAge::",ageList[i],"\tGender::",genderList[i],"\tCurrent Date of Registration::",currentDORList[i],"\nMarital Status::",isMarriedList[i],"\tInsurance::", isInsuranceList[i],"\tDisability::",isDisabilityList[i],"\nDiplomat::",isDiplomatList[i],"\tYearly Income::", yearlyIncomeList[i],"\tTaxable Amount::",taxAmountList[i],"\n\nThis is computer generated tax amount to be paid.\n".format(i))

                    
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
          # numberOfUsers = int(input("Enter the number of users::"))
          # print("Enter the details of", numberOfUsers, "users::")
          # employeeInfo(numberOfUsers)
          # displayInfoWithResult(numberOfUsers)
          # checkStatus("N", "F", "N", "N", "N", 115460000)