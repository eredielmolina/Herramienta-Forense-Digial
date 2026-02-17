import argparse
import os
from datetime import datetime

from dftt.acquisition.copier import secure_copy
from dftt.acquisition.manifest import EvidenceManifest, ManifestEntry
from dftt.chain_of_custody.custody_manager import ChainOfCustody
from dftt.reporting.report_generator import MarkdownReport, HTMLReport


def cmd_acquire(args):
    """Acquire evidence by securely copying a file with SHA-256 verification."""
    secure_copy(args.source, args.destination)
    print(f"Evidence acquired: {args.source} -> {args.destination}")


def cmd_custody_add(args):
    """Add an entry to the chain of custody log."""
    chain = ChainOfCustody()
    if os.path.isfile(args.file):
        chain.load_from_file(args.file)
    chain.add_entry(
        item_id=args.item_id,
        description=args.description,
        handler=args.handler,
        date_time=args.date_time or datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        notes=args.notes or '',
    )
    chain.save_to_file(args.file)
    print(f"Entry added to chain of custody: {args.file}")


def cmd_custody_show(args):
    """Display the chain of custody log."""
    chain = ChainOfCustody()
    if not os.path.isfile(args.file):
        print(f"File not found: {args.file}")
        return
    chain.load_from_file(args.file)
    chain.display_entries()


def cmd_report(args):
    """Generate a forensic report in Markdown or HTML format."""
    content = args.content
    if args.content_file:
        with open(args.content_file, 'r') as f:
            content = f.read()

    if args.format == 'html':
        report = HTMLReport(args.title, content)
    else:
        report = MarkdownReport(args.title, content)

    output = report.generate_report()

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"Report saved to {args.output}")
    else:
        print(output)


def main():
    parser = argparse.ArgumentParser(
        prog='dftt',
        description='DFTT - Digital Forensic Tool (Herramienta Forense Digital)',
    )
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # acquire subcommand
    acquire_parser = subparsers.add_parser('acquire', help='Acquire evidence (secure copy with hash verification)')
    acquire_parser.add_argument('source', help='Source file path')
    acquire_parser.add_argument('destination', help='Destination file path')
    acquire_parser.set_defaults(func=cmd_acquire)

    # custody subcommand
    custody_parser = subparsers.add_parser('custody', help='Chain of custody management')
    custody_sub = custody_parser.add_subparsers(dest='custody_command', help='Custody sub-commands')

    custody_add = custody_sub.add_parser('add', help='Add an entry to the chain of custody')
    custody_add.add_argument('--file', required=True, help='Path to the custody JSON file')
    custody_add.add_argument('--item-id', required=True, help='Evidence item identifier')
    custody_add.add_argument('--description', required=True, help='Description of the custody event')
    custody_add.add_argument('--handler', required=True, help='Name of the handler')
    custody_add.add_argument('--date-time', default=None, help='Date and time (default: now)')
    custody_add.add_argument('--notes', default='', help='Additional notes')
    custody_add.set_defaults(func=cmd_custody_add)

    custody_show = custody_sub.add_parser('show', help='Display the chain of custody')
    custody_show.add_argument('--file', required=True, help='Path to the custody JSON file')
    custody_show.set_defaults(func=cmd_custody_show)

    # report subcommand
    report_parser = subparsers.add_parser('report', help='Generate a forensic report')
    report_parser.add_argument('--title', required=True, help='Report title')
    report_parser.add_argument('--content', default='', help='Report content text')
    report_parser.add_argument('--content-file', default=None, help='Read report content from file')
    report_parser.add_argument('--format', choices=['markdown', 'html'], default='markdown', help='Output format')
    report_parser.add_argument('--output', default=None, help='Output file path (default: stdout)')
    report_parser.set_defaults(func=cmd_report)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()