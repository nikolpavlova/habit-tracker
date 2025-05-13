
import sqlite3

conn = sqlite3.connect("shelter.db")



cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS dogs (
    id INTEGER PRIMARY KEY,       -- Unique ID assigned to each dog (auto-incremented)
    name TEXT,                    -- Name of the dog (e.g., Bella)
    breed TEXT,                   -- Dog's breed (e.g., Labrador)
    color TEXT,                   -- Color of the dog (e.g., golden)
    sex TEXT,                     -- Dog's sex (e.g., Male or Female)
    intake_date TEXT              -- Date the dog arrived at the shelter
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS vaccinations (
    id INTEGER PRIMARY KEY,        -- Unique ID for the vaccine record
    dog_id INTEGER,                -- ID of the dog that received the vaccine
    vaccine_name TEXT,             -- Name of the vaccine (e.g., Rabies)
    date_given TEXT,               -- Date when the vaccine was administered
    FOREIGN KEY(dog_id) REFERENCES dogs(id)  -- Links dog_id to the ID in the dogs table
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS adoptions (
    id INTEGER PRIMARY KEY,        -- Unique ID for the adoption record
    dog_id INTEGER,                -- ID of the adopted dog
    adopter_name TEXT,             -- Name of the person who adopted the dog
    adoption_date TEXT,            -- Date when the adoption took place
    FOREIGN KEY(dog_id) REFERENCES dogs(id)  -- Link dog_id to the 'dogs' table
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS staff (
    id INTEGER PRIMARY KEY,       -- Unique ID for each staff member
    name TEXT,                    -- Staff member's name
    role TEXT,                    -- Their job role (e.g., Vet, Cleaner)
    email TEXT                    -- Contact email
)
''')


cursor.execute("INSERT INTO dogs (name, breed, color, sex, intake_date) VALUES (?, ?, ?, ?, ?)",
               ("Bella", "Labrador", "Golden", "Female", "2024-05-01"))

cursor.execute("INSERT INTO vaccinations (dog_id, vaccine_name, date_given) VALUES (?, ?, ?)",
               (1, "Rabies", "2024-05-02"))

cursor.execute("INSERT INTO adoptions (dog_id, adopter_name, adoption_date) VALUES (?, ?, ?)",
               (1, "Emily Johnson", "2024-05-10"))

cursor.execute("INSERT INTO staff (name, role, email) VALUES (?, ?, ?)",
               ("Dr. Green", "Vet", "dr.green@shelter.org"))

conn.commit()


conn.close()
