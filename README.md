Medical Device Data Simulation and Cloud Dashboard: This project simulates medical device data, uploads it to Oracle Cloud Object Storage, and provides an interactive dashboard to analyze the data. 

Clone this repository:
git clone https://github.com/yourusername/yourproject.git

cd yourproject

Install Python dependencies: pip install -r requirements.txt

Run the data generator script to create fake medical device data as a CSV file: python data_generator/generate_fake_data.py

Upload the CSV file to Oracle Cloud Object Storage (make sure to configure your Oracle Cloud CLI and credentials). The data is uploaded **securely** to Oracle Cloud Object Storage using authenticated API calls. You can configure encryption-at-rest and access control policies on your Oracle Cloud bucket to ensure data privacy: python cloud_upload/upload_to_oracle.py

Start the Streamlit app to visualize the data: streamlit run dashboard/pathology_dashboard.py
