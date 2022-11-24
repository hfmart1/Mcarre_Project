##Importer les bibliothèques globales
import pandas as pd

from datetime import datetime

########################### HARDWARE ###########################
##Importer les bibliothèques spécifiques à la récupération des infos hardware
import wmi

c = wmi.WMI()

##Récupérer les informations sur le PC dans les différentes catégories
##(commentaires sur les deux premières parties mais applicables pour toutes les autres)

######### Système d'exploitation #########

##Définir la fonction pour récuperer les informations sur l'OS
def get_df_os():
    
##  Parcourir l'objet c.Win32_OperatingSystem() pour y récupérer les informations qui nous intéressent
    for temp in c.Win32_OperatingSystem():
            os_infos = [temp.BootDevice,
                        temp.Caption,
                        temp.InstallDate,
                        temp.NumberOfUsers,
                        temp.Organization,
                        temp.OSArchitecture,
                        temp.SystemDrive,
                        temp.Version
                        ]
##  Créer les étiquettes pour le dataframe avec les informations que l'on a récupéré
    labels_os = ["BootDevice", "Caption", "InstallDate", "NumberOfUsers",
                 "Organization", "OSArchitecture", "SystemDrive", "Version"
                 ]
    
##  Création du dataframe panda
    df_os = pd.DataFrame(data = [os_infos],
                         columns = labels_os
                         )
    
##  Modifier le format de la date afin qu'elle soit dans le bon format pour MySQL
    temp = df_os["InstallDate"][0][:df_os["InstallDate"][0].find(".")]
    
    date = datetime.strptime(temp, '%Y%m%d%H%M%S')

    format = "%Y-%m-%dT%H:%M:%S"
    date = date.strftime(format)

    df_os["InstallDate"][0] = date

    return df_os

######### Drivers #########

##Définir la fonction pour récupérer les informations sur les drivers
def get_df_dri():

##  Créer des listes vides pour les informations qui nous intéressent
    temp_c, temp_l, temp_pn, temp_st = ([],[],[],[])

    
##  Parcourir l'objet c.Win32_SystemDriver() pour y récupérer les informations qui nous intéressent
    for temp in c.Win32_SystemDriver():
            temp_c.append(temp.Caption)
            temp_l.append(temp.Name)
            temp_pn.append(temp.PathName)
            temp_st.append(temp.ServiceType)

##  Regrouper les listes des informations qui nous intéressent
    dri_infos = list(zip(temp_c, temp_l, temp_pn, temp_st))
            
##  Créer les étiquettes pour le dataframe avec les informations que l'on a récupéré
    labels_dri = ["Caption", "Name",
                  "PathName", "ServiceType"
                   ]
    
##  Création du dataframe panda
    df_dri = pd.DataFrame(data = dri_infos,
                          columns = labels_dri
                          )
##  Réordonner le dataframe par ordre alphabétique
    df_dri = df_dri.sort_values("Name")

    return df_dri

######### Carte mère #########

def get_df_mb():
    for temp in c.Win32_BaseBoard():
        mb_infos = [temp.Description,
                    temp.Manufacturer,
                    temp.Name,
                    temp.Product,
                    temp.SerialNumber,
                    temp.Version
                    ]


    labels_mb = ["Description", "Manufacturer", "Name",
                 "Product", "SerialNumber", "Version"
                 ]

    df_mb = pd.DataFrame(data = [mb_infos],
                         columns = labels_mb
                         )

    return df_mb

######### BIOS #########

def get_df_bi():
    for temp in c.Win32_BIOS():
            bi_infos = [temp.BiosCharacteristics,
                        temp.BIOSVersion,
                        temp.Manufacturer,
                        temp.ReleaseDate,
                        temp.SerialNumber,
                        temp.Version
                        ]


    labels_bi = ["BiosCharacteristics", "BIOSVersion", "Manufacturer",
                 "ReleaseDate", "SerialNumber", "Version"
                 ]

    df_bi = pd.DataFrame(data = [bi_infos],
                         columns = labels_bi
                         )

    temp = df_bi["ReleaseDate"][0][:df_bi["ReleaseDate"][0].find(".")]
    
    date = datetime.strptime(temp, '%Y%m%d%H%M%S')

    format = "%Y-%m-%dT%H:%M:%S"
    date = date.strftime(format)

    df_bi["ReleaseDate"][0] = date

    return df_bi

######### Processeur #########

