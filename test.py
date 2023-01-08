# 复制BT种子调取迅雷
# from win32com.client import Dispatch
#
# o = Dispatch("ThunderAgent.Agent64.1")
#
# url = '' # 需要下载的链接地址
# filename = '' # 保存的文件名称
# o.AddTask(url, filename)
# o.CommitTasks()


# 调取迅雷 获得文件夹目录下的所有文件
import os

# listdirall_file_name = 'listdirall.txt'
#
# def file_name_walk(file_dir):
#     f_log = open(r'.\log\%s' % listdirall_file_name, 'a', encoding='utf-8')
#     for root, dirs, files in os.walk(file_dir):
#         # print("root", root)  # 当前目录路径
#         # print("dirs", dirs)  # 当前路径下所有子目录
#         # print("files", files)  # 当前路径下所有非目录子文件
#         f_log.write(str(files) + '\n')
#     f_log.close()
#
# file_name_walk("F:\迅雷下载")

