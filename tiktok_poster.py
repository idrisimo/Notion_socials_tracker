import requests

import random
import string
from pprint import pprint
class Tiktok_Wrapper():
    
    def __init__(self,client_key, client_secret):
        # self.user_id = user_id
        # self.access_token = access_token
        self.client_key = client_key
        self.client_secret = client_secret
        self.timeout = 5 # Seconds
        self.base_url = "https://open-api.tiktok.com"
    
    def query_maker(self, query_dict):
        count = 0
        query_string = "?"
        for key, value in query_dict.items():
            count += 1
            if count != len(query_dict):
                query_string += f"{key}={value}&"      
            else:
                query_string += f"{key}={value}"
        return query_string
            
    def csrf_state_generator(self):
        return "".join(random.choice(string.ascii_lowercase + string.digits) for x in range(11))
    
    def get_access_token(self):
        oauth_endpoint = "/oauth/access_token/"
        # query_params = {"client_key":self.client_key, "client_secret":self.client_secret, "code":, "grantt_type":}
        
        # post_url = f"{self.base_url}{oauth_endpoint}{self.query_maker(query_params)}"
        
        
        # post = requests.post(post_url, timeout=self.timeout)
        pass
    
    def upload_video(self, video_loc):
        upload_endpoint = "/share/video/upload/"
        headers = {}
        data = video_loc
        query_params = {"open_id": self.user_id, "access_token": self.access_token}
        post_url = f"{self.base_url}{upload_endpoint}{self.query_maker(query_params)}"
        
        post = requests.post(post_url, data=data ,headers=headers, timeout=self.timeout)
        try:
            if post['data']['err_code'] == 0:
                print("upload success")
                uploaded = True
            else:
                print("upload failed")
                uploaded = False
            return uploaded
        except Exception as err:
            print(err)


# base_url = "https://open-api.tiktok.com/share/video/upload/"
# query_params = {"open_id": 123, "access_token": 456}
# post_url = f"{base_url}?access_token={query_params['access_token']}&open_id={query_params['open_id']}"
# post = requests.post(post_url)
# try:
#     if post['data']['err_code'] == 0:
#         print("upload success")
#         uploaded = True
#     else:
#         print("upload failed")
#         uploaded = False
# except Exception as err:
#     print(err)
# print("begin")
# query_params = {"open_id": 123, "access_token": 456}
# query_string = "?"
# count = 0
# for key, value in query_params.items():
#     count += 1
#     if count != len(query_params):
#         query_string += f"{key}={value}&"      
#     else:
#          query_string += f"{key}={value}"
# print(query_string)


# tiktok = Tiktok_Wrapper(client_key="aw8jtjvejd52bd6s", client_secret="198db9678496a8ee791c6f3a42b6a0cf")

# # tiktok.get_access_token()
# redirect_uri = "https://example.com/auth"
# info = requests.get(f"https://www.tiktok.com/auth/authorize/?client_key=aw8jtjvejd52bd6s&scope=user.info.basic,video.list&response_type=code&redirect_uri={redirect_uri}&state=kv0db9kcwxf")

# pprint(vars(info))
# https://stackoverflow.com/questions/73338099/tiktok-login-kit-web-flow-keep-getting-redirect-uri-error-code-10006


# result = "".join(random.choice(string.ascii_lowercase + string.digits) for x in range(11))
# print(result)
from tiktok_api import TikTokApi

# Authenticate with the TikTok API using your API credentials
api = TikTokApi.get_instance(
    custom_verifyFp="your_verify_fp",
    use_test_endpoints=True,
    **your_other_api_credentials,
)

# Upload your video file to TikTok
video_data = api.upload_video_file("path/to/your/video.mp4")

# Add any additional metadata to your TikTok post (e.g., captions, hashtags, etc.)
post_data = {
    "description": "Check out my awesome video!",
    "hashtags": ["#awesome", "#video", "#tiktok"],
}

# Post your video to TikTok
response = api.post_video(video_data, **post_data)
