from app import app
from models import db, Employ

# データベースへの接続と初期化
with app.app_context():
    # 初期データのリスト
    seed_data = [
        {"name": "イチロー", "email": "ichiro@example.com", "department": "経理"},
        {"name": "大谷翔平", "email": "ootani@example.com", "department": "法務"},
        {"name": "新庄剛志", "email": "shinjo@example.com", "department": "営業"},
        {"name": "松坂大輔", "email": "matsuzaka@example.com", "department": "経理"},
        {"name": "上原浩治", "email": "uehara@example.com", "department": "法務"},
        {"name": "ダルビッシュ有", "email": "darubish@example.com", "department": "営業"},
        {"name": "藤浪晋太郎", "email": "fujinami@example.com", "department": "経理"},
        {"name": "川﨑宗則", "email": "kawasaki@example.com", "department": "法務"},
        {"name": "田中将大", "email": "tanaka@example.com", "department": "営業"},
        {"name": "福留孝介", "email": "fukudome@example.com", "department": "経理"},
        {"name": "藤川球児", "email": "fujikawa@example.com", "department": "法務"},
        {"name": "松井秀喜", "email": "matsui-h@example.com", "department": "営業"},
        {"name": "松井稼頭央", "email": "matsui-k@example.com", "department": "経理"},
        {"name": "和田毅", "email": "wada@example.com", "department": "法務"},
        {"name": "前田健太", "email": "maeda@example.com", "department": "営業"},
    ]

    # テーブルをクリアしてから新しいデータを挿入（必要に応じて）
    db.session.query(Employ).delete()  # 全削除
    for data in seed_data:
        employee = Employ(name=data["name"], email=data["email"], department=data["department"])
        db.session.add(employee)

    # コミットしてデータを保存
    db.session.commit()
    print("Database seeded successfully!")
