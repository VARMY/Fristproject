'''
passline：通关分数
val:分数
'''

#
# def set_passline(passline):
# 	def func(val):
# 		if val >= passline:
# 			print("%d pass"%val)
# 		else:
# 			print("Failed")
# 	return func
#
# func_100 = set_passline(60)
# func_100(70)
# func_150 = set_passline(90)
# func_150(99)

dict={'你好':'aaaa'}
import pymongo
db=pymongo.MongoClient()
db1=db['111']['222']
db1.insert(dict)