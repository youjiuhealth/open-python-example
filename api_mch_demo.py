#!/usr/bin/python3
# coding:utf-8
import requests
import json

class ApiMchDemo:

	"""基本属性"""
	app_id = ''
	app_secret = ''
	tocken = ''
	base_url = 'https://open.youjiuhealth.com/mch/v3'
	access_token = ''

	"""构造函数"""
	def __init__(self,app_id,app_secret):
		self.app_id = app_id
		self.app_secret = app_secret
		# print(app_id,app_secret)

	"""获取token"""
	def getTocken(self):
		# 判断是否存在未过期的token
		# ...
		
		# 不存在则重新获取并缓存
		query = {
			'app_id':self.app_id,
			'app_secret':self.app_secret
		}
		ret = requests.post(self.base_url+'/session',data=query)
		print(ret)
		json_data=json.loads(ret.text)
		return json_data.get('access_token')
		
	"""获取报告列表"""
	def getReportsList(self,query):
		return self.getData('/reports',query)
		
	"""获取报告详情"""
	def getReportsDetail(self,id):
		return self.getData('/reports/'+ str(id))
		
	"""获取小程序码"""
	def getMiniProgramCode(self,id):
		return self.getData('/reports/'+ str(id) +'/miniProgramCode')
	
	"""获取商家列表"""
	def getClients(self,query):
		return self.getData('/clients',query)
					
	"""获取商家设备列表"""
	def getClientDevices(self,client_id):
		return self.getData('/clients/'+ str(client_id) +'/devices')

	"""发起Get请求"""
	def getData(self,path,query={}):
		# 消息头数据
		headers = {
			'Authorization': 'Bearer '+self.getTocken()
		}
		return requests.get(self.base_url + path,data=query,headers=headers)

 
# 实例化类
app_id = '***********'
app_secret = '********************************************'
api = ApiMchDemo(app_id,app_secret)

# 获取token
#+-----------------------------------------------------------------------
ret = api.getTocken()
print(ret)

# 获取报告列表
#+-----------------------------------------------------------------------
query = {
	#'phone':'',
	#'device_sn':'',
	'page':1
}
#ret = api.getReportsList(query)
#print(ret.json())

# 报告ID
measurementId = 38348130;

# 获取报告详情
#+-----------------------------------------------------------------------
#ret = api.getReportsDetail(measurementId)
#print(ret.json())


# 获取报告详情
#+-----------------------------------------------------------------------
#ret = api.getMiniProgramCode(measurementId)
#print(ret.json())


# 获取商家列表
#+-----------------------------------------------------------------------
query = {
	'page':1
}
ret = api.getClients(query)
print(ret.json())


# 获取商家设备列表
#+-----------------------------------------------------------------------
client_id = 3225414
#ret = api.getClientDevices(client_id)
#print(ret.json())









