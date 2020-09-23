# Time: 2020/9/1 9:44
# Author: jiangzhw
# FileName: jira_demo.py

from jira import JIRA
import re

jira = JIRA('http://172.22.56.99:8099', basic_auth=('jiangzhw01', '552165844zjx**'))
search_sql = 'project = "JIAN" AND resolution = "Unresolved" ORDER BY priority DESC, updated DESC'
maxResults = 1000
fields = 'summary,description,comment'


def search_project(project):
    """search project"""
    search_pro = ""
    key_list = []
    if project is "all" or project is "ALL":
        search_pro = jira.projects()
        for pro in search_pro:
            print(str(pro))
    else:
        return jira.project(project)


print(search_project("all"))


def issue_search(jql):
    # issure_result = jira.search_issues(
    #     'project = "JIAN" AND resolution = "Unresolved" ORDER BY priority DESC, updated DESC',
    #     fields='summary,description,comment')
    issure_result = jira.search_issues(jql, fields=fields, maxResults=maxResults)

    return issure_result


def get_issue():
    for issue in issue_search(search_sql):
        issue = str(issue) + r' ' + issue.fields.summary
        print(issue)
    return issue


# get_issue()
# print("问题数量为%s" % len(issue_search(search_sql)))


def get_comment():
    for issue in issue_search():
        comments = issue.raw['fields']['comment']['comments']
        i = 0
        while i < len(comments):
            comment = comments[i]['body']
            pattern = re.search(r"http://172.22.56.99:8099(.*?)gz", comment)
            if pattern != None:
                print(pattern.group())
            i = i + 1
    return comments

# print(get_comment())
