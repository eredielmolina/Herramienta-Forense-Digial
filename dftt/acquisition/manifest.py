class ManifestEntry:
    def __init__(self, identifier, description, acquisition_date):
        self.identifier = identifier  # Unique identifier for the entry
        self.description = description  # Description of the evidence
        self.acquisition_date = acquisition_date  # Date when the evidence was acquired

class EvidenceManifest:
    def __init__(self):
        self.entries = []  # List to hold manifest entries

    def add_entry(self, entry):
        if isinstance(entry, ManifestEntry):
            self.entries.append(entry)
        else:
            raise ValueError('Entry must be a ManifestEntry instance')

    def __repr__(self):
        return (f'EvidenceManifest(entries={self.entries})\n' +
                '\n'.join(str(entry) for entry in self.entries))
