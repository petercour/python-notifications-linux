#!/usr/bin/python3
from message import sendmessage, sendmessageicon, sendmessagetitle, msg
import time

sendmessage("hello you")

icons = ['face-angel','face-sad','stock_smiley-13','face-angry','face-sick','stock_smiley-15','face-cool','face-smile-big','stock_smiley-18','face-crying','face-smile','stock_smiley-1','face-devilish','face-smirk','stock_smiley-22','face-embarrassed','face-surprise','stock_smiley-2','face-glasses','face-tired','stock_smiley-3','face-kiss','face-uncertain','stock_smiley-4','face-laugh','face-wink','stock_smiley-5','face-monkey','face-worried','stock_smiley-6','face-plain','stock_smiley-10','stock_smiley-7','face-raspberry','stock_smiley-11','stock_smiley-8']

for icon in icons:
    sendmessageicon("Important: yada yada yada yada yada yada",icon)
    time.sleep(0.5)
