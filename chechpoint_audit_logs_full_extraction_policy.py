import pandas as pd
import os
import sys
from datetime import datetime
from zipfile import ZipFile



def Find_csv_file():
    
    for file in os.listdir():
        
        if file.endswith(".csv"):
            print("File CSV "+file+" read correctly""\n")
            return file
            break
            
    print("No .CSV files found in the folder""\n")
    return False
    


def Extract_zip_file():
    
    for f in os.listdir():
        
        if f.endswith(".zip"):
            zip = ZipFile(f)
            zip.extractall()
            
            return print("File ZIP "+f+" extracted correctly""\n")
            break
    
    print("No .ZIP files found in the folder""\n")
    return False


def File_exist(F1,F2):
    
    if F1:
        return F2
    elif F2:
        return F2               
    else:  
        return sys.exit()  

"""###ESTRAZIONE POLICY DA CSV"""
print("                                             ")
print("*********************************************")
print("*********************************************")
print("    SCRIPT DI ESTRAZIONE POLICY DA LOG       ")
print("*********************************************")
print("*********************************************")
print("            BY SIMONE ERRIU                  ")
print("                                             ")
print("*********************************************")
print("                                             ")
print("                                             ")    


file = File_exist(Extract_zip_file(),Find_csv_file())
df_csv = pd.read_csv(file)
changes_col = df_csv["Changes"]
word_to_find_start = "Layer Name:"
word_to_find_end = "Policy Names:"
now = datetime.now()
today = now.strftime("%d_%m_%Y_%H_%M_%S")
file_name = 'Policy_to_install_'+today+'.txt'
policy_list = []
list_to_print =[]



for index, word in changes_col.items():
    
    if word_to_find_start in str(word):
        #find index of word to find
        word_index_start = word.find(word_to_find_start)
        word_index_end = word.find(word_to_find_end)
        #save raw txt in policy_raw variable
        policy_raw = word[word_index_start:word_index_end]
        #clean the raw policy
        clean_word = policy_raw.split(" ")[2][1:]
        #take index of cma ploicy
        try:
            df_csv.loc[index,"Domain"],
        except KeyError:
            print("Error: CSV file extracted in wrong version, download FULL version from SmartView, column ""Domain"" is missing \n")
            sys.exit()
        
        domains = df_csv.loc[index,"Domain"]
               
        #create toupla to print
        policy = domains, clean_word
        #append value to a list
        policy_list.append(list(policy))

policy_list.sort()
#take unique values form list      
for i in policy_list:
    if i not in list_to_print:
        list_to_print.append(i)

with open(file_name , 'w+') as f:
    
    print("Policy extraction of  "+today+"\n")
    f.write("Policy extraction of  "+today+"\n")
    
    for cma, pol in list_to_print:

        print("["+cma+"]\t" + pol)
        f.write("["+cma+"]\t"+pol + "\n")
        
        

