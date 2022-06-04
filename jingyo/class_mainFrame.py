from turtle import left
from tkinter import filedialog
from CleaningBox import *
from TransBox import *
from ReductionBox import *
from function_mainFrame import *
from class_AnalysisBox import analysisBox
from tkinter.tix import *
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd



class mainFrame():
    def __init__(self):

        root = tk.Tk()
        root.title("Auto Preprocessing")
        root.geometry("400x400") #가로*세로 + (x좌표 + y 좌표)
        root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기 변경불가)
        wrapper = tk.LabelFrame(root, text="데이터 확인")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")

        def selectData():
            self.dataPath = tk.filedialog.askopenfilename(initialdir='path', title='select file', filetypes=(("csv","*.csv"),("all files","*.*")))
            data = pd.read_csv(self.dataPath)
            self.data = pd.DataFrame(data)     

        btn_selectData = tk.Button(wrapper, text = "Select", command = selectData)
        btn_selectData.grid(row = 0, column = 1, padx = 5, pady = 5)

        btn_view = tk.Button(wrapper, text = "View", command = self.view) 
        btn_view.grid(row = 0, column = 2, padx = 5, pady = 5)

        def viewdetails():
            abox = analysisBox(self)
            
        btn_viewdetails = tk.Button(wrapper, text = "View Details", command = viewdetails, width=10)
        btn_viewdetails.grid(row = 0, column = 3, padx = 5, pady = 5)

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
        
        def save():
            filename = filedialog.asksaveasfilename(initialdir="path", title="Save file",
                        filetypes=(("CSV files", "*.csv"),
                        ("all files", "*.*")))
            dataToCsv(self.data, filename)
        btn = tk.Button(wrapper3, text="Save", command=save)
        btn.grid(row = 0, column = 1, padx = 5, pady = 5)

        wrapper4 = tk.LabelFrame(root, text="도움말")
        wrapper4.pack(padx = 10, pady = 5, fill = "both", expand= "yes")

        btn_help = tk.Button(wrapper4, text = "Interface_help", command = self.help_btn)
        btn_help.grid(row = 0, column = 0, padx = 5, pady = 5)
        step_help = tk.Button(wrapper4, text = "Step_help", command = self.help_step)
        step_help.grid(row = 0, column = 1, padx = 5, pady = 5)

        root.mainloop()
        pass


    def info():
        msgbox.showinfo("알림", "정상적으로 처리 되었습니다.")
    def warn():
        msgbox.showwarning("경고", "오류가 발생했습니다.")
         

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

        reduct_help_1 = tk.Button(wrapper3, text="Select")
        reduct_help_11 = tk.Label(wrapper3, text="축소방법과 column을 선택합니다.")       
        reduct_help_1.grid(row = 0, column = 0, padx = 0, pady = 5)
        reduct_help_11.grid(row = 0, column = 1, padx = 40, pady = 5, sticky="w")

        reduct_help_2 = tk.Label(wrapper3, text="데이터 범주의 기준값")
        reduct_help_22 = tk.Label(wrapper3, text="12 -> Enter -> 9 -> Enter -> 6 -> Enter -> 3 -> Enter -> 0 -> Enter 순서대로 입력하고")       
        reduct_help_2.grid(row = 1, column = 0, padx = 0, pady = 5)
        reduct_help_22.grid(row = 1, column = 1, padx = 40, pady = 5, sticky="w")
        
        reduct_help_3 = tk.Label(wrapper3, text="데이터 범주의 이름")
        reduct_help_33 = tk.Label(wrapper3, text="4분기 -> Enter -> 3분기 -> Enter -> 2분기 -> Enter -> 1분기 -> Enter 순서대로 입력할 때,")       
        reduct_help_3.grid(row = 2, column = 0, padx = 0, pady = 5)
        reduct_help_33.grid(row = 2, column = 1, padx = 40, pady = 5, sticky="w")

        reduct_help_4 = tk.Label(wrapper3, text="")
        reduct_help_44 = tk.Label(wrapper3, text="0<x<=3 1분기, 3<x<=6 2분기, 6<x<=9 3분기, 9<x<=12 4분기")       
        reduct_help_4.grid(row = 3, column = 0, padx = 0, pady = 5)
        reduct_help_44.grid(row = 3, column = 1, padx = 40, pady = 5, sticky="w")

    def help_step(self):
        tableView = tk.Tk()
        tableView.geometry("720x720")
        tableView.title("help - Step")

        wrapper = tk.LabelFrame(tableView, text="데이터 확인 순서")
        wrapper.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper1 = tk.LabelFrame(tableView, text="데이터 처리 순서")
        wrapper1.pack(padx = 10, pady = 5, fill = "both", expand= "yes")
        wrapper2 = tk.LabelFrame(tableView, text="처리 기능")
        wrapper2.pack(padx = 10, pady = 5, fill = "both", expand= "yes")

        step_help_1 = tk.Label(wrapper, text="1.")
        step_help_11 = tk.Label(wrapper, text="Select 버튼을 통해 데이터를 선택한 후, View 버튼을 통해 원하는 데이터가 맞는지 확인합니다.")       
        step_help_1.grid(row = 0, column = 0, padx = 0, pady = 5)
        step_help_11.grid(row = 0, column = 1, padx = 20, pady = 5, sticky="w")
       
        step_help_2 = tk.Label(wrapper, text="2.")
        step_help_2.grid(row = 1, column = 0, padx = 0, pady = 5)
        step_help_22 = tk.Label(wrapper, text="View Details 버튼을 통해 데이터의 기본 통계값, 데이터의 분포, column의 정보등을 얻습니다.")
        step_help_22.grid(row = 1, column = 1, padx = 20, pady = 5, sticky="w")
      
        step_help_clean_1 = tk.Label(wrapper1, text="1.")
        step_help_clean_1.grid(row = 0, column = 0, padx = 0, pady = 5)
        step_help_clean_11 = tk.Label(wrapper1, text="데이터 정제부분에서 결측치 처리, 이상치 처리, column의 자료형 통일등의 작업을 합니다.")
        step_help_clean_11.grid(row = 0, column = 1, padx = 20, pady = 5, sticky="w")

        step_help_clean_2 = tk.Label(wrapper1, text="2.")
        step_help_clean_2.grid(row = 1, column = 0, padx = 0, pady = 5)
        step_help_clean_22 = tk.Label(wrapper1, text="데이터 변환과 축소는 사용자의 필요에 따라 순서를 정할 수 있습니다.")
        step_help_clean_22.grid(row = 1, column = 1, padx = 20, pady = 5, sticky="w")

        step_help_trans_1 = tk.Label(wrapper2, text="데이터 이산화")
        step_help_clean_1.grid(row = 0, column = 0, padx = 0, pady = 5)
        step_help_clean_11 = tk.Label(wrapper2, text="데이터를 ~~ 할때 사용합니다. ")
        step_help_clean_11.grid(row = 0, column = 1, padx = 20, pady = 5, sticky="w")
     
    def getData(self):
        return self.data