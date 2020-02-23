import argparse


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
global arguments
arguments = parser.parse_args()
