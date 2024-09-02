#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# Create the students table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     department TEXT NOT NULL,
                     year INTEGER NOT NULL,
                     email TEXT NOT NULL UNIQUE,
                     phone TEXT NOT NULL UNIQUE
                 )''')

# Commit the changes and close the connection
conn.commit()
conn.close()
print("Database and table created successfully!")


# In[2]:


def add_multiple_students():
    # Ask for the number of students to add
    num_students = int(input("How many students do you want to add? "))
    
    # Connect to the database
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # Loop through the number of students
    for _ in range(num_students):
        # Get student details
        name = input("Enter name: ")
        department = input("Enter department: ")
        year = int(input("Enter year: "))
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        
        # Insert student details into the database
        cursor.execute("INSERT INTO students (name, department, year, email, phone) VALUES (?, ?, ?, ?, ?)",
                       (name, department, year, email, phone))
        print(f"Student {name} added successfully!\n")
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


# In[3]:


def view_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    print("Student Records:")
    for row in rows:
        print(row)


# In[5]:


add_multiple_students()


# In[6]:


view_students()


# In[ ]:




