# !/usr/bin/python
# -*- encoding: utf-8 -*-
import time, pytest
from conf.projectpath import *

now = time.strftime('%Y-%m-%d__%H-%M-%S')
htmlReportFile_path = '--html=' + test_report + '/report' + now + '.html'
allure_path = test_report + '/report/allure/' + now
allureFile_path = '--alluredir=' + allure_path
allure_report = test_report + '/report/allure_report'
# junitxmlFile_path ='--html='+ htmlreport_dir + '/report' + now +'.xml'
# pytest.main(["-s","-v","--html=Outputs/reports/pytest.html","--alluredir=Outputs/allure"])

#pytest.main(['-s', '-v', '-m', 'flyback', htmlReportFile_path, allureFile_path, testcases_path + '/test_case.py'])

pytest.main(['-m','flyback', htmlReportFile_path,testcases_path+'/test_case.py'])
#os.system("allure generate " + allure_path + " -o " + allure_report + ' --clean')
# os.system("allure generate "+allure_path+" -o "+allure_report+' --clean')
# os.system("allure open -h 127.0.0.1 -p 8083 {0}".format(allure_path))
