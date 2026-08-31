
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


def count_confiremed_acts(acts:list[dict])->int:
    confiremed_acts=0
    for act in acts:
        if act["confirmed"]==True:
            confiremed_acts = confiremed_acts + 1
    return(confiremed_acts)

def readiness_message(unconfirmed_minutes:int)->str:
    if unconfirmed_minutes == 0:
        return "Festival line-up is confirmed."
    elif unconfirmed_minutes>=1 and unconfirmed_minutes <=60:
        return "Almost ready."
    elif unconfirmed_minutes>=60 and unconfirmed_minutes <=180:
        return "Several acts still need confirmation."
    else:
        return "unconfirmed_minutes"