from tkinter import *
import tkinter.ttk as ttk
from unicodedata import category
from read_csv import *
import pandas as pd
import numpy as np
from TransformationBox import *

root = Tk()
root.title("Auto Preprocessing")
root.geometry("600x720") #가로*세로 + (x좌표 + y 좌표)
root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경불가)


wrapper = LabelFrame(root, text="데이터 확인")
wrapper.grid(row = 0, column = 0, padx = 5, pady = 5)

dataPath, file_list = get_datalist()
combobox = ttk.Combobox(wrapper, height = 5, width=60, values = file_list)
combobox.current(0)
combobox.grid(row = 0, column = 0, padx = 5, pady = 5)


def selectData():
    global data_name, data, df
    data_name = combobox.get()
    data = pd.read_csv(data_name)
    df = pd.DataFrame(data)
    cols = list(df.columns)
btn_selectData = Button(wrapper, text = "Select", command = selectData)
btn_selectData.grid(row = 0, column = 1, padx = 5, pady = 5)

def view():
    tableView = Tk()
    tree = ttk.Treeview(tableView)
    tree.pack()
    cols = list(df.columns)
    tree["columns"] = cols
    for i in cols:
        tree.column(i, anchor="w")
        tree.heading(i, text=i, anchor='w')
    for index, row in df.iterrows():
        tree.insert("",0,text=index,values=list(row))
btn_view = Button(wrapper, text = "View", command = view)
btn_view.grid(row = 0, column = 2, padx = 5, pady = 5)

def viewdetails():
    pass
btn_viewdetails = Button(wrapper, text = "Viewdetails", command = viewdetails)
btn_viewdetails.grid(row = 1, column = 1, padx = 5, pady = 5)

wrapper2 = LabelFrame(root, text="데이터 처리")
wrapper2.grid(row = 1, column = 0,padx = 5, pady = 5)



class CleaningBox():
    def __init__(self):
        window =  Tk()

        amount_missing = StringVar()
        check_drop = IntVar()

        wrapper = LabelFrame(window, text="Select Column")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper2 = LabelFrame(window, text="Select Options")
        wrapper2.pack(padx = 10, pady = 10, fill = "both", expand= "yes")

        cols = ["column 1", "column 2", "column 3"]
        options = ["Drop Check", "Column Name", "Data Type", "Number of Missing",  "Handle Missing Values"]
        
        label1 = Label(wrapper, text = "Column")
        label1.grid(row=0, column=0, padx = 10, pady = 10)
        
        mycombo = ttk.Combobox(wrapper, height = 15, values = cols, width=30)
        mycombo.current(0)
        mycombo.grid(row = 0, column = 1)

        lbl1 = Label(wrapper2, text = "Data Type")
        lbl1.grid(row=0, column=0, padx = 10, pady=10)
        datatypes = ["Numeric", "Categorical", "Datetime"]
        combo1 = ttk.Combobox(wrapper2, height = 15, values = datatypes, width = 30)
        combo1.grid(row=0, column=1, padx=10, pady=10)

        lbl2 = Label(wrapper2, text = "# of Missing Values :")
        lblMissingValues = Label(wrapper2, text = amount_missing)
        lbl2.grid(row=1, column=0, padx = 10, pady=10)
        lblMissingValues.grid(row=1, column=1, padx = 10, pady=10)

        lbl3 = Label(wrapper2, text = "Handle Missing Values")
        lbl3.grid(row=2, column=0, padx = 10, pady=10)

        handleMissingVals = ["Replacing With Mean", "Replacing With Median", "Others..."]
        combo2 = ttk.Combobox(wrapper2, values = handleMissingVals, height = 15,  width = 30)
        combo2.grid(row=2, column=1, padx=10, pady = 10)

        lbl4 = Label(wrapper2, text = "Drop Check")
        lbl4.grid(row=3, column=0, padx = 10, pady=10)

        checkBox1 = Checkbutton(wrapper2, variable=check_drop)
        checkBox1.grid(row=3, column=1, padx = 10, pady=10)

        window.title("CleaningBox")
        window.geometry("720x300")
        window.resizable(False, False)
        window.mainloop()

        



def btn_data_cleaning():
    c_box = CleaningBox()

btn_select_cleaning = Button(wrapper2, text = "데이터 정제", command = btn_data_cleaning)
btn_select_cleaning.grid(row = 0, column = 0, padx = 5, pady = 5)


wrapper3 = LabelFrame(root, text="데이터 저장")
wrapper3.grid(row = 2, column = 0,padx = 5, pady = 5)

e = Entry(wrapper3, width=30)
e.grid(row = 0, column = 0, padx = 5, pady = 5)
e.insert(0, "파일명을 입력하세요")
def save():
    print(e.get())
btn = Button(wrapper3, text="Save", command=save)
btn.grid(row = 0, column = 1, padx = 5, pady = 5)




def btn_data_Transformation():
    t_box = TransformationBox()

btn_select_transformation = Button(wrapper2, text = "데이터 변환", command = btn_data_Transformation)
btn_select_transformation.grid(row = 0, column = 1, padx = 5, pady = 5)



wrapper3 = LabelFrame(root, text="데이터 저장")
wrapper3.grid(row = 2, column = 0,padx = 5, pady = 5)

e = Entry(wrapper3, width=30)
e.grid(row = 0, column = 0, padx = 5, pady = 5)
e.insert(0, "파일명을 입력하세요")
def save():
    print(e.get())
btn = Button(wrapper3, text="Save", command=save)
btn.grid(row = 0, column = 1, padx = 5, pady = 5)


'''
def ToDataclean():    
    category_1 = ["결측치 처리", "이상치 처리"] 
    method_1 = ["해당 데이터 삭제", "평균값 적용"]
    method_2 = ["구간화 적용", "군집화 적용"]
    global my_category
    global my_method
    combobox_clean_category = ttk.Combobox(root, height=5, values=category_1)
    combobox_clean_category.pack()

    def category_clean_select() :
        my_category = combobox_clean_category.get()
        print(my_category)
        
        if(my_category == "결측치 처리") :
            method_missing_value_select()  
        if(my_category == "이상치 처리") :
            method_noisy_value_select()
        else :
            pass
    def method_missing_value_select():
        combobox_clean_method = ttk.Combobox(root, height=5, values=method_1)
        combobox_clean_category.destroy()
        category_btn.destroy()
        combobox_clean_method.pack()
        method_btn_1 = Button(root, text = "Select" )#, command = 결측치 처리 함수 연결)
        method_btn_1.pack()


    def method_noisy_value_select():
        combobox_clean_method = ttk.Combobox(root, height=5, values=method_2)
        combobox_clean_category.destroy()
        category_btn.destroy()
        combobox_clean_method.pack()
        method_btn_2 = Button(root, text = "Select") #, command = 이상치 처리 함수 연결)
        method_btn_2.pack()


    
    category_btn = Button(root, text = "Select", command = category_clean_select)
    category_btn.pack()
    

def ToDataintergration() :

    nextbtn = Button(root, text = "Next", command = ToDataReduction)
    print("ToDataintergration")
    

def ToDataReduction():

    nextbtn = Button(root, text = "Next", command = ToDatatransformation)
    print("ToDataReduction")

def ToDatatransformation():

    nextbtn = Button(root, text = "Next", command = ToDataintergration)
    print("ToDatatransformation")





def show_table(data):
        global df
        print(data_name)
        
#show_table(data)
#page1
'''

root.mainloop()