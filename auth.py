from google.cloud import bigquery
from google.oauth2 import service_account
from admin import *
from users import *
ad=AdminClass()
us=user_class()


class UserAuthentication:

    def register(self, username, password, role='user'):
        credentials_path = "C:\\Users\\User\\Desktop\\Rev_P[1]\\P1\\gcp_credentials.json"
        client = bigquery.Client.from_service_account_json(credentials_path)
        project_id = 'theta-cell-406519'
        dataset_id = 'Akash_Revfly'
        table_name = 'signups'
        
        if role.lower() not in ['user', 'admin']:
            print("Invalid role. Defaulting to 'user'.")
            role = 'user'

        
        try:
            query = f"INSERT INTO `{project_id}.{dataset_id}.{table_name}` (username, password, role) VALUES ('{username}', '{password}', '{role}')"

            j=client.query(query)
            j.result()
            print("\n--------Registration successful. You can now log in.--------")
        except Exception as e:
            print(f"Error during registration: {e}")

    def login(self, username, password):
        credentials_path = "C:\\Users\\User\\Desktop\\Rev_P[1]\\P1\\gcp_credentials.json"
        client = bigquery.Client.from_service_account_json(credentials_path)
        project_id = 'theta-cell-406519'
        dataset_id = 'Akash_Revfly'
        table_name = 'signups'
        query = f"SELECT * FROM `{project_id}.{dataset_id}.{table_name}` WHERE username = '{username}' AND password = '{password}'"
        
        try:
            query_job = client.query(query)

            for row in query_job:
                if row:
                    role_query = f"SELECT role FROM `{project_id}.{dataset_id}.{table_name}` WHERE username = '{username}'"
                    role_job = client.query(role_query)

                    for role_row in role_job:
                        if role_row['role'] == "admin":
                            print("\n---------You've successfully Logged in as ADMIN---------\n")
                            ad.admin()
                        else:
                            print("\n--------You've successfully Logged in as USER--------\n")
                            us.user()

                        return True, row

            print("\nEither username or password is incorrect. Please try again.")
        except Exception as e:
            print(f"Error during login: {e}")

        return False, None

