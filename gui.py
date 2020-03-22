from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.title("pixel-watcher")

    def create_widgets(self):
        spots = Frame(self)
        spots.pack()
        
        Label(spots, text="Spot List").pack()
        
        self.spotList = Listbox(spots)
        self.spotList.pack(fill=BOTH)
        
        self.spotAddButton = Button(spots)
        self.spotAddButton["text"] = "Add"
        self.spotAddButton["command"] = self.spotAddFunction
        self.spotAddButton.pack(fill=X)
        
        self.spotRemoveButton = Button(spots)
        self.spotRemoveButton["text"] = "Remove"
        self.spotRemoveButton["command"] = self.spotRemoveFunction
        self.spotRemoveButton.pack(fill=X)
        
        self.toggleButton = Button(self)
        self.toggleButton["text"] = "Run"
        self.toggleButton["command"] = self.toggleFunction
        self.toggleButton.pack()

    def spotAddFunction(self):
        size = self.spotList.size()
        item = str(size) + ". Item"
        self.spotList.insert(END, item)
        self.spotList.see(size)
        
    def spotRemoveFunction(self):
        size = self.spotList.size()
        self.spotList.delete(size - 1)
        
    def toggleFunction(self):
        if self.toggleButton["text"] == "Run":
            
            self.toggleButton["text"] = "Stop"
        elif self.toggleButton["text"] == "Stop":
            
            self.toggleButton["text"] = "Run"
        
root = Tk()
app = Application(master=root)
app.mainloop()