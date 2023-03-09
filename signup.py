import mysql.connector as m
con_obj = m.connect(username="root", password="Abhishek242@",
                    host="localhost", database='signup')

cur_obj = con_obj.cursor()
if con_obj.is_connected():
    print("yes")
else:
    print("no")
try:
    cur_obj.execute("insert into new (first_name,Last_name,Email,password,confirm_password) values("asdf","rfdg","af56@gmail.com","asfs43","1223sfd")")
    # cur_obj.Commit()
except Exception as e:
    print("Error:", e)
else:
    for i in cur_obj:
        print(i)
