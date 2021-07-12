from tkinter import *
from tkinter.messagebox import showinfo
master=Tk()

y=""
x=2
player_1=[]
player_2=[]

def press(num):
    global x,y
    global player_1,player_2
    from itertools import permutations
    set1=permutations([1,2,3])
    set2=permutations([1,4,7])
    set3=permutations([1,5,9])
    set4=permutations([2,5,8])
    set5=permutations([3,6,9])
    set6=permutations([3,5,7])
    set7=permutations([4,5,6])
    set8=permutations([7,8,9])
    
    for i in set1,set2,set3,set4,set5,set6,set7,set8:
        for j in list(i):
            plyr_1=all(ele in player_1 for ele in j)
            plyr_2=all(ele in player_2 for ele in j)
            
            if plyr_1==True:
                print("player_1 wins")
                showinfo('game result','player_1 has won')
                break
                
            elif plyr_2==True:
                print("player_2 wins")
                showinfo('game result','player_2 has won')
                break
                
            else:
                pass
    
    
    if num==1:
        if x%2==0:
            y="X"
            player_1.append(num)
            print(player_1)
            
        else:
            y="O"
            player_2.append(num)
            print(player_2)
            
        b1.config(text=y)
        x=x+1
        
    if num==2:
        if x%2==0:
            y="X"
            player_1.append(num)
            print(player_1)
            
        else:
            y="O"
            player_2.append(num)
            print(player_2)
            
        b2.config(text=y)
        x=x+1
    
    if num==3:
        if x%2==0:
            y="X"
            player_1.append(num)
            print(player_1)
            
        else:
            y="O"
            player_2.append(num)
            print(player_2)
            
        b3.config(text=y)
        x=x+1
        
    if num==4:
        if x%2==0:
            y="X"
            player_1.append(num)
            print(player_1)
            
        else:
            y="O"
            player_2.append(num)
            print(player_2)
            
        b4.config(text=y)
        x=x+1
        
    if num==5:
        if x%2==0:
            y="X"
            player_1.append(num)
            print(player_1)
            
        else:
            y="O"
            player_2.append(num)
            print(player_2)
            
        b5.config(text=y)
        x=x+1
        
    if num==6:
        if x%2==0:
            y="X"
            player_1.append(num)
            print(player_1)
            
        else:
            y="O"
            player_2.append(num)
            print(player_2)
            
        b6.config(text=y)
        x=x+1
        
    if num==7:
        if x%2==0:
            y="X"
            player_1.append(num)
            print(player_1)
            
        else:
            y="O"
            player_2.append(num)
            print(player_2)
            
        b7.config(text=y)
        x=x+1
        
    if num==8:
        if x%2==0:
            y="X"
            player_1.append(num)
            print(player_1)
            
        else:
            y="O"
            player_2.append(num)
            print(player_2)
            
        b8.config(text=y)
        x=x+1
        
    if num==9:
        if x%2==0:
            y="X"
            player_1.append(num)
            print(player_1)
            
        else:
            y="O"
            player_2.append(num)
            print(player_2)
            
        b9.config(text=y)
        x=x+1
        

l3=Label(master,text="TIC TAC TOE ",font="times 15",bg="gray")
l3.grid(row=0,column=2)

l1=Label(master,text="Player 1 : X ",font="times 15",bg="red")
l1.grid(row=1,column=1)

l2=Label(master,text="Player 2 : O ",font="times 15",bg="cyan")
l2.grid(row=1,column=3)

b1=Button(master,width=20,height=10,bg="gray",command=lambda:press(1))
b1.grid(row=2,column=1)

b2=Button(master,width=20,height=10,bg="white",command=lambda:press(2))
b2.grid(row=2,column=2)

b3=Button(master,width=20,height=10,bg="gray",command=lambda:press(3))
b3.grid(row=2,column=3)

b4=Button(master,width=20,height=10,bg="white",command=lambda:press(4))
b4.grid(row=3,column=1)

b5=Button(master,width=20,height=10,bg="gray",command=lambda:press(5))
b5.grid(row=3,column=2)

b6=Button(master,width=20,height=10,bg="white",command=lambda:press(6))
b6.grid(row=3,column=3)

b7=Button(master,width=20,height=10,bg="gray",command=lambda:press(7))
b7.grid(row=4,column=1)

b8=Button(master,width=20,height=10,bg="white",command=lambda:press(8))
b8.grid(row=4,column=2)

b9=Button(master,width=20,height=10,bg="gray",command=lambda:press(9))
b9.grid(row=4,column=3)

mainloop()