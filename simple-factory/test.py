import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'SimpleFactory.java'])
subprocess.call(['java', 'SimpleFactory'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'SimpleFactory.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'SimpleFactory.cpp', '-o', 'SimpleFactory'])
subprocess.call(['./SimpleFactory'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'SimpleFactory.ts'])
subprocess.call(['node', 'SimpleFactory.js'])

os.remove('SimpleFactory')
os.remove('SimpleFactory.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)