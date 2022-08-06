from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # To use ENTER
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait   # Loading Wait
from selenium.webdriver.support import expected_conditions as EC    #Loading Wait


# Set information you need !!
srt_id = "01022702604"  # input your phone number
srt_pw = "tlfb490418!"
srt_departure = "동탄"    # () 내에 있는 글자까지 기입
srt_destination = "부산"
srt_date = "08/12(금)"    # 00/00(요일) 반드시 해당 양식으로 기입
srt_adult = "1"   # 어른 승객 명 수
srt_train_no = "311"  # 열차시간 확인 후 해당 열차 번호 기입




# 1. Move to SRT login page
browser = webdriver.Chrome("/Users/silnun/Downloads/chromedriver")
browser.get("https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000")

# 2. Input ID, PW
browser.find_element(By.XPATH, "//*[@id='srchDvCd3']").click()
input_js = ' \
        document.getElementById("srchDvNm03").value = "{id}"; \
        document.getElementById("hmpgPwdCphd03").value = "{pw}"; \
    '.format(id=srt_id, pw=srt_pw)
browser.execute_script(input_js)
browser.find_element(By.XPATH, "//*[@id='login-form']/fieldset/div[1]/div[1]/div[4]/div/div[2]/input").click()

# 3. Set condition
browser.get("https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000")
  # 3.1 Set Path
start = browser.find_element(By.ID, "dptRsStnCdNm")
start.clear()
start.send_keys(srt_departure)
end = browser.find_element(By.ID, "arvRsStnCdNm")
end.clear()
end.send_keys(srt_destination)
  # 3.2 Set Date
date = Select(browser.find_element(By.ID, "dptDt"))
date.select_by_visible_text("2022/" + srt_date)
  # 3.3 Set Adult
adult = Select(browser.find_element(By.NAME, "psgInfoPerPrnb1"))
adult.select_by_visible_text("어른(만 13세 이상) " + srt_adult + "명")
  # 3.3 Set SRT
browser.find_element(By.ID, "trnGpCd300").click()

# 4. Find Train you need
  # 4.1 Mobe to Reservation Page
browser.find_element(By.XPATH, "//*[@id='search_top_tag']/input").click()
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='result-form']/fieldset/div[6]/table/tbody/tr[1]/td[3]")))  # Loading wait
  # 4.2 Maching Reservation Button using srt_train_no
for i in range(1,11) :
  train_path_no = "//*[@id='result-form']/fieldset/div[6]/table/tbody/tr[" + str(i) + "]/td[3]"
  trainNo = browser.find_element(By.XPATH, train_path_no).text
  if (trainNo == srt_train_no) :
    train_path_reserve = "//*[@id='result-form']/fieldset/div[6]/table/tbody/tr[" + str(i) + "]/td[7]/a"
    break

# 5. Macro
while(True):
  reserveTrain = browser.find_element(By.XPATH, train_path_reserve)
  setMacroCondition = reserveTrain.text
  if (setMacroCondition == "예약하기"):
    reserveTrain.click()
    break
  elif (setMacroCondition == "매진"):
    browser.implicitly_wait(3)    # 너무 짧게 하면 ip 벤 당함
    browser.refresh()
    

    



