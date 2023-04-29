import datetime, time


def log_start():
    with open("debug.txt", 'a+', encoding="utf-8") as log:
        log.write("******************************Start******************************\n")
        log.close()


def log_end():
    with open("debug.txt", 'a+', encoding="utf-8") as log:
        log.write("******************************End******************************\n\n")
        log.close()


def file_save(addr, disposition, path):
    # 获取当天日期
    date = str(datetime.date.today())
    file_path = path + addr + "-" + date + ".txt"
    try:
        with open(path + 'temprate.txt', 'w+', encoding="utf-8") as tempfile:  # 写入到临时文件
            tempfile.write(disposition)
            log = "写入到临时文件"
            logs_adding(log)
            tempfile.close()
        log = "开始转存文件"
        logs_adding(log)
        with open('temprate.txt', 'r', encoding="utf-8") as tempfile:  # 读取临时文件
            with open(file_path, 'a+', encoding="utf-8") as file:  # 打开（新建）交换机配置文件
                for line in tempfile.readlines():
                    if line.split():
                        # print(line)
                        file.write(line)
                log = "交换机" + addr + "保存完成\n\n"
                logs_adding(log)
                file.close()
            tempfile.close()
        return log
    except Exception as log:
        logs_adding(log)


def logs_adding(info):
    with open("debug.txt", 'a+', encoding="utf-8") as log:
        log.write(str(datetime.datetime.now()) + '\t\t' + info + '\n')
        log.close()
