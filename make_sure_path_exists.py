# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:15:56 2019

@author: Hernán
"""
#From https://stackoverflow.com/questions/32123394/workflow-to-create-a-folder-if-it-doesnt-exist-already
import os
import errno

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise