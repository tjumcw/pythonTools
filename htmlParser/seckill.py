import datetime
import re
from bs4 import BeautifulSoup
from utils.selenium_utils import get_driver, scroll_to_bottom
import pandas as pd


def getSeckillInfo():
    driver = get_driver()
    today = datetime.datetime.now()
    start_time = (today + datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
    end_time = (today + datetime.timedelta(days=3, hours=2)).strftime("%Y-%m-%d %H:%M:%S")
    url = "https://miaosha.jd.com/"
    driver.get(url)
    scroll_to_bottom(driver, "service-2017")
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    hrefs = []
    names = []
    prices = []
    skus = []
    imgs = []
    start_times = []
    end_times = []
    stocks = []
    items = soup.find_all("li", class_="seckill_mod_goods")
    for item in items:
        # 获取href
        href = item.find("a", class_="seckill_mod_goods_link")['href']
        hrefs.append(href)
        # 获取名称
        names.append(item.find("h4", class_="seckill_mod_goods_title").text)
        # 获取sku
        pattern = r"/(\d+).html"
        result = re.search(pattern, href)
        sku = result.group(1)
        skus.append(sku)
        # 获取图片和库存
        imgs.append(item.find("img", class_="seckill_mod_goods_link_img")['src'])
        stocks.append(200)
        # 获取价格
        ele = item.find("i", class_="seckill_mod_goods_price_now")
        price = "{:.2f}".format(float(ele.text.replace("¥", "")))
        prices.append(price)
        # 获取起始时间和结束时间
        start_times.append(start_time)
        end_times.append(end_time)
    data = {"name": names, "href": hrefs, "sku": skus, "img":  imgs, "stock": stocks,
            "price": prices, "start_time": start_times, "end_time": end_times}
    frame = pd.DataFrame(data)
    frame.to_excel("jd_seckill.xlsx", index=False)


if __name__ == "__main__":
    getSeckillInfo()