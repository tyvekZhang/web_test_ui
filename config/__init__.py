# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# linux驱动路径
LUINX_CHROMEDRIVER = os.path.join(BASE_DIR, 'driver', 'linux', 'chromedriver')
LUINX_FIREFOXDRIVER = os.path.join(BASE_DIR, "driver", "linux", "geckodriver")  # 火狐浏览器

# windos 系统浏览器驱动路劲
IE_PATH = os.path.join(BASE_DIR, "driver", "windos", "IEDriverServer.exe")  # ie浏览器
WIN_CHROMEDRIVER = os.path.join(BASE_DIR, "driver", "windos", "chromedriver.exe")  # 谷歌浏览器
WIN_FIREFOXDRIVER = os.path.join(BASE_DIR, "driver", "windos", "geckodriver.exe")  # 火狐浏览器

# mac 系统浏览器驱动路劲
MAC_CHROMEDRIVER = os.path.join(BASE_DIR, "driver", "mac", "chromedriver")  # 谷歌浏览器
MAC_FIREFOXDRIVER = os.path.join(BASE_DIR, "driver", "mac", "geckodriver")  # 火狐浏览器

# 日志路径
LOG_DIR = os.path.join(BASE_DIR, 'log')

# 测试用例集路径
CASE_DIR = os.path.join(BASE_DIR, 'test_case')

# yaml测试用例数据路径
CASEYMAL_DIR = os.path.join(BASE_DIR, "dataset", "caseYAML", )  # 测试数据
LOCATORYMAL_DIR = os.path.join(BASE_DIR, "dataset", "locatorYAML", )  # 定位数据

### 测试文件路径
DATA_FILE = os.path.join(BASE_DIR, "dataset", "file")

# 测试图片断言路径
DIFF_IMGPATH = os.path.join(BASE_DIR, "dataset", "file", "img")

# 测试用例结果目录
PRPORE_JSON_DIR = os.path.join(BASE_DIR, "output", "report_json")

# 测试结果报告目录
PRPORE_ALLURE_DIR = os.path.join(BASE_DIR, "output", "report_allure")

# 测试截图目录
PRPORE_SCREEN_DIR = os.path.join(BASE_DIR, "output", "report_screen")

# 测试配置目录
STETING_YAML_DIR = os.path.join(BASE_DIR, "config", "setting.yaml")

# 测试临时目录
PRPORE_TMP = os.path.join(BASE_DIR, "output", "report_tmp")