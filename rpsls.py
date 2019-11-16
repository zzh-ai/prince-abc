#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者:邹志宏
日期:2019.11.15
"""
import random
# 0 - 石头
# 1 - 史波克
# 2 - 布
# 3 - 蜥蜴
# 4 - 剪刀
print("欢迎使用RPSLS游戏")
print("---------------")
print("请输入您的选择:")
player_choice=input()
print("---------------")
if player_choice!="剪刀" and player_choice!="石头" and player_choice!="布" and player_choice!="蜥蜴" and player_choice!="史波克":
	print("Error:No Crrect Name")
else:
	print("您的选择为:%s"%player_choice)
num=random.randint(0,4)
def name_to_number(num):
	if num==0:
		return("石头")
	if num==1:
		return("史波克")
	if num==2:
		return("布")
	if num==3:
		return("蜥蜴")
	if num==4:
		return("剪刀")
name_to_number(num)
com_choice=name_to_number(num)
def name_to_number(com_choice):
	if com_choice=="石头":
		return("0")
	if com_choice=="史波克":
		return("1")
	if com_choice=="布":
		return("2")
	if com_choice=="蜥蜴":
		return("3")
	if com_choice=="剪刀":
		return("4")
name_to_number(com_choice)
print("计算机的选择为:%s"%com_choice)
def rpsls(player_choice):
	if player_choice=="石头" and com_choice=="剪刀":
		print("您赢了!")
	if player_choice=="石头" and com_choice=="蜥蜴":
		print("您赢了!")
	if player_choice=="石头" and com_choice=="布":
		print("机器赢了!")
	if player_choice=="石头" and com_choice=="石头":
		print("平局!")
	if player_choice=="石头" and com_choice=="史波克":
		print("平局!")
	if player_choice=="布" and com_choice=="石头":
		print("您赢了!")
	if player_choice=="布" and com_choice=="剪刀":
		print("机器赢了!")
	if player_choice=="布" and com_choice=="蜥蜴":
		print("平局!")
	if player_choice=="布" and com_choice=="布":
		print("平局!")
	if player_choice=="布" and com_choice=="史波克":
		print("平局!")
	if player_choice=="剪刀" and com_choice=="布":
		print("您赢了!")
	if player_choice=="剪刀" and com_choice=="石头":
		print("机器赢了!")
	if player_choice=="剪刀" and com_choice=="蜥蜴":
		print("平局!")
	if player_choice=="剪刀" and com_choice=="史波克":
		print("平局!")
	if player_choice=="剪刀" and com_choice=="剪刀":
		print("平局!")
	if player_choice=="蜥蜴" and com_choice=="史波克":
		print("您赢了!")
	if player_choice=="蜥蜴" and com_choice=="石头":
		print("机器赢了!")
	if player_choice=="蜥蜴" and com_choice=="蜥蜴":
		print("平局!")
	if player_choice=="蜥蜴" and com_choice=="布":
		print("平局!")
	if player_choice=="蜥蜴" and com_choice=="剪刀":
		print("平局!")
	if player_choice=="史波克" and com_choice=="蜥蜴":
		print("机器赢了!")
	if player_choice=="史波克" and com_choice=="史波克":
		print("平局!")
	if player_choice=="史波克" and com_choice=="剪刀":
		print("平局!")
	if player_choice=="史波克" and com_choice=="石头":
		print("平局!")
	if player_choice=="史波克" and com_choice=="布":
		print("平局!")
rpsls(player_choice)

