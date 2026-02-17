# Analyzer Base Class for Forensic Analysis Plugins

class AnalyzerBase:
    """
    Base class for forensic analysis plugins following ISO/IEC 27042.
    """
    def __init__(self, data):
        """
        Initializes the analyzer with the provided data.
        :param data: The data to be analyzed.
        """
        self.data = data

    def analyze(self):
        """
        Perform analysis on the data.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this!")

    def report(self):
        """
        Generate a report of the analysis results.
        This method can be overridden to provide specific reporting.
        """
        return f"Analysis report for data: {self.data}",
