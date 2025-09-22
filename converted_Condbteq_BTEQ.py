#*** Generated code is based on the SnowConvert Python Helpers version 2.0.6 ***
#** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "financial.customer" **
 
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
  #.logon
   
  #** SSC-EWI-0001 - UNRECOGNIZED TOKEN ON LINE '1' COLUMN '8' OF THE SOURCE CODE STARTING AT '192.168'. EXPECTED 'STATEMENT' GRAMMAR. LAST MATCHING TOKEN WAS 'logon' ON LINE '1' COLUMN '2'. FAILED TOKEN WAS '192.168' ON LINE '1' COLUMN '8'. **
  #--192.168.128.128/dbc,dbc
   
  exec("""
    USE DATABASE financial
    """)
  exec("""
    DELETE FROM
      customer_aug18
    """)

  if snowconvert.helpers.error_code == 0:
    INSERT_DEMO()
    return
  exec("""
    CREATE OR REPLACE TABLE FINANCIAL.customer_aug18 (
      cust_id INTEGER NOT NULL,
      income INTEGER,
      age SMALLINT,
      years_with_bank SMALLINT,
      nbr_children SMALLINT,
      gender CHAR(1),
      marital_status CHAR(1)
    )
    """)
  INSERT_DEMO()
  snowconvert.helpers.quit_application()
def INSERT_DEMO():
  exec("""
    INSERT INTO customer_aug18 SELECT
      *
    from
      customer
    """)
  snowconvert.helpers.quit_application()

if __name__ == "__main__":
  main()