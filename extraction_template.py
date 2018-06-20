# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:02:31 2018

@author: limjiaha
"""

import subprocess
import getpass

user = getpass.getuser()

measStep = "B3"

subprocess.call(r'"C:\Program Files\eSquare_x64_2.8.0\e2runjob.exe" -f "C:\Users\\' + user + r'\Desktop\automation_test.xml" -p [(]MeasStep[)]="' + measStep + '" -p [(]BasicType[)]="S1777A" -p [(]jobdef[)]="testing"')

#subprocess.call('"C:\Program Files\eSquare_x64_2.8.0\e2runjob.exe" -n automation_test -p [(]MeasStep[)]="' + measStep + '" -p [(]BasicType[)]="S1777A" -p [(]jobdef[)]="testing"')

