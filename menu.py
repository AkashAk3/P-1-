from auth import UserAuthentication
auth=UserAuthentication()

class MainMenu:
    
    def display_menu(self):
        print("\n=== Main Menu ===")
        print("1. Register")
        print("2. Log In")
        print("3. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-3): ")

            if choice == "1":
                username = input("\nEnter your username: ")
                password = input("Enter your password: ")
                role = input("Enter your role (user/admin): ").lower()
                if role not in ['user', 'admin']:
                    print("Invalid role. Defaulting to 'user'.")
                    role = 'user'
                auth.register(username, password,role)
                
            elif choice == "2":
                username = input("Enter your username: ")
                password = input("Enter y our password: ")
                auth.login(username, password)
                
            elif choice == "3":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    
                    
                    
    

