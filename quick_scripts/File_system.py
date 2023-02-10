import os
import pathlib
import shutil


class  FileActions:
    '''
    A class to do file handling operations in respect to naming conventions and folder structures
    '''
    old_file_folder = "old_folder\\"
    new_file_folder = "new_folder\\"
    CONVENTION_STRING = None
    CONVENTION_MAP = {"finance":
                       {'cost_center': 'noCostCenter',
                        'date': 'noDate',
                        'ALRDtype': 'noType',
                        'ref': 'noRef',
                        'supplier': 'noSupplier',
                        'description': 'noDescription',
                        },
                       "drone":
                       {'project': 'noProject',
                        'location': 'noLoc',
                        'date': 'noDate',
                        }}

    def __init__(self, category, date):
        self.category = category
        self.date = date


        
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
        



if __name__ == '__main__':
    fl = FileActions('drone','20221026')
    fl.set_convention_string(project='testProject', date='20230101')
    fl.bulk_move_and_rename()

    fl2 = FileActions('finance', '20221026')
    fl2.set_convention_string(cost_center=274, date='20230101', ALRDtype='TAX', reference='00544a', supplier='Buco', description='shelves' )

    


