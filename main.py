import tkinter as tk
import sqlite3

# ウィンドウを作成する
window = tk.Tk()
window.title("Overwatch 2 Character Database")

# データベースに接続する
ow2_characters_jp_id_db = sqlite3.connect("ow2_characters_jp_id.db")
ow2_type_db = sqlite3.connect("ow2_type.db")

# ウィンドウのサイズを設定する
window.geometry("600x400")

# ラベルを作成する
label1 = tk.Label(window, text="キャラクター名を入力してください:")
label2 = tk.Label(window, text="ロールを選択してください:")
label3 = tk.Label(window, text="アンチピック:")
label4 = tk.Label(window, text="結果:")

# 検索欄を作成する
entry1 = tk.Entry(window)

# ドロップダウンリストを作成する
roles = ["タンク", "ダメージ", "サポート"]
dropdown = tk.StringVar(window)
dropdown.set(roles[0])
dropdown_menu = tk.OptionMenu(window, dropdown, *roles)

# アンチピックボタンを作成する
button1 = tk.Button(window, text="アンチピック", command=lambda: switch_to_antipick_window())

# 検索ボタンを作成する
button2 = tk.Button(window, text="検索", command=lambda: search_character(entry1.get()))
button3 = tk.Button(window, text="ロールで検索", command=lambda: search_role(dropdown.get()))

# ラベルを配置する
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)

# 検索欄を配置する
entry1.grid(row=0, column=1)

# ドロップダウンリストを配置する
dropdown_menu.grid(row=1, column=1)

# アンチピックボタンを配置する
button1.grid(row=2, column=1)

# 検索ボタンを配置する
button2.grid(row=0, column=2)
button3.grid(row=1, column=2)

# 文字化け対策
window.tk.call('encoding', 'system', 'utf-8')

# アンチピックウィンドウを作成する
antipick_window = tk.Toplevel()
antipick_window.title("アンチピック")

# ラベルを作成する
label5 = tk.Label(antipick_window, text="キャラクター名を入力してください:")

# 検索欄を作成する
entry2 = tk.Entry(antipick_window)

# 検索ボタンを作成する
button4 = tk.Button(antipick_window, text="検索", command=lambda: search_antipick(entry2.get()))

# 元のウィンドウに戻るボタンを作成する
button5 = tk.Button(antipick_window, text="戻る", command=lambda: switch_to_main_window())

# ラベルを配置する
label5.grid(row=0, column=0)

# 検索欄を配置する
entry2.grid(row=0, column=1)

# 検索ボタンを配置する
button4.grid(row=0, column=2)

# 元のウィンドウに戻るボタンを配置する
button5.grid(row=1, column=2)

# アンチピックウィンドウに切り替える関数
def switch_to_antipick_window():
    window.withdraw()
    antipick_window.deiconify()

# 元のウィンドウに戻る関数
def switch_to_main_window():
    antipick_window.withdraw()
    window.deiconify()

# 検索関数を定義する
def search_character(character_name):
    
    # ow2_characters_jp_id.dbの情報を取り出す
    characters_cursor = ow2_characters_jp_id_db.cursor()
    characters_cursor.execute("SELECT * FROM characters  WHERE character_name = ?", (character_name,))
    data1 = characters_cursor.fetchall()

    # ow2_type.dbの情報を取り出す
    type_cursor = ow2_type_db.cursor()
    type_cursor.execute("SELECT * FROM types")
    data2 =type_cursor.fetchall()

    # 結合
    result = [(row1 + row2) for row1 in data1 for row2 in data2 if row1[0] == row2[0]]


    # 新しいウィンドウを作成する
    result_window = tk.Toplevel()
    result_window.title("検索結果")

    # 結果を表示する
    text = ""
    for row in result:
        text += f"name: {row[1]} | role: {row[2]} | dive: {row[3]} | rush: {row[4]} | poke:{row[5]}\n"
    label3 = tk.Label(result_window, text=text)
    label3.grid(row=0, column=0)

