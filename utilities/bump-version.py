import argparse
import json

def bumpVersion(repo, bumpMajorVersion=False, bumpMinorVersion=False, bumpBugVersion=False):

    with open("version.json", "r") as versionFile:
        versionJSON = json.load(versionFile)

    currentVersion = versionJSON[repo]
    major, minor, bug = currentVersion.split(".")

    if bumpBugVersion:
        bug=int(bug)+1

    if bumpMinorVersion:
        minor=int(minor)+1

    if bumpMajorVersion:
        major=int(major)+1

    newVersion = str(major)+"."+str(minor)+"."+str(bug)

    versionJSON["history"].append("[{0}] Bumped {1} Version {2} -> {3}".format(repo, currentVersion, newVersion ))
    
    # with()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--test', dest="testPypiRepo", action="store_true", help="Publish on Test-PyPi")

    parser.add_argument('--main', dest="mainPypiRepo", action="store_true", help="Publish on PyPi")

    parser.add_argument('--major', dest="bumpMajorVersion", action="store_true", help="Release Major Version - X.0.0")

    parser.add_argument('--minor', dest="bumpMinorVersion", action="store_true", help="Release Minor Version - 0.X.0")

    parser.add_argument('--bug', dest="bumpBugVersion", action="store_true", help="Release Minor Version - 0.0.X")

    parser.set_defaults(testPypiRepo=False, mainPypiRepo=False, bumpMajorVersion=False, bumpMinorVersion=False, bumpBugVersion=False)

    args = parser.parse_args() 


    