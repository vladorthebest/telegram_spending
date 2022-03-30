import sqlite3
from datetime import datetime 

class Data_Base():
    con = sqlite3.connect('data_base.db', check_same_thread=False)
    cursor = con.cursor()

    def __init__(self):

        Data_Base.cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                            (user_id text, data text, type text, cost float)''') 
        
    
    def add_in_bd(self, cost, type, user_id):


        query = '''INSERT INTO expenses VALUES 
                        (?, ?, ?, ?)'''
        
        today = str(datetime.now())
        Data_Base.cursor.execute(query, (user_id, today, type, cost))
        Data_Base.con.commit()


    def get_all_cost(self, typ, user_id):
        expenses = 0

        for cost in Data_Base.cursor.execute(f''' SELECT cost FROM expenses WHERE type = "{typ}" AND user_id = "{user_id}"'''):
            print(cost)
            expenses += float(cost[0])
        
        return expenses

            




        

