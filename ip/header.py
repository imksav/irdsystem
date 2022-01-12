import datetime

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


# if __name__ == '__main__':
#           getHeader()