import json
import os
import pickle
import re
import sys

import requests

headers = {
    "accept": "application/vnd.botpy.v1+json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://agent.iyobee.com",
    "referer": "https://agent.iyobee.com/login",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "upgrade-insecure-requests": "1",
}

SESSION_PATH = os.path.join(os.path.dirname(__file__), 'session')
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
# 重试标志
FLAG = 0
# 重试最大次数
MAX_FLAG = 3


def main():
    global FLAG
    if FLAG > MAX_FLAG:
        raise RuntimeError('Exceed The Maximum Number Of Retries')
    if sys.version_info.major < 3:
        raise RuntimeError('Python Version Less Than 3')
    if len(sys.argv) != 2:
        raise RuntimeError('You Must Supply A Phone Number')
    agent_phone = sys.argv[1]
    if FLAG == 0:
        print(f'开始获取手机号{agent_phone}的验证码', end='\n')
    else:
        print('session失效,尝试重新登录', end='\n')
    session = None
    if os.path.exists(SESSION_PATH):
        with open(SESSION_PATH, 'rb') as f:
            try:
                session = pickle.load(f)
            except EOFError:
                pass
    if not session:
        print('正在模拟登录,请耐心等待...', end='\n')
        session = requests.Session()
        session.headers = headers
        session.get('https://agent.iyobee.com/login')
        with open(CONFIG_PATH) as f:
            login_args = json.load(f)
        resp = session.post(
            'https://agent.iyobee.com/login',
            login_args
        )
        if not resp.ok:
            raise RuntimeError('Incorrect Username Or Password, Please Check Your Config File')
        print('登录成功,开始获取验证码')
    resp = session.get(
        f'https://agent.iyobee.com/agent?phone={agent_phone}'
    )
    with open(SESSION_PATH, 'wb') as f:
        redirect = None
        try:
            redirect = resp.json().get('_redirected')
        except json.decoder.JSONDecodeError:
            pass
        if redirect or not resp.ok:
            f.write(b'')
            FLAG += 1
            return main()
        else:
            pickle.dump(session, f)
        f.flush()
    resp.encoding = 'utf-8'
    id_match = re.search(
        r'data-url="/agent/verify_code\?cid=(\d+)',
        resp.text
    )
    if not id_match:
        raise RuntimeError('Invalid Phone Number')
    agent_id = id_match.group(1)
    resp = session.post(
        f'https://agent.iyobee.com/agent/verify_code?cid={agent_id}')
    if not resp.ok:
        raise RuntimeError('获取验证码失败，请删除session文件后重试')
    resp.encoding = 'utf-8'
    return resp.json()['msg']


if __name__ == '__main__':
    try:
        print(main())
    except RuntimeError as e:
        print('*' * 40, file=sys.stderr, end='\n\n')
        print(' Error:', file=sys.stderr, end=' ')
        print(e.args[0], file=sys.stderr, end='\n\n')
        print('*' * 40, file=sys.stderr, end='\n')
