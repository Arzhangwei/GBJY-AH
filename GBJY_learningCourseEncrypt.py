from pickle import FALSE #line:1
from selenium import webdriver #line:2
from selenium .webdriver .common .by import By #line:3
from selenium .common .exceptions import NoSuchElementException #line:5
from selenium .webdriver .support import expected_conditions as EC #line:6
from selenium .webdriver .support .ui import WebDriverWait #line:7
import binascii #line:8
from selenium .webdriver .common .action_chains import ActionChains #line:9
import asyncio ,sys ,re ,datetime #line:10
import base64 #line:11
from PIL import Image #line:12
from io import BytesIO #line:13
import pytesseract #line:14
import ddddocr ,io ,sqlite3 ,requests #line:15
import requests #line:16
from bs4 import BeautifulSoup #line:17
from pickle import FALSE #line:18
from selenium import webdriver #line:19
from cryptography .hazmat .primitives .ciphers import Cipher ,algorithms ,modes #line:20
from cryptography .hazmat .backends import default_backend #line:21
from cryptography .hazmat .primitives import padding #line:22
from base64 import b64encode ,b64decode #line:23
my_link_list =[]#line:29
op =webdriver .EdgeOptions ()#line:34
op .add_experimental_option ("detach",True )#line:35
op .add_experimental_option ('excludeSwitches',['enable-automation'])#line:36
op .add_experimental_option ('useAutomationExtension',False )#line:37
driver =webdriver .Edge (options =op )#line:39
driver .execute_cdp_cmd ("Page.addScriptToEvaluateOnNewDocument",{"source":"""
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """})#line:46
async def print_home ():#line:51
    print (f"""
                                                        ||      ||                                 
                                                        ||      ||                    |||          
             |||||||||||||||                            ||      ||           |||||||||||||         
             |||||||||||||||                            ||      ||           |||||||||             
                  ||                                  | ||| ||||||||||       ||    ||              
                  ||                                  ||||||||||||||||       ||    ||              
                  ||                                  ||||||    ||  ||       ||    ||              
              ||||||||||||      |||||||||||||||||||   ||||||    ||  ||       ||    ||              
              ||||||||||||      |||||||||||||||||||   |||| ||   ||  ||      ||||||||||||||||       
                 |||    ||                            | || |||||||||||||    ||||||||||||||||       
                 ||     ||                           || || |||||||||||||       |   ||              
                 ||     ||                              ||     ||||            ||  || ||           
                 ||     ||                              ||     || ||          |||  || ||||         
                 ||     ||                              ||     || ||         |||   ||   |||        
                |||     ||                              ||    ||   ||       |||    ||    |||       
           ||||||||||||||||||                           ||   |||   |||     |||     ||     |||      
           ||||||||||||||||||                           ||  |||     ||||  |||      ||      |       
                                                        ||||||       |||   |    |||||              
                                                        || ||         |          |||                 
                                                    

                         __                        __                  _      _  
                        [  |                      [  |  _             (_)    (_) 
                        | |.--.   ,--.   _ .--.   | | / ]_   _   __   __     __  
                        | '/'`\ \`'_\ : [ `.-. |  | '' <[ \ [ \ [  ] [  |   [  | 
                        |  \__/ |// | |, | | | |  | |`\ \\ \/\ \/ / _  | | _  | | 
                        [__;.__.' \'-;__/[___||__][__|  \_]\__/\__/[ \_| |[ \_| | 
                                                                    \____/\____/ 
            
                项目:GBJY_study                                      Verion: V1.0
""")#line:80
async def decode_base64_image (OO00000O0OOOO00O0 ):#line:85
    O000000O00O0O0OO0 =base64 .b64decode (OO00000O0OOOO00O0 )#line:90
    return O000000O00O0O0OO0 #line:95
