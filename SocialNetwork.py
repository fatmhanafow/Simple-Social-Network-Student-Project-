import csv
from os import name

class User:
    def __init__(self, name, family, day , month, year, gender, city, username, password):
        self.name = name
        self.family = family
        self.day = day
        self.month = month
        self.year = year 
        self.city = city
        self.gender = gender
        self.username = username
        self.password = password

class Menu(User):
    def __init__(self):
       # self.username = usern
       # self.password = pas
       pass
    def view_messages(self):
        with open('messages.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                    print(row)

    def view_friend_requests(self):
        with open('friends.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def create_account(self):
        name = input("name: ")
        family = input("last name: ")
        gender = input("gender: ")
        city = input("city: ")
        while True:
            year = int(input("Birthday year: "))
            if year > 1300 and year < 1402 :
                break
            else:
                print ("invalid number try again")

        while True:
            month = int(input("Birthday month: "))
            if month > 0 and 13 > month :
                break
            else:
                print("invalid month try again")
        while True:
            day = int(input("Birth day: "))
            if day > 0 and 32 > day:
                break
            else :
                print("invalid day try again")
        while True:
            b = 0
            username = input("username: ")
            with open('users.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[7] != username:                           
                        b = 2
                    else:
                        print("This username has already been selected")
            if b == 2:
                break
        password = input("password: ")
        user = User(name, family,day, month, year, gender, city, username, password)
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, family, day , month, year , gender, city, username, password])
        print("Your username has been registered")

    def login(self):
        self.username = input("username: ")
        self.password = input("password: ")
        a = 0
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[7] == self.username and row[8] == self.password:
                    print("You are logged in")
                    a = 2      
            if a != 2 :
                print("Username and password not found ")
                menu.show_menu()

    def friend_request(self):
        friend_id = input("enter friend's username: ")
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            with open('friends.csv','a',newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([self.username, friend_id])

            for row in reader:
                if row[7] == friend_id:
                    with open('friends.csv','r') as file:
                        read = csv.reader(file)
                        for row in read:
                            if row == f"{self.username }and {friend_id}" or f"{friend_id}and {self.username}":
                                print("you are already friends")
                                return
                    print("Friend request sent")                    
                    return
            print("Friend not found")
    
    def save_friend_request(self, friend_id):
       with open('friends.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.username, friend_id])

    def send_message(self):
        username = input("enter friend's username: ")
        with open('users.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[7] == username:
                        message = input("enter the message: ")
                        f = open('messages.csv','w')
                        f.write(f'{self.username}:{message} => {username}')
                        f.close()
                        print("message send")
                        return
                print('username not exist')

    def create_post(self):
      with open('post.csv', 'w', newline='') as file:            
            post = input("enter your post:")
            f = open('post.csv','w')
            f.write(f'{self.username}:{post}')
            f.close()
            print("post send")
            return

    def view_posts(self):            
            with open('post.csv', 'r') as file:
              reader = csv.reader(file)
              for row in reader:
                print(row) 
               
    def show_menu(self):
        while True:
            print("1.login")
            print("2.login as administrator")
            print("3.create account")
            print("4.exit")
            select = int(input("what you wanna do?:"))

            if select == 1:
                self.login()
                
                while True:
                    print("1.friend request")
                    print("2.send message")
                    print("3.viwe message")
                    print("4.new Post")
                    print("5.view posts")
                    print("6.exit")
                    enter = int(input("what you wanna do?"))
                    if enter == 1:
                        self.friend_request()
                    elif enter == 2:
                        self.send_message()
                    elif enter == 3:
                        self.view_messages() 
                    elif enter == 4:                    
                        self.create_post()
                    elif enter == 5:
                        self.view_posts()                  
                    elif enter == 6:
                        break
            elif select == 2:
                user = input("username: ")
                passw = input("password: ")
                if "admin" == user and "1234" == passw :
                    while True:
                        print('hello world!!')
                        print('1.viwe all message')
                        print('2.viwe all friendship')
                        print('3.exit')
                        sel = int(input())
                        if sel == 1:
                            self.view_messages()
                        elif sel == 2:
                            self.view_friend_requests()
                        elif sel == 3: 
                            self.show_menu()

                else:
                    print('password or username is not correct')

            elif select == 3:
                self.create_account()
                enter = 0
                while True:
                    print("1.friend request ")
                    print("2.send message")
                    print("3.viwe message")
                    print("4.exit")

                    enter = int(input("what you wanna do?"))
                    if enter == 1:
                        self.friend_request()
                    elif enter == 2:
                        self.send_message()
                    elif enter == 3:
                        self.view_messages() 
                    elif select == 4:
                        break
            elif select == 4:
                break
            else:
                print("try again")            
            if name == "__main__":
             menu = Menu()
             menu.show_menu()

menu = Menu()
menu.show_menu()