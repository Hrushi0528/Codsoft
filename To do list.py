import datetime as dt
import pickle as pk
import colorama as ca

def create():
    if len(to_do_list)==0:
        total_task=int(input("Enter total number of task:"))
        for i in range(total_task):
            task=str(input(ca.Fore.MAGENTA+'Enter {} task:'.format(i+1)+ca.Fore.GREEN))
            to_do_list.append(task)
        print(ca.Fore.RED+'To-Do-List Created Successfully'+ca.Fore.WHITE)
        track_tasks('New List','Created')
        Continue()
    else:
        print(ca.Fore.RED+"To-Do-List already exist.You can't create another list but you can add task by action no 3"+ca.Fore.WHITE)
        Continue()
    
        
def check_list():
    if len(to_do_list)==0:
        yes_no=input(ca.Fore.BLUE+'No list Created yet ! \n  Press  Yes to create list. \n  Press No to exit.'+ca.Fore.GREEN)
        if yes_no.strip().capitalize()=='Yes':
            create()
            Continue()
        elif   yes_no.strip().capitalize()=='No': 
            Continue()
        else:
            print(ca.Fore.RED+'Incorrect Input'+ca.Fore.WHITE)
            Continue()
            
def your_list():
    check_list()
    for index in range(len(to_do_list)):
        print(index+1,str('.'),to_do_list[index],sep='')
    track_tasks('Tasks in your list','Viewed')
    Continue()
            
def track_tasks(task,action):
    time=dt.datetime.now()
    day=time.strftime('%A')
    Tracking.append([task,{action:str(time)+" "+str(day)}])
    
def add_task():
    def add_task():
    new_task=input('Enter your task to add:')
    if new_task in to_do_list:
        print('The Task Already exist in your list:')
    elif new_task=='':
        print("Enter a task.It can't be empty")
    else:
        to_do_list.append(new_task)
        print(ca.Fore.GREEN+'Task Successfully added to your list'+ca.Fore.WHITE)
        track_tasks(new_task,'Added')
    Continue()
  
# need to add code for checking whether the task is present in list or not for deleting of a task.
 
def delete_task():
    for index in range(len(to_do_list)):
        print(index+1,str('.'),to_do_list[index],sep='')
    position=int(input("Enter the position of task you wanted to delete"+ca.Fore.GREEN))
    reason=input('Why are you deleting this task (Completed or Deleted )'+ca.Fore.GREEN)
    track_tasks(to_do_list[position-1],reason)
    print('Task has been removed successfully from your list'+ca.Fore.WHITE)
    to_do_list.pop(position-1)
    Continue()
    
def save():
    with open('to-do-list.txt','wb') as f:
        pk.dump([to_do_list,Tracking],f)
    print(ca.Fore.RED+'File Successfully Saved'+ca.Fore.WHITE)
    Continue()

def Continue():
    choice=input(ca.Fore.MAGENTA+'Do you want to perform actions on list :'+ca.Fore.GREEN)
    if choice.strip().capitalize()=='Yes':actions()
    elif choice.strip().capitalize()=='No':
        print(print(ca.Fore.YELLOW+'Thank you !!'+ca.Fore.WHITE)  )
        exit()
    else:
        print(ca.Fore.YELLOW+'Wrong choice ..Try Again'+ca.Fore.WHITE)   
        Continue()
        
    
def actions():
    print(ca.Fore.RED+"\n\n\t\t\t\tActions")
    print(ca.Fore.YELLOW+" \t1.Create Your list \n \t2.View Your Tasks \n \t3.Add a new Task \n \t4.Delete a Task \n \t5.Track your Task \n \t6.Save \n \t7.Exit")
    choice=int(input(ca.Fore.CYAN+"Enter your choice:"+ca.Fore.GREEN))
    if choice==1:
        create()
    elif choice==2:
        your_list()
    elif choice==3:
        add_task()
    elif choice==4:
        delete_task()
    elif choice==5:
        for tracked in Tracking:
            print(tracked)
        print(ca.Fore.GREEN+'Till date actions performed on your list..'+ca.Fore.WHITE)
        Continue()
    elif choice==6:
        save()
    elif choice==7:
        print(ca.Fore.YELLOW+'Thank you !!'+ca.Fore.WHITE)
        exit()
    else:
        print(ca.Fore.YELLOW+'Wrong choice ..Try Again'+ca.Fore.WHITE)   
        Continue()
        
try:
    with open('to-do-list.txt','rb') as f:
        to_do_list,Tracking=pk.load(f)
except EOFError:
    Tracking,to_do_list=[],[]
actions()




