
import pandas as pd
import csv
import os, glob

file20102012 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/preFiles/PreprocessedMedications.csv'
file20152016 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/preFiles/PreprocessedMedications15-16.csv'
file20162017 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2016-2017/preFiles/PreprocessedMedication16-17.csv'
file20172018 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2017-2018/preFiles/PreprocessedMedication17-18.csv'
fileLongitudinal = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/PreprocessedMedsLong.csv'


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

# this method is to check how many patients left the study during the period
def patientsProcess():
    data20102012 = pd.read_csv(file20102012)
    df1=data20102012.drop_duplicates(subset="PtID",keep="first")
    unique_ids20102012 = df1.PtID.array
    
    data20152016 = pd.read_csv(file20152016)
    df1=data20152016.drop_duplicates(subset="PtID",keep="first")
    unique_ids20152016 = df1.PtID.array

    data20162017 = pd.read_csv(file20162017)
    df1=data20162017.drop_duplicates(subset="PtID",keep="first")
    unique_ids20162017 = df1.PtID.array

    data20172018 = pd.read_csv(file20172018)
    df1=data20172018.drop_duplicates(subset="PtID",keep="first")
    unique_ids20172018 = df1.PtID.array

    dataLongi = pd.read_csv(fileLongitudinal)
    df1=dataLongi.drop_duplicates(subset="PtID",keep="first")
    unique_idsLongi = df1.PtID.array

    arr = [unique_ids20102012, unique_ids20152016,unique_ids20162017,unique_ids20172018,unique_idsLongi] 
    output = commonElements(arr) 
    print ("Common Element in 2010-2012 data set and 2015-2016 data set= ",len(output)) 



# createDiffMedicineFile()
# getUniqueCount()
patientsProcess()