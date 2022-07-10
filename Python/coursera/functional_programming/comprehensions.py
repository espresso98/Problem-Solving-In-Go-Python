# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   map_emp = map(mod, employee_list)
   return list(map_emp)

def generate_usernames(mod_list):
   return [item.replace(" ", "_") for item in mod_list]

def map_id_to_initial(employee_list):
   return {item["name"][0]: item["id"]  for item in employee_list}

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")
   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")
   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()
   

"""output
Modified employee list: ['John_Kitchen', 'Paul_House Floor', 'Sarah_Management', 'Lisa_Cold Storage', 'Ryan_Inventory Mgmt', 'Gill_Cashier']
List of usernames: ['John_Kitchen', 'Paul_House_Floor', 'Sarah_Management', 'Lisa_Cold_Storage', 'Ryan_Inventory_Mgmt', 'Gill_Cashier']
Initials and ids: {'J': 12345, 'P': 12456, 'S': 12478, 'L': 12434, 'R': 12483, 'G': 12419}
"""