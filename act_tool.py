acts = [
    {"name": "The Midnight Tacos", "stage": "Main", "category": "music", "minutes": 45, "confirmed": True},
    {"name": "Laser Koala", "stage": "Garden", "category": "dance", "minutes": 30, "confirmed": False},
    {"name": "Quiet Volcano", "stage": "Acoustic", "category": "music", "minutes": 40, "confirmed": True},
    {"name": "Jokes About Bread", "stage": "Main", "category": "comedy", "minutes": 25, "confirmed": False}
]


def acts_format(acts):
formatted_acts = []
    for act in acts:
        formatted_act = f"{act['name']} - {act['stage']} - {act['category']} - {act['minutes']} minutes - {'Confirmed' if act['confirmed'] else 'Not Confirmed'}"
        formatted_acts.append(formatted_act)
   print(formatted_acts) 