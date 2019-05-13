import discord
import openpyxl
import asyncio
import datetime
import json
import time
import urllib
import urllib.request
import os
import bs4
import logging
from discord import Member

client = discord.Client()

now = datetime.datetime.now()

@client.event
async def on_ready():
    print('*Connect Success*')
    print("Client Name= " + "'" + client.user.name + "'")
    print("Client ID= " + "'" + client.user.id + "'")
    print('---LOG---')
    await client.change_presence(game=discord.Game(name='사용법 : /?', type=1))

@client.event
async def on_member_join(member):
    fmt = '{1.name}에 온것을 환영합니다. {0.mention}환자님'
    channel = member.server.get_channel("574856464347430914")
    await client.send_message(channel, fmt.format(member, member.server))
 
@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("453817631603032067")
    fmt = '{0.mention} 님이 정신병동을 퇴원하셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_message(message):
    if message.content.startswith('미치신겁니까'):
        await client.send_file(message.channel, 'Human.jpg')
        
    if message.content.startswith('느껴지십니까') or message.content.startswith('힘의차이가') or message.content.startswith('힘의 차이가'):
        await client.send_file(message.channel, '힘의차이가느껴지십니까.jpg')

    if message.content.startswith('ㄴㅇㄱ') or message.content.startswith('상상도못한정체') or message.content.startswith('상상도 못한 정체'):
        await client.send_file(message.channel, '상상도못한오퍼.jpg')
        
    if message.content.startswith('kia') or message.content.startswith('키아') or message.content.startswith('주모'):
        await client.send_file(message.channel, 'kia.jpg')

    if message.content.startswith('그치만..'):
        await client.send_file(message.channel, '그치만.jpg')

    if message.content.startswith('yee'):
        await client.send_file(message.channel, 'yee.PNG')

    if message.content.startswith('당근빠따죠') or message.content.startswith('당근빳따죠') or message.content.startswith('당빠'):
        await client.send_file(message.channel, '당근빳다죠쉬바.png')
        
    if message.content.startswith('어흑마이깟') or message.content.startswith('어흑 마이깟') or message.content.startswith('어흑 마이 깟'):
        await client.send_file(message.channel, '어흑마이깟.png')
        
    if message.content.startswith('넹기분굿') or message.content.startswith('넹 기분굿') or message.content.startswith('넹 기분 굿'):
        await client.send_file(message.channel, '넹기분굿.jpg')

    if message.content.startswith('핫하받아라')  or message.content.startswith('핫하 받아라'):
        await client.send_file(message.channel, '핫하받아라.gif')

    if message.content.startswith('고오얀놈'):
        await client.send_file(message.channel, '고오얀놈.gif')

    if message.content.startswith('^^7') or message.content.startswith('충성충성'):
        await client.send_file(message.channel, '^^7.gif')

    if message.content.startswith('ㅎㅇ'):
        msg = '안녕하세요 {0.author.mention}환자님'.format(message)
        await client.send_message(message.channel, msg)
        await client.send_file(message.channel, '안녕하살법.gif')

    if message.content.startswith('째트킥'):
        await client.send_file(message.channel, '째트킥.gif')
        
    if message.content.startswith('지랄노') or message.content.startswith('ㅈㄹㄴ'):
        await client.send_file(message.channel, '지랄노.png')
        
    if message.content.startswith('머임'):
        await client.send_file(message.channel, '머임.gif')
        
    if message.content.startswith('안녕하살법'):
        await client.send_file(message.channel, '안녕하살법.gif')
        
    if message.content.startswith('어케했노'):
        await client.send_file(message.channel, '어케했노.gif')
        
    if message.content.startswith('안녕하살받아치기') or message.content.startswith('안녕하살뻡 받아치기'):
        await client.send_file(message.channel, '안녕하살법받아치기.gif')

    if message.content.startswith('하와와'):
        await client.send_file(message.channel, 'hawawa.png')

    if message.content.startswith('에?'):
        await client.send_file(message.channel, '에난닷테.jpg')
    
    if message.content.startswith('호애애애'):
        await client.send_file(message.channel, '好愛曖靄.jpg')

    if message.content.startswith('태보') or message.content.startswith('절대태보해'):
        await client.send_message(message.channel, "@(^ 0^)==@" + "\t" + "@==(^0 ^)@")
        await client.send_file(message.channel, '안녕하세요.gif')
        
    if message.content.startswith('이집 재밌네') or message.content.startswith('이집재밌네') or message.content.startswith('이 집 재밌네') or message.content.startswith('재밌네'):
        await client.send_file(message.channel, '이집재밌네.jpg')
        
    if message.content.startswith('머쓱'):
        await client.send_file(message.channel, '머쓱.png')

    if message.content.startswith('/청소'):
        if message.author.id == "342522847823921154" or message.author.id == "430377165629161482" or message.author.id == "339613968320561154" or message.author.id == "268611192392515584":
            clear = message.content.split(" ")
            async for m in client.logs_from(message.channel, limit=int(clear[1])):
               await client.delete_message(m)
            await client.send_message(message.channel, embed=discord.Embed(description= str(clear[1]) + "개의 메세지를 청소햇어요~ 하와와~"))
            print("\n\t" + '청소완료')
        else:
           embed = discord.Embed(title="안돼", description="청소해줄생각없어 돌아가")
           await client.send_message(message.channel, embed=embed)

    if message.content.startswith('/?'):
        channel = message.channel
        embed = discord.Embed(
            title = '도움말',
            description = '잘새겨듣거라',
            colour = discord.Colour.red()
        )

        embed.add_field(name='/날씨 [지역]', value='날씨를 알려줘', inline=False) 
        embed.add_field(name='/실시간검색어, /실검', value='ㅈㅁㄱ', inline=False)
        embed.add_field(name='/영화순위', value='영화순위를 알려주는 기능이지', inline=False)
        embed.add_field(name='/한강수온, /한강', value='한강으로 다이빙', inline=False)
        embed.add_field(name='/청소 [숫자]', value='숫자만큼 메세지를 없애줘', inline=False)
        embed.add_field(name='/짤방', value='짤방목록', inline=False)
        embed.add_field(name='채팅 기록', value='(제거됨)', inline=False)

        await client.send_message(channel,embed=embed)
        
    if message.content.startswith('/짤방'):
        channel = message.channel
        embed = discord.Embed(
            title = '짤방',
            description = '짤방목록',
            colour = discord.Colour.red()
        )

        embed.add_field(name='미치신겁니까 Human', value='미치신겁니까', inline=False) 
        embed.add_field(name='힘의 차이가 느껴지십니까?', value='느껴지십니까 / 힘의 차이가 / ', inline=False)
        embed.add_field(name='ㄴㅇㄱ', value='ㄴㅇㄱ / 상상도 못한 정체 / 상상도못한정체', inline=False)
        embed.add_field(name='주모!', value='kia / 주모 / ', inline=False)
        embed.add_field(name='그치만.. 오니짱..', value='그치만..', inline=False)
        embed.add_field(name='YEE', value='yee', inline=False)
        embed.add_field(name='어흑마이깟', value='어흑마이깟 / 어흑 마이깟 / 어흑 마이 깟', inline=False)
        embed.add_field(name='당근 빳따죠 쉬바', value='당근빠따죠 / 당근빳따죠 / 당빠', inline=False)
        embed.add_field(name='넹기분굿', value='넹기분굿 / 넹 기분 / ', inline=False)
        embed.add_field(name='핫하받아라', value='핫하받아라 / 핫하 받아라', inline=False)
        embed.add_field(name='충성충성', value='^^7 / ', inline=False)
        embed.add_field(name='째트킥', value='째트킥', inline=False)
        embed.add_field(name='고오얀놈', value='고오얀놈', inline=False)
        embed.add_field(name='지랄도 적당이 하쉽쇼', value='지랄노 / ㅈㄹㄴ', inline=False)
        embed.add_field(name='머임????', value='머임', inline=False)
        embed.add_field(name='안녕하살법', value='안녕하살법', inline=False)
        embed.add_field(name='안녕하살법 받아치기', value='안녕하살뻡받아치기 / 안녕하살뻡 받아치기', inline=False)
        embed.add_field(name='어케했노 시발련ㄴ아 ', value='어케했노', inline=False)
        embed.add_field(name='Hawawa... ', value='하와와', inline=False)
        embed.add_field(name='어케했노 시발련ㄴ아', value='어케했노', inline=False)
        embed.add_field(name='에? 난닷테?', value='에?', inline=False)
        embed.add_field(name='호애애애...', value='호애애애', inline=False)
        embed.add_field(name='@(^0^)==@', value='태보 / 절대태보해', inline=False)
        embed.add_field(name='이 집 재밌네', value='이집재밌네 / 이집 재밌네 / 이 집 재밌네 / ', inline=False)
        embed.add_field(name='머쓱', value='머쓱', inline=False)

        await client.send_message(channel,embed=embed)

    if message.content.startswith('/실시간검색어') or message.content.startswith('/실검'):
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')


        embed = discord.Embed(
            title='네이버 실시간 검색어',
            description='호애애애~',
            colour=discord.Colour.green()
        )
        for i in range(0,20):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query='+realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i+1)+'위', value='\n'+'[%s](<%s>)' % (realTimeSerach, realURL), inline=False)

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('/영화순위'):
        # http://ticket2.movie.daum.net/movie/movieranklist.aspx
        i1 = 0 # 랭킹 string값
        embed = discord.Embed(
            title = "영화순위",
            description = "영화순위인거시와오~",
            colour= discord.Color.red()
        )
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        moviechartBase = bsObj.find('div', {'class': 'main_detail'})
        moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
        moviechart2 = moviechart1.find_all('li')

        for i in range(0, 20):
            i1 = i1+1
            stri1 = str(i1) # i1은 영화랭킹을 나타내는데 사용됩니다
            print()
            print(i)
            print()
            moviechartLi1 = moviechart2[i]  # ------------------------- 1등랭킹 영화---------------------------
            moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div
            moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
            moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목
            print(moviechartLi1MovieName)

            moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
            moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
            moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점
            print(moviechartLi1Ratting)

            moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
            moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임
            moviechartLi1openDay3 = moviechartLi1openDay2[0]
            moviechartLi1Yerating1 = moviechartLi1openDay2[1]
            moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜
            print(moviechartLi1openDay)
            moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동
            print(moviechartLi1Yerating)  # ------------------------- 1등랭킹 영화---------------------------
            print()
            embed.add_field(name='---------------랭킹'+stri1+'위---------------', value='\n영화제목 : '+moviechartLi1MovieName+'\n영화평점 : '+moviechartLi1Ratting+'점'+'\n개봉날짜 : '+moviechartLi1openDay+'\n예매율,랭킹변동 : '+moviechartLi1Yerating, inline=False) # 영화랭킹


        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('/한강'):
        url = 'https://www.wpws.kr/hangang/'
        print(url)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'id': 'content'})

        todayTemp = todayBase.find('/i', {'class': 'todaytemp'})
        print(todayTemp)

        embed = discord.Embed(
            title= '수온 정보',
            description= '한강 수온',
            colour=discord.Colour.gold()
        )

        embed.add_field(name='현재 한강 수온은?', value=todayTemp, inline=False)
        embed.set_footer(text = '반자이는 안되는거시와오')

        await client.send_message(message.channel,embed=embed)
            
    if message.content.startswith("/날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태

        await client.send_message(message.channel,embed=embed)
        
client.run('NTU2NDQ5MzY3ODYzNTkwOTIz.D255bA.M-qkDOV3_o8B0SGkpMOZwq2cRJk')
