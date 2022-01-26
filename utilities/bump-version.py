import argparse
import json
from datetime import datetime


def bumpVersion(repo, bumpMajorVersion=False, bumpMinorVersion=False, bumpBugVersion=False):

    # Read Version.json
    with open("./version.json", "r") as versionFile:
        versionJSON = json.load(versionFile)

    currentVersion = versionJSON[repo]

    # Split Three-Level Version into individual Components
    major, minor, bug = currentVersion.split(".")

    # Bump Bug Version
    if bumpBugVersion:
        bug = int(bug)+1

    # Bump Minor Version
    if bumpMinorVersion: 
        minor = int(minor)+1

    # Bump Major Version
    if bumpMajorVersion:
        major = int(major)+1

    # Joining The Sub-Version Numbers
    newVersion = str(major)+"."+str(minor)+"."+str(bug)

    # Updating New Version
    versionJSON[repo] = newVersion

    now = datetime.now()

    # Logging Statement for tracking Updation Activities
    loggingStatement = "[{0}] Bumped {1} Version {2} -> {3}".format(
        now.strftime("%d/%m/%Y %H:%M:%S"), repo, currentVersion, newVersion)

    versionJSON["logs"].append(loggingStatement)

    # Syncing updates to the version.json
    with open("./version.json", "w") as versionFile:
        json.dump(versionJSON, versionFile, indent=4)

    print(loggingStatement)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--test', dest="testPypiRepo",
                        action="store_true", help="Publish on Test-PyPi")

    parser.add_argument('--main', dest="mainPypiRepo",
                        action="store_true", help="Publish on PyPi")

    parser.add_argument('--major', dest="bumpMajorVersion",
                        action="store_true", help="Release Major Version - X.0.0")

    parser.add_argument('--minor', dest="bumpMinorVersion",
                        action="store_true", help="Release Minor Version - 0.X.0")

    parser.add_argument('--bug', dest="bumpBugVersion",
                        action="store_true", help="Release Minor Version - 0.0.X")

    parser.set_defaults(testPypiRepo=False, mainPypiRepo=False,
                        bumpMajorVersion=False, bumpMinorVersion=False, bumpBugVersion=False)

    args = parser.parse_args()

    if args.testPypiRepo == True and args.mainPypiRepo == False:
        bumpVersion(
            repo="test-pypi",
            bumpMajorVersion=args.bumpMajorVersion,
            bumpMinorVersion=args.bumpMinorVersion,
            bumpBugVersion=args.bumpBugVersion
        )
    elif args.testPypiRepo == False and args.mainPypiRepo == True:
        bumpVersion(
            repo="pypi",
            bumpMajorVersion=args.bumpMajorVersion,
            bumpMinorVersion=args.bumpMinorVersion,
            bumpBugVersion=args.bumpBugVersion
        )
    elif args.testPypiRepo == True and args.mainPypiRepo == True:
        print("Multiple Repo Bumps are not Allowed.")

        # bumpVersion(
        #     repo="test-pypi",
        #     bumpMajorVersion=args.bumpMajorVersion,
        #     bumpMinorVersion=args.bumpMinorVersion,
        #     bumpBugVersion=args.bumpBugVersion
        # )
        # bumpVersion(
        #     repo="pypi",
        #     bumpMajorVersion=args.bumpMajorVersion,
        #     bumpMinorVersion=args.bumpMinorVersion,
        #     bumpBugVersion=args.bumpBugVersion
        # )

if __name__ == "__main__":
    main()

'''
[Usage]

usage: python bump-version.py [-h] [--test] [--main] [--major] [--minor] [--bug]

optional arguments:
  -h, --help  show this help message and exit
  --test      Publish on Test-PyPi
  --main      Publish on PyPi
  --major     Release Major Version - X.0.0
  --minor     Release Minor Version - 0.X.0
  --bug       Release Minor Version - 0.0.X


[Examples]

- To Bump Minor Version for Test-PyPi Repo, use:

python bump-version.py --test --minor


- To Bump Major and Bug Version for PyPi Repo, use:

python bump-version.py --main --major --bug

'''