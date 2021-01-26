"""
代码做接口自动化测试，基本流程：
1.接口文档--接口测试用例--excel里
2.自动化excel表格读取测试用例数据--得到数据
2.执行测试--requests去执行--执行结果
3.执行结果和预期结果对比 --是否通过 Pass/Failed
4.执行结果写入excel表格中去

注意：从excel表格里读取的数字---文本--字符串
eval():从字符串中获取python表达式
"""
# 导入包  这个文件里的函数都可以使用了
from python_class import api_lesson_06
# 执行测试用例
def execute_fun(filename,sheetname):
    cases = api_lesson_06.read_data(filename, sheetname)  # 调用读取数据函数
    for case in cases:
        case_id=case['case_id']
        url = case.get('url')   # 取url
        data = case['data']     # 取测试参数
        # print(type(data))   str类型
        data = eval(data)   # 从字符串里面获取到python表达式（把引号去掉） --字典
        expected_result = case['expected_result']
        expected_result = eval(expected_result)
        expected_msg = expected_result['msg']
        rel_result = api_lesson_06.api_reg_func(url_api=url, api_data=data)
        rel_msg = rel_result['msg']
        print('真实执行结果：{}'.format(rel_msg))
        print('预期执行结果：{}'.format(expected_msg))
        if rel_msg==expected_msg:
            final_result='Passed'
            print("第{}条测试用例执行通过".format(case_id))
        else:
            final_result = 'Failed'
            print("第{}条测试用例执行不通过".format(case_id))
        api_lesson_06.write_result(filename, sheetname, final_result,case_id+1,8)


execute_fun('test_case_api.xlsx','login')

"""
在已有框架下实现的自动化脚本
完整的自动化框架应该有：
1、基础代码
2、测试数据
3、报告、日志
4、
"""

