# -*- coding: utf-8 -*-
import scrapy


class PlayerSpider(scrapy.Spider):
    name = 'playerdetails'
    start_urls = ['https://www.cricbuzz.com/profiles/9311/jasprit-bumrah/']

    def parse(self, response):
        name = (response.xpath('//div[@class="cb-col cb-col-80 cb-player-name-wrap"]/h1/text()').get()).strip()
        team = response.xpath('//div[@class="cb-col cb-col-80 cb-player-name-wrap"]/h3/text()').get()
        personalinfo = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div//div[@class="cb-font-16 text-bold"]/text()').get()).strip(' ')
        born_k = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][1]/text()').get()
        born_v = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][1]/text()').get()
        birthplace_k = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][2]/text()').get()
        birthplace_v = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][2]/text()').get()
        height_k = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div//div[@class="cb-col cb-col-40 text-bold"])/text()').get()
        height_v = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div//div[@class="cb-col cb-col-60"])/text()').get()).strip(' ')
        role_k = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][3]/text()').get()
        role_v = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][3]/text()').get()
        battingst_k = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][4]/text()').get()
        battingst_v = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][4]/text()').get()
        ball_k = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][5]/text()').get()
        ball_v = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][5]/text()').get()
        iccrank = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div//div[@class="cb-font-16 text-bold cb-lst-itm-sm cb-col cb-col-100 cb-sr-rev-label"])/text()').get()
        test = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 text-right cb-plyr-rank"])[1]/text()').get()
        odi = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 text-right cb-plyr-rank"])[2]/text()').get()
        t20 = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 text-right cb-plyr-rank"])[3]/text()').get()
        batting_k = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 text-left cb-plyr-rank text-bold"])[1]/text()').get()
        balling_k = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 text-left cb-plyr-rank text-bold"])[2]/text()').get()
        battest = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[1]/text()').get()
        batodi = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[2]/text()').get()
        batt20 = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[3]/text()').get()
        balltest = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[4]/text()').get()
        ballodi = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[5]/text()').get()
        ballt20 = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-25 cb-plyr-rank text-right"])[6]/text()').get()
        careerinfo = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-100 cb-font-16 text-bold cb-ttl-vts"]/text()').get()
        teams_k = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"])[6]/text()').get()
        teams_v = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"])[6]/text()').get()
        batting_career = response.xpath('(//div[@class="cb-plyr-tbl"]/div)[1]/text()').get()
        test = response.xpath('((//div[@class="cb-plyr-tbl"])[1]/table/tbody/tr/td/strong)[1]/text()').get()
        # length = len(response.xpath('((//div[@class="cb-plyr-tbl"]/table)[1]/thead/tr/th)'))
        # for i in range(1,length):
        #    matchxp = '((//div[@class="cb-plyr-tbl"]/table)[1]/thead/tr/th)[{}]/text()'.format(i+1)
        #    head = response.xpath(matchxp).get()

        header = response.xpath('((//div[@class="cb-plyr-tbl"]/table)[1]/thead/tr/th)/text()').getall()
        testbody = response.xpath('((//div[@class="cb-plyr-tbl"]/table)[1]/tbody/tr)[1]/td/text()').getall()
        testdata = {}
        for i in range(len(header)):
            testdata.update({header[i]:testbody[i]})
         
        yield {
            'Name':name,
            'Team':team,
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
            careerinfo:{teams_k:teams_v},
            batting_career:{
                test:
                testdata
            }
        }