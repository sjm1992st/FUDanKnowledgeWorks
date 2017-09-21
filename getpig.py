
from selenium import webdriver

for i in range(3760000257,3760000258):
    str1='atlas.brain-map.org/cgi-bin/imageservice?path=/external/devhuman/prod14/'
    str2=str1+str(i)+'/'+str(i)
    str3=str2+'_human_rendered.aff&mime=1&zoom=7'
    url=str3
    print url
    profile_dir="C:\Users\user\AppData\Roaming\Mozilla\Firefox\Profiles\udat2g3x.default"
    profile = webdriver.FirefoxProfile(profile_dir)
    driver = webdriver.Firefox(profile)
    #url = 'atlas.brain-map.org/cgi-bin/imageservice?path=/external/devhuman/prod14/3760000289/3760000289_human_rendered.aff&mime=1&zoom=7'
    driver.get("http://atlas.brain-map.org/cgi-bin/imageservice?path=/external/devhuman/prod14/3760000257/3760000257_human_rendered.aff&mime=1&zoom=7")
    driver.close()


