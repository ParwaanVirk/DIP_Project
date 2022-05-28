from psycopg2 import Timestamp
from backend.models import Transformer, TransData
def get_database():
    from pymongo import MongoClient
    import pymongo
    from pymongo import MongoClient

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://Akuver:365YF3O0iDUnRhny@akuver-bot.hv1uq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient

    client = MongoClient(CONNECTION_STRING)
    db = client['myFirstDatabase']

    col = db['transformerdatas']

    x = col.find()
    
    # print(x[0]) -- prints one transformer param instance
    for data in x:
        trans_id = data['transformerId']
        current_trans = Transformer.objects.filter(id = trans_id)

        TransData.objects.create(
            transformer = current_trans,
            Timestamp = data['timeStamp'],
            Current_Input = data['currentInput'],
            Voltage_Input = data['voltageInput'],
            Oil_Temprature = data['oilTemperature'],
            Winding_Temprature = 0,
            Oil_TankLevel = data['oilTankLevel'], 
            Moisture_Level = data['moistureLevel'],
            Tapping_Ratio = data['tappingRatio'],
            Overall_Health = data['overallHealth'],

        )
        

        
        
        
        
        
        
        










    
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    # Get the database
    get_database()