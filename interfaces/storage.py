from interfaces import StorageInterface
import json
class JsonStorage(StorageInterface):
    def __init__(self,data):
         print("Saving data to JSON file...")
         print(json.dumps(data, indent=2))

class CSVStorage(StorageInterface):
    def save(self, data):
        print("Saving data to CSV format...")
        print(",".join(data.keys()))
        print(",".join(str(v) for v in data.values()))
