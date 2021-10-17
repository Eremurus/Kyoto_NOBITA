import tkinter
import tkinter.filedialog
from PIL import Image, ImageTk
import tkinter.font as f

WIDTH  = 640        
HEIGHT = 400
judged = False  
i = 1     
labels = []
circles = []

main = tkinter.Tk()
main.title("NOBITA produced by iGEM Kyoto 2021")
main.geometry("640x440")

kido = []
location_list = []

def choose():
    global image_pil_L
    global image_tk
    global i
    ### グローバル変数
    ### ファイルダイアログ
    name = tkinter.filedialog.askopenfilename(title="choose file")
    ### 画像ロード
    image_pil = Image.open(open(name, 'rb'))
    image_pil = image_pil.resize((224, 224))
    image_pil_L = image_pil.convert("L")
    image_tk = ImageTk.PhotoImage(image_pil_L)
    if len(kido) != 0:
        kido.clear()
    if len(labels) != 0:
        for lab in labels:
            lab.place_forget()
    if len(circles) != 0:
        for circle in circles:
            canvas.delete(circle)
    i = 1
    ### キャンバスに表示
    canvas.create_image(WIDTH/2, HEIGHT/2, image=image_tk)

label = tkinter.Label(main, text="")
label.place(x=100,y=10)

def judge():
    global label
    label.place_forget()
    label = tkinter.Label(main, text=kido)
    label.place(x=100,y=10)

def point_loc(event):
    global i
    x = event.x
    y = event.y
    location = (event.x-208, event.y-88)
    if location[0] >0 and location[0] <224 and location[1] >0 and location[1] <224:
        val = image_pil_L.getpixel(location)
        kido.append([i,":",val])
        circle = canvas.create_oval(
            x-5, y-5, x+5, y+5,outline="red"
        )
        circles.append(circle)
        label_num = tkinter.Label(main, text=i)
        labels.append(label_num)
        label_num.place(x=x, y=y)
        i += 1
        #print(location)
        #print(type(image_pil_L))

main.bind('<Button-1>', point_loc)

### ボタン作成・配置
button1 = tkinter.Button(main, text="Choose image (^^)",command=choose)
button1.pack(side='bottom')
button2 = tkinter.Button(main, text="Display brightness٩( ᐛ )و", command=judge)
button2.pack(side="bottom")
canvas = tkinter.Canvas(main, width=WIDTH, height=HEIGHT)
canvas.place(x=100, y=50) 
canvas.pack()
### キャンバス作成
### イベントループ
main.mainloop()