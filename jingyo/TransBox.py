import tkinter as tk
import tkinter.ttk as ttk
from turtle import right
import pandas as pd
from function_Trans import *
from class_mainFrame import *
import tkinter.messagebox as msgbox
class TransBox():
    def __init__(self, root):
        df = root.getData()
        window =  tk.Tk()
        self.options = {}
        self.log = []

        cols = list(df.columns)
        for c in cols:
            self.options[c] = ['Default', 'Do Nothing', 'Do Nothing']

        wrapper = tk.LabelFrame(window, text="Select Column")
        wrapper.grid(row=0, column = 0, rowspan=2, padx=10, pady=10, sticky="n", ipady = 30)
        wrapper2 = tk.LabelFrame(window, text="Select Options")
        wrapper2.grid(row=1, column = 1, rowspan=2, padx=10, pady=10, sticky="n", ipady = 30)

        wrapper3 = tk.LabelFrame(window, text= "Selected Options", relief="flat", bd=2, width=1000)
        wrapper3.grid(row=0, column = 1, rowspan=2, padx=10, pady=10, sticky="n", ipady = 30)
        self.treeview=ttk.Treeview(wrapper3, column = ["Time", "Column", "method"])
        self.treeview["columns"] = ["Time", "Column", "method"]
        self.treeview.column("#0", width=33)
        self.treeview.heading("#0", text="num")
        for i in range(len(self.treeview["columns"])):
            self.treeview.heading(self.treeview["columns"][i], text = self.treeview["columns"][i], anchor="w")
        self.treeview.column("#1", width = 109)
        self.treeview.column("#2", width = 100)
        self.treeview.pack()
        def insertLog(option):
            self.treeview.insert("", "end", text = len(self.log), values = option, iid=len(self.log))
        
        
        scl_method = ["StandardScaler", "MinMaxScaler", "MaxAbsScaler", "RobustScaler"]  #"RobustScaler", "MaxAbsScaler" 추가 ?

        label1 = tk.Label(wrapper2, text = "변환 방법   :")
        label1.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo = ttk.Combobox(wrapper2, height = 15, values = scl_method, width=30)
        mycombo.current(0)
        mycombo.grid(row = 0, column = 1, padx = 5, pady = 5)



        def selectData():
            global transformation_method
            transformation_method = mycombo.get()
            print(transformation_method)

        btn_selectData = tk.Button(wrapper2, text = "Select", command = selectData)
        btn_selectData.grid(row = 0, column = 2, padx = 5, pady = 5)

        cols_trans = ["Column Not Selected "] + list(filterNumeric(df).columns)
        label2 = tk.Label(wrapper, text = "Column   :")
        label2.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo2 = ttk.Combobox(wrapper, height = 15, values = cols_trans, width=30)
        mycombo2.current(0)
        mycombo2.grid(row = 0, column = 1)

        def selectcolumn():
            global select_trans_column
            select_trans_column = mycombo2.get()
            print(select_trans_column)

        btn_selectData = tk.Button(wrapper, text = "Select", command = selectcolumn)
        btn_selectData.grid(row = 0, column = 2, padx = 5, pady = 5)
        def info():
            msgbox.showinfo("알림", "정상적으로 처리 되었습니다.")
        def warn():
            msgbox.showwarning("경고", "오류가 발생했습니다.")

        
        def colOptions():
            colName = mycombo.get()
            self.options[colName] = [combo1.get(), combo2.get(), combo3.get()]
            insertLog((dt.datetime.now(), colName, combo1.get(), combo2.get(), combo3.get()))
            self.log.append((dt.datetime.now(), colName, combo1.get(), combo2.get(), combo3.get()))
            
        btnSaveOptions = tk.Button(wrapper2, text="Save Column Options", command=colOptions)






        def trans():
            if(transformation_method=="StandardScaler"):
                df['{}'.format(select_trans_column)] = def_StandardScaler(df, select_trans_column)
                print(df)
                info()
            elif(transformation_method=="MinMaxScaler"):
                df['{}'.format(select_trans_column)] = def_MinMaxScaler(df, select_trans_column)
                print(df)
                info()
            elif(transformation_method=="MaxAbsScaler"):
                df['{}'.format(select_trans_column)] = def_MaxAbsScaler(df, select_trans_column)
                print(df)
                info()
            elif(transformation_method=="RobustScaler"):
                df['{}'.format(select_trans_column)] = def_RobustScaler(df, select_trans_column)
                print(df)
                info()
            else:
                pass

        btn_selectData = tk.Button(window, text = "OK", command = trans)
        btn_selectData.pack()
        

        window.title("TransformationBox")
        window.geometry("440x400")
        window.resizable(False, False)
        window.mainloop()
