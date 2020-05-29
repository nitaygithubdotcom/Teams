# -*- coding: utf-8 -*-
# cpoy of players2
import scrapy

class PlayerSpider(scrapy.Spider):
    name = 'indplayers'
    start_urls = ['https://www.cricbuzz.com/cricket-team/india/2/players']

    def parse(self, response):
        linkxp = '//div[@class="cb-col-67 cb-col cb-left cb-top-zero"]/a/@href'
        linklist = response.xpath(linkxp)
        yield from response.follow_all(linklist, self.parsedata)

    def parsedata(self, response):
        name = (response.xpath('//div[@class="cb-col cb-col-80 cb-player-name-wrap"]/h1/text()').get()).strip()
        team = (response.xpath('//div[@class="cb-col cb-col-80 cb-player-name-wrap"]/h3/text()').get()).strip()
        personalinfo = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div//div[@class="cb-font-16 text-bold"]/text()').get()).strip(' ')
        born_k = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][1]/text()').get()).strip()
        born_v = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][1]/text()').get()).strip()
        birthplace_k = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][2]/text()').get()).strip()
        birthplace_v = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][2]/text()').get()).strip()
        height_k = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div//div[@class="cb-col cb-col-40 text-bold"])/text()').get()).strip()
        height_v = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div//div[@class="cb-col cb-col-60"])/text()').get()).strip(' ')
        role_k = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][3]/text()').get()).strip()
        role_v = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][3]/text()').get()).strip()
        battingst_k = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][4]/text()').get()).strip()
        battingst_v = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][4]/text()').get()).strip()
        iccrank = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div//div[@class="cb-font-16 text-bold cb-lst-itm-sm cb-col cb-col-100 cb-sr-rev-label"])/text()').get()).strip()
        test = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 text-right cb-plyr-rank"])[1]/text()').get()).strip()
        odi = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 text-right cb-plyr-rank"])[2]/text()').get()).strip()
        t20 = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 text-right cb-plyr-rank"])[3]/text()').get()).strip()
        batting_k = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 text-left cb-plyr-rank text-bold"])[1]/text()').get()).strip()
        balling_k = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 text-left cb-plyr-rank text-bold"])[2]/text()').get()).strip()
        battest = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[1]/text()').get()).strip()
        batodi = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[2]/text()').get()).strip()
        batt20 = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[3]/text()').get()).strip()
        balltest = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[4]/text()').get()).strip()
        ballodi = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[5]/text()').get()).strip()
        ballt20 = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[6]/text()').get()).strip()
        careerinfo = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-100 cb-font-16 text-bold cb-ttl-vts"]/text()').get()).strip()
        teams_k = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"])[6]/text()').get()
        if teams_k is None:
            teams_k = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"])[5]/text()').get()
        teams_v = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"])[6]/text()').get()
        ball_k = None
        ball_v = None
        teams_val = []
        if teams_v is not None:
            teams_v = (teams_v.strip(' ')).split(',')
            for i in teams_v:
                teams_val.append(i.strip())
            ball_k = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][5]/text()').get()
            ball_k=ball_k
            ball_v = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][5]/text()').get()).strip(' ')
            ball_v=ball_v
        
        if teams_v is None:
            teams_v = ((response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"])[5]/text()').get()).strip(' ')).split(',')
            for i in teams_v:
                teams_val.append(i.strip())
        
        data = {
            "name":name,"team":team,
            personalinfo:{
                born_k:born_v,
                birthplace_k:birthplace_v,
                height_k:height_v,
                role_k:role_v,
                battingst_k:battingst_v,
                ball_k:ball_v
            },
            iccrank:{
                batting_k:{test:battest,odi:batodi,t20:batt20},
                balling_k:{test:balltest,odi:ballodi,t20:ballt20}
            },
            careerinfo:{teams_k:teams_val}
        }
        yield data