async def checkIslogin ():#line:101
    try :#line:102
        OO0OO0O0O0O0O0O00 =90 #line:105
        O000OOO0O000OOOOO =driver .find_element (By .XPATH ,"//*[@id='getYzm']")#line:109
        OOOOOOOO000O0OO0O =O000OOO0O000OOOOO .screenshot_as_base64 #line:111
        O00OOO0000OO0O0OO =await decode_base64_image (OOOOOOOO000O0OO0O )#line:112
        OO0O0O00O0OO0O00O =await OCR_image_Func (O00OOO0000OO0O0OO )#line:113
        driver .find_element (By .XPATH ,"//*[@id='yzm']").send_keys (str (OO0O0O00O0OO0O00O ))#line:114
        await asyncio .sleep (2 )#line:115
        while True :#line:119
            print ("登录超时剩余时间(秒)：",OO0OO0O0O0O0O0O00 )#line:120
            await asyncio .sleep (1 )#line:121
            OO0OO0O0O0O0O0O00 -=1 #line:122
            if OO0OO0O0O0O0O0O00 <=0 :#line:123
                print ("超时登录，程序退出")#line:124
                sys .exit (0 )#line:125
            O0O00000O0O0OOO0O =driver .page_source #line:128
            if "退出登录"in O0O00000O0O0OOO0O :#line:132
                print ("登录成功")#line:133
                break #line:134
            else :#line:135
                continue #line:136
    except Exception as O00OOO0O00O000O0O :#line:138
        print (f"checkIslogin: {O00OOO0O00O000O0O}")#line:139
        sys .exit (0 )#line:140
baseUrl ="https://bankwjj.cf/json/"#line:144
async def openBrowser ():#line:145
    await print_home ()#line:146
def aes_encrypt (O0O000OO0OO0OOOOO ,OO00O00O00000O000 ):#line:154
    OOO0O0OOO00O000O0 =padding .PKCS7 (128 ).padder ()#line:156
    OOOO0OO0O00O000OO =OOO0O0OOO00O000O0 .update (OO00O00O00000O000 )+OOO0O0OOO00O000O0 .finalize ()#line:157
    OOOOOOOO00O0OO00O =b'\x00'*16 #line:160
    O000O000O0OO0OO00 =Cipher (algorithms .AES (O0O000OO0OO0OOOOO ),modes .CBC (OOOOOOOO00O0OO00O ),backend =default_backend ())#line:163
    OOO0O00OO00OOOOO0 =O000O000O0OO0OO00 .encryptor ()#line:166
    OO000OOO000000OO0 =OOO0O00OO00OOOOO0 .update (OOOO0OO0O00O000OO )+OOO0O00OO00OOOOO0 .finalize ()#line:167
    return OO000OOO000000OO0 ,OOOOOOOO00O0OO00O #line:170
def aes_decrypt (O000OOO0O0000O0OO ,OO0OO000OOOO0O00O ,O0OOO00OOOO00O0O0 ):#line:172
    OOO0OO0O00OOO0OO0 =Cipher (algorithms .AES (O000OOO0O0000O0OO ),modes .CBC (OO0OO000OOOO0O00O ),backend =default_backend ())#line:174
    OO0O000OO00O000OO =OOO0OO0O00OOO0OO0 .decryptor ()#line:177
    OO000O00O0OO0OOO0 =OO0O000OO00O000OO .update (O0OOO00OOOO00O0O0 )+OO0O000OO00O000OO .finalize ()#line:178
    O0O00O000OO0O00OO =padding .PKCS7 (128 ).unpadder ()#line:181
    O0OOO00OO000O0000 =O0O00O000OO0O00OO .update (OO000O00O0OO0OOO0 )+O0O00O000OO0O00OO .finalize ()#line:182
    return O0OOO00OO000O0000 .decode ()#line:185
key =b'wujiajia45431701'#line:189
async def RemoveEncrypt (O00O0O0O0000OOOO0 ):#line:192
    OOOO0O0OOO000OOO0 =baseUrl +O00O0O0O0000OOOO0 #line:193
    OOOOO000OOO00OO00 =requests .get (OOOO0O0OOO000OOO0 )#line:194
    if OOOOO000OOO00OO00 .status_code ==200 :#line:195
        O0OO00000OO000000 =OOOOO000OOO00OO00 .text .splitlines ()#line:196
    else :#line:197
        print ("Failed to retrieve data:",OOOOO000OOO00OO00 .status_code )#line:198
    OO0O0OO00O0OO00OO =b64decode (O0OO00000OO000000 [0 ])#line:200
    O0OO0O0O0OOO00OOO =b64decode (O0OO00000OO000000 [1 ])#line:201
    OOOOOO000O00000OO =aes_decrypt (key ,O0OO0O0O0OOO00OOO ,OO0O0OO00O0OO00OO )#line:204
    return OOOOOO000O00000OO #line:207
