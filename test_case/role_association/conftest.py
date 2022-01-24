import pytest
from configs.path import *
from lib.all import *
from tools.ExcelData import ExcelData
from tools.verification_code import verification_code
from tools.commonly_method import *

@pytest.fixture(scope="session",autouse=True)
def empty_report_file():
    """清空report-result文件夹,除environment.properties以外的其它所有文件"""
    try:
        for one in os.listdir(result_path):
            if "environment.properties" not in one:
                os.remove(result_path+os.sep+"{}".format(one))
    except:
        pass

@pytest.fixture(scope="session")
def token_1():
    """省协会登录；返回token"""
    return login("login-001")

@pytest.fixture(scope="session")
def token_2():
    """省公司登录；返回token"""
    return login("login-002")

@pytest.fixture(scope="session")
def token_3():
    """市公司登录；返回token"""
    return login("login-003")

@pytest.fixture(scope="session")
def company_id_1(token_1):
    """获得省协会公司id"""
    return  requests_zzl("test_GetCurrentAllCompany_01",token_1)["data"][0]["id"]

@pytest.fixture(scope="session")
def company_id_2(token_2):
    """获得省公司id"""
    return  requests_zzl("test_GetCurrentAllCompany_01",token_2)["data"][0]["id"]

@pytest.fixture(scope="session")
def company_id_3(token_3):
    """获得省协会公司id"""
    return  requests_zzl("test_GetCurrentAllCompany_01",token_3)["data"][0]["id"]

@pytest.fixture(scope="session")
def year(token_1):
    """获得年份"""
    return  requests_zzl("test_GetYear_01",token_1)["data"][0]











