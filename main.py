'''Python to do list'''

'''What do we need in a To - do list????'''


'''
1 - inputting the tasks
2 - deleting the tasks
3 - checking the tasks 
4 - database to track progress and analyze efficiency
'''
'''creating array for tasks'''
tasks = [] 
def addTask():
  task = input("Enter task: ")
  tasks.append(task)
  print("Task added.")
  

if __name__ == "__main__" :
  ### create a loop to run the app
  print("Welcome to the to so list app :")

  while True :
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")

    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")


    choice = input("Enter your Choice: ")

    if(choice == "1"):
      addTask()
    
    elif(choice == "2"):
      deleteTask()

    elif(choice == "3"):
      ListTasks()

    elif(choice == "4"):
      break

    else :
      print("Invalid input. Please try again.")

  print("Goodbye")
      
    
