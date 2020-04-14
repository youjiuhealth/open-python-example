#!/usr/bin/python3
# coding:utf-8
import requests
import json

class ApiDemo:

	"""基本属性"""
	app_id = ''
	app_secret = ''
	tocken = ''
	base_url = 'https://open.youjiuhealth.com/api'
	access_token = ''

	"""构造函数"""
	def __init__(self,app_id,app_secret):
		self.app_id = app_id
		self.app_secret = app_secret
		print(app_id,app_secret)

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

	"""发起Get请求"""
	def getData(self,path,query={}):
		# 消息头数据
		headers = {
			'Authorization': 'Bearer '+self.getTocken(),
			'accept':'application/vnd.XoneAPI.v2+json'
		}
		return requests.get(self.base_url + path,data=query,headers=headers)

 
# 实例化类
app_id = '***********'
app_secret = '********************************************'
api = ApiDemo(app_id,app_secret)

# 获取token
#+-----------------------------------------------------------------------
#ret = api.getTocken()
#print(ret)

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
measurementId = 24465276;

# 获取报告详情
#+-----------------------------------------------------------------------
#ret = api.getReportsDetail(measurementId)
#print(ret.json())


# 获取报告详情
#+-----------------------------------------------------------------------
ret = api.getMiniProgramCode(measurementId)
print(ret.json())










