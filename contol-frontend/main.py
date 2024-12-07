import tkinter as tk
from MVC import view, model
import hardware_manager

# For CLI mode
import time

# Set to True to run in GUI mode. For now, set to False to run in CLI mode
guiMode = False

if __name__ == "__main__":
    data_model = model.DataModel()
    hardware_manager = hardware_manager.HardwareManager(data_model, view)

    # TODO: At the end make sure to schedule the update function
    if guiMode:
        root = tk.Tk()
        view.MainApplication(root).pack(side="top", fill="both", expand=True)
        root.mainloop()

    else:
        print("Running in CLI mode")
        while True:
            hardware_manager.listen_for_update()
            time.sleep(3)
