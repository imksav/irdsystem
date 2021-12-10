import datetime

# print recepit
def outputResult(
    yourname, gender, address, dob, contact, email, isMarried, monthlyIncome, taxAmount
):
    with open('taxCalculate.txt','w') as f:
        f.write("Yourname: {}\nSex: {}\nAddress: {}\nDOB: {}\nContact Number: {}\nEmail: {}\nMonthly Income: {}\nAnnualy Income: {}\nMarital Status: {}\nTaxable Amount: {}\nNet Income Annually: {}\n======END OF USER======\n".format(yourname, gender, address, dob, contact, email, monthlyIncome, monthlyIncome*12, isMarried, taxAmount, ((monthlyIncome*12)-taxAmount)))

    print(
        """
Customer Name:""",
        yourname,
        """                 Sex:""",
        "Male" if gender.upper() == "M" else "Female",
        """
Address:""",
        address,
        """                                                   DOB:""",
        dob,
        """
Contact Number:""",
        contact,
        """                        Email:""",
        email,
        """
Monthly Income:""",
        monthlyIncome,
        """                                      Annually Income:""",
        monthlyIncome * 12,
        """
Marital Status:""",
        "Married" if isMarried.upper() == "Y" else "Unmarried",
        """                                      Taxable Amount:""",
        taxAmount,
        """
Net Income Annually:""",
        (monthlyIncome * 12) - taxAmount,
        """
This is computer generated tax amount to be paid.
====================================================
""",
    )


# header for tax calculation
def getHeader():
    print(
        """
                           Inland Revenue Department
                          Lazimpat, Kathmandu, Nepal
                       Contact: 16600140000 (Toll Free)
                           Email: serviceird@ird.gov.np
                                          Date:""",
        datetime.datetime.today().strftime("%d-%b-%Y | %H:%M:%S"),
        """
    ====================================================
    """,
    )


# for married couple


def taxForMarried(yearlyIncome):
    taxAmount = 0
    # for less than 4 lakhs
    if yearlyIncome <= 450000:
        taxAmount += (1 / 100) * yearlyIncome
    # for less than 5 lakhs
    elif yearlyIncome <= 550000:
        taxAmount += ((1 / 100) * 450000) + (10 / 100) * (yearlyIncome - 450000)
        # for less than 7 lakhs
    elif yearlyIncome <= 750000:
        taxAmount += (
            ((1 / 100) * 450000)
            + ((10 / 100) * 100000)
            + (20 / 100) * (yearlyIncome - 550000)
        )
    # for less than 20 lakhs
    elif yearlyIncome <= 2000000:
        taxAmount += (
            ((1 / 100) * 450000)
            + ((10 / 100) * 100000)
            + (20 / 100) * (200000)
            + (30 / 100) * (yearlyIncome - 750000)
        )
    # for above 2000000
    else:
        taxAmount += (
            ((1 / 100) * 450000)
            + ((10 / 100) * 100000)
            + (20 / 100) * (200000)
            + (30 / 100) * (1250000)
            + (36 / 100) * (yearlyIncome - 2000000)
        )
    return taxAmount


# for unmarried single life rockers


def taxForUnmarried(yearlyIncome):
    taxAmount = 0
    # for less than 4 lakhs
    if yearlyIncome <= 400000:
        taxAmount += (1 / 100) * yearlyIncome
    # for less than 5 lakhs
    elif yearlyIncome <= 500000:
        taxAmount += ((1 / 100) * 400000) + (10 / 100) * (yearlyIncome - 400000)
        # for less than 7 lakhs
    elif yearlyIncome <= 700000:
        taxAmount += (
            ((1 / 100) * 400000)
            + ((10 / 100) * 100000)
            + (20 / 100) * (yearlyIncome - 500000)
        )
    # for less than 20 lakhs
    elif yearlyIncome <= 2000000:
        taxAmount += (
            ((1 / 100) * 400000)
            + ((10 / 100) * 100000)
            + (20 / 100) * (200000)
            + (30 / 100) * (yearlyIncome - 700000)
        )
    # for above 2000000
    else:
        taxAmount += (
            ((1 / 100) * 400000)
            + ((10 / 100) * 100000)
            + (20 / 100) * (200000)
            + (30 / 100) * (1300000)
            + (36 / 100) * (yearlyIncome - 2000000)
        )
    return taxAmount


# backend for maritial status checking
def checkMaritialStatus(isMarried, monthlyIncome):
    if isMarried.upper() == "Y":
        return taxForMarried(monthlyIncome * 12)
    elif isMarried.upper() == "N":
        return taxForUnmarried(monthlyIncome * 12)
    else:
        print(
            """
            Oops! Something went wrong.
            Thank you for using our service!!!
            See you next time.......
            """
        )


# front end
getHeader()
numberOfUsers = int(input("Enter the number of users::"))
print("Enter the details of", numberOfUsers, "users::")
yournameList = []
genderList = []
addressList = []
dobList = []
contactList = []
emailList = []
isMarriedList = []
monthlyIncomeList = []
taxAmountList = []
for i in range(numberOfUsers):
    yourname = input("Enter your name[{}]::".format(i + 1))
    yournameList.append(yourname)
    gender = input("Enter your gender(M/F)[{}]::".format(i + 1))
    genderList.append(gender)
    address = input("Enter your address[{}]::".format(i + 1))
    addressList.append(address)
    dob = input("Enter your dob(YYYY-MM-DD)[{}]::".format(i + 1))
    dobList.append(dob)
    contact = input("Enter your contact number[{}]::".format(i + 1))
    contactList.append(contact)
    email = input("Enter your email address[{}]::".format(i + 1))
    emailList.append(email)
    isMarried = input("Are you married?(Y/N)[{}]::".format(i + 1))
    isMarriedList.append(isMarried)
    monthlyIncome = int(
        input("Enter the monthly income of the user[{}]::".format(i + 1))
    )
    monthlyIncomeList.append(monthlyIncome)
    print("====================================================")
    taxAmount = checkMaritialStatus(isMarried, monthlyIncome)
    taxAmountList.append(taxAmount)

print("OutPut:::")
for i in range(numberOfUsers):
    getHeader()
    outputResult(
        yournameList[i],
        genderList[i],
        addressList[i],
        dobList[i],
        contactList[i],
        emailList[i],
        isMarriedList[i],
        monthlyIncomeList[i],
        taxAmountList[i],
    )
    print("====================================================")
