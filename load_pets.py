import sqlite3

# Connect to the database
conn = sqlite3.connect('pets.db')
c = conn.cursor()

while True:
    # Ask user for person's ID number
    person_id = int(input("Enter person's ID number (-1 to exit): "))

    # Check if user wants to exit
    if person_id == -1:
        break

    # Query person's data
    c.execute("SELECT first_name, last_name, age FROM person WHERE id=?", (person_id,))
    person_data = c.fetchone()

    # If person exists, print their data
    if person_data:
        print(f"{person_data[0]} {person_data[1]}, {person_data[2]} years old")

        # Query and print person's pets
        c.execute("SELECT pet.name, pet.breed, pet.age FROM pet JOIN person_pet ON pet.id = person_pet.pet_id WHERE person_pet.person_id=?", (person_id,))
        pets_data = c.fetchall()
        for pet in pets_data:
            print(f"Owned {pet[0]}, a {pet[1]}, that is {pet[2]} years old")
    else:
        print("Person not found.")

# Close connection
conn.close()

