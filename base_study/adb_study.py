# Time: 2021/1/12 15:39
# Author: jiangzhw
# FileName: adb_study.py
"""
import subprocess

devices = subprocess.Popen(
    'adb devices'.split(),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
).communicate()[0]
print(devices)
serial_nos = []
for item in devices.split():
    filters = ['list', 'of', 'device', 'devices', 'attached']
    if item.lower() not in filters:
        serial_nos.append(item)
print(serial_nos)
reboot_cmds = []
for serial_no in serial_nos:
    reboot_cmds.append('adb -s %s reboot' % serial_no)
for reboot_cmd in reboot_cmds:
    subprocess.Popen(
        reboot_cmd.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()[0]
"""

import os
import subprocess


def reboot():  # 封装
    print(os.popen('adb devices'))
    os.popen('adb wait-for-device')
    os.popen('adb reboot')
    print("adb reboot success!")


# os.system('cd D://PythonPro//Hogwars01//base_study')
# os.mkdir('aaa.txt')
# reboot()

"""
deviceId = os.popen('adb devices').read()
print(deviceId)
deviceName = os.popen('adb shell getprop ro.product.model').read()
print(deviceName)
platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
print(platformVersion)
device = os.popen('adb shell getprop ro.product.name ').read()
print(device)
"""
cmd1 = "adb shell pm list packages"
# print(subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8"))
print(os.popen(cmd1).read())
