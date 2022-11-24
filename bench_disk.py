import subprocess
import os
import pandas as pd


def run_diskpd_write():
    res = subprocess.run([".\\Diskspd.exe", "-b128K", "-d10", "-o32", "-t1",
                          "-W0", "-S", "-w100", "-Z128K", "c:\\testfile.dat"],
                         capture_output=True,
                         text=True
                         ).stdout.strip("\n")

    return res

def run_diskpd_read():
    res = subprocess.run([".\\Diskspd.exe", "-b128K", "-d10", "-o32", "-t1",
                          "-W0", "-S", "-w0", "c:\\testfile.dat"],
                         capture_output=True,
                         text=True
                         ).stdout.strip("\n")

    return res


def get_write_speed():
    results = run_diskpd_write()
    
    val = results.find("total")

    temp1 = val
    for i in range(0, 2):
        temp1 = results.find("|", temp1 + 1)

    temp2 = results.find("|", temp1 + 1)

    write_speed = results[temp1 + 1: temp2].replace(" ","")

    return float(write_speed)
    
def get_read_speed():
    results = run_diskpd_read()
    
    val = results.find("total")

    temp1 = val
    for i in range(0, 2):
        temp1 = results.find("|", temp1 + 1)

    temp2 = results.find("|", temp1 + 1)

    read_speed = results[temp1 + 1: temp2].replace(" ","")

    return float(read_speed)


def speeds():
    data = {"Write" : [get_write_speed()], "Read" : [get_read_speed()]}
    df_bench_disk = pd.DataFrame(data)

    return df_bench_disk

def final_disk_df():
    os.chdir("./DiskSpd-2.0.21a/x86/")
    return speeds()



##if __name__ == '__main__':
##    os.chdir("./DiskSpd-2.0.21a/x86/")
##    temp = speeds()
##    os.chdir("../..")
##    temp.to_csv('disk_df.csv', index = False )
