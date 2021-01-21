from aip import AipOcr
""" 你的APPID AK SK """

APP_ID = '17335153'
API_KEY = 'HgPGsrU6P9XZqCej1ZiWWPiT'
SECRET_KEY = 'TEkeVW1zCT57amXVEixmg4wHxBgSHoUK'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# image = get_file_content('1122.png')
image = get_file_content('home.jpg')

#这里使用url网页图片，也可以使用本地图片，方法可以查看文档接口说明
options = {}

options["probability"] = "true"

# Result=client.basicGeneralUrl(url,options)
# Result=client.basicGeneral(image)
# Result=client.basicAccurate(image)
Result=client.general(image)

# print(Result["words_result_num"])
show=Result['words_result']
for i in show:
    # print(i['words'])

    if i['words'] == '帮派主管':
        print("到了帮派主管")
        weizhi = i['location']
        x  = weizhi['top']
        y = weizhi['left']
        x = x +40
        y = y + 142
        x = x/2400
        y = y/1080
        print(i['location'])
        print(type(Result))
        print(type(show))