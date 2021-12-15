#-*- conding:utf-8 -*-
#@File      :all.py
#@Time      : 18:44
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import json
import os
import requests
from configs.conf import *
from configs.path import test_xlsx
from tools.update_data import update_data
import datetime
from tools.allureUitl import alluer_new
from tools.md5Uitl import get_md5
from tools.commonly_method import *
from tools.Base import *

class all:
    """
    所有模块
    """
    def __init__(self,token_1,token_2,token_3,company_id_1,company_id_2,company_id_3,inData,conftest=True):
        self.token_1 = token_1
        self.token_2 = token_2
        self.token_3 = token_3
        if "test_ImportMemberTraining_01" in inData["case_id"]\
                or "test_SavePlanEx_01" in inData["case_id"]:
            self.header = {"Cookie":token_2}
        else:
            self.header = {"Cookie":token_1}
        self.proxies = {"http":"http://127.0.0.1:8888"}
        self.inData = inData
        self.new_url= url+inData["url"]
        self.data = json.loads(inData["params"])
        self.conftest=conftest
        self.company_id_1 = company_id_1
        self.company_id_2 = company_id_2
        self.company_id_2 = company_id_3

    def ParameterlessAdjustment(self,year=None):

         #替换字段值；如日期、年份、公司id
        if isinstance(self.data,list):
            pass
        else:
            for key in self.data.keys():
                if key == "plan_year" or key == "training_year" or key == "year":
                    if "test_companyimportauditGetList_01" in self.inData["case_id"]:
                        self.data[key] = year-1
                    else:
                        self.data[key] = year
                if key == "company_id" or key == "companyId" or key == "instid":
                    self.data[key] = self.company_id_1
                if key == "pageNum":
                    self.data[key] = 1
                if key == "pageSize":
                    self.data[key] = 20
                if key == "start_date":
                    self.data[key] = "{}-01-01".format(date_YmdHMS(5))
                if key == "end_date" :
                    self.data[key] = "{}".format(date_YmdHMS(4))
                if key == "date" or key == "created_time":
                    if "test_GetTrendChart_01"  in self.inData["case_id"] \
                            or "test_GetStatisList"  in self.inData["case_id"]\
                            or "test_memberqualificationGetList_02"  in self.inData["case_id"]:
                        pass
                    else:
                        self.data[key][0] = "{}-01-01".format(date_YmdHMS(5))
                        self.data[key][1] = "{}".format(date_YmdHMS(4))


        #接口操作具有依耐性
        if "test_adminuserAdd_03" in self.inData["case_id"]:
            id = requests_zzl("case_adminuserList_03",token_1=self.token_1,company_id_1=self.company_id_1,year=year)["data"]["list"][0]["id"]
            self.data["ids"].append(id)
        if "case_GetTestDetail_03" in self.inData["case_id"]:
            body = requests_zzl("case_GetTestDetail_02",self.token_1)
            self.data["member_id"] = body["data"]["list"][0]["member_id"]
            self.data["detailId"] = body["data"]["list"][0]["year_test_id"]
        if "test_GetCompanyTestSum_02" in self.inData["case_id"]:
            self.data["id"] = requests_zzl("test_GetCompanyTestSum_01",token_1=self.token_1,company_id_1=self.company_id_1,year=year)["data"]["list"][0]["companyId"]
        if "test_ImportMemberTraining_03" in self.inData["case_id"]:
            id = requests_zzl("test_ImportMemberTraining_02",token_1=self.token_1,company_id_1=self.company_id_1,year=year)["data"]["list"][0]["id"]
            self.data["ids"].append(id)


         #需要导入表格的操作
        request_file = None
        if self.inData["case_id"] == "case_GetTestDetail_04":
            request_file = {'file': (excel_08_name,open(excel_08,"rb"), file_application)}
        if self.inData["case_id"] == "test_ImportMemberTraining_01":
            request_file = {'file': (excel_01_name,open(excel_01,"rb"), file_application)}


        #区分是否上传文件；请求
        if "case_GetTestDetail_04" in self.inData["case_id"]\
                or "test_ImportMemberTraining_01" in self.inData["case_id"]:
            body = requests.post(url=self.new_url, headers=self.header, data=self.data,files=request_file)
        else:
            body = requests.post(url=self.new_url, headers=self.header, json=self.data)


        #打印,生成报告
        if self.conftest==True:
            print("\n\n"+self.inData["case_id"]+"-"+self.inData["case_name"])
            print(self.inData)
            print(self.data)
            print(self.new_url)
            print(self.header)
            print(body.json())
            print(self.inData)
            print(json.loads(self.inData["response_expect_result"]))
            print(self.conftest)
        inData = update_data(self.inData,self.data,self.new_url,self.header,body.json(),json.loads(self.inData["response_expect_result"]),self.conftest)
        return inData,body




