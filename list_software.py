import subprocess
import pandas as pd
from datetime import datetime

import os

from bs4 import BeautifulSoup

def softwarem2():
    aue = Bs_data.find_all('ApplicationUninstallerEntry')
    
    tmp = []
    for temp in aue:
        
        disp_name = temp.find('DisplayName')
        if disp_name is not None:
            disp_name = disp_name.text
        else:
            disp_name = ""
        
        disp_version = temp.find('DisplayVersion')
        if disp_version is not None:
            disp_version = disp_version.text
        else:
            disp_version = ""

        disp_date = temp.find('InstallDate')
        disp_date = disp_date.text
        
        disp_pub = temp.find('Publisher')
        if disp_pub is not None:
            disp_pub = disp_pub.text
        else:
            disp_pub = ""
        
        disp_size = temp.find('EstimatedSize')
        disp_size = disp_size.text

        
        tmp.append([disp_name, disp_version, disp_date, disp_pub, disp_size])
        
        
    df_sm2 = pd.DataFrame(data = tmp,
                         columns = ["DisplayName", "DisplayVersion", "InstallDate",
                                    "Publisher", "EstimatedSize"]
                         )

    return df_sm2


##GET ID
   
import wmi
c = wmi.WMI()

def get_df_net():
    temp_mac, temp_ncid = ([], [])

    for temp in c.Win32_NetworkAdapter():
            temp_mac.append(temp.MACAddress)
            temp_ncid.append(temp.NetConnectionID)

    net_infos = list(zip(temp_mac, temp_ncid))
    
    net_infos_temp = [list(temp) for temp in net_infos]

    labels_net = ["MACAddress", "NetConnectionID"]

    df_net = pd.DataFrame(data = net_infos_temp,
                         columns = labels_net
                         )

    df_net = df_net[df_net['NetConnectionID'].str.contains("WiFi") | df_net['NetConnectionID'].str.contains('Ethernet')]

    df_net = df_net.sort_values("NetConnectionID")

##    df_net = pd.DataFrame(columns = labels_net)
##
##    print(df_net.empty)
    
    return df_net
    
########################### FINAL ###########################


def finaldf():
    date = datetime.now()
    format = "%Y-%m-%dT%H:%M:%S"
    date = date.strftime(format)
    
    final_df = softwarem2()

    final_df.insert(0, "Date", str(date))

    temp = get_df_net()

    if temp.empty:
        final_df.insert(0, "Pc_id", "Unknown")
    else:
        final_df.insert(0, "Pc_id", temp.iloc[0]['MACAddress'])

    return final_df





if __name__ == '__main__':
    
    os.chdir(".\\BCUninstaller_4.16_portable")

    subprocess.run([".\BCU-console", "export", "list_soft.xml"])

    with open('list_soft.xml', 'r') as f:
        data = f.read()
        
    Bs_data = BeautifulSoup(data, "xml")

    os.chdir("..")
    
    temp = finaldf()
    temp.to_csv('final_df.csv', index = False )


