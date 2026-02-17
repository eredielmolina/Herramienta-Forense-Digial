# Evidence Manifest Generation and Export Following ISO/IEC 27037

class EvidenceManifest:
    def __init__(self):
        self.evidence_items = []

    def add_item(self, item):
        self.evidence_items.append(item)

    def generate_manifest(self):
        manifest = """Evidence Manifest
Generated following ISO/IEC 27037

Items:
"""
        for item in self.evidence_items:
            manifest += f"- {item}\n"
        return manifest

    def export_manifest(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.generate_manifest())

# Example usage
if __name__ == '__main__':
    manifest = EvidenceManifest()
    manifest.add_item("Item 1: Digital Evidence")
    manifest.add_item("Item 2: Physical Evidence")
    manifest.export_manifest("evidence_manifest.txt")
