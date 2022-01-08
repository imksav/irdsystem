# for married couple
def taxForMaritalStatus(yearlyIncome, minimum_taxable, maximum_taxable, discount):
    taxAmount = 0
    # for less than 4 lakhs
    if yearlyIncome <= minimum_taxable:
        taxAmount += (0.01) * yearlyIncome
    # for less than 5 lakhs
    elif yearlyIncome <= (minimum_taxable+100000):
        taxAmount += ((0.01) * minimum_taxable) + (0.1) * (yearlyIncome - minimum_taxable)
        # for less than 7 lakhs
    elif yearlyIncome <= (minimum_taxable+300000):
        taxAmount += (
            ((0.01) * minimum_taxable)
            + ((0.1) * 100000)
            + (0.2) * (yearlyIncome - (minimum_taxable+100000))
        )
    # for less than 20 lakhs
    elif yearlyIncome <= maximum_taxable:
        taxAmount += (
            ((0.01) * minimum_taxable)
            + ((0.1) * 100000)
            + (0.2) * (200000)
            + (0.3) * (yearlyIncome - (minimum_taxable+300000))
        )
    # for above 2000000
    else:
        taxAmount += (
            ((0.01) * minimum_taxable)
            + ((0.1) * 100000)
            + (0.2) * (200000)
            + (0.3) * (maximum_taxable-200000-100000-minimum_taxable)
            + (0.36) * (yearlyIncome - maximum_taxable)
        )
    
    return taxAmount - (discount * taxAmount)



if __name__=='__main__':
          #  test case for married
          print("Married below 4 lakhs",taxForMaritalStatus(18000, 450000, 2000000, 0)) # 180 ==> below 4 lakhs
          print("Married below 5 lakhs",taxForMaritalStatus(480000, 450000, 2000000, 0)) # 7500 ==> below 5 lakhs
          print("Married below 7 lakhs",taxForMaritalStatus(546000, 450000, 2000000, 0)) # 14100 ==> below 7 lakhs
          print("Married below 20 lakhs",taxForMaritalStatus(1546000, 450000, 2000000, 0)) # 293300 ==> below 20 lakhs
          print("Married above 20 lakhs",taxForMaritalStatus(11546000, 450000, 2000000, 0)) # 3866060 ==> above 20 lakhs
          print("+++++++++++++++++++++++++=============================+++++++++++++++++++++++++")
          #  test case for unmarried
          print("Unmarried below 4 lakhs",taxForMaritalStatus(18000, 400000, 2000000, 0)) # 180 ==> below 4 lakhs
          print("Unmarried below 5 lakhs",taxForMaritalStatus(450000, 400000, 2000000, 0)) # 9000 ==> below 5 lakhs
          print("Unmarried below 7 lakhs",taxForMaritalStatus(546000, 400000, 2000000, 0)) # 23200 ==> below 7 lakhs
          print("Unmarried below 20 lakhs",taxForMaritalStatus(1546000, 400000, 2000000, 0)) # 307800 ==> below 20 lakhs
          print("Unmarried above 20 lakhs",taxForMaritalStatus(11546000, 400000, 2000000, 0)) # 3880560 ==> above 20 lakhs
          # print(taxAmount)
          # taxForWomen(taxAmount)

