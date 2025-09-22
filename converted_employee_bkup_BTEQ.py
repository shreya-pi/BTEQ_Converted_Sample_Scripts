#*** Generated code is based on the SnowConvert Python Helpers version 2.0.6 ***
#** SSC-FDM-0007 - MISSING DEPENDENT OBJECTS "tduser.Employee", "tduser.Salary" **
 
import os
import sys
import snowconvert.helpers
from snowconvert.helpers import Export
from snowconvert.helpers import exec
from snowconvert.helpers import BeginLoading
con = None
def main():
  snowconvert.helpers.configure_log()
  con = snowconvert.helpers.log_on()
  #** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE. LOGON **
  #.LOGON
   
  #** SSC-EWI-0001 - UNRECOGNIZED TOKEN ON LINE '1' COLUMN '8' OF THE SOURCE CODE STARTING AT '192.168'. EXPECTED 'STATEMENT' GRAMMAR. LAST MATCHING TOKEN WAS 'LOGON' ON LINE '1' COLUMN '2'. FAILED TOKEN WAS '192.168' ON LINE '1' COLUMN '8'. **
  #--192.168.1.102/dbc,dbc
   
  exec("""
    USE DATABASE tduser
    """)
  exec("""
    CREATE OR REPLACE TABLE employee_bkup (
      EmployeeNo INTEGER,
      FirstName CHAR(30),
      LastName CHAR(30),
      DepartmentNo SMALLINT,
      NetPay INTEGER,
      UNIQUE (EmployeeNo)
    )
    """)

  if snowconvert.helpers.error_code != 0:
    snowconvert.helpers.quit_application(snowconvert.helpers.error_code)
  exec("""
    SELECT
      *
    FROM
      Employee
    --** SSC-FDM-0033 - SAMPLE CLAUSE BEHAVES DIFFERENTLY IN SNOWFLAKE **
    SAMPLE(1 ROWS)
    """)

  if snowconvert.helpers.activity_count != 0:
    INSERTEMPLOYEE()
    return
  exec("""
    DROP TABLE employee_bkup
    """)

  if snowconvert.helpers.error_code != 0:
    snowconvert.helpers.quit_application(snowconvert.helpers.error_code)
  INSERTEMPLOYEE()
  snowconvert.helpers.quit_application()
def INSERTEMPLOYEE():
  exec("""
    INSERT INTO employee_bkup SELECT
      a.EmployeeNo,
      a.FirstName,
      a.LastName,
      a.DepartmentNo,
      b.NetPay
    FROM
      Employee a
      INNER JOIN
        Salary b
        ON (a.EmployeeNo = b.EmployeeNo)
    """)

  if snowconvert.helpers.error_code != 0:
    snowconvert.helpers.quit_application(snowconvert.helpers.error_code)
  #** SSC-FDM-0027 - REMOVED NEXT STATEMENT, NOT APPLICABLE IN SNOWFLAKE. LOGOFF **
  #.LOGOFF
   

if __name__ == "__main__":
  main()