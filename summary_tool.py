
# total schedule time for all acts
def count_total_time(acts):
    total_time=0
    for act in acts:
        total_time = total_time + act["minutes"]
    return(total_time)

# schedle minutes that are still unconfirmed

def unconfirmed_time(acts:list[dict])->int:
    unconfirmed_minutes=0
    for act in acts:
        if act["confirmed"]== False:
            unconfirmed_minutes = unconfirmed_minutes + act["minutes"]
    return (unconfirmed_minutes)

# count confirmed acts
def count_confirmed_acts(acts:list[dict])->int:
    confirmed_acts=0
    for act in acts:
        if act["confirmed"]==True:
            confirmed_acts = confirmed_acts + 1
    return(confirmed_acts)

# Readiness message for summary
def readiness_message(unconfirmed_minutes:int)->str:
    if unconfirmed_minutes == 0:
        return "Festival line-up is confirmed."
    elif unconfirmed_minutes>=1 and unconfirmed_minutes <=60:
        return "Almost ready."
    elif unconfirmed_minutes>=60 and unconfirmed_minutes <=180:
        return "Several acts still need confirmation."
    else:
        return "unconfirmed_minutes"
    
def summery_message(acts,unconfirmed_time):
    return (f"The total schedule time is {count_total_time(acts)} minutes\n" 
           f"{count_confirmed_acts(acts)} acts has confirmed\n"
           f"Unconfirmed time {unconfirmed_time} minutes \n"
           f"{readiness_message(unconfirmed_time)}")

# ------------test--------

test_acts=[{"name":"Band A","stage":"Main","category":"Music","minutes":30, "confirmed":False},
           {"name":"Dance crow","stage":"Garden","category":"Dance","minutes":50, "confirmed":True}
]

def check_equal(description, actual, expected):
    if actual == expected:
        print("PASS", description)
    else:
        print("FAIL", description, "expected", expected, "got", actual)

def test_count_total_time():
    check_equal("total time of acts",count_total_time(test_acts),80)
    
def test_unconfirmed_time():
    check_equal("check unconfirmed time",unconfirmed_time(test_acts),30)

def test_count_confirmed_acts():
    check_equal("check amount of confirmed acts",count_confiremed_acts(test_acts),1)

def test_readiness_message():
    check_equal("check readiness message",readiness_message(70),"Several acts still need confirmation.")