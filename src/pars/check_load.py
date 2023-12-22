# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def check_load(driver, xpath):
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except:
        return False
