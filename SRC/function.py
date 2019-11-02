# write your functions here:
import re 

def renameF(df,column,old,new):
    df[column] = df[column].replace(old, new)

def findF(f_list,key_word,values):
    for i in values:
        if re.search(key_word,i):
            f_list.append(i)
    return f_list


def find_Time(df,column,time,t,keyword,newword):
    if re.search("(?i)"+keyword,time):
            df[column][t] = newword

def Fatality(df,injuries):
    fatal = ["fatal","kill","die","drown","remain","death","swept","recover"]
    survive = ["injur","bitten","lacer","sever","surv","scrape","punc","marks","bit","cut","lost","serious","not recovered","wound","slash","Strip","bruise","abrasion"]
    for i in range(0,len(injuries)):
        for fat in fatal:
            for surv in survive:
                if re.search("(?i)"+fat,injuries[i]):
                    df["Injury"][i] = "Fatal"
                elif re.search("(?i)"+surv,injuries[i]):
                    df["Injury"][i] = "Survived"
                else:
                    df["Injury"][i] = "Unknown"