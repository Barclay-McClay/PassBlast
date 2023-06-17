import time
from pynput.keyboard import Controller
import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# Initialize the Controller
keyboard = Controller()

#################################################################################################################################

def countdown(n):
    while n > 0:
        countdown_label.configure(text=str(n))
        root.update()
        time.sleep(1)
        n -= 1

def type_string(s):
    for char in s:
        keyboard.type(char)
        time.sleep(0.05)  # Delay between each character (can be removed for instant text)

def start_typing():
    user_input = entry_field.get()
    countdown_label.configure(text="Starting countdown...",text_color='red')
    root.update()
    countdown(3) # 3-second countdown to get your cursor in the right spot
    countdown_label.configure(text="Typing...",text_color='yellow')
    root.update()
    type_string(user_input)
    countdown_label.configure(text="Done!",text_color='green')
    root.update()

####################################################################################################################################

# Create app window
root = ctk.CTk()
root.title("PassBlast 😎")
root.geometry("400x110")

# Create Widgets
lbTop=ctk.CTkLabel(root, text='String to type:')
entry_field = ctk.CTkEntry(root,width=300)
bStart = ctk.CTkButton(root, text='Blast pass!', command=start_typing)
lbCount = countdown_label = ctk.CTkLabel(root, text='')

# Pack it all into the window
lbTop.pack()
entry_field.pack()
bStart.pack()
lbCount.pack()

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