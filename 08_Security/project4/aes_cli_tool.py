import argparse
from utils import *

# -- Setup argparse --
parser = argparse.ArgumentParser(description="AES Encryption CLI Tool")
subparsers = parser.add_subparsers(dest="command")

# encrypt message
encrypt_msg = subparsers.add_parser("encrypt", help="Encrypt a message")
encrypt_msg.add_argument("--message", required=True)

# decrypt message
decrypt_msg = subparsers.add_parser("decrypt", help="Decrypt a message")
decrypt_msg.add_argument("--cipher", required=True)

# encrypt file
encrypt_file_cmd = subparsers.add_parser("encrypt-file", help="Encrypt a file")
encrypt_file_cmd.add_argument("--file", required=True)

# decrypt file
decrypt_file_cmd = subparsers.add_parser("decrypt-file", help="Decrypt a file")
decrypt_file_cmd.add_argument("--file", required=True)

# -- Parse arguments --
args = parser.parse_args()

if args.command == "encrypt":
    encrypt_message(args.message)

elif args.command == "decrypt":
    decrypt_message(args.cipher)

elif args.command == "encrypt-file":
    encrypt_file(args.file)

elif args.command == "decrypt-file":
    decrypt_file(args.file)

else:
    parser.print_help()
