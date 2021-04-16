from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome("chromedriver.exe")


class MelonCrawler:
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.crawl_data = []

    def crawl(self):
        # melon은 로그인 안해도 좋아요 리스트 뜸
        self.driver.get("https://www.melon.com/mymusic/like/mymusiclikesong_list.htm?memberKey=51230892")
        while True:
            try:
                input()
                print("crawling")
                self.pageCrawl()
                print("end")
            except:
                break

        with open("melon_crawl_data.txt", "w", encoding="utf-8") as f:
            f.write(self.crawl_data.__str__())

        return self.crawl_data

    # 한 페이지만 크롤링함
    def pageCrawl(self):
        trlist = self.driver.find_elements_by_xpath("//table[@border=\"1\"]/tbody/tr")
        for tr in trlist:
            try:
                song, artist = tr.find_elements_by_xpath("./td[@class=\"t_left\"]")[0:2]
                song = song.find_element_by_xpath("./div/div/button[@class=\"btn_icon play\"]")
                title = song.get_attribute('title')

                artist = artist.find_element_by_xpath("./div/div/a")
                artistName = artist.text

                music = {'song': song, 'artist': artistName}
                self.crawl_data.append(music)
                print(f'crawling...')
                # f.write(title.split(" 재생 - 새창")[0] + "|" + artistName + '\n')
                # print(title.split(" 재생 - 새창")[0]+"|"+artistName)
            except:
                print("error")


if __name__ == '__main__':
    melon_crawler = MelonCrawler()
    melon_crawler.crawl()

'''
drive.get("http://lms.knu.ac.kr/ilos/main/member/login_form.acl")
drive.find_element_by_id("usr_id").send_keys(lms_id)
drive.find_element_by_id("usr_pwd").send_keys(lms_pw)
drive.find_element_by_id("login_btn").click()
drive.implicitly_wait(10)
drive.find_element_by_id("menu_attend").click()
'''
