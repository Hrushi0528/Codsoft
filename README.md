# CODSOFT Internship

This repository contain Python code for the Tasks given by the codsoft team in the process of Internship.As part of my internship i implemented the following code as per my Knowledge.This repo contains Three projects namely:
<br>&emsp;&emsp;&emsp;<b>1.To-do-list
<br>&emsp;&emsp;&emsp;2.Rock-Paper-Scissor
<br>&emsp;&emsp;&emsp;3.Random Password Generator</b><br><br>

<b>1.To-do-list.py</b>
&emsp;&emsp;&emsp;<b>To execute this program correctly file with to_do_list.txt should exist.</b><br>
&emsp;&emsp;&emsp;It is command line interface.Mainly contains of
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<u><b>i.Creating a new list:</b></u>
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;When a list is empty we can create a new list with number of tasks.This Option is only available when the list is empty.By this Option we create a new to-do-list.This action will be tracked.
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>ii.View your list:</b><br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;You can view your tasks by this option.You can only view the total number of tasks in your list.This action will be tracked.
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>iii.Adding a task:</b><br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;You can add a new task by this option.If you add a duplicate of existing task in list it shows a message that already this task exist in your list.When you add a task in list the action will be tracked.
              <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>iv.Deleting a task:</b><br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;You can delete any task present in your list.If your enter task is not present in list it shows the task does not exist in list.If you wanted to delete existing task then it asks why are deleting this task either completed or deleted.This action will be tracked with the value of either completed or deleted.
              <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>v.Tracking of the list:</b><br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Now-a-days history of any documents and resource is very useful.so this option enable user to check the option applied on the last.It consist of action and date on which the corresponding action is applied.
        <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>vi.Save:</b>   
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;This option will save the option and actions applied on the list.It only saves when you perform this action only other no changes were made.For tracking previous actions applied on list the list of actions and tracked data will store as a file in a local directory and this will be used at the Running of the program.Pickling Concept is used to save and read file.
              <br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>vii.Exit:</b><br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;This option simply exit from the command line interface with a message Thankyou! .


<br><hr><br>
<b>2.Rock-Paper-Scissor</b>
<br><br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;It is GUI based game.User can give any input from Rock,Paper & Scissor.If user input is empty or any other not from Rock,paper,scissor It shows an alert as Invalid input.Rock,paper,scissor can be lowercase,uppercase or combination of lower&upper.Game result can be a tie,win or loss.Computer select randomly from rock,paper,scissor.user-input is Compared with computer selected value.Game evaluation can be done by
<br>
<br><b>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;i.Rock wins over Scissor if both are Compared.
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ii.Paper wins over Rock if both are Compared.
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iii.Scissor wins over Paper if both are Compared.
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iv.It's a tie when both user&computer selects same.</b><br>
<br>&emsp;&emsp;&emsp;&emsp;The Evaluation is also mentioned below the Computer-input.Based on that either computer or user will get a point.For each point got by the user number of points will be incremented by 1 and Points earned by the user shown at top of left side.
For each loss by the user number of chances will be decremented by 1 and Remaining chances for the user shown at top of left side.For tie either points or remaining chances will not be effected.Maximum Chances for user is 3.
<br><br>&emsp;&emsp;&emsp;&emsp;If remaining chances is 0 then the current game is stopped and a pop up window will be displayed.Pop-up as <b> Sorry ! Your Chances are over .Do you want to play Again</b> with 2 options i.Yes ii.No.If <b>Yes</b> is clicked then the game will be refreshed and you can play a new game.If <b>No</b> is clicked then the game will be terminated as interface will destroy.

