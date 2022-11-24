import wmi
import pandas as pd
from tabulate import tabulate

from datetime import datetime

c = wmi.WMI()


########################### OS ###########################


def get_df_os():
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


    labels_os = ["BootDevice", "Caption", "InstallDate", "NumberOfUsers",
                 "Organization", "OSArchitecture", "SystemDrive", "Version"
                 ]

    df_os = pd.DataFrame(data = [os_infos],
                         columns = labels_os
                         )

    return df_os


########################### DRIVERS ###########################


def get_df_dri():
    temp_c, temp_l, temp_pn, temp_st = ([],[],[],[])

    for temp in c.Win32_SystemDriver():
            temp_c.append(temp.Caption)
            temp_l.append(temp.Name)
            temp_pn.append(temp.PathName)
            temp_st.append(temp.ServiceType)

    dri_infos = list(zip(temp_c, temp_l, temp_pn, temp_st))
            

    labels_dri = ["Caption", "Name",
                  "PathName", "ServiceType"
                   ]

    df_dri = pd.DataFrame(data = dri_infos,
                          columns = labels_dri
                          )

    df_dri = df_dri.sort_values("Name")

    return df_dri


########################### MOTHERBOARD ###########################


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


########################### BIOS ###########################


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

    return df_bi

########################### CPU ###########################


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


########################### GPU ###########################


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
    
    return df_gpu


########################### RAM ###########################


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


########################### PHYSICAL DD ###########################


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


########################### LOGICAL DD ###########################


def get_df_ldd():
    temp_c, temp_dt, temp_fs, temp_frs, temp_mt, temp_s, temp_vn = ([],[],[],[],[],[],[])

    for temp in c.Win32_LogicalDisk():
            temp_c.append(temp.Caption)
            temp_dt.append(temp.DriveType)
            temp_fs.append(temp.FileSystem)
            temp_frs.append(int(temp.FreeSpace))
            temp_mt.append(temp.MediaType)
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


########################### NETWORK ###########################


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
    
    return df_net


########################### BATTERY ###########################


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
            print("Please check")

    df_ba = pd.DataFrame(data = [ba_infos],
                         columns = labels_ba
                         )
    return df_ba


########################### SCREEN ###########################


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


########################### PORTS ###########################


def get_df_port():
    temp_ct, temp_d, temp_erd, temp_ird, temp_pt, temp_t = ([],[],[],[],[],[])

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


########################### FINAL ###########################


def final_df():
    date = datetime.now()
    format = "%Y%m%d%H%M%S"
    date = date.strftime(format)


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

    final_df.insert(0, "Pc_id", get_df_net().iloc[1]['MACAddress'])
    final_df.insert(0, "Date", str(date))

    return final_df



if __name__ == '__main__':
    temp = final_df()
    print(temp)
    print(temp.shape)
    temp.to_csv('final_df.csv', index = False )