async def goto_Bixiu_Func (OOOO0000O0OOO00O0 ):#line:212
    try :#line:213
        driver .get (f"https://www.ahgbjy.gov.cn/pc/course/courselist.do?categoryid=&year={OOOO0000O0OOO00O0}&coutype=1&mostNInput=0&mostHInput=0&mostTJInput=&keyword=")#line:215
        await asyncio .sleep (10 )#line:216
        OOOOOOOOO0O00OO0O =await calculatePageNumber ()#line:218
        for O0OO00000000OO0O0 in range (1 ,OOOOOOOOO0O00OO0O +1 ):#line:220
            driver .get (f'https://www.ahgbjy.gov.cn/pc/course/courselist.do?pagenum={O0OO00000000OO0O0}&categoryid=&year={OOOO0000O0OOO00O0}&coutype=1&microcourse=&mostNInput=0&mostHInput=0&mostTJInput=&keyword=')#line:221
            await asyncio .sleep (10 )#line:222
            await FindAll_a_block_Func ()#line:223
    except Exception as O0O0O0OO0OOOOOOO0 :#line:224
        print ("goto_Bixiu_Func 发生异常:",O0O0O0OO0OOOOOOO0 )#line:225
async def goto_Xuanxiu_Func (OOOOO000OO000O0OO ):#line:227
    try :#line:228
        driver .get (f"https://www.ahgbjy.gov.cn/pc/course/courselist.do?categoryid=&year={OOOOO000OO000O0OO}&coutype=0&mostNInput=0&mostHInput=0&mostTJInput=&keyword=")#line:230
        await asyncio .sleep (10 )#line:231
        OOO00OO0000OO000O =await calculatePageNumber ()#line:233
        for OO00O00O0000000O0 in range (1 ,OOO00OO0000OO000O +1 ):#line:235
            driver .get (f'https://www.ahgbjy.gov.cn/pc/course/courselist.do?pagenum={OO00O00O0000000O0}&categoryid=&year={OOOOO000OO000O0OO}&coutype=0&microcourse=&mostNInput=0&mostHInput=0&mostTJInput=&keyword=')#line:236
            await asyncio .sleep (10 )#line:237
            await FindAll_a_block_Func ()#line:238
    except Exception as OOOOO00OOO00OOOOO :#line:240
        print ("goto_Xuanxiu_Func 发生异常:",OOOOO00OOO00OOOOO )#line:241
async def calculatePageNumber ():#line:244
        OOOOOOO0000O0O00O =driver .find_element (By .XPATH ,"//*[@id='detail']/div[2]/div[4]/div/div/ul/span").text #line:245
        OOOOO0O0O00O00000 =re .search (r'\d+',OOOOOOO0000O0O00O )#line:247
        if OOOOO0O0O00O00000 :#line:249
            OOOOO0O0O00O00000 =int (OOOOO0O0O00O00000 .group ())#line:250
        else :#line:251
            OOOOO0O0O00O00000 =None #line:252
        print (OOOOO0O0O00O00000 )#line:253
        return OOOOO0O0O00O00000 #line:254
async def FindAll_a_block_Func ():#line:256
        WebDriverWait (driver ,10 ).until (EC .visibility_of_element_located ((By .CSS_SELECTOR ,"a")))#line:257
        O000OO0OOO0OO0000 =driver .find_elements (By .CSS_SELECTOR ,"a")#line:259
        for O0O0OO0OOOO00O00O in O000OO0OOO0OO0000 :#line:262
            O0OOO0O0000OOOOO0 =O0O0OO0OOOO00O00O .get_attribute ("href")#line:264
            if O0OOO0O0000OOOOO0 and not O0O0OO0OOOO00O00O .is_displayed ():#line:266
                print ("Hidden link href:",O0OOO0O0000OOOOO0 )#line:267
                if "pc/course/coursedetail"in O0OOO0O0000OOOOO0 :#line:268
                    if O0OOO0O0000OOOOO0 not in my_link_list :#line:269
                        my_link_list .append (O0OOO0O0000OOOOO0 )#line:270
