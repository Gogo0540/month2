import os
import tcolors
import colorama
import envparse

colorama.init()
envparse.env.read_envfile('options.env')
user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
tcolors.cprint(tcolors.Color.BLUE + colorama.Back.BLACK + user_name + ' ' + password)