import database
import json

db = database.DB()

query = '''
SELECT * FROM DEALER
ORDER BY dealer_id DESC
'''



db.custom_query(query)
db.close()


