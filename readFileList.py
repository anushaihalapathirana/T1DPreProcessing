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
            
            new_data = []
            for line in f:
                
                line = line.replace("|", ",")
                new_data += [line]
            
            file_name = os.path.basename(f.name)
            updated_file_name = file_name.split('.')[0]+"_new.csv"
            
            textfile = open(output_file+updated_file_name, "w")

            for element in new_data:
                textfile.write(element)
            textfile.close()

            f.close()
  
# remove missing values and save to csv
def preProssData():
    # reading two csv files
    missing_values = ["n/a", "na", '']

    # csvFile0, csvFile1 etc variables created 
    for idx, val in enumerate(outputPaths):
        globals()['csvFile%s' % idx] = [f for f in listdir(val) if isfile(join(val, f))] 
        prepath = prePaths[idx]
        for i, value in enumerate([f for f in listdir(val) if isfile(join(val, f))]):
           
            keyword = 'Preprocessed'
            for fname in os.listdir(val):
                if keyword in fname:
                    print("already processed")
                else: 
                    data1 = pd.read_csv(val+value, error_bad_lines=False, na_values = missing_values, header = None)
                    newOutput = "Preprocessed"+value.split('_')[0]+".csv"
                    data1.to_csv(prepath+newOutput, header=None, na_rep='NaN')
            getUniquePatients(prepath+newOutput, newOutput)

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
        readConverToCSV(val, outputPaths[idx])

convertAllFiles()
preProssData()