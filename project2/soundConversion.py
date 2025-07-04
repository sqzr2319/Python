#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/4 14:06
# @Author: ms169
from aip import AipSpeech
import time
import pygame
from io import BytesIO

# 百度API配置，包含授权码
APP_ID = '6963197'
API_KEY = 'BiVRBMnsI0bvl4R1vBa22m5u'
SECRET_KEY = 'ENZrTRH8pK1lmj64GXFYj4cGMtjExOmq'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def text_to_speech(text):
    """调用百度API，将文本转换为语音并直接播放
    :param: text, 转成语音的文本
    """
    # 调用百度TTS接口（中文女声）
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,  # 音量 0-15
        'per': 0,  # 发音人 0-女声 1-男声 3-情感男声 4-童声
    })

    # 检查合成结果
    if isinstance(result, dict):
        print("语音合成失败:", result)
        return False

        # 使用 pygame 播放音频流
    pygame.mixer.init()
    pygame.mixer.music.load(BytesIO(result))  # 从内存加载二进制音频
    pygame.mixer.music.play()

    # 等待播放完成
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    return True
