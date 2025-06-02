import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timezone

fake = Faker()

def generate_data(num_records):
    data = []
    for i in range(num_records):
        patient_id = fake.uuid4()
        timestamp = datetime.now(timezone.utc).isoformat()
        tissue_type = random.choice(['Breast', 'Liver', 'Skin', 'Colon'])
        stain_type = random.choice(['H&E', 'IHC'])
        diagnostic_confidence = round(random.uniform(0.6, 0.99), 2)
        ai_risk_category = random.choice(['Benign', 'Suspicious', 'Malignant'])
        scanner_location = random.choice(['Clinic A', 'Clinic B', 'Clinic C'])
        image_url = f"https://objectstorage.fakecloud.com/bucket/images/{fake.uuid4()}.dzi"

        data.append({
            'patient_id': patient_id,
            'timestamp': timestamp,
            'tissue_type': tissue_type,
            'stain_type': stain_type,
            'diagnostic_confidence': diagnostic_confidence,
            'ai_risk_category': ai_risk_category,
            'scanner_location': scanner_location,
            'image_url': image_url
        })

    df = pd.DataFrame(data)
    return df

df = generate_data(500)
import os

# Create data directory if it doesn't exist
if not os.path.exists('../data'):
    os.makedirs('../data')
df.to_csv('../data/simulated_pathology_data.csv', index=False)
print("Simulated data generated.")