def get_df_cpu():
    for temp in c.Win32_Processor():
            cpu_infos = [temp.AddressWidth,
                        temp.Architecture,
                        temp.CurrentClockSpeed,
                        temp.CurrentVoltage,
                        temp.DataWidth,
                        temp.Description,
                        temp.Family,
                        temp.L2CacheSize,
                        temp.L3CacheSize,
                        temp.LoadPercentage,
                        temp.Manufacturer,
                        temp.Name,
                        temp.NumberOfCores,
                        temp.NumberOfEnabledCore,
                        temp.NumberOfLogicalProcessors,
                        temp.ProcessorId,
                        temp.SocketDesignation,
                        temp.ThreadCount,
                        temp.UpgradeMethod,
                        temp.Version
                        ]


    labels_cpu = ["AddressWidth", "Architecture", "CurrentClockSpeed", "CurrentVoltage",
                  "DataWidth", "Description", "Family", "L2CacheSize", "L3CacheSize",
                  "LoadPercentage", "Manufacturer", "Name", "NumberOfCores", "NumberOfEnabledCore",
                  "NumberOfLogicalProcessors", "ProcessorId", "SocketDesignation", "ThreadCount",
                 "UpgradeMethod", "Version"
                 ]

    df_cpu = pd.DataFrame(data = [cpu_infos],
                          columns = labels_cpu
                          )

    return df_cpu

######### Carte Graphique #########

def get_df_gpu():
    for temp in c.Win32_VideoController():
            gpu_infos = [temp.AdapterCompatibility,
                         temp.AdapterRAM * -4096,
                         temp.Availability,
                         temp.ConfigManagerErrorCode,
                         temp.Caption,
                         temp.CurrentHorizontalResolution,
                         temp.CurrentVerticalResolution,
                         temp.VideoModeDescription,
                         temp.CurrentRefreshRate,
                         temp.DeviceID,
                         temp.DriverDate,
                         temp.DriverVersion,
                         temp.VideoMemoryType,
                        ]


    labels_gpu = ["AdapterCompatibility", "AdapterRAM", "Availability", "ConfigManagerErrorCode",
                  "Caption", "CurrentHorizontalResolution", "CurrentVerticalResolution",
                  "VideoModeDescription", "CurrentRefreshRate", "DeviceID", "DriverDate",
                  "DriverVersion", "VideoMemoryType"
                 ]

    df_gpu = pd.DataFrame(data = [gpu_infos],
                          columns = labels_gpu
                          )

    temp = df_gpu["DriverDate"][0][:df_gpu["DriverDate"][0].find(".")]
    
    date = datetime.strptime(temp, '%Y%m%d%H%M%S')

    format = "%Y-%m-%dT%H:%M:%S"
    date = date.strftime(format)

    df_gpu["DriverDate"][0] = date
    
    return df_gpu

######### RAM #########


def get_df_ram():
    temp_dl, temp_cpty, temp_cptn, temp_ccs, temp_cv, temp_ff, temp_m, temp_pn, temp_sn = ([],[],[],[],[],[],[],[],[])

    for temp in c.Win32_PhysicalMemory():
            temp_dl.append(temp.DeviceLocator)
            temp_cpty.append(int(temp.Capacity))
            temp_cptn.append(temp.Caption)
            temp_ccs.append(temp.ConfiguredClockSpeed)
            temp_cv.append(temp.ConfiguredVoltage)
            temp_ff.append(temp.FormFactor)
            temp_m.append(temp.Manufacturer)
            temp_pn.append(temp.PartNumber)
            temp_sn.append(temp.SerialNumber)
            


    ram_infos = list(zip(temp_dl, temp_cpty, temp_cptn, temp_ccs, temp_cv, temp_ff, temp_m, temp_pn, temp_sn))

    ram_infos_temp = [list(temp) for temp in ram_infos]

    labels_ram = ["DeviceLocator", "Capacity", "Caption", "ConfiguredClockSpeed", "ConfiguredVoltage",
                  "FormFactor", "Manufacturer", "PartNumber", "SerialNumber"
                  ]

    df_ram = pd.DataFrame(data = ram_infos_temp,
                          columns = labels_ram
                          )
    
    return df_ram

######### Stockage Physique #########

def get_df_dd():
    temp_cd, temp_c, temp_did, temp_it, temp_mt, temp_sn, temp_s, temp_p = ([],[],[],[],[],[], [], [])

    for temp in c.Win32_DiskDrive():
            temp_cd.append(temp.CapabilityDescriptions)
            temp_c.append(temp.Caption)
            temp_did.append(temp.Caption)
            temp_it.append(temp.InterfaceType)
            temp_mt.append(temp.MediaType)
            temp_sn.append(temp.SerialNumber)
            temp_s.append(temp.Size)
            temp_p.append(temp.Partitions)

            dd_infos = list(zip(temp_cd, temp_c, temp_did, temp_it, temp_mt, temp_sn, temp_s, temp_p))


    dd_infos_temp = [list(temp) for temp in dd_infos]

    labels_dd = ["CapabilityDescriptions", "Caption", "DeviceID", "InterfaceType",
                 "MediaType", "SerialNumber", "Size", "Partitions"
                 ]

    df_dd = pd.DataFrame(data = dd_infos_temp,
                         columns = labels_dd
                         )

    return df_dd

