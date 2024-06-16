db=[]

# Add to Database
def insert(id,name,username,password):
    try:
        db.append({"id":id,"name":name,"username":username,"password":password})
    except:
        print("Data is incorrect!")

# for reading / showing data base record
def show():
    for i in db:
        print(i)

# for updating the record value
def updatePassword(id,password):
    for i in db:
        for items in db.items():
            if items["id"]==id:
                items["password"]=password
                print("password updated")
            else:
                print("Record not found!!!!!")

# deleting values from records
def delete(id):
    for i in db:
        for items in db.items():
            if items["id"]==id:
                del i
                print("Record deleted")
            else:
                print("Record not found!!!!!")


