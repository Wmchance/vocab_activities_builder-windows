import os

def destination_path():
    full_path = os.path.realpath(__file__)
    split_path = full_path.split('\\')
    destination_path_components = (split_path[0], split_path[1], split_path[2], 'Desktop', 'worksheet.txt')
    destination_path = '\\'.join(destination_path_components)

    return destination_path