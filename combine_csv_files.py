from os import listdir
import pandas as pd

def combine_csv(path,filename):
    """
    simple python program to combine all .csv files into one single .csv file
    see also : https://www.freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854/
    
    #path = path to the directory containing csv files - close path without a slash
    #filename = desired file name, must end with .csv
    """
    
    files = [path+"/"+f for f in listdir(src) if f.endswith(".csv")] # in a list comprehension, loop through all files that end with .csv given path
    combined = pd.concat([pd.read_csv(f) for f in files]) #concatenate all lines read from a list comprehension that reads multiple .csv files
    assert filename.endswith(".csv"), "Incorrect file format. Must end filename with .csv" #sanity check - check if the filename has the correct extension
    combined.to_csv(path+"/"+ filename, index=False,encoding="utf-8-sig") #output