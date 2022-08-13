#구조도 : day별로 메모장생성 -> 입력 단어들 적재 -> 랜덤 단어 출력
#추가 : 영/한 변경 기능?
import tkinter as tk
from tkinter import Button, ttk
def str():
    print(1)


app = tk.Tk() 
app.geometry('250x100')


comboExample = ttk.Combobox(app, values=[i for i in range(1,31)])
comboExample.grid(column=0, row=0)
comboExample.current(0) #숫자 바꿔줄 것

btnst = ttk.Button(app, text="시작", command=lambda : str()) #stack에 넣기위해.. 개발 편의성
btnst.grid(column = 1, row = 0)

btnex = ttk.Button(app, text="출력") #출력 버튼
btnex.grid(column = 1, row = 1)

btnw = ttk.Button(app, text="입력")
btnw.grid(column = 1, row = 2)

textbox = ttk.Entry(app)
textbox.grid(column=0, row=2)

#print(comboExample.get())


app.mainloop()