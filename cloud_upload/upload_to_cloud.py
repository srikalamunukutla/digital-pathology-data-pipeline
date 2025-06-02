import oci

config = oci.config.from_file()
object_storage = oci.object_storage.ObjectStorageClient(config)

namespace = object_storage.get_namespace().data
bucket_name = 'your_bucket_name'

with open('../data/simulated_pathology_data.csv', 'rb') as f:
    object_storage.put_object(namespace, bucket_name, 'simulated_pathology_data.csv', f)

print("File uploaded to Oracle Cloud.")