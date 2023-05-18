#! /usr/bin/env python
import json
import logging
import os
import requests
import time
from ratelimit import limits, sleep_and_retry
from subprocess import Popen, PIPE

def main():
    json_dir = "/data2/yizheng/tesseract/virustotal"
    output_file = "/home/yz/code/mal/src/dataset/avclass/tesseract_family_pt2_avclass.tsv"
    # ./avclass2/avclass2_labeler.py -staticdir /space1/android/malware/2012/01/ -vt3 > /home/yz/code/mal/src/dataset/avclass/android/2012_01.txt
    cmd = './avclass2/avclass2_labeler.py -staticdir %s -p -vt3 -hash sha256 > %s' % (json_dir, output_file)
    print(cmd)
    os.system(cmd)

    return

if __name__=='__main__':
    main()
