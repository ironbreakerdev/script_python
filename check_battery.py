import subprocess,time

battery = subprocess.check_output("acpi -b | awk '{print $4}' | sed 's/%,//g' ",shell=True)

value_battery = battery.decode('utf-8').strip()
if int(value_battery) == 50:
    subprocess.run(["/usr/bin/zenity", "--warning", "--text", "Attenzione, la batteria è al "+value_battery+"%"])
elif int(value_battery) < 50:
    subprocess.run(["/usr/bin/zenity", "--error", "--text", "Attenzione, la batteria è al "+value_battery+"%"+" si consiglia di inserire la batteria in corrente"])