async def OCR_image_Func (O0OO00O0000O0O0OO ):#line:272
    O00OO0OO0000OOO00 =ddddocr .DdddOcr ()#line:275
    OOOOO00O0000O0O00 =O00OO0OO0000OOO00 .classification (O0OO00O0000O0O0OO )#line:277
    print ("识别结果:",OOOOO00O0000O0O00 )#line:279
    if len (OOOOO00O0000O0O00 )==4 :#line:280
        return OOOOO00O0000O0O00 #line:281
    return '0'#line:282
async def calculateCourseTime (O0OO0OOOO00OOO0O0 ):#line:284
    O0O0000O000O00000 =re .search (r'\d+',O0OO0OOOO00OOO0O0 )#line:286
    if O0O0000O000O00000 :#line:289
        O0O0000O000O00000 =int (O0O0000O000O00000 .group ())#line:290
    else :#line:291
        O0O0000O000O00000 =None #line:292
    if O0O0000O000O00000 is not None :#line:295
        O00O00O0O0O0OOO00 =O0O0000O000O00000 *60 +10 #line:296
        print (O00O00O0O0O0OOO00 )#line:297
        return O00O00O0O0O0OOO00 #line:298
    else :#line:299
        print ("获取课程时间出现异常")#line:300
async def checkBixiu_isOver_Func (OOOO0O000OO00OO00 ):#line:303
    driver .get ('https://www.ahgbjy.gov.cn/pc/my/credituser.do')#line:305
    await asyncio .sleep (8 )#line:306
    O0O00000000OOO00O =driver .find_element (By .XPATH ,"/html/body/div[4]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[2]").text #line:307
    OO0000O0O0O0OO000 =driver .find_element (By .XPATH ,"/html/body/div[4]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[4]").text #line:308
    if OOOO0O000OO00OO00 =='A':#line:310
        if O0O00000000OOO00O =='0':#line:311
            return '1'#line:312
    if OOOO0O000OO00OO00 =='B':#line:313
        if OO0000O0O0O0OO000 =='0.0':#line:314
             return '1'#line:315
    return '0'#line:316
async def getCourseResource_Func (O0O0OO00OO00OO0O0 ):#line:320
    driver .get (O0O0OO00OO00OO0O0 )#line:321
    await asyncio .sleep (8 )#line:322
    OO0O0OO00000OO000 =[]#line:323
    try :#line:324
        OO0000OOOO00O0O0O =[]#line:326
        WebDriverWait (driver ,10 ).until (EC .visibility_of_element_located ((By .CSS_SELECTOR ,"a")))#line:327
        OOOOO00O0OOO0OO0O =driver .find_elements (By .CSS_SELECTOR ,"a")#line:329
        for O0O0O0OO00O0OO0O0 in OOOOO00O0OOO0OO0O :#line:332
            OO000000O000O0O00 =O0O0O0OO00O0OO0O0 .get_attribute ("data-chapterid")#line:334
            if OO000000O000O0O00 is not None :#line:336
                print ("data-chapterid:",OO000000O000O0O00 )#line:337
                OO0000OOOO00O0O0O .append (OO000000O000O0O00 )#line:338
        O00OOOOOO0O0OOO0O =driver .find_element (By .XPATH ,"/html/body/div[4]/div[2]/div[1]/div/section/div/div[2]/table")#line:342
        O00OOO0000OOO0OOO =O00OOOOOO0O0OOO0O .find_elements (By .XPATH ,".//tr")#line:344
        print ('##########################')#line:345
        O0OO00000O0O0O000 =0 #line:347
        for OO000O0O00O000O00 in O00OOO0000OOO0OOO :#line:349
            O000O0OOO000O0000 =[]#line:351
            O0OOO0OOOO0OOOO0O =OO000O0O00O000O00 .find_elements (By .XPATH ,".//td")#line:353
            for OOO00000000O0O000 in O0OOO0OOOO0OOOO0O :#line:355
                print (OOO00000000O0O000 .text )#line:357
                O000O0OOO000O0000 .append (OOO00000000O0O000 .text )#line:359
            O0O00O00O0O0O0000 ="|".join (O000O0OOO000O0000 )#line:361
            OO0OOO00000OOOOOO =O0O00O00O0O0O0000 +"|"+O0O0OO00OO00OO0O0 +"|"+OO0000OOOO00O0O0O [O0OO00000O0O0O000 ]#line:363
            OO0O0OO00000OO000 .append (OO0OOO00000OOOOOO )#line:364
            O0OO00000O0O0O000 +=1 #line:365
        await asyncio .sleep (2 )#line:367
        return OO0O0OO00000OO000 #line:368
    except Exception as O000O0O00O0O0OOO0 :#line:370
        print ("opencourse_Func 发生异常:",O000O0O00O0O0OOO0 )#line:371
