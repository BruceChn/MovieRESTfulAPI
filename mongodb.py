import ast
def add_city(db):
    # Changes to this function will be reflected in the output. 
    # All other functions are for local use only.
    # Try changing the name of the city to be inserted
    db.cities.insert({"sdfsd" : "gsfgsdfg"})
    

def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    # 'examples' here is the database name. It will be created if it does not exist.
    db = client.mv
    return db	

if __name__ == "__main__":
    # For local use
    db = get_db() # uncomment this line if you want to run this locally
    with open("movie.txt",'r') as f:
		for line in f:
			db.movies.insert(ast.literal_eval(line))
			
 