# Chain of Custody Manager

class ChainOfCustody:
    def __init__(self):
        self.entries = []

    def add_entry(self, item_id, description, handler, date_time, notes=''):
        entry = {
            'item_id': item_id,
            'description': description,
            'handler': handler,
            'date_time': date_time,
            'notes': notes
        }
        self.entries.append(entry)

    def display_entries(self):
        for entry in self.entries:
            print(f"Item ID: {entry['item_id']} | Description: {entry['description']} | "
                  f"Handler: {entry['handler']} | Date & Time: {entry['date_time']} | "
                  f"Notes: {entry['notes']}")

    def save_to_file(self, filepath):
        import json
        with open(filepath, 'w') as file:
            json.dump(self.entries, file, indent=4)

    def load_from_file(self, filepath):
        import json
        with open(filepath, 'r') as file:
            self.entries = json.load(file)

# Example usage:
# chain_of_custody = ChainOfCustody()
# chain_of_custody.add_entry('item123', 'Evidence collected', 'John Doe', '2026-02-17 01:27:53', 'Initial handling')
# chain_of_custody.display_entries()
# chain_of_custody.save_to_file('chain_of_custody.json')
