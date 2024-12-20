import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, height="400px", width=600)
        self.parent = parent
       
        self.show_components()
        self.assign_commands()

    def show_components(self):
        '''Instantiate the elements of the main menu'''
        self.label = tk.Label(self, text="Hello, world!")
        self.label.pack()
        self.debugBtn = tk.Button(self, text="Debug")
        self.debugBtn.pack() 

    def assign_commands(self):
        '''Assign appropriate commands to buttons'''
        pass

    def schedule_function(self, function, frequency):
        '''
        Schedule a function to run every frequency milliseconds. This calls itself reursively, so it will 
        keep scheduling the function to run indefinitely.
        
        @param: function - the function to run, no arguments can be passed
        @param: frequency - the frequency in milliseconds
        '''
        
        function()
        self.parent.after(frequency, lambda: self.schedule_function(function, frequency))
