from djangotest1 import settings
import requests
def get_login_info(code):
    # 拼接路径
    code_url = settings.code2Session.format(settings.APP_ID,settings.APPSECRET,code)
    response = requests.get(code_url)  # 返回的是json数据
    print('coderesponse',response)
    json_response = response.json()    # 把json数据转换为字典
    print('jsonresponse',json_response)

    if json_response.get('session_key'):
        return json_response
    else:
        return False

def get_AccessToken():
    code_url = settings.getAccessToken.format(settings.APP_ID, settings.APPSECRET)
    response = requests.get(code_url)  # 返回的是json数据
    print('coderesponse', response)
    json_response = response.json()  # 把json数据转换为字典
    print('jsonresponse', json_response)

    return json_response.get('access_token')
    #     return json_response.access_token
    # else:
    #     return False

