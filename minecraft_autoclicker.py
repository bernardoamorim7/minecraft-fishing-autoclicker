import pyautogui
import time
from pynput import keyboard
from threading import Thread 

def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'exit'
            print("Exiting program")
            exit()   
            
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def main():
    main.status = 'run'
    time.sleep(5)
    
    while True:
        print('running')
        
        pyautogui.click(button='right')
        time.sleep(0.1)
        
        if main.status == 'exit':
            print('Main program closing')
            break

Thread(target=main).start()
Thread(target=exit_program).start()