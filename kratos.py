import subprocess
import os
import pandas as pd

import datetime


########################## CPU ##########################

def get_cpu_bench():
    print("CPU Benchmark running...")

    os.chdir(".\CPU\CinebenchR23")

    results = subprocess.run([".\Cinebench.exe", "g_CinebenchAllTests=true"],
                         capture_output=True,
                         text=True
                         ).stdout.strip("\n")

    multi = int(results[results.find("CB ") + 3 :
                        results.find(".", results.find("CB "))]
                )
    single = int(results[results.rfind("CB ") + 3 :
                         results.find(".", results.rfind("CB "))]
                 )

    data = {"Single":[single], "Multi":[multi]}

    df_bench_cpu = pd.DataFrame(data)

    os.chdir("../..")

    return df_bench_cpu


########################## CPU_GPU ##########################

def get_cpu_gpu_bench():
    print("CPU-GPU Benchmark running...")

    os.chdir(".\CPU_GPU\CINEBENCH_R15")

    results = subprocess.run("cpu_bench_script.bat",
                             capture_output=True,
                             text=True
                             ).stdout.strip("\n")


    val = results.find("CINEBENCH R15 Result")

    results = results[val:]

    single = float(results[results.find("Rendering (Single   CPU) : ") + 27:
                        results.find(" pts", results.find("Rendering (Single   CPU) : "))]
                )

    
    multi = float(results[results.rfind("Rendering (Multiple CPU) : ") + 27:
                         results.find(" pts", results.rfind("Rendering (Multiple CPU) : "))]
                 )

    gpu_opencl = float(results[results.rfind("Shading (OpenGL)                : ") + 34:
                         results.find(" fps", results.rfind("Shading (OpenGL)                : "))]
                 )

    gpu_opencl_match = float(results[results.rfind("Shading (OpenGL) Reference Match: ") + 34:
                                     results.find("%", results.rfind("Shading (OpenGL) Reference Match: "))]
                             )

    data = {"Single" : [single],
            "Multi" : [multi],
            "Gpu_OpenCl" : [gpu_opencl],
            "Gpu_OpenCl_match" : [gpu_opencl_match]
            }
    
    df_bench_cpu_gpu = pd.DataFrame(data)


    os.chdir("../..")

    return df_bench_cpu_gpu


########################## DISK ##########################

#### PROBLEMES POUR LANCER DISKSPD

def get_disk_bench():
    print("DISK Benchmark running...")

    os.chdir("./DISK/DiskSpd-2.0.21a/x86/")

##    res_w = subprocess.run([".\\diskspd.exe", "-b128K", "-d10", "-o32", "-t1",
##                          "-W0", "-S", "-w100", "-Z128K", "c:\\testfile.dat"],
##                         capture_output=True,
##                         text=True
##                         ).stdout.strip("\n")

    res = subprocess.run("write.bat")

    resw = open("resw.txt", "r").read()

    results = resw

    
    val = results.find("total")

    temp1 = val
    for i in range(0, 2):
        temp1 = results.find("|", temp1 + 1)

    temp2 = results.find("|", temp1 + 1)

    write_speed = results[temp1 + 1: temp2].replace(" ","")
    

##    res_r = subprocess.run([".\\diskspd.exe", "-b128K", "-d10", "-o32", "-t1",
##                          "-W0", "-S", "-w0", "c:\\testfile.dat"],
##                         capture_output=True,
##                         text=True
##                         ).stdout.strip("\n")


    res = subprocess.run("read.bat")

    resr = open("resr.txt", "r").read()
    
    results = resr

    
    val = results.find("total")

    temp1 = val
    for i in range(0, 2):
        temp1 = results.find("|", temp1 + 1)

    temp2 = results.find("|", temp1 + 1)

    read_speed = results[temp1 + 1: temp2].replace(" ","")

    data = {"Write" : [write_speed], "Read" : [read_speed]}
    df_bench_disk = pd.DataFrame(data)

    os.chdir("../../..")

    return df_bench_disk

def speed():
    from DISK import bench_disk

    os.chdir(".\DISK")

    temp = bench_disk.final_disk_df()

    print(os.getcwd())
    
    return


########################## BOOT ##########################

def get_boot_bench():
    print("BOOT Benchmark running...")

    os.chdir("./BOOT/")

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
    
    
    time_ln = datetime.datetime.strptime(time_ln, format)
    time_lf = datetime.datetime.strptime(time_lf, format)

    boot_t = time_ln - time_lf

    data = {"Boot_time" : [boot_t]}
    df_bench_boot = pd.DataFrame(data)

    os.remove("logon.txt")
    os.remove("logoff.txt")

    os.chdir("..")

    return df_bench_boot




########################## FINAL ##########################

def all_bench_df():
    temp1 = get_cpu_gpu_bench()
    temp2 = get_disk_bench()
    temp3 = get_boot_bench()
    final_df = pd.concat([temp1,
                          temp2,
                          temp3
                          ],
                         ignore_index = False,
                         axis = 1
                         )
    return final_df

##if __name__ == '__main__':
##    temp = all_bench_df()
##    print(temp)
##    temp.to_csv('final_df.csv', index = False )
