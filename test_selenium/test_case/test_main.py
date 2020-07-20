# Time: 2020/7/7 11:28
# Author: jiangzhw
# FileName: test_main.py
import pytest

from test_selenium.page.main import Main

# 测试用户数据完整格式(照片上传方式搞不定暂不考虑)：
# 姓名,账号,别名,性别(0男 1女)
# 国际区号,手机,座机,邮箱,地址
# 部门,职务,身份(0普通成员 1上级),上级身份负责部门
# 对外职务(0同步公司内职务 1自定义),自定义职务,是否通过邮件或短信发送企业邀请(0否 1是)

userData = [
    (
        "黎晟", "Ethan", "lisheng01",
        1, "853", "17866666666", "101000001", "jajsdjajsd@163.com", "萨达斯柯达",
        None, "测试工程师", 1,
        1, "员工", 0
    )]


class TestMain:

    def setup(self):
        self.main = Main(reuse=True)

    @pytest.mark.parametrize("username, english_name,user_id, "
                             "sex_zip_code, zipCode, mobile, tel, email, address, "
                             "dep, pos, identity_code, "
                             "out_pos, customize, send_email", userData)
    def test_add_member(self, username, english_name, user_id,
                        sex_zip_code, zipCode, mobile, tel, email, address,
                        dep, pos, identity_code,
                        out_pos, customize, send_email):
        """添加成员"""
        # 页面之间的跳转，返回其他的po，使用链式调用，实现多页面的操作。
        self.main.add_member().add_member(username, english_name, user_id,
                                          sex_zip_code, zipCode, mobile, tel, email, address,
                                          dep, pos, identity_code,
                                          out_pos, customize, send_email)
        assert "aaa" in self.main.get_massage()

    def test_import_user(self):
        """导入成员"""
        self.main.import_user("xxxx.file")
        assert "success" in self.main.import_user().get_massage()

    def test_send_message(self):
        """发送消息"""
        message = self.main.send_massage()
        message.send(app="", content="", group="")
        # assert "xxx" in self.main.get_massage()
