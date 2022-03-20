import sqlite3
from datetime import datetime 

class Data_Base():
    con = sqlite3.connect('data_base.db', check_same_thread=False)
    cursor = con.cursor()

    def __init__(self):

        Data_Base.cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                            (data text, cost float)''') 
        
    
    def add_in_bd(self, cost):


        query = '''INSERT INTO expenses VALUES 
                        (?, ?)'''
        
        today = str(datetime.now())
        Data_Base.cursor.execute(query, (today, cost))
        Data_Base.con.commit()

    def get_all_cost(self):
        expenses = 0
        for cost in Data_Base.cursor.execute(''' SELECT cost FROM expenses'''):
            print(cost[0])
            expenses += int(cost[0])
        
        return expenses

            




        

