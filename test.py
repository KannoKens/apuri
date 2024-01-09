import sqlite3

# データベースに接続
conn = sqlite3.connect('ow2_characters_jp_id.db')

# カーソルを作成
cursor = conn.cursor()

# テーブルを作成
cursor.execute('''CREATE TABLE characters
                 (id integer PRIMARY KEY, character_name text, role text)''')

# データを挿入
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (001, 'Ashe', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (002, 'Ana', 'サポート')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (003, 'Baptiste', 'サポート')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (004, 'Bastion', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (005, 'Brigitte', 'サポート')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (006, 'Cassidy', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (007, 'D.Va', 'タンク')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (008, 'Doomfist', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (009, 'Echo', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (010, 'Genji', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (011, 'Hanzo', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (012, 'Illari', 'サポート')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (013, 'Junker Queen', 'タンク')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (014, 'Junkrat', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (015, 'Kiriko', 'サポート')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (016, 'Lifeweaver', 'サポート')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (017, 'Lúcio', 'サポート')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (018, 'Mei', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (019, 'Mercy', 'サポート')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (020, 'Moira', 'サポート')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (021, 'Orisa', 'タンク')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (022, 'Pharah', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (023, 'Reaper', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (024, 'Ramattra', 'タンク')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (025, 'Reinhardt', 'タンク')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (026, 'Roadhog', 'タンク')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (027, 'Sigma', 'タンク')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (028, 'Sojourn', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (029, 'Soldier76', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (030, 'Sombra', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (031, 'Symmetra', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (032, 'Torbjörn', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (033, 'Tracer', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (034, 'Widowmaker', 'ダメージ')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (035, 'Winston', 'タンク')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (036, 'Wrecking Ball', 'タンク')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (037, 'Zarya', 'タンク')")
cursor.execute("INSERT INTO characters (id, character_name, role) VALUES (038, 'Zenyatta', 'サポート')")


# データをコミット
conn.commit()

# データベースを閉じる
conn.close()
