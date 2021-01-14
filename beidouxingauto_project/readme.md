#使用说明
common 文件夹用来存放 一些公共的方法的和类
    -config_handler 读取配置文件,在该项目中没有使用
    -log_handler 解析日志配置文件
    -read_exlce 读取excle文件
    - report_handler 配置测试报告文件
    - request_handler 处理和发送请求的文件
config:用来存放指定的配置文件
libs:用来存放第三方库和插件
log:用来存放系统的日志
reports:用户存放生成的测试报告
testcases:用来存放测试用例
    -一个接口一个测试文件，测试py文件亿test开头，test*.py
    - 测试用例类一定要继承unittest.TestCase
    - 测试方法一定要以test开头
        1.测试数据
        2.测试步骤
        3.断言  
testdata:用来存放测试数据
main:程序的执行入口
setting:用户存放配置文件 可以简化读取文件配置文件的操作 
在python中一般使用.py的作为一个配置文件，在本项目中使用的
也是该文件作为配置文件