# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from src.pars._click_sing_in import ClickSingIn
from src.pars._go_category import GoCategory
from src.pars._load_category import LoadCategory
from src.pars._load_master import LoadMaster
from src.pars._start_site import StartSite


class StartPars:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def start_pars(self):
        res_open = StartSite(self.settings).load_site()

        if not res_open:
            return False

        click_sing_in = ClickSingIn(self.settings).click_sing_in()

        if not click_sing_in:
            return False

        load_master = LoadMaster(self.settings).load_master()

        if not load_master:
            return False

        main_category_list = LoadCategory(self.settings).load_category()

        if not main_category_list:
            return False

        self.settings['main_category_list'] = main_category_list

        res_go_category = GoCategory(self.settings).go_category()

        print()
