import pytest
from configs.conf_path import *
from lib.all import *
from lib.login import login
from tools.ExcelData import ExcelData
from configs.login_token import login_token

@pytest.fixture(scope="session",autouse=True)
def empty_report_file():
    """
    清空report-result文件夹,除environment.properties以外的其它所有文件
    :param request:
    :return:
    """
    try:
        for one in os.listdir(result_path):
            if "environment.properties" not in one:
                os.remove(result_path+os.sep+"{}".format(one))
    except:
        pass

@pytest.fixture(scope="session")
def token():
    """
    获取登录token
    省公司登陆
    :return:
    """
    return  login.login(ExcelData("login-001")[0],conftest=False)
    #return  login_token

@pytest.fixture(scope="session")
def token_city():
    """
    获取登录token
    地市公司登陆
    :return:
    """
    return  login.login(ExcelData("login-002")[0],conftest=False)

@pytest.fixture(scope="session")
def role(token):
    """
    获取角色列表
    :param token:
    :return:
    """
    body = all(token=token,inData=ExcelData("Parameterless-adjustment-874455")[0],conftest=False).ParameterlessAdjustment()
    return body[1].json()["data"][2]["id"]

@pytest.fixture(scope="session")
def company(token):
    """
    省公司
    获取当前账号登录的所属公司id
    :param token:
    :return:
    """
    res = all(token=token,inData=ExcelData("Parameterless-adjustment--001")[0],conftest=False).ParameterlessAdjustment()
    return res[1].json()["data"]["instid"]

@pytest.fixture(scope="session")
def company_city(token_city):
    """
    地市公司
    获取当前账号登录的所属公司id
    :param token:
    :return:
    """
    res =  all(token_city=token_city,inData=ExcelData("Parameterless-adjustment--001")[0],conftest=False).ParameterlessAdjustment()
    return res[1].json()["data"]["instid"]

@pytest.fixture(scope="session")
def account_name(token,company):
    """
    获取账号列表，第一行的账号名称
    :param token:
    :param company:
    :param Data:
    :return:
    """
    res = all(token=token,inData=ExcelData("account_list-001")[0],conftest=False).ParameterlessAdjustment(company=company)
    return  res[1].json()["data"]["list"][0]["nickName"]

@pytest.fixture(scope="session")
def delete_account_id(token,company,role,account_name="无"):
    """
    以列表的形式返回需要删除的id；
    通过校验名称和昵称获取id
    :param token:
    :param company:
    :param role:
    :return:
    """
    res = all(token=token,inData=ExcelData("account_list-001")[0],conftest=False).ParameterlessAdjustment(company=company,account_name=account_name)[1].json()
    del_list = []
    for x in range(int(len(res["data"]["list"]))):
        name = res["data"]["list"][x]["name"]
        nickName = res["data"]["list"][x]["nickName"]
        if  name!=None  or nickName!=None:
            if "test00123" in name or  "test00123" in nickName:
                del_list.append(res["data"]["list"][x]["id"])
    return  del_list

@pytest.fixture(scope="session")
def year(token):
    """
    获取年份
    :param token:
    :return:
    """
    res =all(token=token,inData=ExcelData("Parameterless-adjustment-10004")[0],conftest=False).ParameterlessAdjustment()
    return  res[1].json()["data"][0]

@pytest.fixture(scope="session")
def number_id(token,company,year):
    """
    获取成员的member_id
    :param token:
    :return:
    """
    res =all(token=token,inData=ExcelData("Query_students-001")[0],conftest=False).student_details_list(company=company,year=year)
    return  res[1].json()["data"]["list"][0]["member_id"]

@pytest.fixture(scope="session")
def training_program_id(token,company,year):
    """
    获取当年培训类型id
    :param token:
    :return:
    """
    res =all(token=token,inData=ExcelData("Parameterless-adjustment-314983")[0],conftest=False).ParameterlessAdjustment(company=company,year=year)
    return  res[1].json()["data"]["type"][0]["course_id"]

@pytest.fixture(scope="session")
def training_program_name(token,training_program_id):
    """
    获取当年培训类型的名称
    :param token:
    :return:
    """
    res =all(token=token,inData=ExcelData("Parameterless-adjustment-921206-001")[0],conftest=False).ParameterlessAdjustment(training_program_id=training_program_id)
    return  res[1].json()["data"][1]
