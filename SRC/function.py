# write your functions here:
import re 


def Check_names(names):
    names = names.strip()
    if re.search("male*",names) or re.search("boy.*",names) or re.search("nan$",names):
        names = "Unknown"
    elif re.search("Occupant:+",names):
        names = re.sub("Occupant: ","",names)
        names = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+",names)
    elif re.search("[A-Z][a-z]+\s[A-Z][a-z]+",names):
        x = re.search("[A-Z][a-z]+\s[A-Z][a-z]+",names)
        names = x.group(0)
    else:
        names = "Unknown"
    return names


def renameF(df,column,old,new):
    df[column] = df[column].replace(old, new)
    

def findF(values,key_word):
    if re.search("(?i)"+key_word+".+",values):
        return values


def find_Time(df,column,time,t,keyword,newword):
    if re.search("(?i)"+keyword,time):
            df[column][t] = newword

def Fatality(fatality):
    unknown = ["unknown","0","#VALUE!"]
    n_fatal = [" N","n","N "]
    y_fatal = ["F"]
    survival = []
    for f in range(0,len(fatality)):
        fatal = fatality[f]
        for u in unknown:
            if re.match("(?i)"+u,fatal):
                fatality[f] = ("Unknown")
        for n in n_fatal:
            if re.match("(?i)"+n,fatal):
                fatality[f] = ("N")
        for y in y_fatal:
            if re.match("(?i)"+y,fatal):
                fatality[f] = "Y"
        if fatality[f]!="Y" and fatality[f]!="N" and fatality[f]!="Unknown":
            fatality[f] = "Unknown"
    return fatality