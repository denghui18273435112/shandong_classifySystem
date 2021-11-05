import pytest
from tools.ExcelData import ExcelData
import allure
from tools.caseCheck import caseCheck
from lib.all import all

@allure.epic("山东分类系统")
class Test_all(object):

    @pytest.mark.parametrize("Data",ExcelData("qingqiu"))
    def test_ParameterlessAdjustment(self,token,Data):
        """
        所有测试用例集合
        :param token:
        :param Data:
        :return:
        """
        res =all(token,Data).ParameterlessAdjustment()
        caseCheck().case_Check(res[0])