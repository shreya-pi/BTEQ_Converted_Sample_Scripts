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
  #** SSC-EWI-TD0005 - THE STATEMENT WAS CONVERTED BUT ITS FUNCTIONALITY IS NOT IMPLEMENTED YET **
  Export.report(fr"C:\Users\SARAVANA\Desktop\Edureka\csvexportdec09.csv", ",")
  exec("""
    SELECT
      LEFT(cast(cust_id as VARCHAR), 20) || ',' || LEFT(cast(income as VARCHAR), 20)
    from
      customer
    """)
  #** SSC-EWI-0001 - UNRECOGNIZED TOKEN ON LINE '7' COLUMN '2' OF THE SOURCE CODE STARTING AT 'EXPORT'. EXPECTED 'STATEMENT' GRAMMAR. LAST MATCHING TOKEN WAS 'EXPORT' ON LINE '7' COLUMN '2'. **
  #--EXPORT.RESET
   
  #** SSC-EWI-0001 - UNRECOGNIZED TOKEN ON LINE '8' COLUMN '1' OF THE SOURCE CODE STARTING AT 'logoff'. EXPECTED 'STATEMENT' GRAMMAR. LAST MATCHING TOKEN WAS ';' ON LINE '7' COLUMN '14'. FAILED TOKEN WAS 'logoff' ON LINE '8' COLUMN '1'. **
  #--logoff
   
  snowconvert.helpers.quit_application()

if __name__ == "__main__":
  main()