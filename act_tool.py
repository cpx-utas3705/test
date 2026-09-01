def start_acts()->list[dict]:
    return[
    {"name": "The Midnight Tacos", "stage": "Main", "category": "music", "minutes": 45, "confirmed": True},
    {"name": "Laser Koala", "stage": "Garden", "category": "dance", "minutes": 30, "confirmed": False},
    {"name": "Quiet Volcano", "stage": "Acoustic", "category": "music", "minutes": 40, "confirmed": True},
    {"name": "Jokes About Bread", "stage": "Main", "category": "comedy", "minutes": 25, "confirmed": False}
    ]

#display the acts in a formatted table
def display_all_acts(acts:list[dict])->str:
    result=""
    for act in acts:
        result+= f"{act['name']:<20} {act['stage']:<10} {act['category']:<10} {act['minutes']:<5} {act['confirmed']}\n"
    return result 

#add new act to list
def add_act_format(name,stage,category,minutes,confirmed):
    dict_format= {"name":name,"stage":stage,"category":category,"minutes":minutes,"confirmed":confirmed}
    return dict_format 

#Mark act as confirmed
def confirm_act(acts:list[dict],confirm_name:str)->str:
    found = False
    for act in acts:
        if act['name']==confirm_name:
            act["confirmed"] = True
            return f"{confirm_name} has been confirmed."
            found = True
    if found == False :
        return "Act not found."

        
#view acts by stage
def view_acts_by_stage(acts:list[dict],stage:str)->str:
    list=""
    for act in acts:
        if act['stage']== stage:
            list += f"{act['name']:<20} {act['category']:<10}{act['minutes']:<5} {act['confirmed']:<5}\n"  
            return list
    if list=='':
        return "Stage not found"
        
"""   Test       """

def check_equal(description, actual, expected):
    if actual == expected:
        print("PASS", description)
    else:
        print("FAIL", description, "expected", expected, "got", actual)

def test_add_act_format():
    expect={"name":"Band A","stage":"Main","category":"Music","minutes":30, "confirmed":False}
    check_equal("format add act",add_act_format("Band A","Main","Music",30,False),expect)
    
def test_confirmed_act():
    test_act=[{"name":"Band A","stage":"Main","category":"Music","minutes":30, "confirmed":False}]
    confirm_act(test_act, "Band A")
    check_equal("test if the act has confirmed",test_act[0]["confirmed"],True)

def test_view_act_by_stage():
    test_acts=[{"name":"Band A","stage":"Main","category":"Music","minutes":30, "confirmed":False}]
    check_equal("vies by stage",view_acts_by_stage(test_acts,"Garden"),"Stage not found")
    
