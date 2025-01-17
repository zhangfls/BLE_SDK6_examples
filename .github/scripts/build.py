# #####################################################################################
# The MIT License (MIT)
# Copyright (c) 2023 Renesas Electronics Corporation and/or its affiliates
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.
# #####################################################################################
"""Builds projects in repository using Cmake."""
import argparse
import json
import os
import pathlib
import shutil
import signal
import sys

from common import bashexec, bcolors, findProjectFiles


def parseArgs():
    """Get the arguments passed to script."""
    parser = argparse.ArgumentParser(
        prog="cMakeBuild",
        description="Builds projects in repository using Cmake.",
    )
    parser.add_argument(
        "-p",
        "--projdir",
        default=".",
        help="The directory to search project files. default='.'",
    )
    parser.add_argument(
        "-s",
        "--sdkdir",
        default=os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        ),
        help="the location of the SDK that is to be used for the build. default = ./build.py/../../../..",
    )
    parser.add_argument(
        "-x",
        "--exclude",
        default="",
        help="A list of directories to exclude from the build. Can be a file in any format, a string, or a list",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="verbose logging",
    )
    parser.add_argument(
        "-f",
        "--datafile",
        default="projectData.json",
        help="The projects definition file. default='artifacts/projectData.json'",
    )
    args = parser.parse_args()

    if args.exclude:
        args.exclude = open(args.exclude, "r", errors="ignore").read()

    return args


def setVars():
    """Set the variables used in script."""
    gccPath = bashexec("which arm-none-eabi-gcc")[0].decode("utf-8").rstrip()
    examplesdir = pathlib.Path(__file__).parents[2].resolve()
    startdir = pathlib.Path(os.getcwd())
    projectFiles = findProjectFiles(
        args.projdir, exdir=examplesdir, verbose=args.verbose
    )
    datafile = startdir.joinpath(args.datafile)

    for p in projectFiles:
        if p.absPath.name in args.exclude:
            if args.verbose:
                print(
                    bcolors.WARNING
                    + "Excluding project from build (specified with '-x' option): "
                    + str(p)
                    + bcolors.ENDC
                )
            p.cmakelistsFile = ""

    return projectFiles, gccPath, examplesdir, startdir, datafile


def buildProjects():
    """Build the projects with a CMakeLists.txt file."""
    buildResult = 0

    for p in projectFiles:
        if p.cmakelistsFile:
            print(bcolors.HEADER + "Building " + str(p) + bcolors.ENDC)

            os.chdir(p.absPath)

            if os.path.exists(p.builddir):
                shutil.rmtree(p.builddir)
            p.builddir.mkdir()

            bashexec(
                [
                    "cmake",
                    "-DDEVICE_NAME=" + p.title,
                    "-DCMAKE_BUILD_TYPE=DEBUG",
                    "-DCMAKE_TOOLCHAIN_FILE="
                    + str(examplesdir)
                    + "/build_utils/gcc/arm-none-eabi.cmake",
                    "-DGCC_TOOLCHAIN_PATH=" + str(gccPath),
                    "-DDIALOG_SDK_PATH=" + str(args.sdkdir),
                    "-DDIALOG_EXAMPLE_PATH=" + str(examplesdir),
                    "-S",
                    ".",
                    "-B",
                    str(p.builddir),
                ],
                prnt=args.verbose,
            )

            os.chdir(p.builddir)

            if bashexec("make -j 7", prnt=args.verbose)[1] != 0:
                buildResult += 1
                print(bcolors.FAIL+ str(p)+bcolors.ENDC)

    return buildResult


def writeOutput():
    """Write the output to the standard projectData.json."""
    if args.verbose:
        print("writing output")

    os.chdir(startdir)
    projdat = []
    for p in projectFiles:
        projdat.append(p.toDictComplete())
    jsonProjdat = json.dumps(projdat, indent=2)

    with open(datafile, "w") as outfile:
        outfile.write(jsonProjdat)


def handleAbort(signum, frame):
    """Handle if the script gets aborted."""
    print(bcolors.FAIL + "ABORTING BUILDS..." + bcolors.ENDC)
    writeOutput()
    sys.exit(1)


if __name__ == "__main__":
    args = parseArgs()
    projectFiles, gccPath, examplesdir, startdir, datafile = setVars()
    signal.signal(
        signal.SIGINT, handleAbort
    )  # still write output if script aborted during build
    buildResult = buildProjects()
    writeOutput()

    os.chdir(startdir)
    sys.exit(buildResult)
