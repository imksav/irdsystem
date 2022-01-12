def calculateDiscountRate(gender, isDisability, isDiplomat):
          if(isDiplomat.upper() == "Y"):
                    discountDiplomat = 0.75
          else:
                    discountDiplomat = 0
          if(isDisability.upper() == "Y"):
                    discountDisability = 0.5
          else:
                    discountDisability = 0
          if(gender.upper() == "F"):
                    discountGender = 0.1
          else:
                    discountGender = 0
          # return compareDiscount(discountDiplomat, discountDisability, discountGender)
          return addAllDiscount(discountDiplomat, discountDisability, discountGender)


def compareDiscount(discountDiplomat, discountDisability, discountGender):
          if discountDiplomat>=discountDisability and discountDiplomat>=discountGender:
                    discount = discountDiplomat
          elif discountDisability>=discountDiplomat and discountDisability>=discountGender:
                    discount = discountDisability
          elif discountGender>=discountDiplomat and discountGender>=discountDisability:
                    discount = discountGender
          else:
                    discount = 0
          return discount

def addAllDiscount(discountDiplomat, discountDisability, discountGender):
          discount = discountDiplomat + discountDisability + discountGender
          return discount

# if __name__ == "__main__":
          # print(calculateDiscountRate("M", "N", "N"))
