from office365_api import SharePoint
import re
from pathlib import PurePath
import pandas as pd

def save_file(file_n, file_obj, dest_folder):
    file_dir_path = PurePath(dest_folder, file_n)
    with open(file_dir_path, 'wb') as f:
        f.write(file_obj)

def get_file(file_n, src_folder, dest_folder):
    file_obj = SharePoint().download_file(file_n, src_folder)
    save_file(file_n, file_obj, dest_folder)

def get_files(src_folder,dest_folder):
    files_list = SharePoint().get_files_list(src_folder)
    for file in files_list:
        get_file(file.name, src_folder, dest_folder)

def get_files_by_pattern(keyword, src_folder, dest_folder):
    files_list = SharePoint().get_files_list(src_folder)
    for file in files_list:
        if re.search(keyword, file.name):
            get_file(file.name, src_folder, dest_folder)

def get_sp_list(list_name):
    data = SharePoint().get_list(list_name)
    final_df = pd.DataFrame()
    for item in data:
        df=pd.DataFrame(item.properties, index = [0])
        final_df = pd.concat([final_df,df])
    # Drop column id to avoid duplicate columns     
    final_df.drop(['Id'], axis=1, inplace = True)
    return final_df