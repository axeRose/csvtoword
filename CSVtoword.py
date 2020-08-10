import random
import time
import csv
import pandas as pd
from docxtpl import DocxTemplate

# Source CSV - column names that must match the *** that are {{***}} inside "template.docx"
csvtest = "FB_ads.csv"

def mainfun(n,fname):
    tpl = DocxTemplate("Testtemplate.docx") # In same directory
    df = pd.read_csv(csvtest)
    df_to_doct = df.to_dict() # dataframe -> dict for the template render
    x = df.to_dict(orient='records')
    context = x
    tpl.render(context[n])
    tpl.save("%s.docx" %fname)

    # Wait a random time - increase to (60,180) for real production run.
    wait = time.sleep(random.randint(1,2))

#-------------------Main---------------------#

df2 = len(pd.read_csv(csvtest))

print ("There will be ", df2, "files")

for i in range(0,df2):
    df = pd.read_csv(csvtest)
    columnsData = df.loc[ : , 'Campaign name' ]
    fname = columnsData[i]
    print("Making file: ",f"{fname}," ,"..Please Wait...")
    mainfun(i,fname)

print("Done! - Now check your files")
