from flask import Flask, jsonify
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Set up Azure Blob Storage
CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=ricostgiot123;AccountKey=EPSmvTHdZpjeKfUQkxGKXLbkb4uvZRX0Gp2z0/A4ekRUXeR1FKuyKrA9di3ZT0sTy7tJgvyK12JG+AStenVmPw=="
CONTAINER_NAME = "messages01"
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Set up Flask app
app = Flask(__name__)

# Define route to display the latest image
@app.route('/')
def display_latest_image():
    # List all blobs in the container
    blob_list = container_client.list_blobs()

    # Get the latest blob (which has the largest timestamp in the name)
    latest_blob = max(blob_list, key=lambda x: x.name)

    # Return an HTML page with the latest image
    return f"""
        <html>
            <body>
                <img src="{blob_service_client.primary_endpoint}{CONTAINER_NAME}/{latest_blob.name}">
            </body>
        </html>
    """

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
