# for married couple
def taxForMarried(yearlyIncome, minimum_taxable, maximum_taxable):
    taxAmount = 0
    # for less than 4 lakhs
    if yearlyIncome <= 450000:
        taxAmount += (1 / 100) * yearlyIncome
    # for less than 5 lakhs
    elif yearlyIncome <= 550000:
        taxAmount += ((1 / 100) * minimum_taxable) + (10 / 100) * (yearlyIncome - minimum_taxable)
        # for less than 7 lakhs
    elif yearlyIncome <= 750000:
        taxAmount += (
            ((1 / 100) * minimum_taxable)
            + ((10 / 100) * 100000)
            + (20 / 100) * (yearlyIncome - 550000)
        )
    # for less than 20 lakhs
    elif yearlyIncome <= maximum_taxable:
        taxAmount += (
            ((1 / 100) * minimum_taxable)
            + ((10 / 100) * 100000)
            + (20 / 100) * (200000)
            + (30 / 100) * (yearlyIncome - 750000)
        )
    # for above 2000000
    else:
        taxAmount += (
            ((1 / 100) * minimum_taxable)
            + ((10 / 100) * 100000)
            + (20 / 100) * (200000)
            + (30 / 100) * (1250000)
            + (36 / 100) * (yearlyIncome - maximum_taxable)
        )
    return taxAmount


# for unmarried single life rockers
def taxForUnmarried(yearlyIncome, minimum_taxable, maximum_taxable):
    taxAmount = 0
    # for less than 4 lakhs
    if yearlyIncome <= minimum_taxable:
        taxAmount += (1 / 100) * yearlyIncome
    # for less than 5 lakhs
    elif yearlyIncome <= 500000:
        taxAmount += ((1 / 100) * minimum_taxable) + (10 / 100) * (yearlyIncome - minimum_taxable)
        # for less than 7 lakhs
    elif yearlyIncome <= 700000:
        taxAmount += (
            ((1 / 100) * minimum_taxable)
            + ((10 / 100) * 100000)
            + (20 / 100) * (yearlyIncome - 500000)
        )
    # for less than 20 lakhs
    elif yearlyIncome <= maximum_taxable:
        taxAmount += (
            ((1 / 100) * minimum_taxable)
            + ((10 / 100) * 100000)
            + (20 / 100) * (200000)
            + (30 / 100) * (yearlyIncome - 700000)
        )
    # for above 2000000
    else:
        taxAmount += (
            ((1 / 100) * minimum_taxable)
            + ((10 / 100) * 100000)
            + (20 / 100) * (200000)
            + (30 / 100) * (1300000)
            + (36 / 100) * (yearlyIncome - maximum_taxable)
        )
    return taxAmount

def 




if __name__=='__main__':

          #  test case for married
          print("Married below 4 lakhs",taxForMarried(18000, 450000, 2000000)) # 180 ==> below 4 lakhs
          print("Married below 5 lakhs",taxForMarried(480000, 450000, 2000000)) # 7500 ==> below 5 lakhs
          print("Married below 7 lakhs",taxForMarried(546000, 450000, 2000000)) # 14100 ==> below 7 lakhs
          print("Married below 20 lakhs",taxForMarried(1546000, 450000, 2000000)) # 293300 ==> below 20 lakhs
          print("Married above 20 lakhs",taxForMarried(11546000, 450000, 2000000)) # 3866060 ==> above 20 lakhs
          print("+++++++++++++++++++++++++=============================+++++++++++++++++++++++++")
          #  test case for unmarried
          print("Unmarried below 4 lakhs",taxForUnmarried(18000, 400000, 2000000)) # 180 ==> below 4 lakhs
          print("Unmarried below 5 lakhs",taxForUnmarried(450000, 400000, 2000000)) # 9000 ==> below 5 lakhs
          print("Unmarried below 7 lakhs",taxForUnmarried(546000, 400000, 2000000)) # 23200 ==> below 7 lakhs
          print("Unmarried below 20 lakhs",taxForUnmarried(1546000, 400000, 2000000)) # 307800 ==> below 20 lakhs
          print("Unmarried above 20 lakhs",taxForUnmarried(11546000, 400000, 2000000)) # 3880560 ==> above 20 lakhs

