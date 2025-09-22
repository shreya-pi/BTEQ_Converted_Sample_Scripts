#*** Generated code is based on the SnowConvert Python Helpers version 2.0.6 ***
 
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
    SELECT
      COUNT(*)
    from
      customer_aug18
    """)

  if snowconvert.helpers.activity_count == 0:
    snowconvert.helpers.quit_application()

  for statement in snowconvert.helpers.readrun(fr"C:\Users\SARAVANA\Desktop\Edureka\BTEQ\run.bteq.txt"):
    eval(statement)
  snowconvert.helpers.quit_application()

if __name__ == "__main__":
  main()