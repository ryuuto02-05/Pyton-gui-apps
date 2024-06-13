import tkinter as tk
# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑
label1 = tk.Label(window, text="西暦を入力してください", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    num = int(entry1.get())  # 入力値を取得
    # if num2 = num1 - 1911:
    if num >=1868 and num <=1911:
        if (num-1867)==1:
            label1.config(text=f" 西暦{num}年は,元年")
        label1.config(text=f" 西暦{num}年は,明治{num-1867}年")  # 画面に出力
    if (num-1911)==1:
            label1.config(text=f" 西暦{num}年は,大正元年")
    elif num >=1912 and num <=1925:
        if (num-1911)==1:
            label1.config(text=f" 西暦{num}年は,大正元年")
        label1.config(text=f" 西暦{num}年は,大正{num-1911}年")
        if (num-1925)==1:
            label1.config(text=f" 西暦{num}年は,昭和元年")
    elif num >=1926 and num <=1988:
        label1.config(text=f" 西暦{num}年は,昭和{num-1925}年")
    elif num >=1989 and num <=2018:
        if (num-1988)==1:
            label1.config(text=f" 西暦{num}年は,平成元年")
        label1.config(text=f" 西暦{num}年は,平成{num-1988}年")
    elif num >=2019 and num <=2050:
        if (num-2018)==1:
            label1.config(text=f" 西暦{num}年は,令和元年")
            label1.config(text=f" 西暦{num}年は,令和{num-2018}年")
    else:
        label1.config(text=f"この元号は対応していません")




# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="元号への変換", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
