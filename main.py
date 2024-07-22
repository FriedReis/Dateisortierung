#Tkinter.py
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap import Style
#Versuch.py
import os
import glob
import ntpath
import shutil
#Tkinter.py

def get_entry():
    entry_link_text = tk.filedialog.askdirectory() + '\\'
    entry_extension_text = combo_extension.get()
    entry_foldername_text = entry_foldername.get()
    sortieren(entry_link_text, entry_extension_text, entry_foldername_text)
    root.quit()

#Versuch.py

def sortieren(link, extension, FolderName):
    file_extension = f'*.{extension.lstrip(".")}'
    print(link, extension, file_extension)
    search_path = os.path.join(link, file_extension)
    #Für Datei mit Endung jpg ---> Erste 4 Stellen ---> neuer Folder
    for file_year in glob.glob(search_path):

        #Erstell eine Variable aus den ersten 4 digits
        x = str(ntpath.basename(file_year)[:4])
        path_year = f'{FolderName}' + ' ' + x
        if x.isdigit() == True:
        #Erstell den Path aus dem directory und den ersten 4 digits
            folder_year = os.path.join(link, path_year)
        
        #Erstell Folder für das Jahr
            if not os.path.exists(folder_year):
                os.makedirs(folder_year)
        
        #Move File to folder
            shutil.move(file_year, folder_year)
        else:
            continue
    #Listet die Ordner, die sich in dem Directory befinden
    folder_directory = os.listdir(link)

    #Für Ordner in Ordnerliste // Für Nummer aus liste der ordner
    for i in range(len(folder_directory)):
        #Variable die den jetzigen ordner deklariert
        if_ordner = os.path.join(link, folder_directory[i], file_extension)
        #Für Datei in Ordner
        for file_month in glob.glob(if_ordner):
        
            #Erstelle Variable aus 4-6 digit
            path_month = str(ntpath.basename(file_month)[4:6])
            if path_month.isdigit() == True:

            #Erstellt einen Subfolder(Monat) in dem Jahres Folder
                folder_month = link + folder_directory[i]+ "\\" + path_month
                if not os.path.exists(folder_month):
                    os.makedirs(folder_month)
            
            #Moved die Datei aus dem Jahres Folder in den Monats Folder
                shutil.move(file_month, folder_month)
            else:
                continue
        i += 1

#Tkinter.py
root = ttk.Window(themename='darkly')
root.geometry("1200x600")
root.title('File sort')
root.resizable(True, True)

icon_path = "C:\\Users\\Lenovo\\Documents\\Python Projekte\\Sortieren\\Photo.ico"
root.iconbitmap(icon_path)

myfont = ("Helvetica", 18)
style = Style()
style_custom = Style()
# Create a new style for the button
style.configure('danger.TButton', font=('Helvetica', 25))
style_custom.configure('Custom.TButton', font=('Helvetica', 25))

#entry_extension = tk.Entry(root, font= ("Helvetica", 30), bg= 'light gray')
#entry_extension.grid(row=0, column=1, columnspan= 1, sticky='ew', padx=10, pady=10)

extension = ['.jpg', '.mp4', '.txt']
combo_extension = ttk.Combobox(root, values= extension, font= ("Helvetica", 30))
combo_extension.grid(row=0, column=1, columnspan= 1, sticky='ew', padx=10, pady=10)

label_extension = tk.Label(root, text='File Extension(.jpg, .mp4,...)', font= myfont)
label_extension.grid(row=0,column=0,sticky='nsew', padx=10, pady=10)

entry_foldername = tk.Entry(root, font= ("Helvetica", 30), bg= 'light gray')
entry_foldername.grid(row=1, column=1, columnspan= 1, sticky='ew', padx=10, pady=10)

label_foldername = tk.Label(root, text='Folder name:', font= myfont)
label_foldername.grid(row=1,column=0,sticky='nsew', padx=10, pady=10)



exit_button = ttk.Button(root, text = "Exit", style= 'danger.TButton', command = lambda: root.quit())
exit_button.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)


input_button = ttk.Button(root, text='Run & Choose Folder', style='Custom.TButton', command= lambda: get_entry())
input_button.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)


for i in range(4):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()