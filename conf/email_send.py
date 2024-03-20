import smtplib
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conf.read_conf import read
from conf.logging_config import getLogger

log = getLogger()

class SendMail(object):
    def __init__(self):
        self.conf_dict = read('email_conf.ini')
        # print(self.toaddrs)
        self.toaddrs = self.conf_dict['toaddrs'].split(',')
        self.fromuser = self.conf_dict['fromuser']
        self.userpasswd = self.conf_dict['userpasswd']
        self.smtpaddr = self.conf_dict['smtpaddr']

    # 构造邮件结构
    # toaddrs 收件人可以是多个,["xxx@qq.com","xxx@qq.com"]，
    # subject 邮件的主题，
    # msg 邮件的内容,
    # file_path 附件文件地址,默认不发生附件
    def mailStructure(self, subject, msg, file_path):
        # 邮件对象:
        mailMsg = MIMEMultipart()
        mailMsg['Subject'] = ("<%s>" % subject)
        mailMsg['From'] = ("测试 <%s>" % self.fromuser)
        mailMsg['To'] = ','.join(self.toaddrs)
        # 邮件正文是MIMEText ：
        mailMsg.attach(MIMEText(msg, 'html', 'utf-8'))
        # 如果输入附件文件路径，添加附件发送邮件
        if file_path != "null":
            file_name = file_path.split('/')[-1]
            with open(file_path, "rb") as f:
                attachment = MIMEApplication(f.read(), Name=file_path)
                encoders.encode_base64(attachment)
                attachment.add_header("Content-Disposition", "attachment", filename=file_name)
                mailMsg.attach(attachment)
        return mailMsg.as_string()


    # 发送邮件
    def sendMail(self, subject, msg, file_path='null'):
        mailMsg_as_string = self.mailStructure(subject, msg, file_path)
        # 连接服务器发送邮件
        try:
            server = smtplib.SMTP_SSL(self.smtpaddr, 465)
            server.connect(self.smtpaddr)  # 连接smtp服务器
            server.login(self.fromuser, self.userpasswd)  # 登录邮箱
            server.sendmail(self.fromuser,self.toaddrs, mailMsg_as_string)  # 发送邮件
            server.quit()
            log.info("邮件发送成功")
        except Exception as e:
            print("Error: unable to send email")
            log.info("邮件发送失败")


# e_send = SendMail()
# e_send.sendMail('早上好','邮件来自自动化测试1')