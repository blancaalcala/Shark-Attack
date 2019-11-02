# write your functions here:
import re 

def renameF(df,column,old,new):
    df[column] = df[column].replace(old, new)
    return df[column]

def findF(f_list,key_word,values):
    for i in values:
        if re.search(key_word,i):
            f_list.append(i)
    return f_list


def find_Time(df,column,time,t,keyword,newword):
    if re.search("(?i)"+keyword,time):
            df[column][t] = newword