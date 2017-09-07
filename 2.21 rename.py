# -*- coding:utf-8 -*-

# module os
import os

def renameFiles():
    #(1) get file names from a folder
    file_list = os.listdir(r"F:\F")  #r = raw pack(原包装)
    print (file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"F:\F")
    
    #(2) for each file, rename filename
    for file_name in file_list:
        #打印原文件名
        print ("Old Names - " + file_name)
        #打印新文件名
        print ("New Names - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    print (file_list)
    os.chdir(saved_path)

renameFiles()
