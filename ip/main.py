import header
import employeeInformation
import footer



if __name__ == '__main__':
          header.getHeader()
          # get the number of user for the system to calculate the tax amount
          numberOfUsers = int(input("Enter the number of users::"))
          print("Enter the details of", numberOfUsers, "users::")
          employeeInformation.employeeInfo(numberOfUsers)
          employeeInformation.displayInfoWithResult(numberOfUsers)
          footer.getFooter()
