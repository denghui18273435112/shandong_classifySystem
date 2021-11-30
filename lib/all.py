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

class all:
    """
    所有模块
    """
    def __init__(self,token,inData,conftest=True):
        self.header = {"Cookie":token}
        self.proxies = {"http":"http://127.0.0.1:8888"}
        self.inData = inData
        self.new_url= url+inData["url"]
        self.data = json.loads(inData["params"])
        self.conftest=conftest

    def ParameterlessAdjustment(self,company=None,year=None,number_id=None,role=None,account_name=None,
                                training_program_id=None,training_program_name=None,delete_account_id=None):
        """
        所有测试用例集合
        :return:
        """
        if "Parameterless-adjustment--" in self.inData["case_id"]:
            pass

        #学员详情#
        if "Parameterless-adjustment-11" in self.inData["case_id"]:
            if "Parameterless-adjustment-1100" in self.inData["case_id"]:
                self.data["company_id"] = company
                self.data["plan_year"] = year
            if "Parameterless-adjustment-11107" in self.inData["case_id"]:
                self.data["number_id"] = number_id

        #培训计划报送#
        if "Parameterless-adjustment--445" in self.inData["case_id"]:
            if "Parameterless-adjustment--44--01" in self.inData["case_id"]:
                for x in range(len(self.data)):
                    self.data[x]["companyId"] = company
                    IncrNumber = 0
                    stockNumber = 0
                    for y in range(10):
                        self.data[x]["c{}Incr".format(y+1)] = random.randint(1,100)
                        IncrNumber +=self.data[x]["c{}Incr".format(y+1)]
                        self.data[x]["c{}Stock".format(y+1)] = random.randint(25,50)
                        stockNumber +=self.data[x]["c{}Stock".format(y+1)]
                    self.data[x]["stockNumber"] = IncrNumber
                    self.data[x]["incrNumber"] = stockNumber
                    self.data[x]["remark"] = "自动化接口数据"
                    self.data[x]["planYear"] = year
                    remainder = (stockNumber+IncrNumber)%4
                    average_score = (stockNumber+IncrNumber)//4
                    for z in range(4):
                        self.data[x]["quarter{}Number".format(z+1)]=average_score
                        if remainder !=0 and z==0:
                            self.data[x]["quarter{}Number".format(z+1)] += remainder
            if "Parameterless-adjustment--44--003"  in inData["case_id"]:
                data["company_id"] = company
                data["plan_year"] = year

        #首页-数字概览#
        if "Parameterless-adjustment-333-" in self.inData["case_id"]:
            self.data["company_id"] = company
            self.data["plan_year"] = year

        #首页-公司数据#
        if "Parameterless-adjustment-222-" in self.inData["case_id"]:
            self.data["company_id"] = company
            self.data["plan_year"] = year

        #培训记录导入#
        if "Parameterless-adjustment-11111-001" in self.inData["case_id"]:
            request_file = {'file':('ctest.xlsx',open(test_xlsx,"rb"))}
            self.data["class_date_end"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #获取培训课程#
        if "Parameterless-adjustment-314983" in self.inData["case_id"]:
            self.data["company_id"] = company
            self.data["plan_year"] = year

        #大纲明细#
        if "Parameterless-adjustment-921206" in self.inData["case_id"]:
            if "Parameterless-adjustment-921206-001" in self.inData["case_id"]:
                self.data["courseId"] = training_program_id
            if "Parameterless-adjustment-921206-002" in self.inData["case_id"]:
                self.data["courseId"] = training_program_id
                self.data["module"].append(training_program_name)

        #列表账号管理数据#
        if "Parameterless-adjustment-account_list-00" in self.inData["case_id"]:
            self.data["kw"] ="denghui008"
            self.data["companyId"]=company

        #账号添加#
        if "Parameterless-adjustment-account_add-00" in self.inData["case_id"]:
            if "Parameterless-adjustment-account_add-003" not in self.inData["case_id"]:
                self.data["companyId"] = company
            if "Parameterless-adjustment-account_add-004" not in self.inData["case_id"]:
                self.data["roles"]=[]
                self.data["roles"].append(role)
            if "Parameterless-adjustment-account_add-005" not in self.inData["case_id"]:
                self.data["pwd"] = get_md5(self.data["name"])
            if "Parameterless-adjustment-account_add-006" in self.inData["case_id"]:
                self.data["name"] =self.data["name"]+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                self.data["nickName"] =self.data["nickName"]+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                self.data["pwd"] = get_md5(self.data["name"])
            if "Parameterless-adjustment-account_add-007" in self.inData["case_id"]:
                self.data["name"] =self.data["name"]+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                self.data["nickName"] =self.data["nickName"]+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                self.data["pwd"] = get_md5(self.data["name"])

         #账号删除#
        if "Parameterless-adjustment-account_delete-001" in self.inData["case_id"]:
            self.data["ids"] =delete_account_id

        #接口请求;更新inData的数据;并生成allure报告 Parameterless-adjustment-account_list-00
        print(self.inData["case_id"]+"-"+self.inData["case_name"])
        print(self.new_url)
        print(self.header)
        print(self.data)
        print("\n")

        body = requests.post(url=self.new_url,headers=self.header,json=self.data)
        inData = update_data(self.inData,self.data,self.new_url,self.header,body.json(),json.loads(self.inData["response_expect_result"]),self.conftest)
        return inData,body







