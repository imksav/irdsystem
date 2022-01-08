import header
import employeeInformation
import footer



if __name__ == '__main__':
          header.getHeader()
          numberOfUsers = int(input("Enter the number of users::"))
          print("Enter the details of", numberOfUsers, "users::")
          employeeInformation.employeeInfo(numberOfUsers)
          employeeInformation.displayInfoWithResult(numberOfUsers)
          footer.getFooter()
