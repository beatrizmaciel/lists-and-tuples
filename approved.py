approved = [
    "João Silva", "Maria Garcia", "Ahmed Ali", "Sophie Martin", 
    "Li Wei Chen", "Alejandro Lopez", "Priya Patel", "Yuri Ivanov", 
    "Fatima Al-Mansouri", "Diego Fernandez", "Hans Schmidt", 
    "Sakura Yamamoto", "Amir Khan", "Ingrid Olsen", "Isabella Rossi"
]

available_positions = 5

print("The total approved is: ", len(approved), " people.")

print("The first substitute is: ", approved[available_positions])

admitted = approved[0:available_positions] # excluding available_positions
# we can also change the sintax and use » admitted = approved[:available_positions]

print("Admitted: ", admitted)

substitutes = approved[available_positions:len(approved)]
# we can also change the sintax and use » substitutes = approved[available_positions:]

print("Substitutes: ", substitutes)

print("The last placed was: ", approved[len(approved) - 1])