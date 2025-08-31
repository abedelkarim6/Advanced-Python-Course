import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name", type=str, required=True, help="Your name")

args = parser.parse_args()
print(f"Hello {args.name}")
