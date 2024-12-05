import tkinter as tk
import serial_manager

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Following lines for testing
        self.label = tk.Label(self, text="Hello, world!")
        self.label.pack()
        self.debugBtn = tk.Button(self, text="Debug")
        self.debugBtn.pack()        

        self.assign_commands()

    def assign_commands(self):
        '''Assign appropriate commands to buttons'''
        
        # For testing
        ser = serial_manager.SerialManager()
        self.debugBtn.configure(command=lambda: ser.send_serial("Hello, world!"))

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()