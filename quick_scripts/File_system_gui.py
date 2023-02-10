import tkinter
import tkinter.messagebox
import customtkinter
import os
import pathlib
import shutil

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class  FileActions(customtkinter.CTk):
    '''
    A class to do file handling operations in respect to naming conventions and folder structures
    '''
    old_file_folder = "old_folder\\"
    new_file_folder = "new_folder\\"
    CONVENTION_STRING = None
    CONVENTION_MAP = {"Academic":{
                        'Author': 'noAuthor',
                        'Year': 'noYear',
                        'Geo-region': 'noGeo',
                        'Title':'noTitle',
                        },
                     "data":
                        {'Project':'noProject',
                         'SubProject': 'noSubProject',
                         'Description':'noDescription',
                         'Date': 'noDate',
                        },
                     "drone":
                       {'Project': 'noProject',
                        'Location': 'noLoc',
                        'Date': 'noDate',
                        },
                     "finance":
                       {'Cost Center': 'noCostCenter',
                        'Date': 'noDate',
                        'Type': 'noType',
                        'Reference': 'noRef',
                        'Supplier': 'noSupplier',
                        'Description': 'noDescription',
                        },
                        }

    def __init__(self, category, date):
        super().__init__()
        self.category = category
        self.date = date



                # configure window
        self.title("FILE HANDLER.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2,), weight=1)

        # SIDEBAR
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # LOGO
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="File Handling", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self.sidebar_frame)
        self.radiobutton_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="n")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Bulk or single update")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.bulk_radio = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0, text='Bulk')
        self.bulk_radio.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.single_radio = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1, text='Single')
        self.single_radio.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        
        
        # Side Date buttons
        self.side_date_label = customtkinter.CTkLabel(self.sidebar_frame, text=f"Date", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.side_date_label.grid(row=3, column=0, padx=10, pady=10, sticky='n')
        self.side_date_combo = customtkinter.CTkComboBox(self.sidebar_frame, values=['YYYYMMDD'])
        self.side_date_combo.grid(row=4, column=0, padx=5, pady=(5, 5),sticky='n')
        
        
        
        # create tabview
        self.tabview = customtkinter.CTkTabview(self , width=800, height=500)
        self.tabview.grid(row=1, column=1, columnspan=3,padx=(20, 0), pady=(20, 0), sticky="n")
        
        max_row = 0
        for tab in self.CONVENTION_MAP.keys():
            self.tabview.add(tab.capitalize())
            self.tabview.tab(tab.capitalize()).grid_columnconfigure((0,1), weight=1)  # configure grid of individual tabs
            max_row = 0
            for i, element in enumerate(self.CONVENTION_MAP[tab].items()):
                self.con_label = customtkinter.CTkLabel(self.tabview.tab(tab.capitalize()), text=f"{element[0]}")
                self.con_label.grid(row=i, column=0, padx=10, pady=10)
                self.combobox_var = customtkinter.StringVar(name=f'{tab}_{element[0]}_combo')
                self.con_combo = customtkinter.CTkComboBox(self.tabview.tab(tab.capitalize()), values=[f"{element[1]}"], variable=self.combobox_var)
                self.con_combo.set(f'{tab}_{element[0]}_combo')
                self.con_combo.grid(row=i, column=1, padx=20, pady=(20, 10))
                # print(self.con_combo)
               
                max_row = i
            self.con_button = customtkinter.CTkButton(self.tabview.tab(tab.capitalize()), text="Create Convention", command=lambda:self.set_convention_string())
            self.con_button.grid(row=max_row+1, column=0, columnspan=2, padx=20, pady=(10, 10))
            self.textbox = customtkinter.CTkTextbox(self.tabview.tab(tab.capitalize()), width=250)
            self.textbox.grid(row=max_row+2, column=0, columnspan=2, padx=(10, 0), pady=(10, 0), sticky="n") 
            
            print(self.tabview.get())
            # for i in self.tabview.winfo_children():
            #     print(i)
        

            # print(i)             
            # print(self.CONVENTION_STRING)
            # self.textbox.insert(0,text=str(self.CONVENTION_STRING)) 


# ===============================================================
# LOGIC FUNCTIONS


            # _list = wid.winfo_children() 
            # 
            # 
    def get_tab_view(self):
        return  self.tabview.get()    

    def get_combobox_inputs(self):
      print(self.combobox_var.get())

        
    def set_convention_string(self, **kwargs):
        '''sets the body of the convention (string)'''


        convention_string = ""
        for k,v in kwargs.items():
            self.CONVENTION_MAP[self.category][k] = v
        for k,v in self.CONVENTION_MAP[self.category].items():
            if convention_string == "":
                convention_string = f'{v}'
            else:
                convention_string = f'{convention_string}_{v}'
        self.CONVENTION_STRING = convention_string
        return convention_string



    def bulk_move_and_rename(self):
        '''moves file from source folder to destination folder, required to set convention first'''
        
        folder_name = f'{self.category}_{self.date}'
        if os.path.exists(folder_name):
            print("FOLDER EXISTS")
            return
        else:
            os.mkdir(folder_name)
        
        for i, file in enumerate(os.listdir(self.old_file_folder)):
            file_extension = pathlib.Path(file).suffix
            source_file = f'{self.old_file_folder}{file}'
            destination_loc = f'{folder_name}\\{self.CONVENTION_STRING}_{i+1}{file_extension}'
            shutil.move(source_file,destination_loc)

    
    def single_file_convention(self):
        pass
        


# ===============================================================
# TKINTER FUNCTIONS

    def get_tab_headers(self):
        return [i.capitalize() for i in self.CONVENTION_MAP.keys()]

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

# ===============================================================








if __name__ =="__main__":



    fl = FileActions('drone','20221026')
    # print(fl.get_tab_headers())
    fl.set_convention_string(project='testProject', date='20230101')
    # fl.get_combobox_inputs()
    fl.mainloop()

    # fl.bulk_move_and_rename()