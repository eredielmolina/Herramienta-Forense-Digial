# Forensic Report Generator
# Generates forensic reports in Markdown and HTML formats
# according to the ISO/IEC 27043 standard.


class MarkdownReport:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        report = f'# {self.title}\n\n{self.content}'
        return report


class HTMLReport:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        report = (
            f'<!DOCTYPE html>\n<html>\n<head>\n<title>{self.title}</title>\n'
            f'</head>\n<body>\n<h1>{self.title}</h1>\n<p>{self.content}</p>\n'
            f'</body>\n</html>'
        )
        return report
