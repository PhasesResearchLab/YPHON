from __future__ import division
import sys
import xml.etree.ElementTree as ET
import gzip
import os
 
def get_code_version(xml='vasprun.xml'):
    if xml.endswith(".gz"):
        tree = ET.parse(gzip.open(xml))
    else:
        tree = ET.parse(xml)
    root = tree.getroot()
    codename, version = "", ""
    for i, elem in enumerate(root):
        for code in elem:
            codeprogram = code.get('name')
            if codeprogram=='program':
                codename = code.text
            elif codeprogram=='version':
                version = code.text
            if codename!="" and version!="": return codename, version
 
codename, code_version = get_code_version(xml=sys.argv[1])
if code_version >="6.2.0": print (0.004091649655126895)
else: print ("")
