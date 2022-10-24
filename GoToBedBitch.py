import ctypes
import schedule
import time
import os


def warning():
	ctypes.windll.user32.MessageBoxW(0, "Go to bed", "do it bitch", 1)

def punish():
	os.system("shutdown /s/t 1")

schedule.every().day.at("22:30:00").do(warning)
schedule.every().day.at("23:00:00").do(punish)

while True:
	schedule.run_pending()
	time.sleep(60)