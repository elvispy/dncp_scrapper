# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:13:20 2019

@author: Hernán
"""
#https://stackoverflow.com/questions/34338897/python-selenium-find-out-when-a-download-has-completed

import time
import os

def download_wait(dest_path, directory, timeout = 30):
    """
    Wait for downloads to finish with a specified timeout.

    Args
    ----
    dest_path: int, defaults to None
        The path to the folder plus the filename to move/rename.
    directory : str
        The path to the folder where the files will be downloaded.
    timeout : int
        How many seconds to wait until timing out.
    
    """
    seconds = 0
    dl_complete = False
    
    while dl_complete == False and seconds < timeout:
        time.sleep(1)
        chrome_temp_file = sorted(Path(directory).glob('*.part'))
        downloaded_files = sorted(Path(directory).glob('*.*'))
        if (len(chrome_temp_file) == 0) and \
           (len(downloaded_files) >= 1):
            #Renombrar
            #https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
            os.rename(downloaded_files[0], dest_path)
            dl_complete = True
        seconds += 1
    
    return dl_complete
