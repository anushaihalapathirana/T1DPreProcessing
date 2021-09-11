
import pandas as pd


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
    file20102012 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Initial Enrollment (2010-2012)/preFiles/PreprocessedMedications.csv'
    file20152016 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2015-2016/preFiles/PreprocessedMedications15-16.csv'
    file20162017 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2016-2017/preFiles/PreprocessedMedication16-17.csv'
    file20172018 = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - 2017-2018/preFiles/PreprocessedMedication17-18.csv'
    fileLongitudinal = '/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/PreprocessedMedsLong.csv'


    data20102012 = pd.read_csv(file20102012)
    df1=data20102012.drop_duplicates(subset="PtID",keep="first")
    unique_ids20102012 = df1.PtID.array

    # a = data20102012.groupby('PtID')['DrugName'].apply(list).reset_index(name='new')
    newDataFrame = data20102012.groupby('PtID', sort=True).agg({'DrugName':lambda x: list(x)})
    newDataFrame.to_csv('count.csv', header=None, na_rep='NaN')




    
    # data20152016 = pd.read_csv(file20152016)
    # df1=data20152016.drop_duplicates(subset="PtID",keep="first")
    # ids20152016 = df1.PtID.array

    # data20162017 = pd.read_csv(file20162017)
    # df1=data20162017.drop_duplicates(subset="PtID",keep="first")
    # ids20162017 = df1.PtID.array

    # data20172018 = pd.read_csv(file20172018)
    # df1=data20172018.drop_duplicates(subset="PtID",keep="first")
    # ids20172018 = df1.PtID.array

    # dataLongi = pd.read_csv(fileLongitudinal)
    # df1=dataLongi.drop_duplicates(subset="PtID",keep="first")
    # idsLongi = df1.PtID.array

    # common_member(unique_ids20102012, ids20152016)
    # common_member(ids20152016, ids20162017)
    # common_member(ids20162017, ids20172018)
    # common_member(ids20172018, idsLongi)



commonPtID()