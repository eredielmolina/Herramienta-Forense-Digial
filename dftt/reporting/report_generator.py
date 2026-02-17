# Forensic Report Generator

This script generates forensic reports in Markdown and HTML formats according to the ISO/IEC 27043 standard.

## Features
- Generate reports in Markdown format
- Generate reports in HTML format

## Markdown Report Generation

The following function generates a report in Markdown format:

```python
class MarkdownReport:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        report = f'# {self.title}\n\n{self.content}'
        return report
```

## HTML Report Generation

The following function generates a report in HTML format:

```python
class HTMLReport:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def generate_report(self):
        report = f'<!DOCTYPE html>\n<html>\n<head>\n<title>{self.title}</title>\n</head>\n<body>\n<h1>{self.title}</h1>\n<p>{self.content}</p>\n</body>\n</html>'
        return report
```

# Usage Example

markdown_report = MarkdownReport("Forensic Analysis", "This is the content of the forensic analysis.")
html_report = HTMLReport("Forensic Analysis", "This is the content of the forensic analysis.")

print(markdown_report.generate_report())
print(html_report.generate_report())
