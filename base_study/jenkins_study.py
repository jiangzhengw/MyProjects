# Time: 2021/1/4 10:52
# Author: jiangzhw
# FileName: jenkins_study.py

import jenkins

jenkins_url = 'http://172.22.56.97:8080'
jenkins_user = 'jiangzhw01'
api_token = '11e526dc0b7e7a419de30614eb81fda868'
jenkins_password = '552165844zjx**'
job_name = r'jiangzhw/python_jenkins_api_demo01'

jkServer = jenkins.Jenkins(jenkins_url, jenkins_user, jenkins_password)

user = jkServer.get_whoami()
print(user)
version = jkServer.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
