import sqlite3
conn = sqlite3.connect('pets.db')
c = conn.cursor()
while True:
 person_id = input("Please enter a person's ID: ")
 if person_id == -1:
   break
 c.execute("SELECT * FROM person WHERE id=?", (person_id,))
 person = c.fetchone()
 if person is None:
   print("Person not found.")
   continue
 print("{} {} is {} years old.".format(person[1], person[2], person[3]))
 c.execute("SELECT * FROM person_pet WHERE person_id=?", (person_id,))
 person_pets = c.fetchall()
 for person_pet in person_pets:
   pet_id = person_pet[1]
   c.execute("SELECT * FROM pet WHERE id=?", (pet_id,))
   pet = c.fetchone()
   print("{} owned {} a {} that was {} years old.".format(person[1], pet[1], pet[2], pet[3]))
conn.close()
