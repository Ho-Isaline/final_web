from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore
import random  # 引入 random 模組


app = Flask(__name__)

# Firebase 初始化
cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/")
def home():
    # 從 Firestore 中讀取資料 (book_data 集合)
   # 從 Firestore 中讀取資料 (book_data 集合)
    books_ref = db.collection('book_data')  # 修改為正確的集合名稱
    books = books_ref.stream()

    # 轉換 Firestore 資料為 Python 字典
    book_list = []
    for book in books:
        book_dict = book.to_dict()
        book_list.append({
            "title": book_dict.get("title", "No Title"),
            "author": book_dict.get("author", "Unknown Author"),
            "category": book_dict.get("category", "No Category"),
            "releaseYear": book_dict.get("releaseYear", "N/A")
        })

    # 隨機選取 6 本書
    random_books = random.sample(book_list, min(len(book_list), 6))  # 防止不足 6 本書時報錯

    return render_template("index.html", books=random_books)

if __name__ == "__main__":
    app.run(debug=True)
