from google.cloud import bigquery
from tabulate import tabulate
from google.oauth2 import service_account

class AdminClass:
    def __init__(self):
        credentials_path = "C:\\Users\\User\\Desktop\\Rev_P[1]\\P1\\gcp_credentials.json"
        self.client = bigquery.Client.from_service_account_json(credentials_path)
        self.project_id = 'theta-cell-406519'
        self.dataset_id = 'Akash_Revfly'
        

    def view_travellers(self):
        credentials_path = "C:\\Users\\User\\Desktop\\Rev_P[1]\\P1\\gcp_credentials.json"
        client = bigquery.Client.from_service_account_json(credentials_path)
        project_id = 'theta-cell-406519'
        dataset_id = 'Akash_Revfly'
        table_name='travel'
        table_id=f"{dataset_id}.{table_name}"
        
        query = f"SELECT * FROM `{self.project_id}.{self.dataset_id}.{table_name}` LIMIT 10"

        df=self.client.query(query).to_dataframe()
        
        if df.empty:
            print("No data")
        else:
            print(tabulate(df,headers='keys',tablefmt="pretty"))

    def view_airports(self):
        table_name='airport_codes'
        query = f"SELECT * FROM `{self.project_id}.{self.dataset_id}.{table_name}` LIMIT 10"

        results = self.client.query(query).result()
        result = [dict(row) for row in results]

        data_tuples = [
            ( row['AirportCode'] , row['AirportName'], row['Location'], row['Country'], row['PassengerTraffic'],
             row['Size'], row['Revenue'], row['FlightCount'])
            for row in result
        ]
        headers = result[0].keys()
        print(tabulate(data_tuples, headers=headers, tablefmt="pretty"))

      
    def view_airlines(self):
        table_name = 'airline_codes'
        
        query = f"SELECT Airline_Code,Revenue_Millions_,Number_of_Flights,Passenger_Count FROM `{self.project_id}.{self.dataset_id}.{table_name}` order by Airline_Code"

        df=self.client.query(query).to_dataframe()
        
        if df.empty:
            print("No data")
        else:
            print(tabulate(df,headers='keys',tablefmt="pretty"))


           

    def view_users(self):
        query = f"SELECT * FROM `{self.project_id}.{self.dataset_id}`.signups"

        results = self.client.query(query).result()
        result = [dict(row) for row in results]

        data_tuples = [
            (row['username'], row['password'], row['role'])
            for row in result
        ]
        headers = result[0].keys()
        print(tabulate(data_tuples, headers=headers, tablefmt="pretty"))

    
    def create_records(self, airline_code, revenue, number_of_flights, passenger_count):
        query = f"INSERT INTO `{self.project_id}.{self.dataset_id}`.airline_codes (airline_code, revenue_millions_, number_of_flights, passenger_count) VALUES ('{airline_code}', {revenue}, {number_of_flights}, {passenger_count})"
        
        try:
            job=self.client.query(query)
            job.result()
            print("\nSuccessfully created a new data\n")
        except Exception as e:
            print(f"Error inserting data: {str(e)}")


    def update_records(self, username, password):
        query = f"UPDATE `{self.project_id}.{self.dataset_id}.signups` SET password = '{password}' WHERE username = '{username}'"
        
        try:
            job=self.client.query(query)
            job.result()
            print("\nPassword Updated")
        except Exception as e:
            print(f"Error updating password: {str(e)}")


    def delete_records(self, username):
        query = f"DELETE FROM `{self.project_id}.{self.dataset_id}.signups` WHERE username = '{username}'"
        self.client.query(query)
        print(f"\nID no. {username} has been successfully deleted\n")

    def admin(self):
        while True:
            print("\nChoose the option:")
            print("---------------------")
            print("1. View Travellers")
            print("2. Airports")
            print("3. Airlines")
            print("4. Users details")
            print("5. Create airline data")
            print("6. Update users password")
            print("7. Delete users")
            print("8. Exit")
            choice = input("\nEnter the choice:")
            if choice == "1":
                self.view_travellers()
            elif choice == "2":
                self.view_airports()
            elif choice == "3":
                self.view_airlines()
            elif choice == "4":
                self.view_users()
            elif choice == "5":
                airline_code = input("\nEnter the airline code:")
                revenue = int(input("Enter the revenue"))
                number_of_flights = int(input("Enter the number of flights"))
                passenger_count = int(input("Enter the passenger count"))
                self.create_records(airline_code, revenue, number_of_flights, passenger_count)
            elif choice == "6":
                user_name =input("\nEnter the USERNAME to be changed:")
                new_password = input("Enter the new password:\t")
                self.update_records(user_name, new_password)
            elif choice == "7":
                query = f"SELECT * FROM `{self.project_id}.{self.dataset_id}`.signups"

                results = self.client.query(query).result()
                result = [dict(row) for row in results]

                data_tuples = [
                    (row['username'], row['role'])
                    for row in result
                ]
                headers = result[0].keys()
                print(tabulate(data_tuples, headers=headers, tablefmt="pretty"))
                username = input("\nEnter the USERNAME to be deleted:")
                print(f"\nAre you sure? You want to delete ---> '{username}`")
                res=input("\nY/N ?:  ")
                if res in ['Y','y']:
                    self.delete_records(username)
                else:
                    print("Return back to options")
                    self.admin()
            elif choice == "8":
                break


