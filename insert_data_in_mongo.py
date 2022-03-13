import csv
import logging
logging.basicConfig(filename='mongo.log',level=logging.DEBUG,format='%(asctime)s')

with open('carbon_nanotubes.csv','r') as file:
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
            coll.insert_one(dict_u)
    except Exception as e:
        print(f"an error occured {e}")
