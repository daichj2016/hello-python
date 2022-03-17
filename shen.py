# -*- coding: UTF-8 -*-
import requests
import json
import random
import time


server = ""
account = ''
password = ''
token = 0
vip = 0
game_url = 'http://bzws-s'+server+'.game.zhanyougame.com'
sum = 0


#登陆
def login(account, password):
	login_url = game_url+"/index.php?v=0&c=login&&m=user"
	data = {"u":account,"p":password}
	reponse = requests.post(login_url,data)
	json_data = reponse.text
	dict_data = json.loads(json_data)
	return dict_data
def get_nickname(token):
	url = game_url+"/index.php?v=0&c=member&&m=index"
	data = {"token":token}
	reponse = requests.post(url,data)
	json_data = reponse.text
	dict_data = json.loads(json_data)
	return dict_data['nickname']

def shenjiang_log(token):
	url = game_url+"/index.php?v=0&c=tavern&&m=get_list"
	data = {"token":token,"tab":4}
	reponse = requests.post(url,data)
	json_data = reponse.text
	dict_data = json.loads(json_data)
	return dict_data



token = login(account, password)['token']
nickname = get_nickname(token)
print("当前角色名为： "+nickname)
info = shenjiang_log(token)
shenjiang = info['list']
all_zi = 0
all_shengwang = 0
for i in range(1,len(shenjiang)):
	#print(shenjiang[str(i)]['price'],shenjiang[str(i)]['paytype'],shenjiang[str(i)]['isown'])
	isown = shenjiang[str(i)]['isown']
	if (not isown) and int(shenjiang[str(i)]['paytype']) == 3:
		#print(shenjiang[str(i)]['price'],"紫宝石")
		all_zi += int(shenjiang[str(i)]['price'])
		all_shengwang += int(shenjiang[str(i)]['need_reputation'])
print("还需要 "+str(all_zi)+" 紫宝石")
print("还需要 "+str(all_shengwang)+" 声望")
