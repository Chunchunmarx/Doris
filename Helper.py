import ntpath
import os

def get_filename(file_path):
    head, tail = ntpath.split(file_path)
    file_name = tail or ntpath.basename(head)

def get_file_without_extension(file_path : str):
    return file_path[0:file_path.rfind(".")]

def run_command(cmd):
    # maybe async / create process instead of os
    return os.system(cmd)