######### Stockage Logique #########

def get_df_ldd():
    temp_c, temp_dt, temp_fs, temp_frs, temp_mt, temp_s, temp_vn = ([],[],[],[],[],[],[])

    for temp in c.Win32_LogicalDisk():
            temp_c.append(temp.Caption)
            temp_dt.append(temp.DriveType)
            temp_fs.append(temp.FileSystem)

            if temp.FreeSpace == None:
                temp_frs.append(None)
            else:
                temp_frs.append(int(temp.FreeSpace))
                
            temp_mt.append(temp.MediaType)

            if temp.Size == None:
                temp_s.append(None)
            else:
                temp_s.append(int(temp.Size))
                
            temp_vn.append(temp.VolumeName)

            ldd_infos = list(zip(temp_c, temp_dt, temp_fs, temp_frs, temp_mt, temp_s, temp_vn))


    ldd_infos_temp = [list(temp) for temp in ldd_infos]

    labels_ldd = ["Caption", "DriveType", "FileSystem", "FreeSpace",
                 "MediaType", "Size", "VolumeName"
                 ]

    df_ldd = pd.DataFrame(data = ldd_infos_temp,
                          columns = labels_ldd
                          )


    return df_ldd

######### Réseau #########

def get_df_net():
    temp_d, temp_g, temp_mac, temp_man, temp_ncid = ([],[],[],[],[])

    for temp in c.Win32_NetworkAdapter():
            temp_d.append(temp.Description)
            temp_g.append(temp.GUID)
            temp_mac.append(temp.MACAddress)
            temp_man.append(temp.Manufacturer)
            temp_ncid.append(temp.NetConnectionID)

            net_infos = list(zip(temp_d, temp_g, temp_mac, temp_man, temp_ncid))


    net_infos_temp = [list(temp) for temp in net_infos]

    labels_net = ["Description", "GUID", "MACAddress",
                 "Manufacturer", "NetConnectionID"
                 ]

    df_net = pd.DataFrame(data = net_infos_temp,
                         columns = labels_net
                         )

    df_net = df_net[df_net['NetConnectionID'].str.contains("WiFi") | df_net['NetConnectionID'].str.contains('Ethernet')]

    df_net = df_net.sort_values("NetConnectionID")

    df_net = df_net.dropna().reset_index(drop=True)
    
    return df_net

######### Batterie #########

def get_df_ba():
    ba_infos = list([])

    for temp in c.Win32_Battery():
            ba_infos = [temp.Availability,
                        temp.BatteryStatus,
                        temp.Caption,
                        temp.Chemistry,
                        temp.DesignVoltage,
                        temp.EstimatedChargeRemaining,
                        temp.EstimatedRunTime
                        ]


    labels_ba = ["Availability", "BatteryStatus", "Caption", "Chemistry",
                 "DesignVoltage", "EstimatedChargeRemaining", "EstimatedRunTime"
                 ]

    if len(ba_infos) == 0 :
            ba_infos = [None] * len(labels_ba)

    df_ba = pd.DataFrame(data = [ba_infos],
                         columns = labels_ba
                         )
    return df_ba

######### Ecran #########

def get_df_sc():
    temp_a, temp_c, temp_n, temp_ppx, temp_ppy, temp_pdid = ([],[],[],[],[],[])

    for temp in c.Win32_DesktopMonitor():
            temp_a.append(temp.Availability)
            temp_c.append(temp.Caption)
            temp_n.append(temp.Name)
            temp_ppx.append(temp.PixelsPerXLogicalInch)
            temp_ppy.append(temp.PixelsPerYLogicalInch)
            temp_pdid.append(temp.PNPDeviceID)

            sc_infos = list(zip(temp_a, temp_c, temp_n, temp_ppx, temp_ppy, temp_pdid))


    sc_infos_temp = [list(temp) for temp in sc_infos]

    labels_sc = ["Availability", "Caption", "Name", "PixelsPerXLogicalInch",
                 "PixelsPerYLogicalInch", "PNPDeviceID"
                 ]

    df_sc = pd.DataFrame(data = sc_infos_temp,
                         columns = labels_sc
                         )
    return df_sc

######### Ports #########

