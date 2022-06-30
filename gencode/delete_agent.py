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

D_AGENT_IDS = [
    [3007106163, 8492776261, 6838507054, 4034072093, 8001912689, 8390817815,
     6397981182, 1555872803, 4084735375, 6251418012, 7583424395],
    [2197715224, 6175085972, 8202284681, 7859092872, 6060648786, 7168737356,
     3719918628, 6839732132, 5635042104, 2586185041, 6433765447, 7150948433,
     9137517391, 4247471093, 6714645251, 7196175066, 3767639803, 9412212076,
     1024333594],
    [1061439626, 3108161808, 7278448789, 6372835770, 5589779679, 6248184242,
     5243494691, 7091220404, 7745934133, 7904753784, 3060065126, 4147009862,
     5706565973, 2771114267, 8272336324, 6737631248, 8688656511, 3522740894,
     3143025496, 8949818145, 9565201129, 3901952176, 1345478313, 6853719528,
     5458494770, 1841985405, 2091138180, 8743065284, 3951518897, 8181963224,
     7040895291, 3609629466, 9843656362, 9750165784, 6496281761, 9768223800,
     1673400621, 9332550274, 5712026670, 4987115379, 6270584417, 2232730885,
     5094055868, 7853958417, 6461468741, 1282184901, 6315993619, 8419056243,
     2075112457, 8846113280, 5186742356, 3186294340, 7829386640, 6547847885,
     5878631513, 9317366929, 3873246908, 9956304312, 4908809767, 9999814410,
     8857677502, 8367864275, 6333885691], [5360471762], [5767988228], [1501199119],
    [3077127824, 8602743671]
]


def main():

    with requests.Session() as session:
        print('正在模拟登录,请耐心等待...', end='\n')
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
        print('登录成功,开始删除')
        for agent_ids in D_AGENT_IDS[::-1]:
            for agent_id in agent_ids:
                resp = session.delete(
                    f'https://agent.iyobee.com/agents/{agent_id}?reason=因王凯邀请删除'
                )
                if not resp.ok:
                    print(f"删除代理人{agent_id}成功",end="\n")
                    print(f"删除代理人{agent_id}成功",end="\n", file=file)
                else:
                    print(f"删除代理人{agent_id}失败{resp}",end="\n")
                    print(f"删除代理人{agent_id}失败{resp}", end="\n", file=file)


if __name__ == '__main__':
    file = open("delete.log", "w")
    try:
        main()
    except RuntimeError as e:
        print('*' * 40, file=sys.stderr, end='\n\n')
        print(' Error:', file=sys.stderr, end=' ')
        print(e.args[0], file=sys.stderr, end='\n\n')
        print('*' * 40, file=sys.stderr, end='\n')
    finally:
        file.close()