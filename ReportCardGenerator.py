##################################################
## This script generates a report of an exam with section wise marks for all students appeared in exam by taking data from CSV
##################################################
## Author: Pennada S V Naga Sai
## Email: psvnagasai@gmail.com
##################################################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.text
from pandas import Series,DataFrame
import pandas as pd
from matplotlib import patches
import fitz
from fitz.utils import insertImage

#function will be used later for integrating with a dictionary
def Merge(stat, profile): 
    return(profile.update(stat))

#iterating over the csv file rows
dt = pd.read_csv("D:\Ken related\HazCom_students\Project\interface\data.csv", index_col='ID') 
for i in dt.index:
    
    marks = list(dt.iloc[i-1,4:9])
    score = sum(marks) 
    if score <= 10 :
        remark = 'Poor'
    elif score >10 and score <=20 :
        remark = 'Good'
    else :
        remark = ' Excellent'
    
#Report Analysis (marks 1,2,3,4,5 are different subjects)
    marks1 = list(dt.iloc[i-1,4:5])
    score = sum(marks1)
    if score ==0 :
        retort1 = "Needs improvement. Your speed is average. A little work on\n your speed management will help you in solving more number of questions\n accurately."
    elif score in range(1,6):
        retort1 ="Your speed is average. A little work on your speed management\n will help you in solving more number of questions accurately."
    elif score in range(6,10):
        retort1 ="Your speed is good and you have a good presence of mind.\n Maintaining accuracy can fetch you a better score."
    else :
        retort1 = "You have excellent speed and accuracy."
        
    marks2 = list(dt.iloc[i-1,5:6])
    score = sum(marks2)
    if score ==0 :
        retort2 = "Needs improvement.Try to find a smart and organized approach to\n score more."
    elif score in range(1,7):
        retort2 ="Your consistency is good. Try to find a smart and organized\n approach to score more."
    else :
        retort2 = "Your consistency and accuracy are excellent and you have an\n organized approach towards questions."
        
        
        
    marks3 = list(dt.iloc[i-1,6:7])
    score = sum(marks3)
    if score ==0 :
        retort3 = "Improvement in speed and method of solving is needed."
    elif score in range(1,4):
        retort3 ="You have a good logical approach. Improvement in speed and method\n of solving is needed."
    else :
        retort3 = "Your logical approach and method of solving the questions is \nexcellent."
        
        
        
    marks4 = list(dt.iloc[i-1,7:8])
    score = sum(marks4)
    if score ==0 :
        retort4 = "Needs improvement. More effort in accuracy is required."
    elif score in range(1,6):
        retort4 ="Your logic was moderate. More effort in accuracy is required."
    elif score in range(6,11):
        retort4 ="You have a good balance between logic and accuracy."
    else :
        retort4 = "You have an excellent balance between logic and accuracy. Along with\n that, you have made a good use of bonus marking."
    
    
    
    
    marks5 = list(dt.iloc[i-1,8:9])
    score = sum(marks5)
    if score ==0 :
        retort5 = "Needs improvement in accuracy."
    elif score >=1 and score <= 2.5:
        retort5 ="You have a good logic but you need to work a bit more on accuracy."
    else :
        retort5 = "You have an excellent balance between finding the trick and solving\n the question accurately."
    
    
#Using the function from the beginning to create a new dataframe suitable for plotting
    stat = {'Section':['A', 'B', 'C', 'D','E'], 'Marks':marks, 'Remark':remark , "Retort1": retort1, "Retort2": retort2,"Retort3": retort3,"Retort4": retort4,"Retort5": retort5}

    profile = dict(dt.iloc[i-1,0:4])
    Merge(stat, profile)
    df = pd.DataFrame(profile)
    
    
#using matplotlib as a canvas to plot the data ad pie chart
    
    plt.figure(figsize=(10,20))
    colors = ['#3B4D85', '#E5FFC9', '#000800', '#BDCDFF', '#9ACC64']
    ay = plt.pie(marks, labels=stat['Section'], colors=colors, autopct='%.1f%%', shadow= True, startangle=140)
    plt.title('Students Marks')
    plt.axis('equal')
    
    plt.annotate('Name - ' + profile['NAME'],
            xy=(.10,1000), xycoords='axes points',fontsize=17)
    plt.annotate('School - ' + profile['SCHOOL NAME'],
            xy=(.10, 970), xycoords='axes points',fontsize=13)
    plt.annotate('Contact - ' + str(profile['CONTACT NO.']),
            xy=(.10, 940), xycoords='axes points',fontsize=13)
    plt.annotate('ROUND 1 Test: Report Analysis',
            xy=(120, 850), xycoords='axes points',fontsize=20)
    plt.annotate('SectionA - ' + profile['Retort1'],
            xy=(0, 200), xycoords='axes points',fontsize=15)
    plt.annotate('SectionB - ' + profile['Retort2'],
            xy=(0, 150), xycoords='axes points',fontsize=15)
    plt.annotate('SectionC - ' + profile['Retort3'],
            xy=(0, 100), xycoords='axes points',fontsize=15)
    plt.annotate('SectionD - ' + profile['Retort4'],
            xy=(0, 50), xycoords='axes points',fontsize=15)
    plt.annotate('SectionE - ' + profile['Retort5'],
            xy=(0, 0), xycoords='axes points',fontsize=15)
    
#Saving the file as pdf
    myfile = profile['NAME']
    plt.savefig(myfile+'.pdf')
    
#opening the file again to add an image at the top
    doc = fitz.open(myfile + '.pdf')
    rect= fitz.Rect(0,0,1000,210)
    for page in doc:
         page.insertImage(rect, filename="D:\\Ken related\HazCom_students\Project\interface\dex.jpg")
    doc.saveIncr()
    
#########################################################################

