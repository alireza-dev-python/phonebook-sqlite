import sqlite3

conn = sqlite3.connect("cersell.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS mokhatebin (
id INTEGER PRIMARY KEY AUTOINCREMENT ,
name TEXT NOT NULL
)
""")
cursor.execute("SELECT COUNT (*) FROM mokhatebin")
count = cursor.fetchone()[0]

if count == 0 :
    
    cursor.execute("INSERT INTO mokhatebin(name) VALUES (?)" , ('Amir',))
    cursor.execute("INSERT INTO mokhatebin(name) VALUES (?)" , ('Ali',))
    cursor.execute("INSERT INTO mokhatebin(name) VALUES (?)" , ('reza',))
    cursor.execute("INSERT INTO mokhatebin(name) VALUES (?)" , ('Alireza',))
    cursor.execute("INSERT INTO mokhatebin(name) VALUES (?)" , ('Samira',))
    cursor.execute("INSERT INTO mokhatebin(name) VALUES (?)" , ('Hale',))
    cursor.execute("INSERT INTO mokhatebin(name) VALUES (?)" , ('Neda',)) 
    conn.commit()
    print("مخاطبین اضافه شدند")
else:
    print(f"جدول قبلا {count} مخاطب دارد , INSERT انجام نشد")
while True:
    print("1: نمایش همه مخاطبین")
    print("2: اضافه کردن مخاطب")
    print("3: حذف مخاطب")
    print("4 : خروج از برنامه")

    choice = int(input("گزینه مورد نظر خود را وارد کنید"))
    if choice == 1 :
        cursor.execute("SELECT * FROM mokhatebin")
        print(cursor. fetchall())
    elif choice ==2 :
        name =input("لطفا نام خود را وارد کنید")
        
        cursor.execute("INSERT INTO mokhatebin(name) VALUES (?)" , (name ,))
        conn.commit()
        print("مخاطب اضافه شد")
    elif choice ==3 :
        name =input("لطفا نام مخاطب را برای حذف وارد کنید")
        cursor.execute("DELETE FROM mokhatebin WHERE name = ?" , (name ,))
        conn.commit()
        print("مخاطب حذف شد")
    elif choice == 4:
        break
    else:
        print("باید از گزینه 1 تا 4 را وارد کنید")

conn.close()

