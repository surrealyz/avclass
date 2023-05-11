#! /usr/bin/env python
import json
import logging
import os
import requests
import time
from ratelimit import limits, sleep_and_retry
from subprocess import Popen, PIPE

def main():
    for year in range(2019, 2020):
        for idx, month in enumerate(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']):
            apk_dir = '/data2/yizheng/android/malware/%s/%s' % (year, month)
            output_file = '/home/yz/code/mal/src/dataset/avclass/android/%s_%s.txt' % (year, month)
            # ./avclass2/avclass2_labeler.py -staticdir /space1/android/malware/2012/01/ -vt3 > /home/yz/code/mal/src/dataset/avclass/android/2012_01.txt
            cmd = './avclass2/avclass2_labeler.py -staticdir %s -p -vt3 -hash sha256 > %s' % (apk_dir, output_file)
            print(cmd)
            os.system(cmd)

    return

if __name__=='__main__':
    main()
