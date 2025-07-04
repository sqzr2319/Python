#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/4 14:05
# @Author: ms169

from aip import AipSpeech
import pyaudio

# 百度API配置
APP_ID = '6963197'
API_KEY = 'BiVRBMnsI0bvl4R1vBa22m5u'
SECRET_KEY = 'ENZrTRH8pK1lmj64GXFYj4cGMtjExOmq'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def record_audio(seconds=5):
    """使用麦克风进行录音，默认录音5秒
    :param: seconds, 录音时长
    :return: 录音内容
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                    input=True, frames_per_buffer=1024)
    print(f"录音中({seconds}秒)...")
    frames = [stream.read(1024) for _ in range(0, int(16000 / 1024 * seconds))]
    stream.stop_stream();
    stream.close();
    p.terminate()
    return b''.join(frames)


if __name__ == "__main__":
    input("按回车开始说话...")
    audio_data = record_audio()  # 录音5秒
    result = client.asr(audio_data, 'pcm', 16000, {'dev_pid': 1537})  # 识别
    if 'result' in result:
        user_said = result['result'][0]
        print("你说的是:", user_said)
    else:
        print("识别失败:", result.get('err_msg'))
