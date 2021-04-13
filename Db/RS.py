import os

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

DATABASE = "dev"
USER = "beam_exp_user"
PASSWORD = os.getenv('REDSHIFT_PWD')
if PASSWORD is None:
    print("REDSHIFT_PWD must be set")
    exit()
HOST = "ual-dev-cluster.cahhf1iruygb.us-east-1.redshift.amazonaws.com"
PORT = "5439"
SCHEMA = "dw_rv"
REGION = 'us-east-1'


connection_string = "redshift+psycopg2://%s:%s@%s:%s/%s" % (USER,PASSWORD,HOST,str(PORT),DATABASE)
engine = sa.create_engine(connection_string)
session = sessionmaker()
session.configure(bind=engine)
s = session()
SetPath = "SET search_path TO %s" % SCHEMA
s.execute(SetPath)

query = "SELECT * FROM commitment_stage;"
rr = s.execute(query)
all_results =  rr.fetchall()

def pretty(all_results):
    for row in all_results :
        print("row start >>>>>>>>>>>>>>>>>>>>")
        row_s = ""
        for r in row :
#            print(" ---- %s" % r)
             row_s += str(r)
        print(row_s)
        print("row end >>>>>>>>>>>>>>>>>>>>>>")

pretty(all_results)
s.close()
