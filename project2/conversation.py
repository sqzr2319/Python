#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/4 13:59
# @Author: ms169
from cozepy import Coze, TokenAuth, Message, ChatEventType
from cozepy import COZE_CN_BASE_URL

# Coze API配置访问密码
bot_id = "7523089237752152104"  # 配置自己的bot_id
user_id = "sqzr2319"  # 设置交互的用户名，可以自取

coze_api_token = 'pat_sLkI6lCXToqLvRllB6LkqUsJFPplCbVMB8ERUui9s7xcOFFUn7s3LauGEl9QhK1l'  # 配置自己的API访问密码
coze_api_base = COZE_CN_BASE_URL
coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)
bot_id = f'{bot_id}'
user_id = f'{user_id}'


def coze_chat(text):
    """调用Coze API 与Coze Agent进行对话，返回对话内容
    :param: text, 传给Agent的对话内容
    :return: message_answer, Agent的回答内容
    """
    message_input = text
    message_answer = ""
    for event in coze.chat.stream(bot_id=bot_id, user_id=user_id,
                                  additional_messages=[Message.build_user_question_text(message_input), ], ):
        if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
            message_answer += event.message.content

        if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
            print("token usage:", event.chat.usage.token_count)

    return message_answer
