import os
from flask import current_app

def pic_name_list(folder_name):
    path = os.path.join(current_app.root_path , 'static/images/', folder_name)
    pic_list = os.listdir(path)
    return pic_list
