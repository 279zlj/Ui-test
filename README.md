# Ui-test
selenium-uinttest

如果你的系统是linux，而且为无GUI，必须加上

from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
options=Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')                       //不用沙盒
display = Display(visible=0, size=(800,600))
display.start()
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)
display.close()

