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

def get_act_inform():
    name = get_error_detect.get_str("Name of act: ")
    stage = get_error_detect.get_str("Stage locate: ")
    category = get_error_detect.get_str("Category of the act: ")
    minutes = get_error_detect.get_minutes()
    confirmed = get_error_detect.get_confirmed()
    return act_tool.add_act_format(name,stage,category,minutes,confirmed)

def run_test():
    act_tool.test_add_act_format()
    act_tool.test_confirmed_act()
    act_tool.test_view_act_by_stage()
    summary_tool.test_count_confirmed_acts()
    summary_tool.test_readiness_message()
    summary_tool.test_count_total_time()
    summary_tool.test_unconfirmed_time()


    
def main():
    choice = ''
    
    while choice !="6":
         print_menu()
         choice =input("Which function do you want to choose:")
         if choice == "1":
            display= act_tool.display_all_acts(acts)
            print (display)
            
         elif choice == "2" :
        
            dict= get_act_inform()
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
             print(summary_tool.summery_message(acts,unconfirmed_time))
         elif choice =="6":
             break
         else:
            print("Option can not be found")
        
            
main()
run_test()