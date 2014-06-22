# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2013 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

""" Custom OTA commands for d2 devices """

def FullOTA_InstallEnd(info):

  # /system/lib/hw

  info.script.AppendExtra('ifelse(is_substring("T32", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/lib/hw/mondrian/* /system/lib/hw"));')
  info.script.AppendExtra('ifelse(is_substring("T525", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/lib/hw/picassolte/* /system/lib/hw"));')

  # /system/lib/

  info.script.AppendExtra('ifelse(is_substring("T32", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/lib/mondrian/* /system/lib/"));')
  info.script.AppendExtra('ifelse(is_substring("T525", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/lib/picassolte/* /system/lib/"));')

  # /system/vendor/lib/

  info.script.AppendExtra('ifelse(is_substring("T32", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/vendor/lib/mondrian/* /system/vendor/lib/"));')
  info.script.AppendExtra('ifelse(is_substring("T525", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp -R /system/vendor/lib/picassolte/* /system/vendor/lib/"));')
