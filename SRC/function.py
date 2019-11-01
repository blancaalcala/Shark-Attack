# write your functions here:

def renameF(df,column,old,new):
    df[column] = df[column].replace(new, old)
    return df[column]