<br><hr><br>
<b>3.Random password generator</b>
<br><br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;The Idea of generating random password is pretty simple. But to Implement it in the form GUI is a bit complex task.Generally password are classified into weak,Strong and very strong passwords.A password can contain lowercase,uppercase ,numbers and special Characters.
In this project 1100x400 dimensions interface is cretaed.In this interface there are some major components.They are:
<br>
<br><b>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;i.4 Labels
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ii.1 Entry field 
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iii.1 Button</b>
<br><br>&emsp;&emsp;&emsp;&emsp;Entry Field takes the size of the required password.The input must be between 8 and 25 inclusive.At the first time the '<b> Refresh '</b> button is hidden.After the valid length given automatically password is generated.After generating the password The '<b> Refresh </b>' button will be available .User did not like the password generated he/her can be genearted another password by clicking the Refresh Button.
<br><br>&emsp;&emsp;&emsp;&emsp;<b>Merits:</b>
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;i.Can generate strong to very strong passwords
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ii.Flexibility in choosing password.
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iii.Combination of lowercase,uppercase,numbers and symbols makes the project more secure.
<br><br>&emsp;&emsp;&emsp;&emsp;<b>Demerits:</b>
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;i.Can't Select the generated password.
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ii.Below average in generating long passwords.
<br><hr><br>
<b>ScreenShots:
<br>
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1.To-do-list <br><br>
![image](https://github.com/user-attachments/assets/62230acc-91dc-4b5a-a261-ffe83f0fbea1)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;a.Overview of To-do-list<br><br>
![image](https://github.com/user-attachments/assets/51835182-3e01-4d6c-bdb8-1c18bc351707)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;b.Creating a new List<br><br>
![image](https://github.com/user-attachments/assets/f46d8fe8-0f45-4614-8343-e509b8fa0c6c)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;c.Viewing the to-do-list<br><br>
![image](https://github.com/user-attachments/assets/ec19640e-e76b-4aef-8462-3431f4ab6cab)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;d.Adding a task in to-do-list<br><br>
![image](https://github.com/user-attachments/assets/0018a4c6-1163-4565-a87c-378cb4942262)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;e.After Adding a task in to-do-list<br><br>
![image](https://github.com/user-attachments/assets/309aec8b-b426-4188-9f16-73f891c8d86b)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;f.Deleting a task in to-do-list<br><br>
![image](https://github.com/user-attachments/assets/d3c009ce-d9e8-4344-9862-663295d54c8d)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;g.After Deleting a task in to-do-list<br><br>
![image](https://github.com/user-attachments/assets/c59af187-b867-464f-b37b-25bb60415a4d)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;h.Tracking the actions performed on to-do-list<br><br>
![image](https://github.com/user-attachments/assets/ab7f26da-8d7b-4cf1-81e2-989f6f770e96)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;i.Saving the to-do-list<br><br>
![image](https://github.com/user-attachments/assets/8f69eebc-0494-49d3-86e3-331afd3780e9)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;j.Exiting the to-do-list<br><br>

<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2.Rock-Paper-Scissor<br><br>
![image](https://github.com/user-attachments/assets/46fcee0c-77aa-473f-b306-04b6750088af)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;a.Overview of the interface<br><br>
![image](https://github.com/user-attachments/assets/50c3ab10-f3d6-4554-8600-c58795801049)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;b.Player wins a point<br><br>
![image](https://github.com/user-attachments/assets/6fb00b29-81a4-4fee-beb5-71da30272a30)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;c.Tie Break<br><br>
![image](https://github.com/user-attachments/assets/8c9ef962-a35f-4790-87d7-f21dd40f5225)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;d.Player Lose a point as well as chance<br><br>
![image](https://github.com/user-attachments/assets/59459095-6e72-4a2e-b1d3-c8a3f1f25d77)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;e.All chances runned out<br><br>
![image](https://github.com/user-attachments/assets/4b956a51-c3b7-4766-9ad6-6b26ed1727ec)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;f.Want to play again<br><br>
![image](https://github.com/user-attachments/assets/68695389-afb1-4921-970c-a6b57412b188)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;g.After selecting yes the game restarts<br><br>

<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;3.Random Password generator<br><br>
![image](https://github.com/user-attachments/assets/203376e5-aa00-471d-aa1d-01014437b064)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;a.Overview of Random Password generator<br><br>
![image](https://github.com/user-attachments/assets/bd07579c-2e35-4bc0-a22a-bca4cc857896)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;b.After generating password<br><br>
![image](https://github.com/user-attachments/assets/de919391-8be7-4e11-81b6-c1aecd8869f3)
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;c.After refreshing the generating password<br><br>

<hr>
Work done by:<br>
<b>Hrushikesh Dodla
<br>email:dodlahrushikesh5683@gmail.com







