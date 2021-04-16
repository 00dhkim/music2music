from selenium import webdriver
from selenium.webdriver.common.alert import Alert

drive = webdriver.Chrome("chromedriver.exe")


def pageCrawl():
    trlist = drive.find_elements_by_xpath("//table[@border=\"1\"]/tbody/tr")
    for tr in trlist:
        try:
            song, artist = tr.find_elements_by_xpath("./td[@class=\"t_left\"]")[0:2]
            song = song.find_element_by_xpath("./div/div/button[@class=\"btn_icon play\"]")
            title = song.get_attribute('title')

            artist = artist.find_element_by_xpath("./div/div/a")
            artistName = artist.text

            f.write(title.split(" 재생 - 새창")[0] + "|" + artistName + '\n')
            # print(title.split(" 재생 - 새창")[0]+"|"+artistName)
        except:
            print("error")


# melon은 로그인 안해도 좋아요 리스트 뜸
drive.get("https://www.melon.com/mymusic/like/mymusiclikesong_list.htm?memberKey=51230892")
p = pageCrawl

f = open("musicList.txt", "a", encoding="utf-8")

print("init setting end")

while (1):
    input()
    print("crawling")
    p();
    print("end")

f.close()

'''
drive.get("http://lms.knu.ac.kr/ilos/main/member/login_form.acl")
drive.find_element_by_id("usr_id").send_keys(lms_id)
drive.find_element_by_id("usr_pwd").send_keys(lms_pw)
drive.find_element_by_id("login_btn").click()
drive.implicitly_wait(10)
drive.find_element_by_id("menu_attend").click()
'''