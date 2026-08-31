def get_minutes() ->int:
    while True:
        try:
            minutes = int(input("Enter minutes:"))
            if minutes<0:
                print("Minutes cannot be negative.")
            else:
                return minutes
            
        except ValueError:
            print ("Please enter a valid integer")

def get_str(messege:str)->str:
    while True:
        value = input(messege).strip()
        
        if value =="":
            print("Can not be empty")
        else:
            return value
        
def get_confirmed()->bool:
    while True:
        confirmed = input("Has this act confirmed?(Yes/No)").lower().strip()
        if confirmed == "yes":
            return True
        elif confirmed == "no":
            return False
        else:
            print("Yes or No only")
        