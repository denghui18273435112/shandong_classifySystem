import pytest
from tools.ExcelData import ExcelData
import allure
from tools.caseCheck import caseCheck
from lib.all import all

@allure.epic("山东分类系统")
class Test_all(object):

    @pytest.mark.parametrize("Data",ExcelData("test"))
    def test_ParameterlessAdjustment(self,token_1,token_2,token_3,company_id_1,company_id_2,company_id_3,Data,
                                     year):
        """所有测试用例集合"""
        res =all(token_1=token_1,token_2=token_2,token_3=token_3,company_id_1=company_id_1,company_id_2=company_id_2,company_id_3=company_id_3,inData=Data).\
            ParameterlessAdjustment(year=year)
        caseCheck().case_Check(res[0])