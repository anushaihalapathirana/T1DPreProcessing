# This program will open and read files in defined directory
# Change the file format and save new file as csv file.

import os
import pandas as pd
from os import listdir
from os.path import isfile, join
import glob



path20102012Original = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/Data Tables/'
path20152016Original = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/Data Tables/'
path20162017Original = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2016-2017/Data Tables/'
path20172018Original = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2017-2018/Data Tables/'
pathLongitudinalOriginal = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/Data Tables/'

originalPaths = [path20102012Original, path20152016Original,path20162017Original,path20172018Original, pathLongitudinalOriginal]

path20102012Out = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/csvFiles/'
path20152016Out = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/csvFiles/'
path20162017Out = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2016-2017/csvFiles/'
path20172018Out = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2017-2018/csvFiles/'
pathLongitudinalOut = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/csvFiles/'

outputPaths = [path20102012Out, path20152016Out, path20162017Out, path20172018Out, pathLongitudinalOut]

path20102012Pre = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/preFiles/'
path20152016Pre = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/preFiles/'
path20162017Pre = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2016-2017/preFiles/'
path20172018Pre = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2017-2018/preFiles/'
pathLongitudinalPre = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/'


prePaths = [path20102012Pre, path20152016Pre, path20162017Pre, path20172018Pre,pathLongitudinalPre]

# read, change and save as csv file
def readConverToCSV(file_dir, output_file):
    files = os.listdir(file_dir)
    for file in files:
        if os.path.isfile(os.path.join(file_dir, file)):
            f = open(os.path.join(file_dir, file),'r', encoding="utf-8", errors='ignore')
            # print(f.name)
            df = pd.read_csv(os.path.join(file_dir, file), sep='|', engine='python', quotechar='"', error_bad_lines=False)
            
            file_name = os.path.basename(f.name)
            # updated_file_name = file_name.split('.')[0]+"_new.csv"
            
            newOutput = "Preprocessed"+file_name.split('.')[0]+"_new.csv"
            textfile =output_file+newOutput
            df.to_csv(textfile, na_rep='NA')
            getUniquePatients(textfile, newOutput)

            f.close()


# get unique patients count
def getUniquePatients(path, file):
    data = pd.read_csv(path)
    df1=data.drop_duplicates(subset="PtID",keep="first") 
    with open("uniquePatientCount.txt", "a") as file_object:
        string = 'Number of Unique patients in '+file+': '+ str(df1.PtID.size)
        file_object.write(string)
        file_object.write("\n")


def convertAllFiles():
    for idx, val in enumerate(originalPaths):
        readConverToCSV(val, prePaths[idx])

convertAllFiles()
