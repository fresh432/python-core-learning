import requests
from lxml import html
import csv
import random
import time
import re

# 常量
MOVIE_LIST_FILE = "data/movie_list.csv"
DB_BASE_URL = "https://www.maoyan.com"
DB_TOP_URL1 = "https://movie.douban.com/top250"
DB_TOP_URL2 = "https://movie.douban.com/top250?start=%d&filter="
HEADERS = {
    # 1. User-Agent：模拟浏览器身份（保持默认即可，或者换成你浏览器的版本）
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',

    # 2. Referer：告诉服务器你是从哪个页面跳转过来的（非常重要！）
    # 这里必须填写电影列表页的地址，而不是详情页地址
    'Referer': 'https://movie.douban.com/top250',

    # 3. Cookie：这是你的“通行证”，用来证明你是已登录的真实用户
    # 请复制你浏览器 F12 -> Network -> 请求头里的完整 Cookie 字符串粘贴在这里
    'Cookie': '运行时请自行配置',
    # 4. Host：指定目标主机（可选，但加上更稳妥）
    'Host': 'movie.douban.com'
}

# 保存电影数据, 保存为 csv 文件
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE, "w", encoding= "utf-8", newline= "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "导演", "简介"])
        writer.writeheader() # 写入表头
        writer.writerows(all_movies) # 写入数据

# 获取电影年份
def get_movie_year(movie_years):
    movie_year = movie_years[0].strip() if movie_years else ''
    return movie_year.replace("(", "").replace(")", "")

# 获取电影上映时间
def get_movie_publish_date(movie_dates):
    movie_date = movie_dates[0].strip() if movie_dates else ''
    date = re.search(r"\d{4}-\d{2}-\d{2}", movie_date)
    return date.group() if date else None

# 获取电影时长
def get_movie_cost_time(movie_cost_times):
    cost_time = movie_cost_times[0].strip() if movie_cost_times else ''
    cs_time = re.search("\d+", cost_time)
    return cs_time.group() if cs_time else None

# 获取电影详情
def get_movie_info(movie_info_url):
    # 1. 发送请求, 获取电影详情数据
    movie_response = requests.get(movie_info_url, headers= HEADERS, timeout = 60)
    print(f"发送请求{movie_info_url}, 获取电影详情数据 ...")

    # 调试信息
    # print(f"状态码: {movie_response.status_code}")
    # print(f"响应长度: {len(movie_response.text)}")
    # print(f"最终URL: {movie_response.url}")
    # print(f"movie_response.text内容: {movie_response.text}")

    # 每次请求后随机等待 1 到 3 秒
    delay_time = random.uniform(1,4)
    time.sleep(delay_time)

    # 2. 解析数据, 获取电影详情
    movie_doc = html.fromstring(movie_response.text)
    # 电影名称
    movie_names = movie_doc.xpath("//*[@id='content']/h1/span[@property='v:itemreviewed']/text()") # 电影名称
    movie_years = movie_doc.xpath("//*[@id='content']/h1/span[2]/text()") # 上映年限
    movie_dates = movie_doc.xpath("//span[@class='pl'][contains(text(), '上映日期')]/following-sibling::span[@property='v:initialReleaseDate']/text()") # 上映时间
    movie_tags = movie_doc.xpath("//*[@id='info']/span[@property='v:genre']/text()") # 类型
    movie_cost_times = movie_doc.xpath("//*[@id='info']/span[@property='v:runtime']/text()") # 时长
    movie_scores = movie_doc.xpath("//*[@id='interest_sectl']/div[1]/div[2]/strong/text()") # 评分
    movie_languages = movie_doc.xpath("//span[@class='pl'][contains(text(), '语言:')]/following-sibling::text()[1]") # 语言
    movie_directors = movie_doc.xpath("//*[@id='info']/span[1]/span[2]/a/text()") # 导演
    movie_descriptions = movie_doc.xpath("//span[@property='v:summary']/text()") # 简介
    movie_summary = "".join(movie_descriptions)

    # 3. 返回电影详情 - 字典
    movie_info = {
        "电影名": movie_names[0].strip() if movie_names else '',
        "年份": get_movie_year(movie_years),
        "上映时间": get_movie_publish_date(movie_dates),
        "类型": ",".join(movie_tags) if movie_tags else '',
        "时长": get_movie_cost_time(movie_cost_times),
        "评分": movie_scores[0].strip() if movie_scores else '',
        "语言": ",".join(movie_languages) if movie_languages else '',
        "导演": ",".join(movie_directors) if movie_directors else '',
        "简介": re.sub(r'\s+', '', movie_summary) if movie_summary else ''
    }
    # print(movie_info)
    return movie_info


# 主函数: 定义核心逻辑
def main():
    all_movies = [] # 保存所有电影的数据

    for i in range(0, 8):
        page_num = i *25
        # 1.发送请求, 获取高分电影榜单数据
        if page_num == 0:
            response = requests.get(DB_TOP_URL1, headers=HEADERS, timeout=60)
        else:
            response = requests.get(DB_TOP_URL2 % page_num, headers=HEADERS, timeout=60)
        print(f"发送请求, 访问第{i + 1}页的数据, 获取豆瓣电影榜单数据 ...")

        # 调试信息
        # print(f"状态码: {response.status_code}")
        # print(f"响应长度: {len(response.text)}")
        # print(f"最终URL: {response.url}")

        # 2.解析数据, 获取电影列表
        document = html.fromstring(response.text)
        movie_list = document.xpath("//*[@id='content']/div/div[1]/ol/li")

        # 3.遍历电影列表, 获取电影详情
        for movie in movie_list:
            movie_urls = movie.xpath("./div/div[1]/a/@href")
            if movie_urls:
                # 电影详情的url
                movie_info_url = movie_urls[0]
                # print(movie_info_url)
                # 发送请求, 获取电影详情数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)

    # 4.保存数据, 保存为 csv 文件
    print("获取到所有的电影详情, 保存电影数据到csv文件 ...")
    save_all_movies(all_movies)

if __name__ == "__main__":
    main()
