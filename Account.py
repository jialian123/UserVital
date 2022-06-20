#_*_encoding:utf-8_*_
import re
import hashlib
from urllib.parse import urlencode,unquote
import requests
requests.packages.urllib3.disable_warnings()
import math
import json
import time
from Base import request

header = {
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
    'User-Agent': 'okhttp/3.12.6'
}
timeout = 10

class Account:
    def login(self,account,passwd,version,base_url):
        account_info = {}
        params = {
            'mod': 'user', 
            'ac': 'other_login', 
            'type': '3', 
            'mobile': account, 
            'zone': '86', 
            'code': '', 
            'smstype': '', 
            'name': '', 
            'a_key_token': '', 
            'pwd': passwd, 
            'mobile_type': '2', 
            'is_new': '', 
            'startid': '16551000929990d5ba', 
            'client': '2', 
            'height': '2265', 
            'stepid': '6', 
            'anon_id': '4657f457a846fb8e4f0aaeedf6c22717', 
            'package': 'com.bokecc.dance', 
            'compileabi': '64-Bit', 
            'operator': '46000', 
            'cpu': 'vendor_Kirin980', 
            'dic': 'gf', 
            'div': version, 
            'dpi': '480', 
            'ver': 'v2', 
            'oaid': '7efbffeb-edef-ee94-befe-f5caebb942dd', 
            'time': int(time.time() * 1000), 
            'uuid': '5141bb982b8223731848c22892dcb881', 
            'gtcid': '97e557092c76492b3fc5d5fad7a6d393', 
            'netop': '%E7%A7%BB%E5%8A%A8', 
            'width': '1080', 
            'xinge': '', 
            'version': version, 
            'all_startid': '165509901010130248', 
            'sdkversion': '10', 
            'channel': 'gf', 
            'height2': '2340', 
            'bucketlist': 'app_log_switch-on%2Capp_record_oritation-off%2C0%2Ccommunity_homepage-old%2Cdance_feed_ad-new%2Cdownload_ad_head-new%2Cdownload_ad_tail-new%2Cdownload_dance_play-old%2Cdownload_definition-old%2Cdownload_list_rank-old%2Cdownload_play_optimize-old%2Cdownload_split_tab-new%2Cdownload_video_cache-new%2Cdownpage_hide_send_new-new1%2Cdownpage_video_fold-old%2Cfavpage_add_feed-old%2Cfeed_plaque_ad_new2-new%2Cfeed_rank_tab-old%2Cfeed_video_tag-old%2Cfollowdance_throwingend-new%2Cfollowdance_video_content-old_equal%2Chigh_definition_down-old%2Chistorypage_add_feed-old%2Chomepage_tab-old%2Cicon_red_dot-new%2Cjump_home_multitype-new%2Cjump_home_video_rec-new%2Cjump_video_turn-new%2C-1%2Clogin_optimize-new%2Cmember_block-new2%2Cnew_feedui_optimize-old%2Cnewuser_feed_button-old%2Cnewuser_interest_label2-old%2Cnewuser_kingkong-new%2Cnewuser_login_guide-new%2Cnewuser_masking-old%2Cplayad_noheadad_v3-old%2Cplaypage_plaque_ad_new-old%2Cplaypage_to_exercise-new1%2Cpreload_ad-new%2Cpreload_end_ad-old%2Cpush_sdk-new%2Cquit_plaque_ad-new%2Crecord_config-new%2Cremove_ad_frame-new%2Csearch_mid_ad-new%2Csearch_resultpage_tab-old%2Csend_revision-new%2Cshare_flowers-new%2Cshare_no_adv-old%2Cshow_direction_v2-old%2Cspace_ui-new%2Ctab_icon-old_3%2Cvideo_cache-new%2Cvideo_result_rank-old%2Cvideo_tag1-old%2Cvideo_tag2-old%2Cvip_buy_first-old%2Cvip_buy_name-new%2Cvip_intro-old%2Cvip_video-old%2Cvip_video_dv-old%2Cvip_video_section-old%2Cvisitor_vip-old', 
            'smallvideo': '1', 
            'nettype': 'WIFI',
            'isvirtualapp': '0'
        }
        response = request.send_get(url=base_url,params=params,need_hash=True)
        if response['data']['code'] == '0':
            account_info['uid'] = response['data']['datas'][0]['id']
            account_info['name'] = response['data']['datas'][0]['name']
            account_info['token'] = response['data']['datas'][0]['token'] 
            account_info['avatar'] = response['data']['datas'][0]['avatar']
            return account_info
        else:
            return False



account = Account()