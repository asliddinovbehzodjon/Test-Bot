import aiohttp
import asyncio
from loader import db
import requests
import json
from environs import Env
env = Env()
env.read_env()
# URL = env.str('URL')
from telegraph.aio import Telegraph
async def create_user(telegram_id:str,language:str=None,name:str=None,role:str=None
                      ,group:str=None):
    info = db.select_user(telegram_id=telegram_id)
    try:
        if info == {}:
           print(role)
           db.add_user(telegram_id=telegram_id,name=name,language=language,
                       role=role,guruh=group)
        else:
            pass
    except Exception as e:
        print(e)
        pass
async def get_all_users():
    try:
        data = db.select_all_users()
        return data
    except:
        return []
async def get_user(telegram_id):
    try:
        data = db.select_user(telegram_id=telegram_id)
        return data
    except:
        return {}
async def users_count():
    try:
        data = db.count_users()
        return data[0]
    except:
        return 0

async def change_user_language(telegram_id,language):
    try:
       db.update_user_language(language=language,telegram_id=telegram_id)
    except:
        pass
async def change_user_name(telegram_id,name):
    try:
       db.update_user_name(name=name,telegram_id=telegram_id)
    except:
        pass
async def change_user_role(telegram_id,role):
    try:
       db.update_user_role(role=role,telegram_id=telegram_id)
    except:
        pass
async def change_user_group(telegram_id,guruh):
    try:
       db.update_user_group(guruh=guruh,telegram_id=telegram_id)
    except:
        pass
async def add_channel(channel_id:str,channel_name:str=None,channel_members_count:str=None):
    try:
        db.add_channel(channel_id=channel_id,channel_members_count=channel_members_count,channel_name=channel_name)
    except:
        pass
async def get_all_channels():
    try:
        data = db.select_all_channels()
        return data

    except:
        return []
async def get_channel(channel_id):
    try:
        data = db.select_channel(channel_id=channel_id)
        return data
    except:
        return {}
async def delete_channel(channel_id):
    try:
       db.delete_channel(channel_id=channel_id)
    except:
        return "Bad"
#  Answers DB
async def create_answers(answers:str=None,telegram_id:str=None,type_test:str=None,code:str=None):
    try:
        id =  db.add_test(answers=answers,telegram_id=telegram_id,code=code,type_test=type_test)
        return id
         
    except Exception as e:
        print(e)
        pass
async def get_test(id):
    try:
        data = db.select_test(id=id)
        return data
    except:
        return {}
#  Results DB
async def create_results(code: int = None, name: str = None,trues:str=None,falses:str=None,telegram_id:str=None):
    try:
         await db.add_result(code=code,name=name,trues=trues,falses=falses,telegram_id=telegram_id)
         
    except Exception as e:
        print(e)
        pass
async def get_results(code):
    try:
        data = db.select_all_results(code=code)
        return data

    except Exception as e:
        print(e)
        return []
async def done_or_not(code,telegram_id):
    try:
        data = db.select_result(code=code,telegram_id=telegram_id)
        return data

    except Exception as e:
        print(e)
        return {}

async def delete_result_(code):
    try:
       db.delete_result(code=code)
    except Exception as e:
        print(e)
        return "Bad"
async def delete_answer_(id):
    try:
       db.delete_answers(id=id)
    except:
        return "Bad"
# ######################

async def delete_answer_school_(id):
    try:
       db.delete_answers_school(id=id)
    except:
        return "Bad"
async def create_answers_school(answers:str=None,telegram_id:str=None,type_test:str=None,class_number:str=None,subject:str=None,code:str=None):
    try:
        id =  db.add_test_school(answers=answers,telegram_id=telegram_id,code=code,type_test=type_test,class_number=class_number,subject=subject)
        return id
         
    except Exception as e:
        print(e)
        pass
async def get_test_school(id):
    try:
        data = db.select_test_school(id=id)
        return data
    except:
        return {}