from re import I
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from function_Reduction import *
from class_mainFrame import *
import tkinter.messagebox as msgbox

class ReductionBox():
    def __init__(self, root):
        df = root.getData()
        window =  tk.Tk()
        self.options = {}
        amount_missing = tk.StringVar()
        cols = ["Column Not Selected "] + list(filterNumeric(df).columns)
        wrapper = tk.LabelFrame(window, text="Select Column")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper2 = tk.LabelFrame(window, text="Select Options")
        wrapper2.pack(padx = 10, pady = 10, fill = "both", expand= "yes")

        label1 = tk.Label(wrapper, text = "Column   :")
        label1.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo = ttk.Combobox(wrapper, height = 15, values = cols, width=30)
        mycombo.current(0)
        mycombo.grid(row = 0, column = 1)
  
        def selectcolumn_reduct():
            global select_reduct_column
            select_reduct_column = mycombo.get()
            print(select_reduct_column)
        btn_selectData = tk.Button(wrapper, text = "Select", command = selectcolumn_reduct)
        btn_selectData.grid(row = 0, column = 2, padx = 5, pady = 5)

        redction_method = ["데이터 범주화"]

        label2 = tk.Label(wrapper, text = "축소 방법   :")
        label2.grid(row=1, column=0, padx = 10, pady = 10)
        
        mycombo1 = ttk.Combobox(wrapper, height = 15, values = redction_method, width=30)
        mycombo1.current(0)
        mycombo1.grid(row = 1, column = 1)     

        def selectmethod_reduct():
            global select_reduction_method
            select_reduction_method = mycombo1.get()
            print(select_reduction_method)
        btn_selectmethod = tk.Button(wrapper, text = "Select", command = selectmethod_reduct)
        btn_selectmethod.grid(row = 1, column = 2, padx = 5, pady = 5)

        lbl1 = tk.Label(wrapper2, text = "데이터 범주의 개수   :")
        lbl1.grid(row=0, column=0, padx = 10, pady=10)
        entry1 = tk.Entry(wrapper2, text="개수를 입력하세요.")
        entry1.grid(row=0, column=1, padx = 10, pady=10)
        def divide_num_get():
            global num
            num = entry1.get()
            print(num)
        btn_selectmethod1 = tk.Button(wrapper2, text = "Enter", command = divide_num_get)
        btn_selectmethod1.grid(row = 0, column = 2, padx = 5, pady = 5)     

        lbl2 = tk.Label(wrapper2, text = "데이터 범주의 기준값   :")
        lbl2.grid(row=1, column=0, padx = 10, pady=10)
        entry2 = tk.Entry(wrapper2, text="기준값을 큰 순서대로 입력하세요.")
        entry2.grid(row=1, column=1, padx = 10, pady=10)
        lbl2_1 = tk.Label(wrapper2, text ="기준값을 큰 순서대로 입력하세요.")
        lbl2_1.grid(row=1, column=3, padx =10, pady=10)
        bins = []
        def divide_point_get():
            global i
            i = 0
            bins.insert(0, float(entry2.get()))
            print(bins)
            print(bins[0])

            i= i+1
        btn_selectmethod2 = tk.Button(wrapper2, text = "Enter", command = divide_point_get)
        btn_selectmethod2.grid(row = 1, column = 2, padx = 5, pady = 5)   

        lbl3 = tk.Label(wrapper2, text = "데이터 범주의 이름   :")
        lbl3.grid(row=2, column=0, padx = 10, pady=10)
        entry3 = tk.Entry(wrapper2, text="범주의 이름을 큰 순서대로 입력하세요.")
        entry3.grid(row=2, column=1, padx = 10, pady=10)
        lbl3_1 = tk.Label(wrapper2, text ="범주의 이름을 큰 순서대로 입력하세요.")
        lbl3_1.grid(row=2, column=3, padx =10, pady=10)
        labels = []
        def divide_name_get():
            global j    
            j = 0
            labels.insert(0,entry3.get())
            print(labels)
            print(labels[0])
            j =j+1
        btn_selectmethod3 = tk.Button(wrapper2, text = "Enter", command = divide_name_get)
        btn_selectmethod3.grid(row = 2, column = 2, padx = 5, pady = 5) 
        #로그창에서 bins와 lables 확인할 수 있게 확인 ?


        def reduction():
            if(select_reduction_method=='데이터 범주화'):
                print(bins)
                print(labels)
                df['{}'.format(select_reduct_column)] = def_data_divide(df, select_reduct_column,num,bins,labels)
                print(df)
                j =0
                i =0
                info()
        btn_selectData = tk.Button(window, text = "OK", command = reduction)
        btn_selectData.pack()
        def info():
            msgbox.showinfo("알림", "정상적으로 처리 되었습니다.")
        def warn():
            msgbox.showwarning("경고", "오류가 발생했습니다.")

        window.title("ReductionBox")
        window.geometry("640x400")
        window.resizable(False, False)
        window.mainloop()
