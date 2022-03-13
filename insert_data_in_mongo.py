import pymongo
import csv
import logging
logging.basicConfig(filename='mongo.log',level=logging.DEBUG,format='%(asctime)s')

try: 
    logging.info("trying to initiate connection with mongo db server")
    client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.nlmjr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    db=client['dataBase']
    coll=db['Collection']
except Exception as e:
    logging.error(f"an error occured while connecting with mongo server:{e}")

def insert_into_mongo(dict_a):
    """A function that insert input argument dictionary as document in collection"""
    try: 
        coll.insert_one(dict_a)
    except Exception as e:
        logging.error(f"an error occured:{e}")

filename='carbon_nanotubes.csv' #csv file from which the data is inserted to mongodb server
with open(filename,'r') as file:
    csvfile=csv.reader(file, delimiter=";")
    dict_u={}
    logging.info("trying to read the csv file and intiating dictioary to insert into the mongodb Database")
    try: 
        for i in csvfile:
            for j,k in enumerate(i):
                dict_u[k]=j
            break
        coll.insert_one(dict_u)
    except Exception as e:
        logging.error(f"an error occured:{e}")
    try:
        for x,i in enumerate(csvfile):
            dict_u['_id']=x
            for j,key in zip(i,dict_u.keys()):
                dict_u[key]=j.split(',')
            insert_into_mongo(dict_u)
    except Exception as e:
        logging.error(f"an error occured:{e}")
            
