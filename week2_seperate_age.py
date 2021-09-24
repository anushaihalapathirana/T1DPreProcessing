
import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from functools import reduce
from removeColumns import getColNames, deleteCols, deleteRows, countColRows

df1 = pd.read_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/PreprocessedVisitsLong_new.csv')

teen_file = '/home/kali/Documents/thesis/Preprocessing_codes/age_seperated_data/teenagers.csv'
adult_file = '/home/kali/Documents/thesis/Preprocessing_codes/age_seperated_data/adults.csv'
elder_file = '/home/kali/Documents/thesis/Preprocessing_codes/age_seperated_data/elders.csv'
selected_col_file = '/home/kali/Documents/thesis/Preprocessing_codes/age_seperated_data/selected_col.csv'

columns = ['PtID', 'Visit', 'ACEARB', 'age', 'AlbCreatRat_mggNew', 'AutonomicNeuroCl', 'BGTestAvgNumMeter', 'BldPrDia', 'BldPrSys', 'bmi', 'BUN', 'diabDur','DiagAgeCombo','DirectLDL','GFR','GFRIsBelow60','HbA1c','HbA1cImputeDtMnC', 'HDL','HDLUnits','InsulinUsedNew1-InsulinUsedNew6', 'LDL','LDLUnits', 'LipidsFastingStatus', 'NumPumpBolusOrShortAct','PancreasTrans','PregAtVisit','PregInPastYear','Pt_A1cGoalLev','Pt_ExtBioFamT1D','Pt_SHFlg', 'Pt_DKAFlg','Pt_SmokeCurr','SMBGperDayPtMeterComboCat', 'TotChol', 'TotalDailyInsPerKg', 'Triglyc','TSH', 'UnitsInsBasalOrLongAct']
def seperate_by_ages(df):
    teenagers_df = df[df['age'] <= 20]
    adults_df = df[(df['age'] > 20) & (df['age'] <=45)]
    elders_df = df[df['age'] > 45]

    teenagers_df.to_csv(teen_file, na_rep='NA', index= False)
    adults_df.to_csv(adult_file, na_rep='NA', index= False)
    elders_df.to_csv(elder_file, na_rep='NA', index= False)

# cols to remove
def removeCols(l1, file, df):
    removeList = [x for x in getColNames(df) if x not in l1]
    deletedDF = deleteCols(df,removeList)
    deleteRowsDF = deleteRows(deletedDF, 140461)
    countColRows(deleteRowsDF)

    deleteRowsDF.to_csv(file, na_rep='NA', index= False)

def graphs(df):
    df=df.drop_duplicates(subset="PtID",keep="first")

    # graphs of individual count of variables
    # df["GFR"].fillna(0, inplace = True) 
    sns.countplot(df['TSH'],label="Count")
    plt.show()



elder_df = pd.read_csv(elder_file)

# graphs(elder_df)
removeCols(columns,selected_col_file, df1)
reduce_df = pd.read_csv(selected_col_file)
seperate_by_ages(reduce_df)

countColRows(elder_df)