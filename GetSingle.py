"""
Code : Extracting a row of data from raw excel sheet and create multiple docx suign different row inputs
Authour :Hardik Gadher
Date : 30/05/2022
Location: Berlin

"""
import pandas as pd
from docx import Document
import os, os.path
import tkinter as tk
from tkinter import simpledialog

#initializing a dataframe from raw file
df01 = pd.read_excel ( 'Raw data.xlsm' )

#Input window
ROOT = tk.Tk()
ROOT.withdraw()
Rownumber = simpledialog.askstring(title="Test", prompt=f'Which row number you want to print? Please enter between 0 to {len(df01)}')
Rownumber = int(Rownumber)

Probe = Document ( 'Router.docx' )
table = Probe.tables[0]
df01['Router No'] = df01['Router No'].astype ( 'int' )
table.cell ( 0, 1 ).text = str ( df01['Router No'][Rownumber - 1].item () )

table.cell ( 1, 1 ).text = str ( df01['Order Number'][Rownumber - 1].item () )
table.cell ( 0, 3 ).text = str ( df01['Description'][Rownumber - 1] ) + ' / ' + str ( df01['Size'][Rownumber - 1] )
table.cell ( 0, 5 ).text = str ( df01['Article No'][Rownumber - 1] )
table.cell ( 1, 5 ).text = str ( df01['Product Id'][Rownumber - 1] ) + ', ' + str (df01['Article No'][Rownumber - 1] ) + ', ' + str (df01['Revision'][Rownumber - 1] )
table.cell ( 0, 7 ).text = str ( (df01['Lot No'][Rownumber - 1]).item () ) + ', ' + str ((df01['Quantity'][Rownumber - 1]).item () )
table.cell ( 1, 7 ).text = str ( df01['Expiry Date'][Rownumber - 1] )
Router_number = table.cell ( 0, 1 ).text
if not os.path.exists(f'C:\\Personal\\Aufgaben\\Code\\1\\{Router_number}'):
    path = os.path.join('C:\\Personal\\Aufgaben\\Code\\1',f'{Router_number}')
    os.mkdir(path)
Probe.save(f'C:\\Personal\\Aufgaben\\Code\\1\\{Router_number}\\{Router_number}.docx')