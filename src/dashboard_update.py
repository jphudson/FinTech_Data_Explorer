import pandas as pd
import os
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_projects_dataframe
from tableau_api_lib.utils.querying import get_views_dataframe

# Function to update Tableau dashboard (using Tableau API)
def update_dashboard(dataframe, tableau_connection, project_name, dashboard_name):
    """
    Updates a Tableau dashboard with new data.

    Parameters:
    dataframe (pd.DataFrame): Data to update in the dashboard.
    tableau_connection (TableauServerConnection): Established connection to Tableau Server.
    project_name (str): The name of the Tableau project containing the dashboard.
    dashboard_name (str): The name of the dashboard to update.
    """
    try:
        # Save the DataFrame to a CSV file
        csv_path = 'data/processed/updated_data.csv'
        dataframe.to_csv(csv_path, index=False)

        # Publish the CSV to Tableau Server or Tableau Online
        publish_data_source(tableau_connection, csv_path, project_name, dashboard_name)

        print("Dashboard update successful.")
    except Exception as e:
        print(f"Error updating dashboard: {e}")

def publish_data_source(connection, file_path, project_name, data_source_name):
    """
    Publishes a data source file to Tableau.

    Parameters:
    connection (TableauServerConnection): Tableau connection object.
    file_path (str): Path to the data source file (CSV).
    project_name (str): Name of the Tableau project.
    data_source_name (str): Data source name in Tableau.
    """
    try:
        # Get the project ID
        projects_df = get_projects_dataframe(connection)
        project_id = projects_df[projects_df['name'] == project_name]['id'].values[0]

        # Publish the data source
        connection.publish_data_source(file_path, project_id, data_source_name)
        print("Data source published successfully.")
    except Exception as e:
        print(f"Error publishing data source: {e}")

# Example usage
if __name__ == "__main__":
    # Example Tableau connection setup
    connection = TableauServerConnection(
        host='https://your-tableau-server.com',
        site_id='your-site-id',
        api_version='3.10',
        username='your-username',
        password='your-password'
    )

    # Connect to Tableau
    connection.sign_in()

    # Load processed data
    df = pd.read_csv('data/processed/updated_data.csv')

    # Update the dashboard
    update_dashboard(df, connection, 'Financial Analysis', 'Stock Dashboard')

    # Sign out
    connection.sign_out()