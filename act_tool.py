from dataclasses import dataclass

@dataclass
class acts_data:
    name: str
    stage: str 
    category: str
    minutes: int
    confirmed: bool

acts = [
    {"name": "The Midnight Tacos", "stage": "Main", "category": "music", "minutes": 45, "confirmed": True},
    {"name": "Laser Koala", "stage": "Garden", "category": "dance", "minutes": 30, "confirmed": False},
    {"name": "Quiet Volcano", "stage": "Acoustic", "category": "music", "minutes": 40, "confirmed": True},
    {"name": "Jokes About Bread", "stage": "Main", "category": "comedy", "minutes": 25, "confirmed": False}
]

#display the acts in a formatted table
def acts_format(acts):
    print("\n")
    for act in acts:
        print (f"{act['name']:<20} {act['stage']:<10} {act['category']:<10} {act['minutes']:<5} {act['confirmed']}")
    print("\n")

#add new act to list
def add_act(name,stage,category,minutes,confirmed):
    acts.append({"name":name,"stage":stage,"category":category,"minutes":minutes,"confirmed":confirmed})

#Mark act as confirmed
def confirm_act(confirm_name):
    for act in acts:
        if act['name']==confirm_name:
            act['confirmed'] = True
            print(f"{confirm_name} has been confirmed.")
            return
        else:
            print("Act not found")

#view acts by stage
def view_acts_by_stage(stage):
    for act in acts:
        if act['stage']== stage:
            print(f"{act['name']:<20} {act['category']:<10}{act['minutes']:<5} {act['confirmed']:<5}")

