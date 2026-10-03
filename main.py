"""Clipboard Clear Now — Empty the Windows clipboard after printing whether it held text or an image."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='clipboard_clear_now',
        description='Empty the Windows clipboard after printing whether it held text or an image.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Clipboard Clear Now')
    print('Clear the clipboard on a shared PC.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
