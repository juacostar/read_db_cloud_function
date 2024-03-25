import sqlite3

def read_database(device, client, transactions):
    
  databse_path = '/Users/juancamiloacosta/Documents/uniandes/software architecture/challenge 2/cloud function/read_db_cloud_function/database.db'
  
  connection = sqlite3.connect(databse_path)
  cursor = connection.cursor()
  
  cursor.execute("SELECT COUNT(*) FROM  transactions  tr WHERE tr.device_id=? and tr.client=?", (device, client))
  
  count = cursor.fetchone()[0]
  
  connection.close()
  
  return count

print(read_database(50, 'Exito', 0))