# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.browser.createbrowser_uc import CreatBrowser
from src.pars.start_pars import StartPars


def main():
    browser = CreatBrowser()

    settings = {
        'driver': browser.driver
    }

    res_job = StartPars(settings).start_pars()

    print()


if __name__ == '__main__':
    main()
