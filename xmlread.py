#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "errrolyan"
# Date: 18-10-16

import os
import os.path
import xml.etree.ElementTree as ET
import pinyin

def coverFiles(sourceDir,  targetDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(sourceFile):
            open(targetFile, "wb").write(open(sourceFile, "rb").read())

def fileread(filepath):
    pathDir = os.listdir(filepath)
    for s in pathDir:
        newDir = os.path.join(filepath, s)
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".xml":
                print(newDir)
                tree = ET.parse(newDir)
                root = tree.getroot()
                print(root)
                for text in root.iter('text'):
                    print(text.text)
                    new_pinyin = pinyin.get(text.text, format="numerical", delimiter=" ") #  format="strip"
                    text.text = str(new_pinyin)
                    text.set('updated', 'yes')
        tree.write(newDir)

def xml_to_pinyin():
    coverFiles("./xml_in", "./xml_out")
    fileread("./xml_out")

xml_to_pinyin()