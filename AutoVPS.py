import requests
import time
import json
import os,subprocess
import sqlite3
url = "https://api64.ipify.org/?format=json"

payload={}
headers = {
'Content-Type': 'application/json',
    }

response = requests.request("GET", url, headers=headers, data=payload)
ip = response.json();
print("VPS:"+str(ip['ip']));

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("C:\Cheat sever\Cheat\Database\data.db")
        print("Connect DB success!")
    except:
        print("Lỗi Connect DB!")

    return conn

def delete_task(conn):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM account'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print('Delete account local success!...')

# vòng while check nhiem vụ
while(True):
    try:
        url = "http://accpremium-env.ap-southeast-1.elasticbeanstalk.com/vps/checkresetvps?vps="+str(ip['ip']);
        payload={}
        headers = {
        'Content-Type': 'application/json',
        'Authorization': '1'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json();
        #print('vpsoptine=')
        print("vpsoptine=" + str(data['vpsreset']))
        if(data['vpsreset']==1 or data['vpsreset']==2 or data['vpsreset']=='NULL' ):
            os.system(r'taskkill /im FastExecuteScript.exe /f /T');
            time.sleep(5);
            if(data['vpsreset']==2):
                connnn=create_connection();
                if(connnn!=None):
                    delete_task(connnn);
                # Reset acc server!
                url = "http://accpremiumpostget-env.ap-southeast-1.elasticbeanstalk.com/gmails/resetaccountbyvps?vps="+str(ip['ip']);
                payload={}
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': '1'
                }
                response = requests.request("GET", url, headers=headers, data=payload)
                status = response.json();
                if(status['status']=='true'):
                    print('Delete account server success!...');
                else:
                    print('Delete account server fail!...');

            time.sleep(60);
            print('Start App...')
            #path = "D:/BrowserAutomationStudio/release/APIVerify/"
            #subprocess.call('start','r"D://BrowserAutomationStudio//release//APIVerify//APIVerify.exe"')
            #os.chdir(path)
            #os.system(r"RUN.bat")
            #os.startfile(r"D:\BrowserAutomationStudio\release\APIVerify\RUN.bat")
            #os.system("taskkill /im  C:\\APIVerify\\appsremote\\APIVerify\\SIDebca2406\\engine\\FastExecuteScript.exe /f")
            os.system(r'Start ""  "C:\\Cheat sever\\CheatViewAuto\\RemoteExecuteScriptSilent.exe"')
            #os.system(r'Start ""  "D:\\BrowserAutomationStudio\\release/APIVerify\\RemoteExecuteScriptSilent.exe"')
            #time.sleep(15);
        print('Continue check... 120s')
        time.sleep(120);
    except:
        print("Lỗi API")
        time.sleep(120);
        
        



