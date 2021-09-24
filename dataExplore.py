import pandas as pd  
pd.options.mode.chained_assignment = None

df = pd.read_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/PreprocessedVisitsLong_new.csv')
df = df.drop_duplicates('PtID')
fullCount = df['PtID'].count()

def getGenderCount(df):

    countF = df[df['Pt_Gender'] == 'F']['PtID'].count()
    countM = df[df['Pt_Gender'] == 'M']['PtID'].count()
    countNA = df[df['Pt_Gender'] == 'NA']['PtID'].count()
    countT = df[df['Pt_Gender'] == 'T']['PtID'].count()

    print('Female percentage: ',countF/fullCount*100)
    print('Male percentage: ',countM/fullCount*100)
    print('Transgender percentage: ',countT/fullCount*100)

def getAgeCounts(df):
    
    countTeenagers = df[df['age'] <= 19]['PtID'].count()
    countAdults = df[df['age'] > 19]['PtID'].count()

    print('lessthan 19 kids percentage: ',countTeenagers/fullCount*100)
    print('Adults percentage: ',countAdults/fullCount*100)

def getAnnualIncome(df):
    # df['Pt_AnnualInc'] =  df['Pt_AnnualInc'].str.replace(r'$', '')

    # print(df['Pt_AnnualInc'])

    # df['Pt_AnnualInc'] = pd.to_numeric(df['Pt_AnnualInc'], errors='coerce')
    # df = df.dropna(subset=['Pt_AnnualInc'])
    # df['Pt_AnnualInc'] = df['Pt_AnnualInc'].astype(int)

    countLevel1 = df[df['Pt_AnnualInc'] == 'Less than 25,000']['PtID'].count()
    countLevel2 = df[df['Pt_AnnualInc'] == '$25,000 - $35,000']['PtID'].count()
    countLevel3 = df[df['Pt_AnnualInc'] == "$35,000 - less than $50,000"]['PtID'].count()
    countLevel4 = df[df['Pt_AnnualInc'] == '$50,000 - less than $75,000']['PtID'].count()
    countLevel5 = df[df['Pt_AnnualInc'] == '$75,000 - less than $100,000']['PtID'].count()
    countLevel6 = df[df['Pt_AnnualInc'] == '$100,000 - less than $200,000']['PtID'].count()
    countLevel7 = df[df['Pt_AnnualInc'] == '$200,000 or more']['PtID'].count()


    print('lessthan 25000 percentage: ',countLevel1/fullCount*100)
    print('25-35 percentage: ',countLevel2/fullCount*100)
    print('35-50 percentage: ',countLevel3/fullCount*100)
    print('50-75 percentage: ',countLevel4/fullCount*100)
    print('75-100 percentage: ',countLevel5/fullCount*100)
    print('100-00 percentage: ',countLevel6/fullCount*100)
    print('200+ percentage: ',countLevel7/fullCount*100)



def getbmi(df):
    underweight = df[df['bmi'] < 18.5]['PtID'].count()
    healthy = df[(df['bmi'] >= 18.5) & (df['bmi'] < 25)]['PtID'].count()
    overweight = df[(df['bmi'] >= 25) & (df['bmi'] < 30)]['PtID'].count()
    obesity = df[df['bmi'] >= 30 ]['PtID'].count()

    print('underweight: ', underweight/fullCount*100)
    print('healthy: ', healthy/fullCount*100)
    print('overweight: ', overweight/fullCount*100)
    print('obesity: ', obesity/fullCount*100)

def getMaxvalues(df, colName):
    column = df[colName]
    max_value = column.max() 
    return max_value

def getMinvalues(df, colName):
    column = df[colName]
    min_value = column.min() 
    return min_value

def getAverage(df, colName):
    column = df[colName]
    avg_value = column.mean() 
    return avg_value

def patientsContinueStudieIn5Yrs():
    df = pd.read_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/PreprocessedVisitsLong_new.csv')
    df = df.loc[(df['Visit'] == 'Enrollment1')]
    df = df.drop_duplicates('PtID')
    fullCount = df['PtID'].count()
    print(fullCount)

def getIdListVisit():
    df = pd.read_csv('/home/kali/Documents/thesis/Preprocessing_codes/focus dataset/Registry - Longitudinal/preFiles/PreprocessedVisitsLong_new.csv')
    # df = df.loc[(df['Visit'] == 'Enrollment1') | (df['Visit'] == 'Enrollment2')]
    df1 = df[df['Visit'].isin(['Enrollment1'])]
    df2 = df[df['Visit'].isin(['Year 5'])]

    
    # print(df.head())
    df1 = df1.drop_duplicates('PtID')
    df2 = df2.drop_duplicates('PtID')

    df_merge = pd.merge(df1, df2, on=['PtID'], how='inner')
  
    fullCount1 = df_merge['PtID'].count()

    print(fullCount1)
   

getIdListVisit()
# getGenderCount(df)
# print('----------------------------------')
# getAgeCounts(df)
# print('Maximum age: ', getMaxvalues(df,'age'))
# print('Minimum age: ', getMinvalues(df,'age'))
# print('Average age: ', getAverage(df,'age'))

# print('----------------------------------')
# getAnnualIncome(df)
# print('----------------------------------')
# getbmi(df)
# print('----------------------------------')

