import sqlite3

# Create an in-memory database and establish a connection
connection = sqlite3.connect(':memory:')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# 1. Create the Roster table
cursor.execute('''
CREATE TABLE Roster (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Species TEXT,
    IQ INTEGER
)
''')

# 2. Populate the table with values
cursor.executemany('''
INSERT INTO Roster (ID, Name, Species, IQ) VALUES (?, ?, ?, ?)
''', [
    (1, 'Jean-Baptiste Zorg', 'Human', 122),
    (2, 'Korben Dallas', 'Meat Popsicle', 100),
    (3, 'Ak\'not', 'Mangalore', -5)
])

# 3. Update the Species of Korben Dallas to be Human
cursor.execute('''
UPDATE Roster
SET Species = 'Human'
WHERE Name = 'Korben Dallas'
''')

# 4. Display the names and IQs of everyone classified as Human
cursor.execute('''
SELECT Name, IQ
FROM Roster
WHERE Species = 'Human'
''')

# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
connection.close()
