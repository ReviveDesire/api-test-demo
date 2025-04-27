from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# 创建Chrome配置选项对象
options = Options()

# 添加用户数据目录路径
options.add_argument(r'--user-data-dir=C:\Users\ReviveDesire\AppData\Local\Google\Chrome\User Data')

# 添加指定用户配置文件目录
options.add_argument('--profile-directory=Profile 8')

# 初始化Chrome浏览器驱动
driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com")  # 替换为实际URL

try:
    # 等待元素可点击
    chip = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "chip-container"))
    )
    # 点击元素
    chip.click()
    print("元素点击成功")
    
except Exception as e:
    print(f"点击元素时出错: {e}")
    
finally:
    # 等待3秒以便观察结果
    input("按回车键退出...")
    driver.quit()