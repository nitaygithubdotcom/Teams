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
        born_v = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][1]/text()').get()).strip()
        birthplace_k = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][2]/text()').get()
        birthplace_v = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][2]/text()').get()).strip()
        height_k = response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div//div[@class="cb-col cb-col-40 text-bold"])/text()').get()
        height_v = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div//div[@class="cb-col cb-col-60"])/text()').get()).strip()
        role_k = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][3]/text()').get()
        role_v = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][3]/text()').get()).strip()
        battingst_k = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][4]/text()').get()
        battingst_v = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][4]/text()').get()).strip()
        ball_k = response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"][5]/text()').get()
        ball_v = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"][5]/text()').get()).strip()
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
        careerinfo = (response.xpath('//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-100 cb-font-16 text-bold cb-ttl-vts"]/text()').get()).strip()
        teams_k = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-40 text-bold cb-lst-itm-sm"])[6]/text()').get()).strip()
        teams_v = (response.xpath('(//div[@class="cb-col cb-col-33 text-black"]/div/div[@class="cb-col cb-col-60 cb-lst-itm-sm"])[6]/text()').get()).strip()

        batting_career = response.xpath('(//div[@class="cb-plyr-tbl"]/div)[1]/text()').get()
        battest = response.xpath('((//div[@class="cb-plyr-tbl"])[1]/table/tbody/tr/td/strong)[1]/text()').get()
        batodi = response.xpath('((//div[@class="cb-plyr-tbl"])[1]/table/tbody/tr/td/strong)[2]/text()').get()
        bat20 = response.xpath('((//div[@class="cb-plyr-tbl"])[1]/table/tbody/tr/td/strong)[3]/text()').get()
        batipl = response.xpath('((//div[@class="cb-plyr-tbl"])[1]/table/tbody/tr/td/strong)[4]/text()').get()
        header = response.xpath('((//div[@class="cb-plyr-tbl"]/table)[1]/thead/tr/th)/text()').getall()
        testbody = response.xpath('((//div[@class="cb-plyr-tbl"]/table)[1]/tbody/tr)[1]/td/text()').getall()
        odibody = response.xpath('((//div[@class="cb-plyr-tbl"]/table)[1]/tbody/tr)[2]/td/text()').getall()
        t20body =  response.xpath('((//div[@class="cb-plyr-tbl"]/table)[1]/tbody/tr)[3]/td/text()').getall()
        iplbody = response.xpath('((//div[@class="cb-plyr-tbl"]/table)[1]/tbody/tr)[4]/td/text()').getall()
        testdata = {}
        odidata = {}
        t20data = {}
        ipldata = {}
        for i in range(len(header)):
            testdata.update({header[i]:testbody[i]})
            odidata.update({header[i]:odibody[i]})
            t20data.update({header[i]:t20body[i]})
            ipldata.update({header[i]:iplbody[i]})


        balling_career = response.xpath('(//div[@class="cb-plyr-tbl"]/div)[2]/text()').get()
        balltest = response.xpath('((//div[@class="cb-plyr-tbl"])[2]/table/tbody/tr/td/strong)[1]/text()').get()
        ballodi = response.xpath('((//div[@class="cb-plyr-tbl"])[2]/table/tbody/tr/td/strong)[2]/text()').get()
        ball20 = response.xpath('((//div[@class="cb-plyr-tbl"])[2]/table/tbody/tr/td/strong)[3]/text()').get()
        ballipl = response.xpath('((//div[@class="cb-plyr-tbl"])[2]/table/tbody/tr/td/strong)[4]/text()').get()
        ballheader = response.xpath('((//div[@class="cb-plyr-tbl"]/table)[2]/thead/tr/th)/text()').getall()
        balltestbody = response.xpath('((//div[@class="cb-plyr-tbl"]/table)[2]/tbody/tr)[1]/td/text()').getall()
        ballodibody = response.xpath('((//div[@class="cb-plyr-tbl"]/table)[2]/tbody/tr)[2]/td/text()').getall()
        ballt20body =  response.xpath('((//div[@class="cb-plyr-tbl"]/table)[2]/tbody/tr)[3]/td/text()').getall()
        balliplbody = response.xpath('((//div[@class="cb-plyr-tbl"]/table)[2]/tbody/tr)[4]/td/text()').getall()
        balltestdata = {}
        ballodidata = {}
        ballt20data = {}
        ballipldata = {}
        for i in range(len(ballheader)):
            balltestdata.update({ballheader[i]:balltestbody[i]})
            ballodidata.update({ballheader[i]:ballodibody[i]})
            ballt20data.update({ballheader[i]:ballt20body[i]})
            ballipldata.update({ballheader[i]:balliplbody[i]})

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
                battest:testdata,
                batodi:odidata,
                bat20:t20data,
                batipl:ipldata
            },
            balling_career:{
                balltest:balltestdata,
                ballodi:ballodidata,
                ball20:ballt20data,
                ballipl:ballipldata
            }
        }