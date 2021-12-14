import os
current =os.path.abspath(__file__)                          #当前文件的路径
BASE_DIR = os.path.dirname(os.path.dirname(current))        # 当前项目的绝对路径

#文件夹路径
config_path = BASE_DIR +os.sep+"config"
log_path = BASE_DIR +os.sep+"logs"
data_path =BASE_DIR +os.sep+"docs"
file_path =BASE_DIR +os.sep+"file"
report_path =BASE_DIR +os.sep+"report"
testcase_path =BASE_DIR +os.sep+"test_case"
result_path = report_path+os.sep+"result"
allure_reportt_path = report_path+os.sep+"allure_report"
screenshots_path = file_path+os.sep+"screenshots"
file_data =BASE_DIR +os.sep+"data"
report_file  = file_data+os.sep+"01常规导入"
report_file_1  = file_data+os.sep+"02流程操作"

#文件路径
_config_file = config_path +os.sep+"conf.yaml"            #定义conf.yaml的路径
_yonglie_file = config_path +os.sep+"yonglie.yaml"            #定义conf.yaml的路径
_db_config_file = config_path +os.sep+"db_conf.yaml"     #定义db_conf.yaml的路径
test_xlsx = data_path+os.sep+"ctest.xlsx"

#上传文件
file_application = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

#导入文件
excel_08_name = "08培训测评批量查询模板.xlsx"
excel_08 = report_file +os.sep+excel_08_name

excel_01_name = "01山东保险从业人员分级分类执业培训记录汇总表导入模板(寿险).xlsx"
excel_01 = report_file_1 +os.sep+excel_01_name