import act_tool
import summary_tool
import get_error_detect
acts = act_tool.start_acts()
def print_menu():
    print()
    print("Festival Planner Menu:")
    print("1. List all acts")
    print("2. Add a new act")
    print("3. Mark an existing act as confirmed")
    print ("4.List acts for one stage")
    print("5. List festival summary")
    print("6. Quit")

def main():
    choice = ''
    
    while choice !="6":
         print_menu()
         choice =input("Which function do you want to choose:")
         if choice == "1":
            display= act_tool.display_all_acts(acts)
            print (display)
            
        
         elif choice == "2" :
            name = get_error_detect.get_str("Name of act: ")
            stage = get_error_detect.get_str("Stage locate: ")
            category = get_error_detect.get_str("Category of the act: ")
            minutes = get_error_detect.get_minutes()
            confirmed = get_error_detect.get_confirmed()
            dict= act_tool.add_act_format(acts,name,stage,category,minutes,confirmed)
            acts.append(dict)
            
         elif choice == "3":
            act_choice= get_error_detect.get_str("Which act do you want to mark as confirmed:")
            confirm_message = act_tool.confirm_act(acts, act_choice)
            print (confirm_message)
        
            
         elif choice == "4":
             stage_choice = get_error_detect.get_str ("Stage that you want to list: ")
             print(act_tool.view_acts_by_stage(acts,stage_choice))
             
         elif choice == "5":
             print("\n")
             unconfirmed_time = summary_tool.unconfirmed_time(acts)
             print(f"The total schedule time is {summary_tool.count_total_time(acts)} minutes\n" 
                   f"{summary_tool.count_confiremed_acts(acts)} acts has confirmed\n"
                   f"Unconfirmed time {unconfirmed_time} minutes \n"
                   f"{summary_tool.readiness_message(unconfirmed_time)}")
         elif choice =="6":
             break
         else:
            print("Option can not be found")
        
            
main()