# ロールで検索する関数を定義する
def search_role(role):
   # ow2_characters_jp_id.dbの情報を取り出す
    characters_cursor = ow2_characters_jp_id_db.cursor()
    characters_cursor.execute("SELECT * FROM characters  WHERE role = ?", (role,))
    data1 = characters_cursor.fetchall()

    # ow2_type.dbの情報を取り出す
    type_cursor = ow2_type_db.cursor()
    type_cursor.execute("SELECT * FROM types")
    data2 =type_cursor.fetchall()

    # 結合
    result = [(row1 + row2) for row1 in data1 for row2 in data2 if row1[0] == row2[0]]

    # 新しいウィンドウを作成する
    result_window = tk.Toplevel()
    result_window.title("検索結果")

    # 結果を表示する
    text = ""
    for row in result:
        text += f"name: {row[1]} | role: {row[2]} | dive: {row[3]} | rush: {row[4]} | poke:{row[5]}\n"
    label3 = tk.Label(result_window, text=text)
    label3.grid(row=0, column=0)

# アンチピックを検索する関数を定義する
def search_antipick(character_name):

    characters_cursor = ow2_characters_jp_id_db.cursor()
    type_cursor = ow2_type_db.cursor()
    # キャラクターIDを取得する
    character_id = ow2_characters_jp_id_db.cursor().execute("SELECT id FROM characters WHERE character_name = ?", (character_name,)).fetchone()[0]

    # ow2_type.dbの数の比較情報を取り出す
    result=type_cursor.execute("SELECT MAX(dive) AS max_dive, MAX(rush) AS max_rush, MAX(poke) AS max_poke FROM types WHERE id = ?", (character_id,)).fetchone()

    #ow2_characters_jp_id.dbのキャラを取得する
    #characters_cursor.execute("SELECT * FROM characters  WHERE id != ?", (character_id,))
    #data=characters_cursor.fetchall()

    #結果の表示
    result_window = tk.Toplevel()
    result_window.title("アンチピック")


    if result[0] > result[1] and result[0] > result[2]:
        type_cursor.execute('''
            SELECT id, rush
            FROM types
            WHERE id != ? AND rush != 0
            ORDER BY rush DESC
            ''', (character_id,))
        anti_text = ""
        anti_text = f"有効なtypeは rush です\n"
        label4 = tk.Label(result_window, text=anti_text)
        label4.grid(row=0, column=0)
        
    # rushが一番大きい場合はpokeでソートして表示
    elif result[1] > result[0] and result[1] > result[2]:
        type_cursor.execute('''
            SELECT id, poke
            FROM types
            WHERE id != ? AND poke != 0
            ORDER BY poke DESC
        ''', (character_id,))
        anti_text = ""
        anti_text = f"有効なtypeは poke です\n"
        label4 = tk.Label(result_window, text=anti_text)
        label4.grid(row=0, column=0)
    # pokeが一番大きい場合はdiveでソートして表示
    else:
        type_cursor.execute('''
            SELECT id, dive
            FROM types
            WHERE id != ? AND dive != 0
            ORDER BY dive DESC
        ''', (character_id,))
        anti_text = ""
        anti_text = f"有効なtypeは dive です\n"
        label4 = tk.Label(result_window, text=anti_text)
        label4.grid(row=0, column=0)

    # 他の行を表示
    sorted_data = type_cursor.fetchall()

    # 結合
    characters_cursor.execute("SELECT * FROM characters  WHERE id != ?", (character_id,))
    characters_data = characters_cursor.fetchall()
    result = [(row1 + row2) for row1 in sorted_data for row2 in characters_data if row1[0] == row2[0]]

    
    data_text = ""
    for row in result:
        data_text += f"name: {row[3]} | role: {row[4]} | type_point: {row[1]} \n"
    
    label4 = tk.Label(result_window, text=data_text)
    label4.grid(row=1, column=0)
    

# メインループを開始する
window.mainloop()