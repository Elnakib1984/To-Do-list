'''Python to do list'''

'''What do we need in a To - do list????'''


'''
1 - inputting the tasks
2 - deleting the tasks
3 - checking the tasks 
4 - database to track progress and analyze efficiency
'''
'''creating array for tasks'''

tasks = [] # 1 - writing the Array
def addTask(): #Defining function for adding tasks
  task = input("Enter task: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list .")


def listTasks(): #Defining functon for adding tasks
  if not tasks:
    print("There are no tasks currently.")
  else:
    print("Current tasks: ")
    for index, task in enumerate(tasks):
      print(f"Task #{index}. {task}")

def deleteTask(): #Defining function for adding tasks
  listTasks() # Calling listTasks Function

  try:
    taskToDelete = int(input("Enter the # to delete: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed")
    else :
      print(f"Task #{taskToDelete} was not found")

  except:
    print("Invalid input.")





  

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
      listTasks()

    elif(choice == "4"):
      break

    else :
      print("Invalid input. Please try again.")

  print("Goodbye")