from aip import AipSpeech
import tkinter as tk
root = tk.Tk()
root.title("语音合成")
root.geometry('550x250')
def sc():
    APP_ID = '19231821'
    API_KEY = 'fMbeWhqXH6BZXMIZoBNTU5Hg'
    SECRET_KEY = 'zXOOvoXC81odMKUwwTpLwHp9tYXXYd4V'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    # zh 中文 ； 1 windows
    result = client.synthesis(t1.get(0,0,"end"),'zh', 1, {
        "vol": 10,  # 音量
        "spd": 5,  # 语速
        "pit": 6,  # 语调
        "per": 4,  # 音色
    })
    with open("audio.mp3", "wb") as f:
        f.write(result)
b1 = tk.Button(root,text="MAKE",command=sc)
b1.grid()
b2 = tk.Button(root,text="CLEAR")
b2.grid(row=0,column=1)
t1 = tk.Text(root)
t1.grid(row=1,columnspan=2)
root.mainloop()