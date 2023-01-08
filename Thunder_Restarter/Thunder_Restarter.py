import psutil
import time
import os

file_name = '%s.txt' % time.strftime("%Y-%m-%d", time.localtime())

def get_now_time():
    """
    获取当前日期时间
    :return:当前日期时间
    """
    now = time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
    return now_time

def getNet():
    sent_before = psutil.net_io_counters().bytes_sent  # 已发送的流量
    recv_before = psutil.net_io_counters().bytes_recv  # 已接收的流量
    time.sleep(1)
    sent_now = psutil.net_io_counters().bytes_sent
    recv_now = psutil.net_io_counters().bytes_recv
    sent = (sent_now - sent_before)/1024  # 算出1秒后的差值
    recv = (recv_now - recv_before)/1024
    # print(time.strftime(" [%Y-%m-%d %H:%M:%S] ", time.localtime()))
    # print("上传：{0}KB/s".format("%.2f"%sent))
    # print("下载：{0}KB/s".format("%.2f"%recv))
    # print('-'*32)
    return recv

if __name__ == "__main__":
    index = 0
    while 1:
        # 3000是当前PC的下载网速
        if getNet() < 3000:
            index += 1
            if index == 10:
                os.system('echo aaa')
                os.system(r'.\Thunder_Restarter.bat')
                now_time = get_now_time()
                f_log = open(r'.\log\%s' % file_name, 'a')
                f_log.write(now_time + '\n')
                f_log.close()
                index = 0
                time.sleep(60 * 5)
        else:
            if index > 0:
                index = -1
        time.sleep(60)
