# Time: 2021/4/9 11:12
# Author: jiangzhw
# FileName: test_nowcoder_interviw.py
import requests


class TestNowCoderInterview:
    """牛客hr系统-面试系统case'"""

    def test_set_interview(self):
        """面试-面试系统设置"""
        r = requests.get(
            'https://hr.nowcoder.com/v1/users/324461/interviewsettings'
            '?token=&access_token=978fb3d504211e91864a9d833f5b4369f5d8076338b78fb62106a14e7a2a60a1&_=1617934725760')
        assert r.json()["msg"] == "OK"
        assert r.status_code == 200

    def test_set_interview_keep_video(self):
        pass
