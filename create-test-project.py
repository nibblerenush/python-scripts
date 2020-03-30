#!/bin/python3

import os
import sys

def main():
  dirTarget = sys.argv[1]
  projectName = sys.argv[2]
  projectDir = dirTarget + "/" + projectName

  try:
    os.mkdir(projectDir)
    os.mkdir(projectDir + "/build")
  except OSError:
    print("Creation of the directory %s failed" % projectDir)

  mainCppContent = \
    "#include <iostream>\n" \
    "\n" \
    "int main()\n" \
    "{\n" \
    "  return 0;\n" \
    "}\n"
  
  with open(projectDir + "/main.cpp", 'w') as mainCppFile:
    mainCppFile.write(mainCppContent)
  
  cmakeListsContent = \
    "cmake_minimum_required(VERSION 3.0.0)\n" \
    "project(" + projectName + ")\n" \
    "add_executable(${PROJECT_NAME} main.cpp)\n" \
    "target_compile_options(${PROJECT_NAME} PRIVATE -Wall -O0 -g -pg)\n"
  
  with open(projectDir + "/CMakeLists.txt", "w") as cmakeListsFile:
    cmakeListsFile.write(cmakeListsContent)
  
if __name__ == "__main__":
  main()
