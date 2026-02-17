# Herramienta Forense Digital (DFTT)

Digital Forensic Tool – a command-line application for evidence acquisition, chain-of-custody tracking, and forensic report generation, following ISO/IEC standards.

## Features

- **Evidence Acquisition** – secure file copying with SHA-256 integrity verification (ISO/IEC 27037).
- **Chain of Custody** – JSON-based custody log with handler, timestamp, and notes tracking.
- **Report Generation** – produce Markdown or HTML forensic reports (ISO/IEC 27043).
- **Extensible Analysis** – base class for building forensic analysis plugins (ISO/IEC 27042).

## Usage

```bash
# Show help
python -m dftt.main --help

# Acquire evidence (secure copy with hash verification)
python -m dftt.main acquire <source> <destination>

# Add a chain-of-custody entry
python -m dftt.main custody add --file custody.json \
    --item-id EV001 --description "Initial collection" \
    --handler "Jane Doe" --notes "Laptop hard drive"

# Display chain of custody
python -m dftt.main custody show --file custody.json

# Generate a Markdown report
python -m dftt.main report --title "Analysis Report" --content "Findings..."

# Generate an HTML report and save to file
python -m dftt.main report --title "Analysis Report" --content "Findings..." \
    --format html --output report.html
```

## Running Tests

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```
dftt/
├── main.py                          # CLI entry point
├── core/constants.py                # Forensic constants & ISO/IEC standards
├── acquisition/
│   ├── copier.py                    # Secure file copying with SHA-256
│   └── manifest.py                  # Evidence manifest tracking
├── analysis/analyzer_base.py        # Base class for analysis plugins
├── chain_of_custody/custody_manager.py  # Chain of custody management
└── reporting/report_generator.py    # Markdown & HTML report generation
```

## Standards

| Standard | Description |
|---|---|
| ISO/IEC 27037 | Identification, collection, acquisition, and preservation of digital evidence |
| ISO/IEC 27041 | Assuring suitability and adequacy of forensic processes |
| ISO/IEC 27042 | Analysis and interpretation of digital evidence |
| ISO/IEC 27043 | Incident investigation principles and processes |
| ISO/IEC 29100 | Privacy framework |