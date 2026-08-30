
# total schedule time for all acts
def count_total_time(acts):
    toatl_time=0
    for act in acts:
        total_time = total_time + act["minutes"]

# schedle minutes that are still unconfirmed

def unconfirmed_time(acts:list[acts_data])->int:
    unconfirmed_time=0
    for act in acts:
        if act["confirmed"]==False:
            unconfirmed_time = unconfirmed_time + act["minutes"]



