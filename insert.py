from pymongotest import get_database
from datetime import datetime
from dateutil import parser
import time
dbname = get_database()

# Create a new collection
old_collection = dbname["data"]
new_collection=dbname["newdata"]
item_details = old_collection.find()
for item in item_details:
    mydate=datetime.now()
    vot=item['pressure']['value']/200.0 + 20
    new_item={
        "date" : parser.parse(mydate.isoformat()) ,
        "temperature" : vot ,
        "type" : 4
    }    
    if vot<30:
    	time.sleep(10)
    	new_collection.insert_one(new_item)
