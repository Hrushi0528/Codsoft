# CODSOFT

This repository contain Python code for the Tasks given by the codsoft team in the process of Internship.

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


