from tkinter import filedialog, Tk

root = Tk()
root.attributes("-topmost", True)
root.withdraw()

pickFile = lambda: filedialog.askopenfilename()