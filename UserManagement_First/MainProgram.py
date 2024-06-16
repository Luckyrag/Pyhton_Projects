# making the project which make user management which having the records of user.
import database as db
def main(answer="yes"):
    while answer in ["yes","Yes","YES",'y',"Y"]:
        # making button for user chiose
        print("Enter choice : ")
        print("1.Add Record")
        print("2.Show Record")
        print("3.Update Password")
        print("4.Delete Record")
        print("5.Go to Main")
        print("6. Exit")

        choice=int(input("Enter Your choice"))
        match choice:
            case 1:
                id=input("Enter your id :-")
                name=input("Enter your name")
                username=input("Enter Username")
                password=input("Enter your password")
                if (id.isnumeric() and name.isalpha() and username.isalnum() and password.isalnum()):
                    db.insert(id,name,username,password) # making proper sequence
                else:
                    print("Error ! Incorect input() ")
            case 2:
                db.show()
            case 3:
                id=input("Enter your id :-")
                password=input("Enter your password")
                if (id.isnumeric() and password.isalnum()):
                   db.updatePassword(id,password)
                else:
                    print("Error ! Incorect input() ")
            case 4:
                id=input("Enter your id")
                if id.isnumeric():
                    db.delete(id)
                else:
                    print("INCORRECT OUTPUT")
            case 5:
                main()

            case 6:
                answer="none"
            case _:
                print("!!Error(defult)")


if __name__=="__main__":
    main()