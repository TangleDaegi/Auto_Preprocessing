from turtle import left
from CleaningBox import CleaningBox
from TransBox import *
from ReductionBox import *
from function_mainFrame import *
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd



class mainFrame():
    def __init__(self):
        self.dataPath, self.dataList = get_datalist()
        self.data = None
        self.dataName = ""

        root = tk.Tk()
        root.title("Auto Preprocessing")
        root.geometry("720x720") #가로*세로 + (x좌표 + y 좌표)
        root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경불가)
        wrapper = tk.LabelFrame(root, text="데이터 확인")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")

        
        combobox = ttk.Combobox(wrapper, height = 5, width=60, values = self.dataList)
        combobox.current(0)
        combobox.grid(row = 0, column = 0, padx = 5, pady = 5)

        def selectData():
            data_name = combobox.get()
            self.dataName = list(data_name.split("."))[0]
            e.insert(0, self.dataName + "_processed.csv")
            data = pd.read_csv(data_name)
            df = pd.DataFrame(data)
            self.data = df

        btn_selectData = tk.Button(wrapper, text = "Select", command = selectData)
        btn_selectData.grid(row = 0, column = 1, padx = 5, pady = 5)

        btn_view = tk.Button(wrapper, text = "View", command = self.view) 
        btn_view.grid(row = 0, column = 2, padx = 5, pady = 5)

        def viewdetails():
            pass
        btn_viewdetails = tk.Button(wrapper, text = "Viewdetails", command = viewdetails)
        btn_viewdetails.grid(row = 0, column = 3, padx = 5, pady = 5)


        btn_help = tk.Button(wrapper, text = "Interface_help", command = self.help_btn)
        btn_help.grid(row = 1, column = 1, padx = 5, pady = 5)

        step_help = tk.Button(wrapper, text = "Step_help", command = self.help_step)
        step_help.grid(row = 1, column = 2, padx = 5, pady = 5)

        wrapper2 = tk.LabelFrame(root, text="데이터 처리")
        wrapper2.pack(padx = 10, pady = 5, fill = "both", expand= "yes")


        def btn_data_cleaning():
            cbox = CleaningBox(self)
            pass
        btn_select_cleaning = tk.Button(wrapper2, text = "데이터 정제", command = btn_data_cleaning)
        btn_select_cleaning.grid(row = 0, column = 0, padx = 5, pady = 5)

        def btn_data_Transformation():
            tbox = TransBox(self)
            pass
        btn_select_cleaning = tk.Button(wrapper2, text = "데이터 변환", command = btn_data_Transformation)
        btn_select_cleaning.grid(row = 0, column = 1, padx = 5, pady = 5)

        def btn_data_Reduction():
            rbox = ReductionBox(self)
            pass
        btn_select_reduction = tk.Button(wrapper2, text = "데이터 축소", command = btn_data_Reduction)
        btn_select_reduction.grid(row = 0, column = 2, padx = 5, pady = 5)

        wrapper3 = tk.LabelFrame(root, text="데이터 저장")
        wrapper3.pack(padx = 10, pady = 5, fill = "both", expand= "yes")

        e = tk.Entry(wrapper3, width=30)
        e.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        def save():
            print(e.get())
            dataToCsv(self.data, self.dataPath, e.get())
        btn = tk.Button(wrapper3, text="Save", command=save)
        btn.grid(row = 0, column = 1, padx = 5, pady = 5)

        wrapper4 = tk.LabelFrame(root, text="상태 창")
        wrapper4.pack(padx = 10, pady = 5, fill = "both", expand= "yes")

        statusBox = tk.Label(wrapper4)
        statusBox.grid(row = 0, column = 0, padx = 5, pady = 5)

        def test_func():
            statusBox = tk.Label(wrapper4, text="작업이 정상적으로 처리되었습니다.")
            statusBox.grid(row=0, column=1, padx=5, pady=5)

        bttest = tk.Button(wrapper4, text="test", command=test_func)
        bttest.grid(row = 1, column = 1, padx = 5, pady = 5)

        root.mainloop()
        pass


               

    def modifyData(self, data):
        self.data = data
    def view(self):
        tableView = tk.Tk()
        tableView.geometry("600x280")
        tableView.title("Data Head")
        tree = ttk.Treeview(tableView)
        tree.pack()
        cols = list(self.data.columns)
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')
        for index, row in self.data[:5].iterrows():
            tree.insert("",0,text=index,values=list(row))
    def help_btn(self):
        tableView = tk.Tk()
        tableView.geometry("750x900")
        tableView.title("help - MainPage")

        scrollbar = tk.Scrollbar(tableView)
        scrollbar.pack(side="right", fill="y")

        wrapper = tk.LabelFrame(tableView, text="MainPage")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper1 = tk.LabelFrame(tableView, text="데이터 정제")
        wrapper1.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper2 = tk.LabelFrame(tableView, text="데이터 변환")
        wrapper2.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper3 = tk.LabelFrame(tableView, text="데이터 축소")
        wrapper3.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        
        select_help = tk.Label(wrapper, text="작업을 처리할 데이터 파일을 선택합니다.")
        btn_selectData = tk.Button(wrapper, text = "Select")   
        btn_selectData.grid(row=0, column=0, padx = 5, pady = 5)        
        select_help.grid(row = 0, column = 1, padx = 40, pady = 5, sticky="w")

        view_help = tk.Label(wrapper, text="파일의 상위 5개 데이터를 보여줍니다.")
        btn_view_help = tk.Button(wrapper, text = "View")   
        btn_view_help.grid(row=1, column=0, padx = 5, pady = 5) 
        view_help.grid(row=1, column=1, padx = 40, pady = 5, sticky="w") 

        viewdetails_help = tk.Label(wrapper, text="데이터의 통계 정보들을 알려줍니다.")
        btn_viewdetails_help = tk.Button(wrapper, text = "Viewdetails")   
        btn_viewdetails_help.grid(row=2, column=0, padx = 5, pady = 5) 
        viewdetails_help.grid(row=2, column=1, padx = 40, pady = 5, sticky="w") 

        dataclean_help = tk.Label(wrapper, text="전처리의 첫번째 단계로, column의 자료형 변환, missing data의 처리 등의 작업을 합니다.")
        btn_dataclean_help = tk.Button(wrapper, text = "데이터 정제")   
        btn_dataclean_help.grid(row=3, column=0, padx = 5, pady = 5)     
        dataclean_help.grid(row=3, column=1, padx = 40, pady = 5, sticky="w") 
        
        datatrans_help = tk.Label(wrapper, text="전처리의 두번째 단계로, column의 데이터를 scailing 처리 등의 작업을 합니다.")
        btn_datatrans_help = tk.Button(wrapper, text = "데이터 변환")   
        btn_datatrans_help.grid(row=4, column=0, padx = 5, pady = 5) 
        datatrans_help.grid(row=4, column=1, padx = 40, pady = 5, sticky="w") 

        datareduct_help = tk.Label(wrapper, text="전처리의 세번째 단계로, column의 데이터를 범주화 처리 등의 작업을 합니다.")
        btn_datareduct_help = tk.Button(wrapper, text = "데이터 축소")   
        btn_datareduct_help.grid(row=5, column=0, padx = 5, pady = 5) 
        datareduct_help.grid(row=5, column=1, padx = 40, pady = 5, sticky="w") 

        save_help = tk.Label(wrapper, text="처리된 파일을 입력한 파일명으로 저장합니다.")
        btn_save_help = tk.Button(wrapper, text = "save")   
        btn_save_help.grid(row=6, column=0, padx = 5, pady = 5) 
        save_help.grid(row=6, column=1, padx = 40, pady = 5, sticky="w") 

        select_help = tk.Label(wrapper1, text="데이터를 선택합니다.")
        btn_selectData = tk.Button(wrapper, text = "Select")   
        btn_selectData.grid(row=0, column=0, padx = 5, pady = 5)        
        select_help.grid(row = 0, column = 1, padx = 40, pady = 5, sticky="w")

        select_help_clean = tk.Label(wrapper1, text="작업을 처리할 column을 선택합니다.")
        btn_select_help_clean = tk.Button(wrapper1, text = "Select")   
        btn_select_help_clean.grid(row=0, column=0, padx = 5, pady = 5)        
        select_help_clean.grid(row = 0, column = 1, padx = 40, pady = 5, sticky="w")

        datatype_help_1 = tk.Label(wrapper1, text="Numeric")
        datatype_help_11 = tk.Label(wrapper1, text="숫자형 자료형")       
        datatype_help_1.grid(row = 1, column = 0, padx = 0, pady = 5)
        datatype_help_11.grid(row = 1, column = 1, padx = 40, pady = 5, sticky="w") 

        datatype_help_2 = tk.Label(wrapper1, text="Categorical")
        datatype_help_22 = tk.Label(wrapper1, text="문자열 자료형")       
        datatype_help_2.grid(row = 2, column = 0, padx = 0, pady = 5)
        datatype_help_22.grid(row = 2, column = 1, padx = 40, pady = 5, sticky="w")    

        datatype_help_3 = tk.Label(wrapper1, text="Datetime")
        datatype_help_33 = tk.Label(wrapper1, text="시간 자료형")       
        datatype_help_3.grid(row = 3, column = 0, padx = 0, pady = 5)
        datatype_help_33.grid(row = 3, column = 1, padx = 40, pady = 5, sticky="w")    

        datatype_help_4 = tk.Label(wrapper1, text="# of Missing Values :")
        datatype_help_44 = tk.Label(wrapper1, text="column의 Missing Value의 수")       
        datatype_help_4.grid(row = 4, column = 0, padx = 0, pady = 5)
        datatype_help_44.grid(row = 4, column = 1, padx = 40, pady = 5, sticky="w") 

        datatype_help_5 = tk.Label(wrapper1, text="Replacing With Mean")
        datatype_help_55 = tk.Label(wrapper1, text="column의 Missing Value를 평균값으로 변환하는 방법.")       
        datatype_help_5.grid(row = 5, column = 0, padx = 0, pady = 5)
        datatype_help_55.grid(row = 5, column = 1, padx = 40, pady = 5, sticky="w") 

        datatype_help_6 = tk.Label(wrapper1, text="Replacing With Median")
        datatype_help_66 = tk.Label(wrapper1, text="column의 Missing Value를 중앙값으로 변환하는 방법.")       
        datatype_help_6.grid(row = 6, column = 0, padx = 0, pady = 5)
        datatype_help_66.grid(row = 6, column = 1, padx = 40, pady = 5, sticky="w") 

        datatype_help_7 = tk.Button(wrapper1, text="Save Column Options")
        datatype_help_77 = tk.Label(wrapper1, text="선택한 옵션들을 저장합니다.")       
        datatype_help_7.grid(row = 7, column = 0, padx = 0, pady = 5)
        datatype_help_77.grid(row = 7, column = 1, padx = 40, pady = 5, sticky="w") 

        datatype_help_8 = tk.Button(wrapper1, text="OK")
        datatype_help_88 = tk.Label(wrapper1, text="선택한 옵션들로 작업을 처리합니다.")       
        datatype_help_8.grid(row = 8, column = 0, padx = 0, pady = 5)
        datatype_help_88.grid(row = 8, column = 1, padx = 40, pady = 5, sticky="w") 

        trans_help_1 = tk.Button(wrapper2, text="Select")
        trans_help_11 = tk.Label(wrapper2, text="변환방법과 column을 선택합니다.")       
        trans_help_1.grid(row = 0, column = 0, padx = 0, pady = 5)
        trans_help_11.grid(row = 0, column = 1, padx = 40, pady = 5, sticky="w")

        trans_help_2 = tk.Label(wrapper2, text="StandardScaler")
        trans_help_22 = tk.Label(wrapper2, text="data들을 표준 정규화 합니다.")       
        trans_help_2.grid(row = 1, column = 0, padx = 0, pady = 5)
        trans_help_22.grid(row = 1, column = 1, padx = 40, pady = 5, sticky="w")        

        trans_help_3 = tk.Label(wrapper2, text="MinMaxScaler")
        trans_help_33 = tk.Label(wrapper2, text="data들을 0~1 사이 범위에 정규화 합니다.")       
        trans_help_3.grid(row = 2, column = 0, padx = 0, pady = 5)
        trans_help_33.grid(row = 2, column = 1, padx = 40, pady = 5, sticky="w")    

        trans_help_4 = tk.Label(wrapper2, text="MaxAbsScaler")
        trans_help_44 = tk.Label(wrapper2, text="data들을 -1~1 사이 범위에 정규화 합니다. (값이 양수만 존재할 경우, MinMaxScaler와 동일합니다.")       
        trans_help_4.grid(row = 3, column = 0, padx = 0, pady = 5)
        trans_help_44.grid(row = 3, column = 1, padx = 40, pady = 5, sticky="w")      

        trans_help_5 = tk.Label(wrapper2, text="RobustScaler")
        trans_help_55 = tk.Label(wrapper2, text="중앙값과 IQR(사분위수)를사용 아웃라이어의 영향을 최소화합니다. 기본값은 1분위와 3분위 사이입니다.")       
        trans_help_5.grid(row = 4, column = 0, padx = 0, pady = 5)
        trans_help_55.grid(row = 4, column = 1, padx = 40, pady = 5, sticky="w")  

        trans_help_6 = tk.Button(wrapper2, text="OK")
        trans_help_66 = tk.Label(wrapper2, text="선택한 옵션들로 작업을 처리합니다.")       
        trans_help_6.grid(row = 5, column = 0, padx = 0, pady = 5)
        trans_help_66.grid(row = 5, column = 1, padx = 40, pady = 5, sticky="w")  

    def help_step(self):
        tableView = tk.Tk()
        tableView.geometry("720x720")
        tableView.title("help - Step")

        wrapper = tk.LabelFrame(tableView, text="MainPage")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper1 = tk.LabelFrame(tableView, text="데이터 정제")
        wrapper1.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper2 = tk.LabelFrame(tableView, text="데이터 변환")
        wrapper2.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper3 = tk.LabelFrame(tableView, text="데이터 축소")
        wrapper3.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        

    def getData(self):
        return self.data
