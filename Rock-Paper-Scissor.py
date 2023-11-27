import tkinter as tk
from random import choice

def modify_entry():
    user_input.delete(0,tk.END)
    user_input.insert(0,'')
    
def close_game():
    interface.destroy()
    message.destroy()
    
def restart_game():
    interface.destroy()
    message.destroy()
    main()
       
def game_evaluation():
    computer_value=choice(['Rock','Paper','Scissor'])
    Computer_input['text']=computer_value
    user_value,point,chance=user_input.get(),int(points_index['text']),int(chances_index['text'])
    user_value=user_value.strip().capitalize()
    if user_value in ['Rock','Paper','Scissor']:
        Computer_label['text']='Computer-Input : '
        if computer_value==user_value:
            plays['text']='Since both you and computer has chosen same'
            winner['text']="It's a tie"
            interface.after(1000,modify_entry)
        else:
            cases=[['Paper','Rock'],['Rock','Scissor'],['Scissor','Paper']]
            plays['text']='Since you selected {} & Computer Selected {}'.format(user_value,computer_value)
            for case in cases:
                if user_value in case and computer_value in case:
                    if case[0]==user_value:
                        winner['text']='Congratulations ! You are the Winner.'
                        point+=1
                        points_index['text']=str(point)
                    else:
                        winner['text']='Sorry ! Computer is the Winner.'
                        chance-=1
                        chances_index['text']=str(chance)
                    break
            if chance==0:
                global message
                
                message=tk.Tk()
                message.title('Are you sure..')
                message.geometry('1100x300')
                message.configure(bg='black')
                answer=tk.Label(message,text='Sorry ! Your Chances are over .Do you want to play Again',fg='white',bg='black',font=('Helvetica bold', 18 ,'italic'))
                answer.grid(columnspan=2,row=1,padx=200,pady=50,rowspan=2)
                yes=tk.Button(message,text='Yes',font=('Helvetica bold', 16 ,'italic'),bg='Green',command=restart_game).grid(row=3,column=0,pady=50,padx=80)
                no=tk.Button(message,text='No',font=('Helvetica bold', 16 ,'italic'),bg='red',command=close_game).grid(row=3,column=1)
                
                tk.mainloop()
        interface.after(1000,modify_entry)
    elif user_value=='':
        plays['text']="This field can't be empty"
        winner['text'],Computer_input['text']='',''
    else:
        plays['text']='You have entered irrelevant input in the game'
        winner['text']='Please! Try Again'
        interface.after(1500,modify_entry)
        
def main():    
    global winner,interface,user_points,user_chances,space,name,user_label,user_input,points_label,play,points_index,Computer_label,Computer_input,chances_index,chances_label,plays  
    
    interface=tk.Tk()
    interface.title('Rock-Paper-Scissor Game')
    interface.geometry('1100x550')
    interface.configure(bg='cyan')
    user_points,user_chances=0,3
    space=tk.Label(interface,text='',bg='cyan').grid(row=0,column=0,pady=20)
    name=tk.Label(interface,text='Rock-Paper-Scissor',font=('Helvetica bold', 18 ,'italic'),bg='cyan').grid(row=0,column=1)
    user_label=tk.Label(interface,text='User-Input : ',font=('Helvetica bold', 18 ,'italic'),bg='cyan').grid(row=1,column=0,pady=10)
    user_input=tk.Entry(interface,font=('Times new Roman', 18 ,'bold'),bg='white',width=20)
    user_input.grid(row=1,column=1)
    points_label=tk.Label(interface,text='Points',font=('Times new Roman', 24 ,'bold'),bg='cyan').grid(pady=10,row=1,column=2,padx=100)
    play=tk.Button(interface,text='Play',font=('Times new Roman', 14),width=10,command=game_evaluation).grid(row=2,column=1,pady=5)
    points_index=tk.Label(interface,text=str(user_points),font=('Helvetica bold', 24 ,'italic'),bg='cyan',fg='orange')
    points_index.grid(row=2,column=2)
    Computer_label=tk.Label(interface,text='',font=('Helvetica bold', 18 ,'italic'),bg='cyan')
    Computer_label.grid(row=3,column=0,padx=20,pady=10)
    Computer_input=tk.Label(interface,text='',font=('Times new Roman', 18 ,'bold'),bg='cyan',fg='purple',width=25)
    Computer_input.grid(row=3,column=1,pady=0)
    chances_label=tk.Label(interface,text='Remaining chances',font=('Times new Roman', 24 ,'bold'),bg='cyan').grid(pady=20,row=3,column=2)
    plays=tk.Label(interface,text='',font=('Helvetica bold', 18,'bold'),bg='cyan')
    plays.grid(row=5,column=1,pady=20)
    chances_index=tk.Label(interface,text=str(user_chances),font=('Helvetica bold', 24 ,'italic'),bg='cyan',fg='red')
    chances_index.grid(row=4,column=2)
    winner=tk.Label(interface,text='',font=('Helvetica bold', 18,'bold'),bg='cyan',fg='salmon')
    winner.grid(row=6,column=1,padx=10)
    interface.mainloop()
    
main()
