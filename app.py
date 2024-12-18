from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Firebase 初始化
cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/")
def home():
    # 從 Firestore 中讀取新書資料
    books_ref = db.collection('new_releases')
    books = books_ref.stream()

    book_list = []
    for book in books:
        book_list.append(book.to_dict())

    return render_template("index.html", books=book_list)

if __name__ == "__main__":
    app.run(debug=True)
