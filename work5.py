import tkinter as tk
import random

class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("タイピングアプリ")
        
        # ランダムな単語リスト
        self.words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange"]
        
        # プロパティ辞書の定義
        self.properties = {"current": random.choice(self.words), "score": 0}
        
        # ラベル1: 現在の単語表示
        self.word_label = tk.Label(root, text=self.properties["current"], font=("Helvetica", 24))
        self.word_label.pack(pady=20)
        
        # テキストボックス: ユーザーの入力
        self.entry = tk.Entry(root, font=("Helvetica", 24))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_typing)
        
        # ラベル2: スコア表示
        self.score_label = tk.Label(root, text=f"スコア: {self.properties['score']}", font=("Helvetica", 24))
        self.score_label.pack(pady=20)
        
        # ボタン: 次の単語
        self.next_button = tk.Button(root, text="次の単語", command=self.next_word, font=("Helvetica", 18))
        self.next_button.pack(pady=10)
    
    def check_typing(self, event):
        user_input = self.entry.get()
        if self.word_label.cget("text") == user_input:
            self.properties["score"] += 1
            self.score_label.config(text=f"スコア: {self.properties['score']}")
        self.entry.delete(0, tk.END)
        self.next_word()
    
    def next_word(self):
        self.properties["current"] = random.choice(self.words)
        self.word_label.config(text=self.properties["current"])

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
