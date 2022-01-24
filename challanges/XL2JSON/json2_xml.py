from pprint import pprint
import os
import json
import csv
import pandas as pd
import win32com.client as win32 # pip install pywin32

#json_data = json.loads(open('data.json').read())
#pprint(json_data)
x = """{
    "groups":[{
         "group_name":"GROUP_ALPHA",
         "members":[{
                  "person_name": "Vincent Casta" ,
                  "email": "vincent.casta@student.bxl.be"}
                  ,{
                  "person_name": "Giovanni Di Tulio",
                  "email":"Giovanni.ditullio@student.bxl.be "     
                  
                  }, {
                  "person_name": "Milain VandeVelde" ,
                  "email":"Milan.Vanvelde@student.bxl.be"     
                                  
         }]
    }]
}"""
#string naar json object
json_data = json.loads(x)

#loop in data om de rijen te formateren.
rows = []
for x3 in json_data["groups"]:
    group = x3["group_name"]
    for x4 in x3["members"]:
        name = x4["email"]
        email = x4["person_name"]
        rows.append([group,email,name]) 
  
 #open excel app   
ExcelApp = win32.Dispatch('Excel.Application')
ExcelApp.Visible = True


wb = ExcelApp.Workbooks.Add()
ws = wb.Worksheets(1)

header_labels = ('group', 'email', 'name')

# insert header labels
for indx, val in enumerate(header_labels):
    ws.Cells(1, indx + 1).Value = val

# insert Records
row_tracker = 2
column_size = len(header_labels)

for row in rows:
    ws.Range(
        ws.Cells(row_tracker, 1),
        ws.Cells(row_tracker, column_size)
    ).value = row
    row_tracker += 1

wb.SaveAs(os.path.join(os.getcwd(), 'output.xlsx'), 51)
wb.Close()
ExcelApp.Quit()
ExcelApp = None

