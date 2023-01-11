import configparser
import os, shutil


class DashboardSettings:
    def __init__(self):
        # Path to this file
        SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

        CONFIG_PATH = os.path.join(SCRIPT_PATH, '..', 'config.ini')
        DEFAULT_CONFIG_PATH = os.path.join(SCRIPT_PATH, '..' , 'config.ini.default')

        # Check if the config file exists and copy the default one if not
        if not os.path.isfile(CONFIG_PATH):
            shutil.copyfile(DEFAULT_CONFIG_PATH, CONFIG_PATH)

        # Read it if exists
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_PATH)

