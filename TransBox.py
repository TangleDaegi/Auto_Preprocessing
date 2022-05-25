import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from function_Trans import *
from class_mainFrame import *

class TransBox():
    def __init__(self, root):
        df = root.getData()
        window =  tk.Tk()
        self.options = {}
        amount_missing = tk.StringVar()
        check_drop = tk.IntVar()
        cols = list(df.columns)  

        wrapper = tk.LabelFrame(window, text="데이터 변환 방법 선택")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper2 = tk.LabelFrame(window, text="세부사항 선택")
        wrapper2.pack(padx = 10, pady = 10, fill = "both", expand= "yes")

        scl_method = ["StandardScaler", "MinMaxScaler"]  #"RobustScaler", "MaxAbsScaler" 추가 ?

        label1 = tk.Label(wrapper, text = "변환 방법 :")
        label1.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo = ttk.Combobox(wrapper, height = 15, values = scl_method, width=30)
        mycombo.current(0)
        mycombo.grid(row = 0, column = 1, padx = 5, pady = 5)



        def selectData():
            global transformation_method
            transformation_method = mycombo.get()
            print(transformation_method)
            if(transformation_method=="StandardScaler"):
                lbl1 = tk.Label(wrapper, text = "data들을 표준 정규화 한다.")
                lbl1.grid(row=1, column=3, padx = 5, pady=5)
            elif(transformation_method=="MinMaxScaler"):
                lbl1 = tk.Label(wrapper, text = "data들을 0~1 사이 범위에 정규화 한다.")
                lbl1.grid(row=1, column=3, padx = 5, pady=5)

        btn_selectData = tk.Button(wrapper, text = "Select", command = selectData)
        btn_selectData.grid(row = 0, column = 2, padx = 5, pady = 5)

        cols_trans = list(df.columns)
        label2 = tk.Label(wrapper2, text = "Column :")
        label2.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo2 = ttk.Combobox(wrapper2, height = 15, values = cols_trans, width=30)
        mycombo2.current(0)
        mycombo2.grid(row = 0, column = 1)

        def selectcolumn():
            global select_trans_column
            select_trans_column = mycombo2.get()
            print(select_trans_column)

        btn_selectData = tk.Button(wrapper2, text = "Select", command = selectcolumn)
        btn_selectData.grid(row = 0, column = 2, padx = 5, pady = 5)
        def trans():
            if(transformation_method=="StandardScaler"):
                df['{}'.format(select_trans_column)] = def_StandardScaler(df, select_trans_column)
                print(df)
            elif(transformation_method=="MinMaxScaler"):
                df['{}'.format(select_trans_column)] = def_MinMaxScaler(df, select_trans_column)
                print(df)
            else: pass
        btn_selectData = tk.Button(wrapper2, text = "변환", command = trans)
        btn_selectData.grid(row = 1, column = 6, padx = 5, pady = 5)
        
        window.title("TransformationBox")
        window.geometry("720x300")
        window.resizable(False, False)
        window.mainloop()

#t_box = TransformationBox()

