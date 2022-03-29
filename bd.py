import sqlite3
from datetime import datetime 

class Data_Base():
    con = sqlite3.connect('data_base.db', check_same_thread=False)
    cursor = con.cursor()

    def __init__(self):

        Data_Base.cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                            (data text, type text, cost float)''') 
        
    
    def add_in_bd(self, cost, type):


        query = '''INSERT INTO expenses VALUES 
                        (?, ?, ?)'''
        
        today = str(datetime.now())
        Data_Base.cursor.execute(query, (today, type, cost))
        Data_Base.con.commit()


    def get_all_cost(self, typ):
        expenses = 0
        for cost in Data_Base.cursor.execute(f''' SELECT cost FROM expenses WHERE type = "{typ}"'''):
            print(cost)
            expenses += float(cost[0])
        
        return expenses

            




        

