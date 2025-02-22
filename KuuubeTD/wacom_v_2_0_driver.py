import vmulti_handler
import sys
import serial_port_handler

vmulti_device = None
try:
    vmulti_device = vmulti_handler.find_device()
except Exception as e:
    print(e)
    sys.exit()
vmulti_device.open()

vmulti_device_report = vmulti_device.find_output_reports()[-1]

try:
    serial_port = serial_port_handler.setup_wacom_v_2_0()
except Exception as e:
    print("Serial device setup failed.")
    print(e)
    sys.exit()

while(True):
    report_parsed = serial_port_handler.read_data_wacom_v_2_0(serial_port)
    vmulti_handler.send_report_wacom_v_2_0(vmulti_device_report, report_parsed[0], report_parsed[1], report_parsed[2], report_parsed[3], report_parsed[4], report_parsed[5], report_parsed[6], report_parsed[7], report_parsed[8])
