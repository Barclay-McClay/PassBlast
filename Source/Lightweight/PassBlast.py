import time
from pynput.keyboard import Controller
import tkinter as tk

# Initialize the Controller
keyboard = Controller()

#################################################################################################################################

def countdown(n):
    n = int(n)
    while n > 0:
        lbCountdown.configure(text=str(n))
        root.update()
        time.sleep(1)
        n -= 1

def type_string(s):
    for char in s:
        keyboard.type(char)
        time.sleep(0.05)  # Delay between each character (can be removed for instant text)

def blast_pass(index,timer):
    user_input = BLASTERS[index]['wBlastField'].get()
    lbCountdown.configure(text="Starting countdown...",fg='red')
    for blst in BLASTERS:
        blst['wBlastField'].config(state='disabled')
        blst['bStart'].config(state='disabled')
    root.update()
    countdown(timer) # countdown to get your cursor in the right spot
    lbCountdown.configure(text="Typing...",fg='yellow')
    root.update()
    type_string(user_input)
    lbCountdown.configure(text="Done!",fg='green')
    for blst in BLASTERS:
        blst['wBlastField'].config(state='normal')
        blst['bStart'].config(state='normal')
    root.update()

def add_blaster(frBlasters):
    blst = {}
    i = len(BLASTERS)
    blst['index'] = i
    blst['wBlastField'] = tk.Entry(frBlasters,width=40)
    blst['bStart'] = tk.Button(frBlasters, text='Blast!', relief='raised', command=lambda: blast_pass(i,varCount.get()))
    # Grid
    blst['wBlastField'].grid(row=0+i,column=0)
    blst['bStart'].grid(row=0+i,column=1)
    BLASTERS.append(blst)

def remove_blaster():
    i = len(BLASTERS)
    i -= 1
    blst = BLASTERS.pop(i)
    blst['wBlastField'].destroy()
    blst['bStart'].destroy()
####################################################################################################################################

BLASTERS = []

# CREATE ROOT WINDOW
root = tk.Tk()
root.title("PassBlast 😎")

# FRAMES
frTimer = tk.Frame(root)
frBlasters = tk.Frame(root)
frAddRemove = tk.Frame(root)

## CREATE WIDGETS
# Timer
lbTimer = tk.Label(frTimer, text='Coundown timer length:')
numbers = [str(x) for x in range(1, 11)]
varCount = tk.StringVar(value="3")
wTimerSelect = tk.OptionMenu(frTimer,varCount,*numbers)
wTimerSelect.configure(relief='flat')
# Blasters
add_blaster(frBlasters)
add_blaster(frBlasters)
lbCountdown = tk.Label(root, text='Ready to PassBlast')

lbAddRemove = tk.Label(frAddRemove,text="Add/Remove Fields:")
wAddBlaster = tk.Button(frAddRemove,text="➕",relief='flat',command=lambda: add_blaster(frBlasters))
wRemoveBlaster = tk.Button(frAddRemove,text="➖",relief='flat',command=lambda: remove_blaster())

## LAYOUT
# Frames
frAddRemove.grid(row=0,column=0)
frTimer.grid(row=1,column=0)
lbCountdown.grid(row=2,column=0)
frBlasters.grid(row=3,column=0)

# Add/Remove
lbAddRemove.grid(row=0,column=0)
wAddBlaster.grid(row=0,column=1)
wRemoveBlaster.grid(row=0,column=2)

# Timer Select
lbTimer.grid(row=0,column=0)
wTimerSelect.grid(row=0,column=1)



#### MAIN LOOP ###
root.mainloop()
"""
                                                                                                                         
                                                                                                                         
                  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&         &&&&&&@         &&&&&&&&&&&&&&&&&&&&&&&&&&&&&                   
  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&    &&&&&&&&&&&       &&&&&&&@@        &&&&&&&&&      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  
    &&&&&&&&&&&&&&&&&&&&    &&&&&&&&&&  &&&&&&&&&       &&&&&&&@@       &&&&&&&&   &&&&&&&&&&    &&&&&&&&&&&&&&&&&&&&    
                  &&&&&&&&&&&&&&   &&&&&& &&&&&&&&&       && @@       &&&&&&&&& &&&&&    &&&&&&&&&&&&&&                  
        &&&&&&&&&&&&&&&&&&&  &&&&&&&&  &&&& && &&&&&&&&    & @    &&&&&&&&.&& &&&&  &&&&&&&    &&&&&&&&&&&&&&&&&&        
         &&&&&&&&&&&    &&&&&&&&&&  &&&&  &&&              & @              &&&  &&&&  &&&&&&&&&      &&&&&&&&&&         
                  &&&&&&&&&&&&   &&&&&   &&    %&&&&&&&    & @    &&&&&&&%   &&&&  &&&&&   &&&&&&&&&&&&                  
                  &&&&&&&    &&&&&&&  &&&&   &&&&&&&&&&&&# & @ #&&&&&&&&&&&    &&&&  &&&&&&     &&&&&&&                  
                          &&&&&&&   &&&&&   &&&&&          & @          &&&&&   &&&&&   &&&&&&&                          
                                  &&&&&     &&&&           & @           &&&&     &&&&&                                  
                                            &&&&&&         & @         &&&&&&                                            
                                             *&&&&&&&      & @      &&&&&&&*                                             
                                                &&&&&&&&&& & @ &&&&&&&&&&                                                
                                                    &&&&&&&&&@&&&&&
                                                   &&&&    & @&&&&&&&&                                                   
                                                 &&&&&     & @     &&&&&                                                 
                                                 &&&&&&    & @    &&&&&                                                  
                                                   &&&&&&&&&&@  &&&&                                                     
                                                        &&&&&&&&&&&&                                                     
                                                    &&&&&  & @  &&&&&                                                    
                                                   &&&&&&  & @   &&&&                                                    
                                                     &&&&&&&&&&&&&&&                                                     
                                                      &&&&   @ &&&&                                                      
                                                       &&&&& @ &&&&
                                                        &&&& &&&&&
                                                         &&& @&&&
                                                         &&& &&&
                                                          && &&
                                                          % @ %
                                                            @
                                                            @
                                                            @

Barclay McClay
"""