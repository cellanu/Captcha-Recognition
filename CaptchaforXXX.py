#!/usr/bin/env python
# -*- conding:utf-8 -*-

import muggle_ocr
import re,time,base64,os


def main():
    try:
        sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
        with open(r"captcha.png", "rb") as f:
            b = f.read()
        text = sdk.predict(image_bytes=b)
        print('\n'+text+'\n')
    except:
        text= '0000'
        print('\nfailed！\n')
    
    if text =='':
        text= '0000'
        print('\nfailed！\n')

if __name__ == '__main__':
    main();
    
