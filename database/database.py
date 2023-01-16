import sqlite3
import json

class DB:
    #initializing class to establish connection to database
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.c = self.conn.cursor()

    # insertion functions to insert values into tables
    def dealer_insert(self, dealer_id, img_id, fname, lname, username, password, last_login, contact_number, company_name, create_date, address, status):
        with self.conn:
            self.c.execute("INSERT INTO DEALER VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dealer_id, img_id, fname, lname, username, password, last_login, contact_number, company_name, create_date, address, status))
        

    def admin_insert(self, admin_id, admin_name, username, password, last_login, contact_number, status):
        with self.conn:
            self.c.execute("INSERT INTO ADMIN VALUES(?, ?, ?, ?, ?, ?, ?)", (admin_id, admin_name, username,password, last_login, contact_number, status))
        

    def customer_insert(self, customer_id, fname, lname, gender, email_id, contact, password, address, city, state, pincode):
        with self.conn:
            self.c.execute("INSERT INTO CUSTOMER VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (customer_id, fname, lname, gender, email_id, contact, password, address, city, state, pincode))
        

    def vehicle_insert(self, veh_id, dealer_id, veh_name, veh_model, veh_type, veh_description, veh_cost, status, create_date):
        with self.conn:
            self.c.execute("INSERT INTO VEHICLE VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (veh_id, dealer_id, veh_name, veh_model, veh_type, veh_description, veh_cost, status, create_date))
        

    def showroom_insert(self, showroom_id, name, dealer_id, address, city, pincode, state, contact, status, image_path):
        with self.conn:
            self.c.execute("INSERT INTO SHOWROOM VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (showroom_id, name, dealer_id, address, city, pincode, state, contact, status, image_path))
        

    def image_insert(self, img_id, veh_id, img_name, default_img, img_path):
        with self.conn:
            self.c.execute("INSERT INTO IMAGE VALUES(?, ?, ?, ?, ?)", (img_id, veh_id, img_name, default_img, img_path))
        

    def sales_insert(self, cust_id, sales_id, veh_id, desc, ord_date, veh_cost, showroom_id, status, deal_date, tax_id):
        with self.conn:
            self.c.execute("INSERT INTO SALES VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (cust_id, sales_id, veh_id, desc, ord_date, veh_cost, showroom_id, status, deal_date, tax_id))
        

    def tax_insert(self, tax_id, tax, tax_desc, status):
        with self.conn:
            self.c.execute("INSERT INTO TAX VALUES(?, ?, ?, ?)", (tax_id, tax, tax_desc, status))
        

    # display function to display table contents
    def show_table(self, table_name, attribute = "*"):
        with self.conn:
            self.c.execute(f"SELECT {attribute} FROM {table_name}")
            print(self.c.fetchall())

    def show_where(self, table_name, condition, attribute = "*"):
        with self.conn:
            self.c.execute(f"SELECT {attribute} FROM {table_name} WHERE {condition}")
            print(self.c.fetchall())

    def show_distinct(self, table_name, attributes='*'):
        with self.conn:
            self.c.execute(f"SELECT DISTINCT {attributes} FROM {table_name}")
            print(self.c.fetchall())

    def show_limited(self, table_name, limit, attributes='*'):
        with self.conn:
            self.c.execute(f"SELECT {attributes} FROM {table_name} LIMIT {limit}")
            print(self.c.fetchall())

    #functions to delete rows from tables
    def delete_row(self, table_name, condition=None):
        with self.conn:
            self.c.execute(f"DELETE FROM {table_name} WHERE {condition}")

    def delete_table(self, table_name):
        with self.conn:
            self.c.execute(f"DELETE FROM {table_name}")

    #function to update values in a table
    def update_value(self, table_name, values, condition):
        with self.conn:
            self.c.execute(f"UPDATE {table_name} SET {values} WHERE {condition}")

    #function to view table in a particular order
    def order_by(self, table_name, conditions, attributes = '*'):
        with self.conn:
            self.c.execute(f"SELECT {attributes} FROM {table_name} ORDER BY {conditions}")
            print(self.c.fetchall())


    #function for custom/complex queries
    def custom_query(self, query):
        with self.conn:
            self.c.execute(query)
            print(self.c.fetchall())
            
           
    #close function to close connection
    def close(self):
        self.conn.close()
    