def get_df_port():
    temp_ct, temp_d, temp_erd, temp_ird, temp_pt, temp_t = ([],[],[],[],[],[])

    port_infos = []

    for temp in c.Win32_PortConnector():
            temp_ct.append(temp.ConnectorType)
            temp_d.append(temp.Description)
            temp_erd.append(temp.ExternalReferenceDesignator)
            temp_ird.append(temp.InternalReferenceDesignator)
            temp_pt.append(temp.PortType)
            temp_t.append(temp.Tag)

            port_infos = list(zip(temp_ct, temp_d, temp_erd, temp_ird, temp_pt, temp_t))



    labels_port = ["ConnectorType", "Description", "ExternalReferenceDesignator",
                   "InternalReferenceDesignator", "PortType", "Tag"]


    df_port = pd.DataFrame(data = port_infos,
                           columns = labels_port
                           )
    return df_port

######### Final #########

##Définir la fonction pour créer un dataframe contenant toutes les informations
def final_df():
    
##  Récupérer la date et l'heure du PC
    date = datetime.now()
    format = "%Y-%m-%dT%H:%M:%S"
    date = date.strftime(format)

##  Concaténer les dataframes des informations que l'on souhaite récupérer
    final_df = pd.concat([get_df_os().add_suffix('_os'),
                          get_df_dri().add_suffix('_dri'),
                          get_df_mb().add_suffix('_mb'),
                          get_df_port().add_suffix('_port'),
                          get_df_bi().add_suffix('_bi'),
                          get_df_cpu().add_suffix('_cpu'),
                          get_df_gpu().add_suffix('_gpu'),
                          get_df_ram().add_suffix('_ram'),
                          get_df_dd().add_suffix('_dd'),
                          get_df_ldd().add_suffix('_ldd'),
                          get_df_net().add_suffix('_net'),
                          get_df_ba().add_suffix('_ba'),
                          get_df_sc().add_suffix('_sc')
                          ],
                         ignore_index = False,
                         axis = 1
                         )

##  Ajouter la date dans le dataframe
    final_df.insert(0, "Date", str(date))
    
##  Ajouter un identifiant unique
    temp = get_df_net()

    if temp.empty:
        final_df.insert(0, "Pc_id", "Unknown")
    else:
        final_df.insert(0, "Pc_id", temp.iloc[0]['MACAddress'])

        
    return final_df

##Exporter le dataframe sous forrme d'un fichier csv
def get_csv_hardware():
    final_df().to_csv('hardware.csv', index = False )



########################### SOFTWARE ###########################

##Importer les bibliothèques spécifiques à la récupération des infos hardware
import subprocess
import os

from bs4 import BeautifulSoup

##On récupère la liste des logiciels avec BCUnistaller

######### Liste des logiciels #########

##Définir la fonction pour récupérer la liste des logiciels sur le PC
def softwarem2():

##  Naviguer dans le bon dossier
    os.chdir(".\\BCUninstaller_4.16_portable")

##  Lancer le logiciel BCUninstaller pour exporter la liste des logiciels et importer le fichier .xml généré
    subprocess.run([".\BCU-console", "export", "list_soft.xml"], encoding='utf-8')

    with open('list_soft.xml', 'r', encoding='utf-8') as f:
        data = f.read()

##  Création d'un arbre syntaxique avec BeautifulSoup 
    Bs_data = BeautifulSoup(data, "xml")

##  Chercher toutes les applications dans le fichier xml
    aue = Bs_data.find_all('ApplicationUninstallerEntry')

##  Parcourir la liste de toutes les applications pour récupérer les informations qui nous intéressent
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

##      Ajouter à la liste les informations du logiciel
        tmp.append([disp_name, disp_version, disp_date, disp_pub, disp_size])
        
##  Créer un dataframe    
    df_sm2 = pd.DataFrame(data = tmp,
                         columns = ["DisplayName", "DisplayVersion", "InstallDate",
                                    "Publisher", "EstimatedSize"]
                         )

##  Supprimer le fichier .xml et retourner dans le dossier de départ
    os.remove("list_soft.xml")
    os.chdir("..")

    return df_sm2

    
######### FINAL #########

##Créer un dataframe contenant toutes les informations
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



def get_csv_software():
    finaldf().to_csv('software.csv', index = False )



########################### DATABASE ###########################
##Importer les bibliothèques spécifiques à la base de données
import pymysql

from sqlalchemy import create_engine





if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://{user}:{pw}@10.1.15.12:3306/{db}"
                           .format(user="dev", pw="dev",
                                   db="m2db"))

    ####### GET DFs #######
    get_csv_hardware()
    get_csv_software()

    df_hard = pd.read_csv("hardware.csv")
    df_soft = pd.read_csv("software.csv")

    os.remove("hardware.csv")
    os.remove("software.csv")


    ####### EXPORT HARDWARE #######

    df_hard.to_sql('hardwarem2', con = engine, if_exists = 'append', chunksize = 1000, index=False)

    ####### EXPORT SOFTWARE #######

    df_soft.to_sql('softwarem2', con = engine, if_exists = 'append', chunksize = 1000, index=False)