async def main ():#line:375
    await openBrowser ()#line:376
    try :#line:377
        driver .get ('https://www.ahgbjy.gov.cn/pc/index.do')#line:379
        await asyncio .sleep (8 )#line:381
        await checkIslogin ()#line:383
        await asyncio .sleep (8 )#line:384
        OOO0OO00O00000OO0 =datetime .datetime .now ()#line:387
        OOO0O000OO00OO00O =OOO0OO00O00000OO0 .year #line:389
        print (OOO0O000OO00OO00O )#line:390
        OOOO00OO0OO000OOO =await RemoveEncrypt ("spider_out.txt")#line:393
        OO0OO00OO00OO00O0 =OOOO00OO0OO000OOO .split ('\n')#line:396
        for O0O0O0O000OOO0OOO in OO0OO00OO00OO00O0 :#line:397
            OOO00OO0OO00O0OOO ,OOO0O00O00000OOOO ,OOOO0OOOOO00OOO00 ,O0OO00O0OO0O000O0 ,OO0O00O00O0O0OO00 ,O0000OO00O00OO0O0 ,O0OO00OO00O0O0OO0 ,O000OO0O0000OOOOO =O0O0O0O000OOO0OOO .strip ().split ("|")#line:399
            OOOOOO000OOOO00OO =await checkBixiu_isOver_Func (O000OO0O0000OOOOO )#line:401
            if '1'==OOOOOO000OOOO00OO :#line:403
                continue #line:404
            OO00OO0O00OOO000O =await getCourseResource_Func (O0000OO00O00OO0O0 )#line:408
            for O0O0O0O000OOOO0O0 in OO00OO0O00OOO000O :#line:412
                O00OOO0OOO0O000O0 ,O00OOOOO000O00OOO ,OOO00000OO00OOOOO ,OOOO0O0000OO00OO0 ,O000O00O0OOOO0O0O ,O0O0OO0O0000O0OOO ,O0O0O0OO0000000OO ,O0OO0OO00O0O0O00O =O0O0O0O000OOO0OOO .strip ().split ("|")#line:413
                if '已学 100%'in OOOO0O0000OO00OO0 :#line:415
                    continue #line:416
                O0000000OOOO00O00 =O0000OO00O00OO0O0 +"&chapterid="+O0OO00OO00O0O0OO0 #line:418
                O00O0O00O0O0O00O0 =O0000000OOOO00O00 .replace ("coursedetail","playscorm")#line:420
                driver .get (O00O0O00O0O0O00O0 )#line:422
                await asyncio .sleep (8 )#line:423
                O0OO0OO0O000OOO0O =await calculateCourseTime (OOO0O00O00000OOOO )#line:431
                while True :#line:433
                    print ("播放剩余时间（秒）：",O0OO0OO0O000OOO0O )#line:434
                    O0OO0OO0O000OOO0O -=1 #line:435
                    await asyncio .sleep (1 )#line:436
                    if O0OO0OO0O000OOO0O <=0 :#line:437
                        driver .find_element (By .XPATH ,"//*[@id='completebtn']").click ()#line:438
                        await asyncio .sleep (2 )#line:439
                        O0OO00O000O0OOO0O =driver .switch_to .alert #line:442
                        O0OO00O000O0OOO0O .accept ()#line:444
                        await asyncio .sleep (1 )#line:445
                        break #line:446
    except Exception as O000O0000000OOOO0 :#line:455
        print (f"登录异常 : {O000O0000000OOOO0}")#line:456
        sys .exit (0 )#line:457
asyncio .run (main ())