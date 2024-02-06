from google.cloud import bigquery
from google.oauth2 import service_account
from menu import *
import pandas as pd
import os
# Replace 'your-project-id' with your actual Google Cloud project ID
# credentials='gcp_access.json'

# with open(credentials) as f:
#     credential_info=json.load(f)

# credentials =service_account.Credentials.from_service_account_file('C:\\Users\\User\\Desktop\\Rev_P[1]\\P1\\gcp_credentials.json')
# try:
#     with open(credentials) as f:
#         credential_info = json.load(f)
# except FileNotFoundError:
#     print(f"File '{credentials}' not found.")
# project_id = 'theta-cell-406519'
# dataset_id = 'Akash_Revfly'
# table_name='signups'
# table_id=f"{dataset_id}.{table_name}"

# client=bigquery.Client(credentials=credentials,project=project_id)



# # Set up BigQuery client
# client = bigquery.Client(project=project_id)

# query = f"SELECT * FROM `{project_id}.{dataset_id}.{table_id}`"

# # Run the query
# query_job = client.query(query)

# # Fetch the results
# results = query_job.result()

# # Print the results
# for row in results:
#     print(row)

# Create dataset if not exists
# dataset_ref = client.dataset(dataset_id)
# dataset = bigquery.Dataset(dataset_ref)
# try:
#     client.create_dataset(dataset)
#     print(f'Dataset {dataset_id} created.')
# except Exception as e:
#     print(f'Dataset {dataset_id} already exists.')

#  ---------------------------------------TABLE SIGNUPS-----------------------------------   

# # Define the table schema
# schema = [
#     bigquery.SchemaField('ID', 'STRING', mode='REQUIRED', description='Auto-generated UUID'),
#     bigquery.SchemaField('username', 'STRING', mode='NULLABLE'),
#     bigquery.SchemaField('password', 'STRING', mode='NULLABLE'),
#     bigquery.SchemaField('role', 'STRING', mode='NULLABLE'),
# ]

# # Create table if not exists
# table_ref = dataset_ref.table('signups')
# table = bigquery.Table(table_ref, schema=schema)
# try:
#     client.create_table(table)
#     print('Table Signups created.')
# except Exception as e:
#     print('Table travel already exists.')
  
  
  #  ---------------------------------------TABLE TRAVEL-----------------------------------   


 #Define the table schema
# schema = [
#     bigquery.SchemaField('Passenger_ID', 'INT64'),
#     bigquery.SchemaField('First_Name', 'STRING'),
#     bigquery.SchemaField('Last_Name', 'STRING'),
#     bigquery.SchemaField('Gender', 'STRING'),
#     bigquery.SchemaField('Age', 'INT64'),
#     bigquery.SchemaField('Nationality', 'STRING'),
#     bigquery.SchemaField('Airport_Name', 'STRING'),
#     bigquery.SchemaField('Airport_Country_Code', 'STRING'),
#     bigquery.SchemaField('Country_Name', 'STRING'),
#     bigquery.SchemaField('Airport_Continent', 'STRING'),
#     bigquery.SchemaField('Continents', 'STRING'),
#     bigquery.SchemaField('Departure_Date', 'DATE'),
#     bigquery.SchemaField('Arrival_Airport', 'STRING'),
#     bigquery.SchemaField('Pilot_Name', 'STRING'),
#     bigquery.SchemaField('Flight_Status', 'STRING'),
#     bigquery.SchemaField('Airline_Code', 'STRING'),
#     bigquery.SchemaField('TravelID', 'STRING'),
# ]

# # Create table if not exists
# table_ref = dataset_ref.table('travel')
# table = bigquery.Table(table_ref, schema=schema)
# try:
#     client.create_table(table)
#     print('Table travel created.')
# except Exception as e:
#     print('Table travel already exists.')

# print('Table creation process completed.')

#  ---------------------------------------TABLE AIRPORT-----------------------------------   


# schema = [
#     bigquery.SchemaField('AirportCode', 'STRING'),
#     bigquery.SchemaField('AirportName', 'STRING'),
#     bigquery.SchemaField('Location', 'STRING'),
#     bigquery.SchemaField('Country', 'STRING'),
#     bigquery.SchemaField('PassengerTraffic', 'FLOAT64'),
#     bigquery.SchemaField('Size', 'INT64'),
#     bigquery.SchemaField('Revenue', 'INT64'),
#     bigquery.SchemaField('FlightCount', 'INT64'),
# ]

# # Create a table reference
# table_ref = client.dataset(dataset_id).table('airport_codes')

# # Create the table
# table = bigquery.Table(table_ref, schema=schema)

# # Create the table if it doesn't exist
# try:
#     client.create_table(table)
#     print('Table airport_codes created.')
# except Exception as e:
#     print('Table airport_codes already exists.')


#  ---------------------------------------TABLE AIRLINE-----------------------------------   

# schema = [
#     bigquery.SchemaField('airline_Code', 'INT64'),
#     bigquery.SchemaField('revenue', 'INT64'),
#     bigquery.SchemaField('number_of_flights', 'INT64'),
#     bigquery.SchemaField('passenger_count', 'INT64'),
# ]

# # Create a table reference
# table_ref = client.dataset(dataset_id).table('airline_codes')

# # Create the table
# table = bigquery.Table(table_ref, schema=schema)

# # Create the table if it doesn't exist
# try:
#     client.create_table(table)
#     print('Table airline_codes created.')
# except Exception as e:
#     print('Table airline_codes already exists.')

# print('Table creation process completed.')




#-----------------------------Data Load------------------------------------

# def load_csv_into_bq(csv_path, table_id):
#     # Load CSV data into a Pandas DataFrame
#     df = pd.read_csv(csv_path)

#     # Specify the destination table
#     destination_table = f'{project_id}.{dataset_id}.{table_id}'
    
#     df.to_gbq(destination_table=destination_table, if_exists='replace')

   

#     print(f'Data from {csv_path} loaded into BigQuery table {table_id}.')

# # Specify the paths of your CSV files and corresponding table names
# csv_files = ["C:/Users/User/Desktop/Rev_P[1]/dataset/travel.csv", 
#              "C:/Users/User/Desktop/Rev_P[1]/dataset/airline_codes.csv", 
#              "C:/Users/User/Desktop/Rev_P[1]/dataset/airport_codes.csv"]
# table_names = ["travel", "airline_codes", "airport_codes"]

# # Load data from each CSV file into the corresponding table
# for csv_file, table_name in zip(csv_files, table_names):
#     load_csv_into_bq(csv_file, table_name)

#-------------------------Calling Menu----------------------------------
 
menu=MainMenu()
menu.run()

