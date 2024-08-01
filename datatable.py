import sqlite3

# Setup: List of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png',
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Create a connection to an SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('file_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table with an auto-increment primary integer field and a string field
cursor.execute('''
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT
)
''')

# Filter the file names to include only those with a '.txt' extension
txt_files = [filename for filename in fileList if filename.endswith('.txt')]

# Insert the filtered file names into the database
for filename in txt_files:
    cursor.execute('INSERT INTO files (filename) VALUES (?)', (filename,))

# Commit the transaction to save the changes
conn.commit()

# Retrieve and print the filenames from the database
cursor.execute('SELECT filename FROM files')
rows = cursor.fetchall()

print("Text files in the database:")
for row in rows:
    print(row[0])

# Close the connection to the database
conn.close()
