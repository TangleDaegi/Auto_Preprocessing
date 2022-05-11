#데이터 탐색 시각화해서 보여줌

# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Prev",
                            command = lambda : controller.show_frame(Page1))
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(Page3))
        button2.grid(row = 7, column = 4, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Select",
                            command = lambda : controller.show_frame(Page3))
        button3.grid(row = 7, column = 4, padx = 10, pady = 10)