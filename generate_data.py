import random
import sqlite3

# Table Structure
# id_tx transaction id
# device device id 
# client client
# value ocean drive

clients = ['Exito', 'Carulla', 'Metro', 'Panamericana', 'Surtimax']
databse_path = '/Users/juancamiloacosta/Documents/uniandes/software architecture/challenge 2/cloud function/read_db_cloud_function/database.db'



class Transaction:
    def __init__(self, id, device, client, value):
        self.id = id
        self.device = device
        self.client = client
        self.value = value
    

def generate_random_data():
    random_id_tx = random.randint(1, 10000000)
    random_device_id = random.randint(1, 50)
    random_client = random.choice(clients)
    random_value = random.randint(1, 1000000)
    
    return Transaction(random_id_tx, random_device_id, random_client, random_value)


def create_database():
    
    connection = sqlite3.connect(databse_path)
    cursor = connection.cursor()
    
    #creating table
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS 'transactions'
                   (id_tx INTEGER PRIMARY KEY,
                    device_id INTEGER,
                    client TEXT,
                    value INTEGER
                   )''')
    
    for i in range(5000):
        transaction = generate_random_data()
        cursor.execute("INSERT INTO transactions (id_tx, device_id, client, value) VALUES (?,?,?,?)", (transaction.id, transaction.device, transaction.client, transaction.value))
        
        
    connection.commit()
    connection.close()
    
create_database()
        
        