#그리드:격자
from tkinter import *  
root = Tk()
root.title("계산기")
root.geometry("205x270+200+200")

#to show
ans = []
#to cal..후위식
cal = []
save_op = []
#이름 바꿔야 될 듯
def add_num(n):
  if len(ans)>30:
    #경고 창 띄우기
    return
  ans.append(str(n))
  if n == 'clear':
    ans.clear()
  label1.config(text = ''.join(ans))
  if 0<=int(n)<=9:
    #숫자 여러개 연속으로 나오는 경우 처리 해야 함
    cal.append(n)
  elif n == '*' or n == '/':
    pass
  elif n == '+' or n == '-':
    pass
  elif n == '=':
    pass


#그냥 class 쓸 걸..
#clear
btn_clear = Button(root, text="clear",padx=10,pady=10,command=lambda : add_num('clear'))
btn_equal = Button(root, text="=",padx=10,pady=10,command=lambda : add_num('='))
btn_div = Button(root, text="/",padx=10,pady=10,command=lambda : add_num('/'))
btn_mul = Button(root, text="*",padx=10,pady=10,command=lambda : add_num('*'))

btn_clear.grid(row =1 , column =0, sticky=N+E+W+S,padx=3,pady=3)
btn_equal.grid(row =1 , column =1, sticky=N+E+W+S,padx=3,pady=3)
btn_div.grid(row =1 , column =2, sticky=N+E+W+S,padx=3,pady=3)
btn_mul.grid(row =1 , column =3, sticky=N+E+W+S,padx=3,pady=3)

#7시작
btn_7 = Button(root, text="7",padx=10,pady=10,command=lambda : add_num(7))
btn_8 = Button(root, text="8",padx=10,pady=10,command=lambda : add_num(8))  #command는 직접적으로 인자를 못 받는 건가??
btn_9 = Button(root, text="9",padx=10,pady=10,command=lambda : add_num(8))
btn_sub = Button(root, text="-",padx=10,pady=10,command=lambda : add_num('-'))

btn_7.grid(row =2 , column =0, sticky=N+E+W+S,padx=3,pady=3)
btn_8.grid(row =2 , column =1, sticky=N+E+W+S,padx=3,pady=3)
btn_9.grid(row =2 , column =2, sticky=N+E+W+S,padx=3,pady=3)
btn_sub.grid(row =2 , column =3, sticky=N+E+W+S,padx=3,pady=3)

#4시작
btn_4 = Button(root, text="4",padx=10,pady=10,command=lambda : add_num(4))
btn_5 = Button(root, text="5",padx=10,pady=10,command=lambda : add_num(5))
btn_6 = Button(root, text="6",padx=10,pady=10,command=lambda : add_num(6))
btn_add = Button(root, text="+",padx=10,pady=10,command=lambda : add_num('+'))

btn_4.grid(row =3 , column =0, sticky=N+E+W+S,padx=3,pady=3)
btn_5.grid(row =3 , column =1, sticky=N+E+W+S,padx=3,pady=3)
btn_6.grid(row =3 , column =2, sticky=N+E+W+S,padx=3,pady=3)
btn_add.grid(row =3 , column =3, sticky=N+E+W+S,padx=3,pady=3)

#1 시작
btn_1 = Button(root, text="1",padx=10,pady=10,command=lambda : add_num('1'))
btn_2 = Button(root, text="2",padx=10,pady=10,command=lambda : add_num('2'))
btn_3 = Button(root, text="3",padx=10,pady=10,command=lambda : add_num('3'))
btn_enter = Button(root, text="enter",padx=10,pady=10)  #세로로 합쳐짐

btn_1.grid(row =4 , column =0, sticky=N+E+W+S,padx=3,pady=3)    #grid에 pad를 부여해  버튼 사이의 간격을 둠
btn_2.grid(row =4 , column =1, sticky=N+E+W+S,padx=3,pady=3)
btn_3.grid(row =4 , column =2, sticky=N+E+W+S,padx=3,pady=3)
btn_enter.grid(row =4 , column =3, rowspan =2, sticky=N+E+W+S,padx=3,pady=3)  #row 2개를 합치겠다(현재 위치로부터 아래쪽으로 몇 줄을 더함

#0 시작 줄
btn_0=Button(root, text="0",padx=10,pady=10,command=lambda : add_num(0))    #가로로 합쳐짐
btn_dot=Button(root,text=".",padx=10,pady=10,command=lambda : add_num('.'))

btn_0.grid(row =5, column = 0, columnspan = 2, sticky=N+E+W+S,padx=3,pady=3)
btn_dot.grid(row =5 , column =2, sticky=N+E+W+S,padx=3,pady=3)

#정답 출력
label1 = Label(root)
label1.grid(row = 6, column=0, columnspan=4,sticky=W)
root.mainloop()   