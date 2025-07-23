from flask import Flask, request, jsonify  # Flask本体とリクエスト・レスポンス用のモジュールをインポート
from flask_cors import CORS               # CORS（クロスオリジン通信）を許可するためのモジュールをインポート
import pymysql                            # MySQLに接続するためのモジュールをインポート

app = Flask(__name__)                     # Flaskアプリケーションのインスタンスを作成
CORS(app)                                 # このアプリでCORSを有効化

# RDS接続情報（適宜書き換えてください）
db_config = {
    "host": "memoapp.cdagswo00s5k.ap-northeast-1.rds.amazonaws.com",  # データベースのホスト名
    "user": "admin",                                                  # データベースのユーザー名
    "password": "5656tyoko",                                          # データベースのパスワード
    "database": "memo_app"                                            # 使用するデータベース名（スキーマ名）
}

@app.route('/memo', methods=['POST'])      # /memoエンドポイントにPOSTリクエストが来たときの処理
def add_memo():
    data = request.json                   # リクエストのJSONデータを取得
    conn = pymysql.connect(**db_config)   # データベースに接続
    with conn.cursor() as cursor:         # カーソル（SQL実行用オブジェクト）を作成
        sql = "INSERT INTO memos (title, content) VALUES (%s, %s)"  # SQL文を準備
        cursor.execute(sql, (data['title'], data['content']))       # SQL文を実行し、データを挿入
    conn.commit()                         # 挿入した内容をデータベースに保存（コミット）
    conn.close()                          # データベース接続を閉じる
    return jsonify({'message': 'メモをDBに保存しました'})  # 保存完了メッセージをJSONで返す

@app.route('/memo', methods=['GET'])       # /memoエンドポイントにGETリクエストが来たときの処理
def get_memos():
    conn = pymysql.connect(**db_config)    # データベースに接続
    with conn.cursor() as cursor:          # カーソルを作成
        cursor.execute("SELECT title, content FROM memos")           # メモ一覧を取得するSQLを実行
        rows = cursor.fetchall()           # 取得した全ての行をリストで受け取る
        memos = [{"title": row[0], "content": row[1]} for row in rows]  # 各行を辞書型に変換
    conn.close()                           # データベース接続を閉じる
    return jsonify(memos)                  # メモ一覧をJSONで返す

if __name__ == '__main__':                 # このファイルが直接実行された場合のみ
    app.run(debug=True)
