import cv2
import numpy as np
from pdf2image import convert_from_path
import glob
import os

base_directory = "____________________________________"
print(base_directory + "*.pdf")

for img in glob.glob(base_directory + "*.pdf"):
    pdf_file=img
    pdf_file_re=pdf_file
    
    print(len(base_directory))
    print(pdf_file[len(base_directory):][:-4])
   # print(pdf_file(len(base_directory):))
    folder_name = pdf_file_re[len(base_directory):][:-4]
    print("folder name: ",folder_name)
    complete_folder_name = base_directory + folder_name+"/"
    print("cmplt folder name: ", complete_folder_name)
    
    os.mkdir(complete_folder_name)
    os.chdir(complete_folder_name)
    pages=convert_from_path(pdf_file_re,fmt="png")
   
    
    count=0
    for i in range(len(pages)):
        count=count+1
        pages[i].save(folder_name+ "_"+str(count) +'.png', 'PNG')