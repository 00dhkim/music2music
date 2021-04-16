import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

drive = webdriver.Chrome("chromedriver.exe")

f = open("musicList.txt", "r", encoding="utf-8")
musicList = f.readlines()

drive.get("https://vibe.naver.com/search?query=화분")
print("press X button by your mouse and log-in")
input()

errorList = []

for music in musicList:
    song, artist = music[:-1].split('|')

    print(song, artist, "start")

    try:
        drive.get("https://vibe.naver.com/search?query=" + song + ' ' + artist)
        time.sleep(1)
        a = drive.find_elements_by_xpath("//div[@class=\"content is_searching\"]/div")[1]
        b = a.find_elements_by_xpath("./div/div")[0]
        # 메뉴버튼 점세개짜리
        c = b.find_element_by_xpath("./div[@class=\"option\"]")

        islove = c.find_element_by_xpath("./div/div/a")
        if islove.get_attribute("class") == "btn_option on":
            print("already loved")
            continue

        c.click()
        d = c.find_elements_by_xpath("./div/div/div[@role=\"menu\"]/a")[0]
        d.click()

        print("end\n")
        time.sleep(1)

    except:
        print("error", song, artist)
        errorList.append((song, artist))

# drive.get("")

f.close()