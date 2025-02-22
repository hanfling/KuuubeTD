from pywinusb import hid
from internal_constants import *
import tablet_monitor_mapping

report = [0x00]*65

def find_device():
    all_devices = hid.HidDeviceFilter(vendor_id = VMULTI_DEVICE_VENDOR_ID, product_id = VMULTI_DEVICE_PRODUCT_ID,).get_devices()

    if len(all_devices) > 0:
        virtual_device = all_devices[-1]
        return virtual_device

    else:
        raise Exception("Virtual Multitouch Device driver not loaded.")

def send_report_wacom_v_2_0(vmulti_device_report, proximity, pointer, button_flag, pos_x, pos_y, buttons, pressure, tilt_x, tilt_y):    
    report[0] = VMULTI_ID
    report[1] = USAGE_PAGE_DIGITIZER
    report[2] = OUTPUT_MODE

    flags = 0
    if (button_flag):
        if (pointer):
            if (bool((buttons & 0x01))): # pen tip
                flags = flags | int(0x01) # pen tip

            if (bool((buttons & 0x02))): # bottom pen button
                flags = flags | int(0x02) # barrel button

            #if (bool((buttons & 0x04))): # top pen button
            #    flags = flags | int(0x02) # barrel button

            if (bool((buttons & 0x04))): # eraser
                flags = flags | int(0x08) # invert
        else:
            # tablet and mouse buttons are not implemented
            pass
    
    if (proximity):
        flags = flags | int(0x10)

    report[3] = flags

    scaled_pos_x = tablet_monitor_mapping.map_x(pos_x)
    report[4] = scaled_pos_x & 0x00FF
    report[5] = (scaled_pos_x & 0xFF00) >> 8

    scaled_pos_y = tablet_monitor_mapping.map_y(pos_y)
    report[6] = scaled_pos_y & 0x00FF
    report[7] = (scaled_pos_y & 0xFF00) >> 8

    scaled_pressure = int(pressure * VMULTI_PRESSURE_SCALING_WACOM_IVE_1_4)
    report[8] = scaled_pressure & 0x00FF
    report[9] = (scaled_pressure & 0xFF00) >> 8

    report[10] = int(tilt_x * VMULTI_TILT_SCALING_WACOM_IVE_1_4)
    report[11] = int(tilt_y * VMULTI_TILT_SCALING_WACOM_IVE_1_4)

    vmulti_device_report.set_raw_data(report)
    vmulti_device_report.send()

def send_report_wacom_ive_1_4(vmulti_device_report, proximity, pointer, button_flag, pos_x, pos_y, buttons, pressure, tilt_x, tilt_y):    
    report[0] = VMULTI_ID
    report[1] = USAGE_PAGE_DIGITIZER
    report[2] = OUTPUT_MODE

    flags = 0
    if (button_flag):
        if (pointer):
            if (bool((buttons & 0x01))): # pen tip
                flags = flags | int(0x01) # pen tip

            if (bool((buttons & 0x02))): # bottom pen button
                flags = flags | int(0x02) # barrel button

            #if (bool((buttons & 0x04))): # top pen button
            #    flags = flags | int(0x02) # barrel button

            if (bool((buttons & 0x04))): # eraser
                flags = flags | int(0x08) # invert
        else:
            # tablet and mouse buttons are not implemented
            pass
    
    if (proximity):
        flags = flags | int(0x10)

    report[3] = flags

    scaled_pos_x = tablet_monitor_mapping.map_x(pos_x)
    report[4] = scaled_pos_x & 0x00FF
    report[5] = (scaled_pos_x & 0xFF00) >> 8

    scaled_pos_y = tablet_monitor_mapping.map_y(pos_y)
    report[6] = scaled_pos_y & 0x00FF
    report[7] = (scaled_pos_y & 0xFF00) >> 8

    scaled_pressure = int(pressure * VMULTI_PRESSURE_SCALING_WACOM_IVE_1_4)
    report[8] = scaled_pressure & 0x00FF
    report[9] = (scaled_pressure & 0xFF00) >> 8

    report[10] = int(tilt_x * VMULTI_TILT_SCALING_WACOM_IVE_1_4)
    report[11] = int(tilt_y * VMULTI_TILT_SCALING_WACOM_IVE_1_4)

    vmulti_device_report.set_raw_data(report)
    vmulti_device_report.send()

