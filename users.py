import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.cloud import bigquery
from tabulate import tabulate
from admin import AdminClass

ac=AdminClass()

class user_class:
    
    def __init__(self):
        credentials_path = "C:\\Users\\User\\Desktop\\Rev_P[1]\\P1\\gcp_credentials.json"
        self.client = bigquery.Client.from_service_account_json(credentials_path)
        self.project_id = 'theta-cell-406519'
        self.dataset_id = 'Akash_Revfly'
        

    def view_travellers(self):
        # credentials_path = "C:\\Users\\User\\Desktop\\Rev_P[1]\\P1\\gcp_credentials.json"
        # # client = bigquery.Client.from_service_account_json(credentials_path)
        # project_id = 'theta-cell-406519'
        # dataset_id = 'Akash_Revfly'
        table_name='travel'
        # table_id=f"{dataset_id}.{table_name}"
        
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
            (row['AirportCode'],row['AirportName'], row['Location'], row['Country'], row['PassengerTraffic'],
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
        query = f"SELECT username,role FROM `{self.project_id}.{self.dataset_id}`.signups"

        results = self.client.query(query).result()
        result = [dict(row) for row in results]

        data_tuples = [
            (row['username'], row['role'])
            for row in result
        ]
        headers = result[0].keys()
        print(tabulate(data_tuples, headers=headers, tablefmt="pretty"))

    def analyze_flights(self):
        # f"""
        # CREATE OR REPLACE VIEW `{self.project_id}.{self.dataset_id}`.analyse AS
        # SELECT t.passenger_id, t.first_name, t.country_name, t.airline_code, a.revenue, a.number_of_flights
        # FROM `{self.project_id}.{self.dataset_id}`.travel AS t
        # INNER JOIN `{self.project_id}.{self.dataset_id}`.airline_codes AS a
        # ON t.Airline_Code = a.airline_Code 
        # """
        
                
        # query2 = f"""
        # SELECT country_name, COUNT(number_of_flights) AS Total_Flights
        # FROM `{self.project_id}.{self.dataset_id}`.analyse
        # GROUP BY country_name
        # """
        
        q3=f"""
        SELECT
        t.Country_Name as Country_Name,
        SUM(a.number_of_flights) AS Total_Flights
        FROM
        `{self.project_id}.{self.dataset_id}`.travel AS t
        INNER JOIN
        `{self.project_id}.{self.dataset_id}`.airline_codes AS a
        ON
        t.Airline_Code = a.airline_Code
        GROUP BY
        t.country_name;
        """
        result = self.client.query(q3).result()
        # print(result)
        
        data = [(row[0], row[1]) for row in result]

# Create a DataFrame with appropriate column names
        df_Airline = pd.DataFrame(data, columns=['Country_Name', 'Total_Flights'])

        if df_Airline.empty:
            print("No data found for country code")
        else:
            plt.figure(figsize=(14, 8))
            sns.barplot(x='Country_Name', y='Total_Flights', data=df_Airline, palette='viridis')
            plt.title('Total Flights by Country')
            plt.xlabel('Country')
            plt.ylabel('Total Flights')
            plt.show()

        # Airline_data = result
        # df_Airline = pd.DataFrame(Airline_data)
        # print(df_Airline)
        # if df_Airline.empty:
        #     print(f"No data found for country code")
        # else:
        #     col_data = ['Country_Name', 'Total_Flights']

        #     plt.figure(figsize=(14, 8))
        #     sns.barplot(x=col_data[0], y=col_data[1], data=df_Airline, palette='viridis')
        #     plt.title('Total Flights by Country')
        #     plt.xlabel('Country')
        #     plt.ylabel('Total Flights')
        #     plt.show()
        
    def analyze_revenue_airline(self):
        
        
        q1=f"""
        SELECT
        airline_code,Revenue_Millions_
        FROM
        `{self.project_id}.{self.dataset_id}`.airline_codes 
        """
        result = self.client.query(q1).result()
        # print(result)
        
        data = [(row[0], row[1]) for row in result]

        # Create a DataFrame with appropriate column names
        df_Airline = pd.DataFrame(data, columns=['airline_code', 'Revenue_Millions_'])

        if df_Airline.empty:
            print("No data found for country code")
        else:
            plt.figure(figsize=(14, 8))
            sns.barplot(x='airline_code', y='Revenue_Millions_', data=df_Airline, palette='viridis')
            plt.title('Total revenue by Airline')
            plt.xlabel('Airlines')
            plt.ylabel('Total revenue ( Millions )')
            plt.show()
            
    def analyze_passenger_count(self):
            
            
            q1=f"""
            SELECT
            airline_code,Passenger_Count
            FROM
            `{self.project_id}.{self.dataset_id}`.airline_codes 
            """
            
            result = self.client.query(q1).result()
            # print(result)
            
            data = [(row[0], row[1]) for row in result]

    # Create a DataFrame with appropriate column names
            df_Airline = pd.DataFrame(data, columns=['airline_code', 'Passenger_Count'])

            if df_Airline.empty:
                print("No data found for country code")
            else:
                plt.figure(figsize=(14, 8))
                sns.barplot(x='airline_code', y='Passenger_Count', data=df_Airline, palette='viridis')
                plt.title('Total passengers by airlines')
                plt.xlabel('Airlines')
                plt.ylabel('Passenger Count ( Millions )')
                plt.show()


    def user(self):
        while True:
            print("\nChoose the option:")
            print("1. View Travellers")
            print("2. Airports")
            print("3. Airlines")
            print("4. Users")
            print("5. Analyse the flight count across country")
            print("6. Total revenue by particular Airlines")
            print("7. Total passenger count by particular Airlines")
            print("8. Exit")
            choice = input("\nEnter the choice:")
            if choice == "1":
                # self.view_travellers()
                ac.view_travellers()
            elif choice == "2":
                self.view_airports()
            elif choice == "3":
                self.view_airlines()
            elif choice == "4":
                self.view_users()
            elif choice == "5":
                self.analyze_flights()
            elif choice == "6":
                self.analyze_revenue_airline()
            elif choice == "7":
                self.analyze_passenger_count()
            elif choice == "8":
                break
