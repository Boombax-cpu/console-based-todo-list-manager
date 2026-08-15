#PROJECT_console_based_to-do_list_manager

print("Welcome to the To-Do List Manager!")
To_Do_List = []

#user interface

while True:


    print("\nMenu:")
    print("1. Add a task:")
    print("2. View tasks:")
    print("3. Remove a task:")
    print("4. Exit Task")

    choice = input("Enter your choice (1-4): ")

#Add a task

    if choice == "1":
        task = input("Enter the task you want to add: ")
        To_Do_List.append(task)
        print(f"Task '{task}' added to the list.")




#View tasks

    elif choice == "2":
        if len(To_Do_List) == 0:
            print("No tasks in the list.")

        else:

            print("Your Task List:")
            for task in To_Do_List:
                print(f"- {task}")

            


#Remove a task

    elif choice == "3":
        if len(To_Do_List) == 0:
            print("No task to remove.")
        else:
            print("Your Task List:")
            for index, task in enumerate(To_Do_List, start=1):
                print(f"{index}. {task}")

                task_num = input("Enter the number of the task you want to remove:")
                if task_num.isdigit():
                    task_num = int(task_num)


                    if 1 <= task_num <= len(To_Do_List):
                        removed_task = To_Do_List.pop(task_num - 1)
                        print(f"Task '{removed_task}' is removed from the list successfully")

                    else:
                        print("Invalid task number. Please try again.")
                    


                else:
                    print("Invalid input. Please enter a valid task number.")





#exit from To_Do_LIst

    elif choice == "4":
        print("Exiting the To-Do List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")