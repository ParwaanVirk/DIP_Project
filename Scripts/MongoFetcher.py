def get_database():
    from pymongo import MongoClient
    import pymongo
    from pymongo import MongoClient

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://Akuver:365YF3O0iDUnRhny@akuver-bot.hv1uq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient

    client = MongoClient(CONNECTION_STRING)
    db = client.admin

    
    return db.command("serverStatus")
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    print(dbname)