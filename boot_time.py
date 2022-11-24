import subprocess
import os
import pandas as pd

import datetime

def create_bat():
    tfile = open('script_time.bat', 'a')
 
    tfile.write("echo off" + "\n" +
                "cls" + "\n" +
                'wevtutil qe system "/q:*[System [(EventID=7001)]]" /rd:true /f:text /c:1 | findstr /i "date" >> logon.txt' + "\n" +
                'wevtutil qe system "/q:*[System [(EventID=7002)]]" /rd:true /f:text /c:1 | findstr /i "date" >> logoff.txt' + "\n" +
                "cls" + "\n" +
                "exit" + "\n"
                )
                
    tfile.close()


def compute_boot_time():
    res = subprocess.run("script_time.bat")

    time_ln = open("logon.txt", "r").read()

    time_ln = time_ln[time_ln.find("T") + 1:
                      time_ln.find("T") + 9
                      ]

    time_lf = open("logoff.txt", "r").read()

    time_lf = time_lf[time_lf.find("T") + 1:
                      time_lf.find("T") + 9
                      ]

    format = "%H:%M:%S"
    
##    print(time_ln)
##    print(time_lf)
    
    time_ln = datetime.datetime.strptime(time_ln, format)
    time_lf = datetime.datetime.strptime(time_lf, format)

##    print(time_ln)
##    print(time_lf)
    
    return time_ln - time_lf


def export_time():
    tfile = open('time.txt', 'a')
 
    tfile.write(str(compute_boot_time()))
                
    tfile.close()



def final_boot_df():

    create_bat()
    
    data = {"Boot_time" : [compute_boot_time()]}
    df_bench_boot = pd.DataFrame(data)

    os.remove("script_time.bat")
    os.remove("logon.txt")
    os.remove("logoff.txt")

    return df_bench_boot



    

##if __name__ == '__main__':
##    create_bat()
##    export_time()
##
##
##
##os.remove("script_time.bat")
##os.remove("logon.txt")
##os.remove("logoff.txt")
