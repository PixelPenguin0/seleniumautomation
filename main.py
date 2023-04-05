import multiprocessing
import dropmail
import time
import os.path
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os


random_email = None
link = ''

def countdown():
    time.sleep(15)
    print('no email received, rebooting...')
    time.sleep(1)
    os.execl(sys.executable, sys.executable, *sys.argv)

def fetch_mail(mailboxnew):
    p = multiprocessing.Process(target=countdown, name='countdown')
    p.start()
    # p.join(5)
    global link
    target_mail = mailboxnew.next_message()
    link = target_mail['text'].split('\n')
    link = link[7].split('](')
    link = link[0].lstrip().rstrip()
    link = link.split('[')
    link = link[1]
    p.terminate()
    print(link)
    final()

def signup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # open chrome and wait for site to load
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', chrome_options=options)
    driver.get('http://www.vanceai.com/')
    time.sleep(10)

    # email signup process
    driver.find_element(By.CSS_SELECTOR, 'i.icon_user').click()
    time.sleep(2)
    email_input = driver.find_element(By.XPATH,
                                      '//*[@id="__layout"]/div/div[6]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/input')
    email_input.click()
    email_input.send_keys(str(random_email))
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[6]/div/div[2]/div[2]/div/div[1]/div[3]/button').click()
    print('signup completed')
    fetch_mail(mailbox)

def final():
    time.sleep(1)

    # user details signup process
    driver.get(link)
    time.sleep(5)
    firstname_input = driver.find_element(By.XPATH,
                                          '//*[@id="__layout"]/div/div[3]/div[2]/div/div/div/form/div[1]/div[1]/div/div/div/input')
    firstname_input.click()
    firstname_input.send_keys('laskdj')
    time.sleep(2)

    lastname_input = driver.find_element(By.XPATH,
                                         '//*[@id="__layout"]/div/div[3]/div[2]/div/div/div/form/div[1]/div[2]/div/div/div/input')
    lastname_input.click()
    lastname_input.send_keys('paskdk')
    time.sleep(1)

    driver.find_element(By.XPATH,
                        '//*[@id="__layout"]/div/div[3]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/input').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[5]').click()
    time.sleep(1)

    pass_input1 = driver.find_element(By.XPATH,
                                      '//*[@id="__layout"]/div/div[3]/div[2]/div/div/div/form/div[2]/div[1]/div/div[1]/div/input')
    pass_input1.click()
    pass_input1.send_keys('yash1212')
    time.sleep(1)
    pass_input2 = driver.find_element(By.XPATH,
                                      '//*[@id="__layout"]/div/div[3]/div[2]/div/div/div/form/div[2]/div[2]/div/div/div/input')
    pass_input2.click()
    pass_input2.send_keys('yash1212')
    time.sleep(1)
    submit_button = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[2]/div/div/div/form/button')
    submit_button.click()
    time.sleep(5)

    driver.get('http://www.vanceai.com/')
    JS_DROP_FILES = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"

    def drop_files(element, files, offsetX=0, offsetY=0):
        driver = element.parent
        isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
        paths = []

        # ensure files are present, and upload to the remote server if session is remote
        for file in (files if isinstance(files, list) else [files]):
            if not os.path.isfile(file):
                raise FileNotFoundError(file)
            paths.append(file if isLocal else element._upload(file))

        value = '\n'.join(paths)
        elm_input = driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
        elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

    WebElement.drop_files = drop_files

    time.sleep(10)
    startnow_button = driver.find_element(By.XPATH,
                                          '//*[@id="__layout"]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/div')
    startnow_button.click()
    time.sleep(5)
    dropzone = driver.find_element(By.XPATH, '''//*[@id="__layout"]/div/div[3]/div/div[1]/div[2]/div/div/div/div[2]/
                                                                            div[1]/div[1]/div[2]/div[1]/div/div/div/div''')
    dropzone.drop_files(rf"C:\Users\yashj\Desktop\TSHIRTS\test\{i}")

    driver.find_element(By.XPATH,
                        '''//*[@id="pane-feature"]/div/div[1]/div[1]/div[1]/div[1]/span/span/i''').click()  # select dd
    time.sleep(0.5)
    driver.find_element(By.XPATH, '''/html/body/div[2]/div[1]/div[1]/ul/li[1]''').click()  # dd enhance
    time.sleep(0.5)
    driver.find_element(By.XPATH, '''//*[@id="pane-feature"]/div/div[2]/button''').click()  # add new dd
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        '''//*[@id="pane-feature"]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]''').click()  # dd denoiser auto button
    time.sleep(0.5)
    driver.find_element(By.XPATH, '''//*[@id="pane-feature"]/div/div[3]/button''').click()  # add new dd
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        '''//*[@id="pane-feature"]/div/div[3]/div[1]/div[1]/div[1]/span/span/i''').click()  # select new dd
    time.sleep(0.5)
    driver.find_element(By.XPATH, '''/html/body/div[3]/div[1]/div[1]/ul/li[3]''').click()  # select enlarge
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        '''//*[@id="pane-feature"]/div/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]''').click()  # select enlarge auto
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        '''//*[@id="__layout"]/div/div[3]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]''').click()  # start process
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div[1]/div[8]/div/div/div[1]/i').click()
    time.sleep(20)
    download_button = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="__layout"]/div/div[3]/div/div[1]/div[2]/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div[3]/div[1]/div[5]/div/div/div/div[2]/div[2]/span[3]/i'''))) # download
    download_button.click()
    time.sleep(20)
    os.replace(rf'C:\Users\yashj\Desktop\TSHIRTS\test\{i}', rf'C:\Users\yashj\Desktop\TSHIRTS\done\{i}')
    #time.sleep(4)
    driver.quit()


if __name__ == '__main__':
    images = os.listdir(r'C:\Users\yashj\Desktop\TSHIRTS\test')
    for i in images:
        print(f'{i}')
        mailbox = dropmail.Dropmail()
        random_email = mailbox.new_email()
        print(random_email)
        signup()


