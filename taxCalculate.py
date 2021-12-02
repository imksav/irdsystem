import datetime

# for married couple


def taxForMarried(yearlyIncome):
    taxAmount = 0
    # for less than 4 lakhs
    if(yearlyIncome <= 450000):
        taxAmount += (1/100)*yearlyIncome
    # for less than 5 lakhs
    elif(yearlyIncome <= 550000):
        taxAmount += ((1/100)*450000) + (10/100)*(yearlyIncome-450000)
        # for less than 7 lakhs
    elif(yearlyIncome <= 750000):
        taxAmount += ((1/100)*450000) + ((10/100)*100000) + \
            (20/100)*(yearlyIncome-550000)
    # for less than 20 lakhs
    elif(yearlyIncome <= 2000000):
        taxAmount += ((1/100)*450000) + ((10/100)*100000) + \
            (20/100)*(200000)+(30/100)*(yearlyIncome-750000)
    # for above 2000000
    else:
        taxAmount += ((1/100)*450000) + ((10/100)*100000) + \
            (20/100)*(200000)+(30/100)*(1250000)+(36/100)*(yearlyIncome-2000000)
    return taxAmount

# for unmarried single life rockers


def taxForUnmarried(yearlyIncome):
    taxAmount = 0
    # for less than 4 lakhs
    if(yearlyIncome <= 400000):
        taxAmount += (1/100)*yearlyIncome
    # for less than 5 lakhs
    elif(yearlyIncome <= 500000):
        taxAmount += ((1/100)*400000) + (10/100)*(yearlyIncome-400000)
        # for less than 7 lakhs
    elif(yearlyIncome <= 700000):
        taxAmount += ((1/100)*400000) + ((10/100)*100000) + \
            (20/100)*(yearlyIncome-500000)
    # for less than 20 lakhs
    elif(yearlyIncome <= 2000000):
        taxAmount += ((1/100)*400000) + ((10/100)*100000) + \
            (20/100)*(200000)+(30/100)*(yearlyIncome-700000)
    # for above 2000000
    else:
        taxAmount += ((1/100)*400000) + ((10/100)*100000) + \
            (20/100)*(200000)+(30/100)*(1300000)+(36/100)*(yearlyIncome-2000000)
    return taxAmount

# header of the output ui


def returnDetails(yourname, address, age, marriedStatus, monthlyIncome, taxAmount):
    print("""
                            Income Tax Calculation
                          Lazimpat, Kathmandu, Nepal
                            Contact: 9869260495
                            Email: imksav@ird.gov.np
                                                        Date:""", datetime.datetime.today().strftime("%d-%b-%Y | %H:%M:%S"), """
    ============================================================
    Dear""", yourname, """,
                    Your Personal Details are as follows:
    ============================================================
    Address:""", address, """
    Age:""", age, """
    Marital Status:""", marriedStatus, """
    Monthly Income: {:,}""".format(monthlyIncome), """
    Your final payable tax amount: {:,}""".format(taxAmount), """
    ============================================================
                Thank you for using our service!!!
                See you next time
    ============================================================
    """)

# header of the input ui


def getHeader():
    print("""
                            Income Tax Calculation
                          Lazimpat, Kathmandu, Nepal
                            Contact: 9869260495
                            Email: imksav@ird.gov.np
                                                        Date:""", datetime.datetime.today().strftime("%d-%b-%Y | %H:%M:%S"), """
    ============================================================
    """)
    getPersonalDetails()

# get the personal information of the users


def getPersonalDetails():
    print("Enter your Details:\n============================================================")
    yourname = input("Enter your name::")
    address = input("Enter your address::")
    age = int(input("Enter your age::"))
    print("=================================================")
    monthlyIncome = float(input("Enter your monthly income::"))
    marriedStatus = input("Are you married?(Y/N)")
    taxAmount = checkMaritalStatus(marriedStatus, monthlyIncome)
    returnDetails(yourname, address, age, marriedStatus,
                  monthlyIncome, taxAmount)
    print("=================================================")

# checking the marital status


def checkMaritalStatus(marriedStatus, monthlyIncome):
    if marriedStatus.upper() == "Y":
        return taxForMarried(monthlyIncome*12)
    elif marriedStatus.upper() == "N":
        return taxForUnmarried(monthlyIncome*12)
    else:
        print("Oops! Invalid Input!!!")
        choice = input("Do you want to continue?(Y/N)")
        if(choice.upper() == "Y"):
            getPersonalDetails()
        else:
            print("""
            Thank you for using our service!!!
            See you next time
            """)


getHeader()
