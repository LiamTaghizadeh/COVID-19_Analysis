import json
import csv
import sys

class JsonToCsvConverter:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.data = None
        self.fieldnames = []

    def load_json(self):
        with open(self.input_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def normalize_data(self):
        if isinstance(self.data, dict):
            self.data = [self.data]
        elif not isinstance(self.data, list):
            raise ValueError("JSON must be an object or an array.")

    def collect_fieldnames(self):
        keys = set()
        for record in self.data:
            keys.update(record.keys())
        self.fieldnames = sorted(keys)

    def flatten_value(self, value):
        if isinstance(value, (dict, list)):
            return json.dumps(value, ensure_ascii=False)
        return value

    def write_csv(self):
        with open(self.output_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames, restval='')
            writer.writeheader()
            for record in self.data:
                row = {key: self.flatten_value(record.get(key, '')) for key in self.fieldnames}
                writer.writerow(row)

    def convert(self):
        self.load_json()
        self.normalize_data()
        self.collect_fieldnames()
        self.write_csv()
        print(f"CSV file successfully saved to '{self.output_path}'.")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
    else:
        in_file = './data.json'
        out_file = "Crona_covid_19.csv"
        if not out_file:
            out_file = "output.csv"

    try:
        converter = JsonToCsvConverter(in_file, out_file)
        converter.convert()
    except Exception as e:
        print(f"Error: {e}")
