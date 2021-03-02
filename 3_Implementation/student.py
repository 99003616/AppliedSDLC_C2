"""Module of class of students and automailers"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from ClassRoom import *
from graph import *


class student:
    """This is a student class"""
    def __init__(self, ps):
        """Constructor"""
        self.ps = ps

    def getScore(self):
        """To get score"""
        my_data = data_for_graph()
        return my_data[self.ps]

    def classAverage(self):
        """To return class average"""
        res = avg()
        print(student.__doc__)
        return res

    def get_Graph(self):
        """To access and get graphs"""
        return radar_graph(self.ps)


class faculty:
    """This is a Faculty Class"""
    def __init__(self, ps_list):
        """Constructor"""
        self.ps_list = ps_list

    def getAvg(self):
        """To get Avg of students"""
        print(faculty.__doc__)
        return avg()

    def get_top_five(self):
        """To get top 5 """
        return top_five(0)

    def get_bottom_five(self):
        """To get bottom 5"""
        return bottom_five(0)

    def get_graph(self):
        """To get graphs"""
        for i in range(0, 10):
            print(radar_graph(self.ps_list[i]))

    def get_mail(self):
        """To get mails"""
        mail_list = []
        for i in range(0, 10):
            mail_list.append(post_test.iloc[i, 3])
        return mail_list

    def send_mail(self):
        '''To send mails'''
        list1 = ['ashish.pareek@ltts.com', 'lalit.bhardwaj@ltts.com', 'ashish.nayak@ltts.com', 'prashantsudhir.bagal@ltts.com', 'aakarsh.mehta@ltts.com', 'yash.jhajharia@ltts.com', 'manzar.hussain@ltts.com', 'digendrakumar.sahu@ltts.com', 'ankitkumar.yadav@ltts.com', 'manu.nadar@ltts.com']
        for i in range(0, 10):
            psnumber = get_PS()
            for i in range(10):
                image1 = f'RMap_0_of_{psnumber[i]}.jpeg'
                image2 = f'RMap_1_of_{psnumber[i]}.jpeg'
                image3 = f'RMap_2_of_{psnumber[i]}.jpeg'
                image4 = f'RMap_3_of_{psnumber[i]}.jpeg'
                sender_email = 'learningcorporate7@gmail.com'
                sender_ePass = '99003708'
                receiver_email = list1[i]
                print(receiver_email)
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = receiver_email
                message['Subject'] = 'Mail using python'
                mail_text = '''Hello,
                This is a simple mail. There is file attachments in the mail, The mail is sent using Python SMTP library.
                Thank You'''
                message.attach(MIMEText(mail_text, 'plain'))
                with open(image1, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                encoders.encode_base64(part)

                with open(image2, "rb") as attachment:
                    part1 = MIMEBase("application", "octet-stream")
                    part1.set_payload(attachment.read())

                encoders.encode_base64(part1)
                with open(image3, "rb") as attachment:
                    part2 = MIMEBase("application", "octet-stream")
                    part2.set_payload(attachment.read())

                encoders.encode_base64(part2)
                with open(image4, "rb") as attachment:
                    part3 = MIMEBase("application", "octet-stream")
                    part3.set_payload(attachment.read())

                encoders.encode_base64(part3)

                part.add_header('Content-Disposition',
                                "attachment; filename= %s" % image1)
                part1.add_header('Content-Disposition',
                                 "attachment; filename= %s" % image2)
                part2.add_header('Content-Disposition',
                                 "attachment; filename= %s" % image3)
                part3.add_header('Content-Disposition',
                                 "attachment; filename= %s" % image4)
                message.attach(part)
                message.attach(part1)
                message.attach(part2)
                message.attach(part3)
                servers = smtplib.SMTP('smtp.gmail.com', 587)
                servers.starttls()
                servers.login(sender_email, sender_ePass)
                text = message.as_string()
                servers.sendmail(sender_email, receiver_email, text)
                servers.quit()
                print('Mail Sent')

