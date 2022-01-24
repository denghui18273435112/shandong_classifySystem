import pytest
from tools.ExcelData import ExcelData
import allure
from tools.caseCheck import caseCheck
from lib.all import all
import requests

def setup_module():
    allure.attach(body="TEST-01", name="所有用例执行前，执行一次", attachment_type=allure.attachment_type.TEXT)
def teardown_module():
    allure.attach(body="TEST-06", name="所有用例执行完，执行一次", attachment_type=allure.attachment_type.TEXT)

    #登录
    data = {"type":"I","Name":"zxs-sd","Vcode":"denghui","Pwd":"21ad15b19ad2fcc3ed51c089a8cc39ca"}
    url = "http://60.216.62.188:10263/base/home/Login"
    header = {"Content-Type": "application/json"}
    body = requests.post(url=url,json=data,headers=header)
    token = "{0}={1}".format("cipmcms-token",body.cookies["cipmcms-token"])

        #身份证查询个人信息 删除
        # for x in ["431225199212061818","M30102575","362130197312312425","HO4983324"]:
        #     url1 = "http://sc.maintain.giiatop.com/api/member/DeleteMember"
        #     data1= {"idNumber":"{}".format(x)}
        #     header1 = {"Cookie":token}
        #     body1 = requests.post(url=url1,json=data1,headers=header1)
        #     body1.json()
        #     allure.attach(body=json.dumps(body1.json()), name="身份证查询个人信息查询返回的数据", attachment_type=allure.attachment_type.TEXT)

    #获取列表档案信息档案
    url2 = "http://60.216.62.188:10263/api/member/GetMemberTriningOffline"
    data2= {"year":2022,"className":"","pageNum":1,"pageSize":20,"total":275,"createdTime":[]}
    header2 = {"Cookie":token}
    body2 = requests.post(url=url2,json=data2,headers=header2)
    body2.json()


    #获取需要删除的数据id
    delete_id = []
    len_s= body2.json()["data"]["list"]
    for x  in range(len(len_s)):
        if  len_s[x]["className"] == "自动审核数据":
            delete_id.append(len_s[x]["id"])

    #删除档案数据
    for x  in delete_id:
        url3 = "http://60.216.62.188:10263/api/home/TrainingClear"
        data3= {"ids":[x]}
        header3 = {"Cookie":token}
        body3 = requests.post(url=url3,json=data3,headers=header3)
        body3.json()


@allure.epic("山东分类系统")
class Test_all(object):

    @pytest.mark.parametrize("Data",ExcelData("test_GetDetailList"))
    def test_ParameterlessAdjustment(self,token_1,token_2,token_3,company_id_1,company_id_2,company_id_3,Data,year):
        """所有测试用例集合"""
        res =all(token_1=token_1,token_2=token_2,token_3=token_3,company_id_1=company_id_1,company_id_2=company_id_2,company_id_3=company_id_3,inData=Data).ParameterlessAdjustment(year=year)
        caseCheck().case_Check(res[0])