def send_report_wacom_iv_1_2_to_1_4(vmulti_device_report, proximity, pointer, button_flag, pos_x, pos_y, buttons, pressure):    
    report[0] = VMULTI_ID
    report[1] = USAGE_PAGE_DIGITIZER
    report[2] = OUTPUT_MODE

    flags = 0
    if (button_flag):
        if (pointer):
            if (bool((buttons & 0x01))): # pen tip
                flags = flags | int(0x01) # pen tip

            if (bool((buttons & 0x02))): # bottom pen button
                flags = flags | int(0x02) # barrel button

            #if (bool((buttons & 0x04))): # top pen button
            #    flags = flags | int(0x02) # barrel button

            if (bool((buttons & 0x04))): # eraser
                flags = flags | int(0x08) # invert
        else:
            # tablet and mouse buttons are not implemented
            pass
    
    if (proximity):
        flags = flags | int(0x10)

    report[3] = flags

    scaled_pos_x = tablet_monitor_mapping.map_x(pos_x)
    report[4] = scaled_pos_x & 0x00FF
    report[5] = (scaled_pos_x & 0xFF00) >> 8

    scaled_pos_y = tablet_monitor_mapping.map_y(pos_y)
    report[6] = scaled_pos_y & 0x00FF
    report[7] = (scaled_pos_y & 0xFF00) >> 8

    scaled_pressure = int(pressure * VMULTI_PRESSURE_SCALING_WACOM_IV_1_2_TO_1_4)
    report[8] = scaled_pressure & 0x00FF
    report[9] = (scaled_pressure & 0xFF00) >> 8

    vmulti_device_report.set_raw_data(report)
    vmulti_device_report.send()

def send_report_wacom_iv_1_0_to_1_1(vmulti_device_report, proximity, pointer, button_flag, pos_x, pos_y, buttons, pressure):    
    report[0] = VMULTI_ID
    report[1] = USAGE_PAGE_DIGITIZER
    report[2] = OUTPUT_MODE

    flags = 0
    if (button_flag):
        if (pointer):
            if (bool((buttons & 0x01))): # pen tip
                flags = flags | int(0x01) # pen tip

            if (bool((buttons & 0x02))): # bottom pen button
                flags = flags | int(0x02) # barrel button

            #if (bool((buttons & 0x04))): # top pen button
            #    flags = flags | int(0x02) # barrel button

            if (bool((buttons & 0x04))): # eraser
                flags = flags | int(0x08) # invert
        else:
            # tablet and mouse buttons are not implemented
            pass
    
    if (proximity):
        flags = flags | int(0x10)

    report[3] = flags

    scaled_pos_x = tablet_monitor_mapping.map_x(pos_x)
    report[4] = scaled_pos_x & 0x00FF
    report[5] = (scaled_pos_x & 0xFF00) >> 8

    scaled_pos_y = tablet_monitor_mapping.map_y(pos_y)
    report[6] = scaled_pos_y & 0x00FF
    report[7] = (scaled_pos_y & 0xFF00) >> 8

    scaled_pressure = int(pressure * VMULTI_PRESSURE_SCALING_WACOM_IV_1_0_TO_1_1)
    report[8] = scaled_pressure & 0x00FF
    report[9] = (scaled_pressure & 0xFF00) >> 8

    vmulti_device_report.set_raw_data(report)
    vmulti_device_report.send()

def send_report_wacom_ii_s(vmulti_device_report, proximity, pointer, pos_x, pos_y, buttons, button_flag, pressure):
    report[0] = VMULTI_ID
    report[1] = USAGE_PAGE_DIGITIZER
    report[2] = OUTPUT_MODE

    flags = 0
    if (pointer or button_flag):
        if (bool((buttons & 0x01))): # pen tip
            flags = flags | int(0x01) # pen tip

        if (pressure > 1): # pen tip
            flags = flags | int(0x01) # pen tip
    else:
        # mouse buttons are not implemented
        pass
    
    if (proximity):
        flags = flags | int(0x10)

    report[3] = flags

    scaled_pos_x = tablet_monitor_mapping.map_x(pos_x)
    report[4] = scaled_pos_x & 0x00FF
    report[5] = (scaled_pos_x & 0xFF00) >> 8

    scaled_pos_y = tablet_monitor_mapping.map_y(pos_y)
    report[6] = scaled_pos_y & 0x00FF
    report[7] = (scaled_pos_y & 0xFF00) >> 8

    scaled_pressure = int(pressure * VMULTI_PRESSURE_SCALING_WACOM_II_S)
    report[8] = scaled_pressure & 0x00FF
    report[9] = (scaled_pressure & 0xFF00) >> 8

    vmulti_device_report.set_raw_data(report)
    vmulti_device_report.send()
