import os
import tempfile
import unittest

from dftt.acquisition.copier import secure_copy
from dftt.acquisition.manifest import EvidenceManifest, ManifestEntry
from dftt.analysis.analyzer_base import AnalyzerBase
from dftt.chain_of_custody.custody_manager import ChainOfCustody
from dftt.core.constants import FORENSIC_CONSTANTS, ISO_IEC_STANDARDS
from dftt.reporting.report_generator import HTMLReport, MarkdownReport


class TestConstants(unittest.TestCase):
    def test_forensic_constants_exist(self):
        self.assertIn("BYTE", FORENSIC_CONSTANTS)
        self.assertEqual(FORENSIC_CONSTANTS["BYTE"], 8)

    def test_iso_standards_exist(self):
        self.assertIn("ISO/IEC 27037", ISO_IEC_STANDARDS)


class TestSecureCopy(unittest.TestCase):
    def test_copy_and_verify(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as src:
            src.write(b"forensic evidence data")
            src_path = src.name
        dst_path = src_path + '.copy'
        try:
            secure_copy(src_path, dst_path)
            with open(src_path, 'rb') as f1, open(dst_path, 'rb') as f2:
                self.assertEqual(f1.read(), f2.read())
        finally:
            os.unlink(src_path)
            if os.path.exists(dst_path):
                os.unlink(dst_path)

    def test_copy_nonexistent_source(self):
        with self.assertRaises(FileNotFoundError):
            secure_copy('/nonexistent/file.txt', '/tmp/dst.txt')


class TestManifest(unittest.TestCase):
    def test_add_entry(self):
        manifest = EvidenceManifest()
        entry = ManifestEntry('EV001', 'Hard drive image', '2026-01-15')
        manifest.add_entry(entry)
        self.assertEqual(len(manifest.entries), 1)
        self.assertEqual(manifest.entries[0].identifier, 'EV001')

    def test_add_invalid_entry(self):
        manifest = EvidenceManifest()
        with self.assertRaises(ValueError):
            manifest.add_entry("not a ManifestEntry")


class TestAnalyzerBase(unittest.TestCase):
    def test_analyze_raises(self):
        analyzer = AnalyzerBase("sample data")
        with self.assertRaises(NotImplementedError):
            analyzer.analyze()

    def test_report_returns_string(self):
        analyzer = AnalyzerBase("sample data")
        result = analyzer.report()
        self.assertIsInstance(result, str)
        self.assertIn("sample data", result)


class TestChainOfCustody(unittest.TestCase):
    def test_add_and_save(self):
        chain = ChainOfCustody()
        chain.add_entry('EV001', 'Collected', 'Jane Doe', '2026-01-15 10:00:00', 'Initial')
        self.assertEqual(len(chain.entries), 1)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as f:
            filepath = f.name
        try:
            chain.save_to_file(filepath)
            chain2 = ChainOfCustody()
            chain2.load_from_file(filepath)
            self.assertEqual(len(chain2.entries), 1)
            self.assertEqual(chain2.entries[0]['item_id'], 'EV001')
        finally:
            os.unlink(filepath)


class TestReportGenerator(unittest.TestCase):
    def test_markdown_report(self):
        report = MarkdownReport("Test Title", "Test content.")
        output = report.generate_report()
        self.assertIn("# Test Title", output)
        self.assertIn("Test content.", output)

    def test_html_report(self):
        report = HTMLReport("Test Title", "Test content.")
        output = report.generate_report()
        self.assertIn("<title>Test Title</title>", output)
        self.assertIn("<h1>Test Title</h1>", output)
        self.assertIn("<p>Test content.</p>", output)
        self.assertTrue(output.startswith("<!DOCTYPE html>"))


if __name__ == '__main__':
    unittest.main()
