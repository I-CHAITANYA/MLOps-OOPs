class chatbook:
    __user_id = 1
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default User"     # hidden attribute
        self.username = ""
        self.password = ""
        self.logged_in = False
        #self.menu()


    @staticmethod
    def get_id():
        return chatbook.__user_id

    @staticmethod
    def set_id(id):
        chatbook.__user_id = id


    def get_name(self):
        return self.__name


    def set_name(self, name):
        self.__name = name 


    def menu(self):
        print("Welcome to Chatbook!! How would you like to proceed?")
        user_input =input ("""
                1. Press 1 to signup
                2. Press 2 to signin
                3. Press 3 to write a post
                4. Press 4 to message a friend
                5. Press any other key to exit
                
                """)
        print("\n")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_msg()
        else: 
            exit()





    def signup(self):
        email = input("Enter your email here : ")
        pwd = input("Setup you password here: ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()


    def signin(self):
        if self.username == '' and self.password == '':
            print("Pls signup first by pressing 1 in the main menu.")
        else:
            uname = input("Enter your email here : ")
            pwd = input("Enter you password here: ")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully!!")
                self.logged_in = True
            else:
                print("Pls input correct credentials...")
        print("\n")
        self.menu()



    def my_post(self):
        if self.logged_in == True:
            txt = input("Enter your message here: ")
            print(f"following content has been posted : {txt}")
        else:
            print("You need to sign in to post something.")
        print("\n")
        self.menu()


    def send_msg(self):
        if self.logged_in == True:
            txt = input("Enter your message here: ")
            friend = input("whom to send message?")
            print(f"Your message has been successfully delivered to {friend}")
        else:
            print("You need to sign in to post something.")
        print("\n")
        self.menu()       



# obj = chatbook()