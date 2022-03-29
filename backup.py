from ibm_cloud_databases.cloud_databases_v5 import *
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
import os


# Check for the optional postgreSQL CRN / Service URL
if not os.environ.get("POSTGRES_SERVICE_URL"):
    postgres_service_url = "https://api.us-south.databases.cloud.ibm.com/v5/ibm"
else:
    postgres_service_url = os.environ.get("POSTGRES_SERVICE_URL")

# Create an IAM authenticator.
authenticator = IAMAuthenticator(os.environ.get("IBM_API_KEY"))

# Construct the service client.
cloud_databases_service = CloudDatabasesV5(authenticator=authenticator)
cloud_databases_service.set_service_url(postgres_service_url)

# Function to backup the deployment
def on_demand_backup(deployment_id):
    start_ondemand_backup_response = cloud_databases_service.start_ondemand_backup(
        id=deployment_id).get_result()
    print(json.dumps(start_ondemand_backup_response, indent=2))

# Calling the on demand backup function
on_demand_backup(os.environ.get("POSTGRES_DEPLOYMENT_ID"))