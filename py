
# Keyboard module in Python 
import keyboard 
  
keyboard.add_hotkey('a', lambda: keyboard.write('Amacorp')) 
keyboard.add_hotkey('ctrl + shift + a', print, args =('you entered', 'hotkey')) 
  
keyboard.wait('esc') 


or



# Keyboard module in Python 
import keyboard 
  
# It records all the keys until escape is pressed 
rk = keyboard.record(until ='Esc') 
  
# It replay back the all keys 
keyboard.play(rk, speed_factor = 1) 

