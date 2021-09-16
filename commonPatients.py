
import pandas as pd
import numpy as np
import csv
import os, glob

file20102012 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/preFiles/PreprocessedMedications_new.csv'
file20152016 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/preFiles/PreprocessedMedications15-16_new.csv'
file20162017 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2016-2017/preFiles/PreprocessedMedication16-17_new.csv'
file20172018 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2017-2018/preFiles/PreprocessedMedication17-18_new.csv'
fileLongitudinal = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/PreprocessedMedsLong_new.csv'


# Python program to find the common elements
# in two lists
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        common = a_set & b_set
        print(len(common))
    else:
        print("No common elements")

def commonPtID():
    
    data20102012 = pd.read_csv(file20102012)
    df1=data20102012.drop_duplicates(subset="PtID",keep="first")
    unique_ids20102012 = df1.PtID.array
    
    data20152016 = pd.read_csv(file20152016)
    df1=data20152016.drop_duplicates(subset="PtID",keep="first")
    ids20152016 = df1.PtID.array

    data20162017 = pd.read_csv(file20162017)
    df1=data20162017.drop_duplicates(subset="PtID",keep="first")
    ids20162017 = df1.PtID.array

    data20172018 = pd.read_csv(file20172018)
    df1=data20172018.drop_duplicates(subset="PtID",keep="first")
    ids20172018 = df1.PtID.array

    dataLongi = pd.read_csv(fileLongitudinal)
    df1=dataLongi.drop_duplicates(subset="PtID",keep="first")
    idsLongi = df1.PtID.array

    common_member(unique_ids20102012, ids20152016)
    common_member(ids20152016, ids20162017)
    common_member(ids20162017, ids20172018)
    common_member(ids20172018, idsLongi)

def createIDDrugListFile():
    data20102012 = pd.read_csv(file20102012)
    newDataFrame = data20102012.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame.to_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/preFiles/idVsDrugList.csv', header=None, na_rep='NaN')

    data20152016 = pd.read_csv(file20152016)
    newDataFrame1 = data20152016.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame1.to_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/preFiles/idVsDrugList.csv', header=None, na_rep='NaN')

    data20162017 = pd.read_csv(file20162017)
    newDataFrame2 = data20162017.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame2.to_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2016-2017/preFiles/idVsDrugList.csv', header=None, na_rep='NaN')

    data20172018 = pd.read_csv(file20172018)
    newDataFrame3 = data20172018.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame3.to_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2017-2018/preFiles/idVsDrugList.csv', header=None, na_rep='NaN')

    dataLongi = pd.read_csv(fileLongitudinal)
    newDataFrame4 = dataLongi.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame4.to_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/idVsDrugList.csv', header=None, na_rep='NaN')


def createDiffMedicineFile():
    with open('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/preFiles/idVsDrugList.csv', 'r') as t1, open('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/preFiles/idVsDrugList.csv', 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    with open('diff.csv', 'w') as outFile:
        for line in filetwo:
            if line not in fileone:
                outFile.write(line)

        for line in fileone:
            if line not in filetwo:
                outFile.write(line)

def getUniqueCount():

    df1=pd.read_csv('diff.csv', sep='\t', names=["PtID", "DrugName"]).drop_duplicates(subset="PtID",keep="first")
    string = 'Number of Unique patients in: '+ str(df1.PtID.size)
    print(string)

    df2=pd.read_csv('merged.csv', sep='\t', names=["PtID", "DrugName"]).drop_duplicates(subset="PtID",keep="first")
    string2 = 'Number of Unique patients in all files: '+ str(df2.PtID.size)
    print(string2)

    print("patient count different is: " ,df2.PtID.size-df1.PtID.size)

# Function to find common elements in n arrays 
def commonElements(arr): 
      
    # initialize result with first array as a set 
    result = set(arr[0]) 
    for currSet in arr[1:]: 
        result.intersection_update(currSet) 
  
    return list(result) 

# method to get unique ID list in csv files
def getUniqueID(fileName):
    data = pd.read_csv(fileName)
    df1=data.drop_duplicates(subset="PtID",keep="first")
    return df1.PtID.array


# this method is to check how many patients left the study during the period
def patientsProcess():
    unique_ids20102012 = getUniqueID(file20102012)
    unique_ids20152016 = getUniqueID(file20152016)
    unique_ids20162017 = getUniqueID(file20162017)
    unique_ids20172018 = getUniqueID(file20172018)
    unique_idsLongi = getUniqueID(fileLongitudinal)

    print('new patients in 2010/12: ', len(unique_ids20102012))
    # patients data in 2010
    arr = [unique_ids20102012, unique_ids20152016] 
    output = commonElements(arr) 
    print ("Common number of patients in 2010-2012 data set and 2015-2016 data set= ",len(output)) 

    arr2 = [unique_ids20102012, unique_ids20152016,unique_ids20162017] 
    output2 = commonElements(arr2) 
    print ("Common number of patients in 2010-2012 data set and 2016-2017 data set= ",len(output2)) 

    arr3 = [unique_ids20102012, unique_ids20152016,unique_ids20162017,unique_ids20172018] 
    output3 = commonElements(arr3) 
    print ("Common number of patients in 2010-2012 data set and 2017-2018 data set= ",len(output3)) 

    print("-----------------------------------------------")
    # 2015 new patients 
    # print("All patients in 2015 list: ",len(unique_ids20152016))

   # remove all the elements in 2010 list to get new 2015 patients list
    newPatients2015 = [x for x in unique_ids20152016 if x not in unique_ids20102012]
 
    print('new patients in 2015/16: ', len(newPatients2015))

    arr5 = [unique_ids20102012, newPatients2015] 
    output5 = commonElements(arr5) 
    print ("Common number of patients in 2010-2012 data set and 2015-2016 data set= ",len(output5))

    arr6 = [newPatients2015, unique_ids20162017] 
    output6 = commonElements(arr6) 
    print ("Common number of patients in 2015-2016 data set and 2016-2017 data set= ",len(output6))

    arr7 = [newPatients2015,unique_ids20162017, unique_ids20172018] 
    output7 = commonElements(arr7) 
    print ("Common number of patients in 2015-2016 data set and 2017-2018 data set= ",len(output7))
    
    print("-----------------------------------------------")
    # 2016 new patients 
    # print("All patients in 2016/17 list: ",len(unique_ids20162017))

   # remove all the elements in 2010 list to get new 2015 patients list
    newPatients2016 = [x for x in unique_ids20162017 if x not in newPatients2015]
 
    print('new patients in 2016/17: ', len(newPatients2016))

    arr8 = [newPatients2015, newPatients2016] 
    output8 = commonElements(arr8) 
    print ("Common number of patients in 2015/16 data set and 2016/17 data set= ",len(output8))

    arr9 = [newPatients2016, unique_ids20172018] 
    output9 = commonElements(arr9) 
    print ("Common Element in 2016/17 data set and 2017/18 data set= ",len(output9))


    print("-----------------------------------------------")
    # 2017 new patients 
    # print("All patients in 2017/18 list: ",len(unique_ids20172018))

   # remove all the elements in 2010 list to get new 2015 patients list
    newPatients2017 = [x for x in unique_ids20172018 if x not in newPatients2016]
 
    print('new patients in 2017/18: ', len(newPatients2017))

    arr10 = [newPatients2016, newPatients2017] 
    output10 = commonElements(arr10) 
    print ("Common Element in 2016/17 data set and 2017/18 data set= ",len(output10))

# createIDDrugListFile()
createDiffMedicineFile()
getUniqueCount()
patientsProcess()