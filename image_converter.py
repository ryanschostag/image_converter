#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 23:34:03 2018

@author: Ryan Schostag

Converts list of files to a different image type. For example, pdf -> png, 
png -> jpg, or pdf -> jpeg
"""

from subprocess import call
from os import chdir, path
from glob import glob
from sys import platform


def change_directory(directory):
    if path.isdir(directory):
        chdir(directory)
        return True
    else:
        print('Path not found: {}'.format(directory))
        return False
    

def generate_file_list(search_filter, recurse=False):
    if search_filter is None:
        search_filter = "*"
    try:
        return glob(search_filter)
    except Exception:
        print(Exception)
        return False
    

def convert_files_to_image(files, img_type):
    try:
        for file in files:
            file_name = file.split('.')[0]
            print('{} ==> {}'.format(file, file_name + '.' + img_type))
            call(['convert', file, file.split('.')[0] + '.' + img_type])
        return True
    except Exception:
        print(Exception)
        return False


def main():
    
    if platform.lower() != 'linux':
        print('This program is for Linux only')
        return 1
    
    change_directory(r'/home/path/to/directory')
    file_list = generate_file_list(search_filter='*.pdf', recurse=False)
    convert_files_to_image(file_list, 'png')


if __name__ == "__main__":
    main()