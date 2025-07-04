#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/4 14:10
# @Author: ms169

from soundRecognition import record_audio, client as asr_client
from soundConversion import text_to_speech
from conversation import coze_chat
import os


def clear_screen():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """主函数，实现连续的人机交互"""
    print("=" * 50)
    print("欢迎使用智能助手，您可以通过语音或文字与我交流")
    print("输入数字'1'进行语音交互，输入数字'2'进行文字交互")
    print("随时输入'quit'或说出'退出'结束程序")
    print("=" * 50)

    while True:
        # 让用户选择交互方式
        choice = input("\n请选择交互方式 (1:语音 2:文字): ")

        # 获取用户输入
        user_input = ""
        if choice == '1':
            # 语音交互模式
            print("请开始说话...")
            audio_data = record_audio(5)  # 录音5秒
            result = asr_client.asr(audio_data, 'pcm', 16000, {'dev_pid': 1537})

            if 'result' in result:
                user_input = result['result'][0]
                print(f"识别到: {user_input}")
            else:
                print(f"识别失败: {result.get('err_msg')}")
                continue
        elif choice == '2':
            # 文字交互模式
            user_input = input("请输入您的问题: ")
        else:
            print("无效的选择，请输入1或2")
            continue

        # 检查是否退出
        if user_input.lower() == 'quit' or '退出' in user_input:
            print("感谢使用，再见！")
            text_to_speech("感谢使用，再见！")
            break

        # 发送到Agent并获取回复
        print("正在思考...")
        agent_response = coze_chat(user_input)

        # 显示并播放回复
        print(f"\nAgent回复: {agent_response}")
        text_to_speech(agent_response)


if __name__ == "__main__":
    main()
