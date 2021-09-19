
# check patients's medication changed throughout the years
import pandas as pd
import numpy as np
import csv
import os, glob

file20102012 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/preFiles/PreprocessedMedications_new.csv'
file20152016 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/preFiles/PreprocessedMedications15-16_new.csv'
file20162017 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2016-2017/preFiles/PreprocessedMedication16-17_new.csv'
file20172018 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2017-2018/preFiles/PreprocessedMedication17-18_new.csv'
fileLongitudinal = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/PreprocessedMedsLong_new.csv'


# method to create file with patient id and his  medical list
def createIDDrugListFile():
    data20102012 = pd.read_csv(file20102012)
    newDataFrame = data20102012.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame.to_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/preFiles/idVsDrugList.csv')

    data20152016 = pd.read_csv(file20152016)
    newDataFrame1 = data20152016.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame1.to_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/preFiles/idVsDrugList.csv')

    data20162017 = pd.read_csv(file20162017)
    newDataFrame2 = data20162017.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame2.to_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2016-2017/preFiles/idVsDrugList.csv')

    data20172018 = pd.read_csv(file20172018)
    newDataFrame3 = data20172018.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame3.to_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2017-2018/preFiles/idVsDrugList.csv')

    dataLongi = pd.read_csv(fileLongitudinal)
    newDataFrame4 = dataLongi.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame4.to_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/idVsDrugList.csv')


def createDiffMedicineFile(file1, file2, outputFile):
    with open(file1, 'r') as t1, open(file2, 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    with open(outputFile, 'w') as outFile:
        for line in filetwo:
            if line not in fileone:
                outFile.write(line)

        for line in fileone:
            if line not in filetwo:
                outFile.write(line)

def removeCommonRows(file1, file2, outputFile):
    df1 = pd.read_csv(file1, names = ['PtID', 'DrugName'])
    df2 = pd.read_csv(file2, names = ['PtID', 'DrugName'])

    print( 'id count : ',df1.PtID.size)

    df_merge = pd.merge(df1, df2, on=['PtID', 'DrugName'], how='inner')
    df1 = df1.append(df_merge) 

    fullID = df1.drop_duplicates(subset="PtID",keep="first")

    df1['Duplicated'] = df1.duplicated(keep=False) # keep=False marks the duplicated row with a True
    df_final = df1[~df1['Duplicated']] # selects only rows which are not duplicated.
    del df_final['Duplicated'] # delete the indicator column
    df_final.to_csv(outputFile)

def getUniqueID(fileName):
    data = pd.read_csv(fileName)
    df1=data.drop_duplicates(subset="PtID",keep="first")
    return df1.PtID.array

def removeRowsInMultipleDFs(file1, file2, file3, file4, outputFile):
    df1 = pd.read_csv(file1, names = ['PtID', 'DrugName'])
    df2 = pd.read_csv(file2, names = ['PtID', 'DrugName'])
    df3 = pd.read_csv(file3, names = ['PtID', 'DrugName'])
    df4 = pd.read_csv(file4, names = ['PtID', 'DrugName'])

    print( 'id count 2010/12 : ',df1.PtID.size)
    print( 'id count 2015/16 : ',df2.PtID.size)
    print( 'id count 2016/17 : ',df3.PtID.size)
    print( 'id count 2017/18 : ',df4.PtID.size)


    df_merge = pd.merge(df1, df2, on=['PtID', 'DrugName'], how='inner')
    df1 = df1.append(df_merge) 
    df_merge2 = pd.merge(df1, df3, on=['PtID', 'DrugName'], how='inner')
    df1 = df1.append(df_merge2) 
    df_merge3 = pd.merge(df1, df4, on=['PtID', 'DrugName'], how='inner')
    df1 = df1.append(df_merge3) 
    df1.sort_values("PtID")
    df1.to_csv('sort.csv')

    fullID = df1.drop_duplicates(subset="PtID",keep="first")

    df1['Duplicated'] = df1.duplicated(keep=False) # keep=False marks the duplicated row with a True
    df_final = df1[~df1['Duplicated']] # selects only rows which are not duplicated.
    del df_final['Duplicated'] # delete the indicator column
    df_final.to_csv(outputFile)

# createIDDrugListFile() # run this first to create files
file1 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/preFiles/idVsDrugList.csv'
file2 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/preFiles/idVsDrugList.csv'
file3 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2016-2017/preFiles/idVsDrugList.csv'
file4 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2017-2018/preFiles/idVsDrugList.csv'
file5 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/idVsDrugList.csv'
outputFile1 = '/home/kali/Documents/thesis/Preprocessing_codes/mediList/medi2010_2016.csv'
outputFile2 = '/home/kali/Documents/thesis/Preprocessing_codes/mediList/medi2010_2017.csv'
outputFile3 = '/home/kali/Documents/thesis/Preprocessing_codes/mediList/medi2010_2018.csv'
outputFile4 = '/home/kali/Documents/thesis/Preprocessing_codes/mediList/medi2010_long.csv'

outputFile5 = '/home/kali/Documents/thesis/Preprocessing_codes/mediList/medi2016_long.csv'
outputFile6 = '/home/kali/Documents/thesis/Preprocessing_codes/mediList/medi2017_long.csv'
outputFile7 = '/home/kali/Documents/thesis/Preprocessing_codes/mediList/medi2018_long.csv'

out = '/home/kali/Documents/thesis/Preprocessing_codes/mediList/medi_all.csv'



# print('---------2010/12-2015/16-----------')
# removeCommonRows(file1, file2, outputFile1)
# idList = getUniqueID(outputFile1)
# print("changed medicine count: ", idList.size)

# print('---------201/12-2016/17-----------')
# removeCommonRows(file1, file3, outputFile2)
# idList2 = getUniqueID(outputFile2)
# print("changed medicine count: ", idList2.size)

# print('---------201/12-2017/18-----------')
# removeCommonRows(file1, file4, outputFile3)
# idList3 = getUniqueID(outputFile3)
# print("changed medicine count: ", idList3.size)

print('---------2010/12-long-----------')
removeCommonRows(file1, file5, outputFile4)
idList4 = getUniqueID(outputFile4)
print("changed medicine count: ", idList4.size)

print('---------2015/16-long-----------')
removeCommonRows(file2, file5, outputFile5)
idList5 = getUniqueID(outputFile5)
print("changed medicine count: ", idList5.size)

print('---------2016/17-long-----------')
removeCommonRows(file3, file5, outputFile6)
idList6 = getUniqueID(outputFile6)
print("changed medicine count: ", idList6.size)

print('---------2017/18-long-----------')
removeCommonRows(file4, file5, outputFile7)
idList7 = getUniqueID(outputFile7)
print("changed medicine count: ", idList7.size)

print(" --------common in all------------")
removeRowsInMultipleDFs(file1, file2, file3, file4, out)
idList8 = getUniqueID(out)
print("changed medicine count in all: ", idList8.size)
