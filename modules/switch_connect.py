import telnetlib
from modules.file_handing import *
import re


def telnetsw(ip, username, password, cmd):
    # 连接Telnet交换机
    # print(ip, username, password, cmd)
    tn = telnetlib.Telnet(ip, port=23, timeout=50)  # 创建telnet对象
    # cmd = bytes(cmd.encode())
    try:
        log = "尝试登录中"
        logs_adding(log)

        # 模拟输入登录用户名
        # tn.read_until(b"Username:",timeout=3)
        time.sleep(1)
        tn.write(bytes(username.encode()) + b'\n')
        # 模拟输入登录密码
        tn.read_until(b'Password:')

        tn.write(bytes(password.encode()) + b'\n')

        time.sleep(1)
        res = tn.read_very_eager().decode()
        login_success = re.compile('<(.*)>')  # 创建登录成功的匹配对象
        # print(res)
        des = ''
        if login_success.search(res):  # 在返回的配置中匹配登录成功的对象
            log = "登录成功，准备输入" + str(cmd) + "命令"
            logs_adding(log)

            time.sleep(1)
            # print(bytes(cmd.encode()))
            tn.write(bytes(cmd.encode()) + b'\n')  # 输入命令
            # tn.write(b'display cur' + b'\n')
            break_flag = True
            # while not login_success.search(res):
            while break_flag:
                tn.write(b" ")  # 模拟敲空格使配置完整显示
                time.sleep(0.1)
                # print(res)
                res = tn.read_very_eager().decode()  # 获得结果
                if login_success.search(res):
                    break_flag = False
                des = des + res
            # print(des)
            log = "获取配置成功"
            logs_adding(log)
            # print(res)

            # 命令执行完毕后，终止Telnet连接（或输入exit退出）
            tn.close()  # tn.write('exit\n')
            log = "关闭telnet连接"
            logs_adding(log)

        else:  # 在返回的配置中匹配登录失败的对象
            log = "登录失败，未知错误"
            logs_adding(log)
        # res = tn.read_very_eager().decode()
        # print(res)
        return des, log

    except Exception as e:
        print(e)
        logs_adding(e)
        return str(e)
