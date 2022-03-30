import sqlite3
from datetime import datetime 

class Data_Base():
    con = sqlite3.connect('data_base.db', check_same_thread=False)  #connect DataBase
    cursor = con.cursor() #create cursor for DataBase

    def __init__(self):
        """ Create table in the DataBase """
        
        Data_Base.cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                            (user_id text, data text, type text, cost float)''')  
        
    
    def add_in_bd(self, cost, type, user_id):
        """ Add new record in the DataBase
        Args: value, category, user_id
        """

        #command "adding"
        query = '''INSERT INTO expenses VALUES 
                        (?, ?, ?, ?)'''
        
        today = str(datetime.now()) #date today

        #add record in DataBase
        Data_Base.cursor.execute(query, (user_id, today, type, cost)) 
        Data_Base.con.commit()
        
        print(f"Add {user_id}: {type} {cost}") #log

    def get_all_cost(self, typ, user_id):
        """ Function return cost amount from the category
        Args: category, user_id
        """
        expenses = 0 #cost amount

        #select all record in the category from user
        for cost in Data_Base.cursor.execute(f''' SELECT cost FROM expenses WHERE type = "{typ}" AND user_id = "{user_id}"'''):
            expenses += float(cost[0]) #add cost in the cost amount

        print(f"Result {user_id}: {typ} {expenses}") #log

        return expenses

            




        

