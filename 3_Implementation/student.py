from ClassRoom import *
from graph import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class student:
    def __init__(self, ps):
        self.ps = ps

    def getScore(self):
        my_data = data_for_graph()
        return my_data[self.ps]

    def classAverage(self):
        res = avg()
        return res

    def get_Graph(self):
        return radar_graph(self.ps)


class faculty:
    def __init__(self, ps_list):
        self.ps_list = ps_list

    def getAvg(self):
        return avg()

    def get_top_five(self):
        return top_five(0)

    def get_bottom_five(self):
        return bottom_five(0)

    def get_graph(self):
        for i in range(0, 10):
            print(radar_graph(self.ps_list[i]))

    def get_mail(self):
        mail_list = []
        for i in range(0, 10):
            mail_list.append(post_test.iloc[i, 1])
        return mail_list

    def send_mail(self):
        li = []
        for i in range(0, 10):
            li.append(post_test.iloc[i, 3])
        ps = self.ps_list

        for i in range(10):

            radar_graph(ps[i])
            image1 = f'RMap_PreSurvey_of_{ps[i]}.jpeg'
            image2 = f'RMap_PreTest_of_{ps[i]}.jpeg'
            image3 = f'RMap_PostSurvey_of_{ps[i]}.jpeg'
            image4 = f'RMap_PostTest_of_{ps[i]}.jpeg'

            sender_email = 'learningcorporate7@gmail.com'
            sender_ePass = '99003708'
            receiver_email = li[i]

            print(receiver_email)

            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = 'Score Card'

            mail_text = '''Hello , Please find the attached copy of your pre_test, post_test, pre_survey and post_survey 
            Thank you!.'''

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
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender_email, sender_ePass)
            text = message.as_string()
            s.sendmail(sender_email, receiver_email, text)
            s.quit()
            print('Mail Sent')