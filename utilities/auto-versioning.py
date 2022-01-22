import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--major', dest="updateForMajorVersion", action="store_true", help="Release Major Version - X.0.0")

    parser.add_argument('--minor', dest="updateForMinorVersion", action="store_true", help="Release Minor Version - 0.X.0")

    parser.add_argument('--bug', dest="updateForBugVersion", action="store_true", help="Release Minor Version - 0.0.X")

    parser.set_defaults(updateForMajorVersion=False, updateForMinorVersion=False, updateForBugVersion=False)

    args = parser.parse_args() 
    