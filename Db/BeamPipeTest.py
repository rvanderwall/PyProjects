import os
import sys
from time import sleep
from json import dumps, loads

from kafka import KafkaProducer
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

RS_USER = "beam_exp_user"
RS_PWD = os.getenv('REDSHIFT_PWD')
if PASSWORD is None:
    print("REDSHIFT_PWD must be set")
    exit()
RS_HOST = "ual-dev-cluster.cahhf1iruygb.us-east-1.redshift.amazonaws.com"
RS_PORT = "5439"
RS_REGION = 'us-east-1'

RS_DATABASE = "dev"
RS_SCHEMA = "dw_staging"

KAFKA_HOST = "localhost:9092"
KAFKA_TOPIC="AUDIT"


def get_session():
    connection_string = "redshift+psycopg2://%s:%s@%s:%s/%s" % (RS_USER,RS_PWD,RS_HOST,str(RS_PORT),RS_DATABASE)
    engine = sa.create_engine(connection_string)
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()
    SetPath = "SET search_path TO %s" % RS_SCHEMA
    s.execute(SetPath)
    return s

def close_session(s):
    s.close()

def get_count(session, table):
    query = f"SELECT count(*) FROM {table};"
    rr = session.execute(query)
    all_results =  rr.fetchall()
    return all_results


def get_kafka_producer():
    producer = KafkaProducer(bootstrap_servers=kafka_host.split(','),
                             value_serializer=lambda x: 
                             dumps(x).encode('utf-8'))

    return producer

def modify_json(orig, mods):
    new_json = copy.deepcopy(orig)
    for key in mods.keys():
        if "." in key:
            parts = key.split(".")
            p1 = new_json[parts[0]]
            p1[parts[1]] = mods[key]
        else:
            new_json[key] = mods[key]
    return new_json


def pretty(all_results):
    for row in all_results :
        print("row start >>>>>>>>>>>>>>>>>>>>")
        row_s = ""
        for r in row :
#            print(" ---- %s" % r)
             row_s += str(r)
        print(row_s)
        print("row end >>>>>>>>>>>>>>>>>>>>>>")


def test_portal():
    sess = get_session()
    count1 = get_count(sess,"project_stage")
    print(count1)


if __name__ == "__main__":
    test_portal()
