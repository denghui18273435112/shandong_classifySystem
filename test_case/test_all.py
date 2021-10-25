import pytest
from tools.ExcelData import ExcelData
import allure
from tools.caseCheck import caseCheck
from lib.all import all

@allure.epic("山东分类系统")
class Test_all(object):

    @pytest.mark.parametrize("Data",ExcelData("Parameterless-adjustment"))
    def test_ParameterlessAdjustment(self,token,Data,company,year,training_program_id,training_program_name,
                                     role,account_name,delete_account_id):
        """
        所有测试用例集合
        :param token:
        :param Data:
        :return:
        """
        res =all(token,Data).ParameterlessAdjustment(company=company,year=year,training_program_id=training_program_id,
                                                     training_program_name=training_program_name,delete_account_id=delete_account_id)
        caseCheck().case_Check(res[0])