# Time: 2021/1/4 9:54
# Author: jiangzhw
# FileName: jenkinsapi_study.py

from jenkinsapi import jenkins

jenkins_url = 'http://172.22.56.97:8080'
jenkins_user = 'jiangzhw01'
api_token = '11e526dc0b7e7a419de30614eb81fda868'
jenkins_password = '552165844zjx**'
job_name = r'jiangzhw/python_jenkins_api_demo01'

# 实例化jenkins对象，连接远程的jenkins master server
J = jenkins.Jenkins(jenkins_url, jenkins_user, api_token)

# J.build_job(job_name)
# print(J.get_job(job_name))


# 打印一下server查是否连接成功
# 返回一个jenkins对象<jenkins.Jenkins object at 0x10807d190>
print(J)

# 打印jenkins 版本信息
print(J.version)

# 构建job名为testJob的job（不带构建参数）
J.build_job(job_name)

# 查看某个job的构建信息
job_info = J.get_job(job_name)
print(job_info)

# 获取job名为testJob的job的最后次构建号
# lastbuildNumber = J.get_job(job_name)['lastBuild']['number']

# 获取job名为testJob的job的最后1次构建的执行结果状态
# result = J.get_job(job_name, lastbuildNumber)['result']

# 判断testJob是否还在构建中
# status = J.get_job(job_name, lastbuildNumber)['building']
# print(status)
