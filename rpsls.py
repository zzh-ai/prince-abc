#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
����:��־��
����:2019.11.15
"""
import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ��
# 3 - ����
# 4 - ����
print("��ӭʹ��RPSLS��Ϸ")
print("---------------")
print("����������ѡ��:")
player_choice=input()
print("---------------")
if player_choice!="����" and player_choice!="ʯͷ" and player_choice!="��" and player_choice!="����" and player_choice!="ʷ����":
	print("Error:No Crrect Name")
else:
	print("����ѡ��Ϊ:%s"%player_choice)
num=random.randint(0,4)
def name_to_number(num):
	if num==0:
		return("ʯͷ")
	if num==1:
		return("ʷ����")
	if num==2:
		return("��")
	if num==3:
		return("����")
	if num==4:
		return("����")
name_to_number(num)
com_choice=name_to_number(num)
def name_to_number(com_choice):
	if com_choice=="ʯͷ":
		return("0")
	if com_choice=="ʷ����":
		return("1")
	if com_choice=="��":
		return("2")
	if com_choice=="����":
		return("3")
	if com_choice=="����":
		return("4")
name_to_number(com_choice)
print("�������ѡ��Ϊ:%s"%com_choice)
def rpsls(player_choice):
	if player_choice=="ʯͷ" and com_choice=="����":
		print("��Ӯ��!")
	if player_choice=="ʯͷ" and com_choice=="����":
		print("��Ӯ��!")
	if player_choice=="ʯͷ" and com_choice=="��":
		print("����Ӯ��!")
	if player_choice=="ʯͷ" and com_choice=="ʯͷ":
		print("ƽ��!")
	if player_choice=="ʯͷ" and com_choice=="ʷ����":
		print("ƽ��!")
	if player_choice=="��" and com_choice=="ʯͷ":
		print("��Ӯ��!")
	if player_choice=="��" and com_choice=="����":
		print("����Ӯ��!")
	if player_choice=="��" and com_choice=="����":
		print("ƽ��!")
	if player_choice=="��" and com_choice=="��":
		print("ƽ��!")
	if player_choice=="��" and com_choice=="ʷ����":
		print("ƽ��!")
	if player_choice=="����" and com_choice=="��":
		print("��Ӯ��!")
	if player_choice=="����" and com_choice=="ʯͷ":
		print("����Ӯ��!")
	if player_choice=="����" and com_choice=="����":
		print("ƽ��!")
	if player_choice=="����" and com_choice=="ʷ����":
		print("ƽ��!")
	if player_choice=="����" and com_choice=="����":
		print("ƽ��!")
	if player_choice=="����" and com_choice=="ʷ����":
		print("��Ӯ��!")
	if player_choice=="����" and com_choice=="ʯͷ":
		print("����Ӯ��!")
	if player_choice=="����" and com_choice=="����":
		print("ƽ��!")
	if player_choice=="����" and com_choice=="��":
		print("ƽ��!")
	if player_choice=="����" and com_choice=="����":
		print("ƽ��!")
	if player_choice=="ʷ����" and com_choice=="����":
		print("����Ӯ��!")
	if player_choice=="ʷ����" and com_choice=="ʷ����":
		print("ƽ��!")
	if player_choice=="ʷ����" and com_choice=="����":
		print("ƽ��!")
	if player_choice=="ʷ����" and com_choice=="ʯͷ":
		print("ƽ��!")
	if player_choice=="ʷ����" and com_choice=="��":
		print("ƽ��!")
rpsls(player_choice)

