import ssl

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from kuikform_backend.settings import SMTP_PASSWORD, SMTP_USERID, REPLY_TO_ADDRESS


def send_reset_mail(name, mail_id, reset_link):
    context = ssl.create_default_context()

    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = "Here is your reset link"
        message["From"] = "KuikForm <kuikform@gmail.com>"
        message["To"] = f"{name} <{mail_id}>"
        message["reply-to"] = REPLY_TO_ADDRESS

        html = """   
    <!doctype html>
    <html lang="en-US">

    <head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <title>Reset Password Email Template</title>
    <meta name="description" content="Reset Password Email Template.">
    <style type="text/css">
        a:hover {text-decoration: underline !important;}
    </style>
    </head>

    <body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #ffffff;" leftmargin="0">
    <!--100% body table-->
    <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#ffffff"
        style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
        <tr>
            <td>
                <table style="background-color: #ffffff; max-width:670px;  margin:0 auto;" width="100%" border="0"
                    align="center" cellpadding="0" cellspacing="0">
                    <tr>
                        <td style="height:80px;">&nbsp;</td>
                    </tr>
                    <tr>
                        <td style="text-align:center;">
                          <a href="https://kuikform.tanmoy.codes" title="logo" target="_blank">
                            <img width="180" src="https://cdn.jsdelivr.net/gh/KuikForm/cdn@main/kuikform_logo.png" title="KuikForm" alt="KuikForm">
                          </a>
                        </td>
                    </tr>
                    <tr>
                        <td style="height:20px;">&nbsp;</td>
                    </tr>
                    <tr>
                        <td>
                            <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0"
                                style="max-width:670px;background:#fff; border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                                <tr>
                                    <td style="height:40px;">&nbsp;</td>
                                </tr>
                                <tr>
                                    <td style="padding:0 35px;">
                                        <h1 style="color:#1e1e2d; font-weight:500; margin:0;font-size:32px;font-family:'Rubik',sans-serif;">You have
                                            requested to reset your password</h1>
                                        <span
                                            style="display:inline-block; vertical-align:middle; margin:29px 0 26px; border-bottom:1px solid #cecece; width:100px;"></span>
                                        <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">
                                            We cannot simply send you your old password. A unique link to reset your
                                            password has been generated for you. To reset your password, click the
                                            following link and follow the instructions.
                                        </p>
                                        <a href='""" + reset_link + """'
                                            style="background:#20e277;text-decoration:none !important; font-weight:500; margin-top:35px; color:#fff;text-transform:uppercase; font-size:14px;padding:10px 24px;display:inline-block;border-radius:50px;">Reset
                                            Password</a>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="height:40px;">&nbsp;</td>
                                </tr>
                            </table>
                        </td>
                    <tr>
                        <td style="height:20px;">&nbsp;</td>
                    </tr>
                    <tr>
                        <td style="text-align:center;">
                            <p style="font-size:14px; color:rgba(69, 80, 86, 0.7411764705882353); line-height:18px; margin:0 0 0;">&copy; <strong>kuikform.tanmoy.codes</strong></p>
                        </td>
                    </tr>
                    <tr>
                        <td style="height:80px;">&nbsp;</td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    <!--/100% body table-->
    </body>

    </html>"""
        part1 = MIMEText(html, "html")
        message.attach(part1)

        smtp_user = SMTP_USERID
        smtp_pass = SMTP_PASSWORD
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(smtp_user, smtp_pass)

        server.sendmail("kuikform@gmail.com", mail_id, message.as_string())
        print("Success Mailed")
    except Exception as e:
        print(e)
        # return  str(e)


def send_verification_link_mail(name, mail_id, verify_link):
    context = ssl.create_default_context()

    try:
        print(verify_link)
        message = MIMEMultipart("alternative")
        message["Subject"] = "Verify KuikForm Account"
        message["From"] = "KuikForm <kuikform@gmail.com>"
        message["To"] = f"{name} <{mail_id}>"
        message["reply-to"] = REPLY_TO_ADDRESS


        html = """   
    <!doctype html>
    <html lang="en-US">

    <head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <title>Verify Your Mail</title>
    <meta name="description" content="Reset Password Email Template.">
    <style type="text/css">
        a:hover {text-decoration: underline !important;}
    </style>
    </head>

    <body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #ffffff;" 
    leftmargin="0"> <!--100% body table--> <table cellspacing="0" border="0" cellpadding="0" width="100%" 
    bgcolor="#ffffff" style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,
    400,600,700); font-family: 'Open Sans', sans-serif;"> <tr> <td> <table style="background-color: #ffffff; 
    max-width:670px;  margin:0 auto;" width="100%" border="0" align="center" cellpadding="0" cellspacing="0"> <tr> 
    <td style="height:80px;">&nbsp;</td> </tr> <tr> <td style="text-align:center;"> <a href="https://kuikform.tanmoy.codes" 
    title="KuikForm" target="_blank"> <img width="180" 
    src="https://cdn.jsdelivr.net/gh/KuikForm/cdn@main/kuikform_logo.png" 
    title="KuikForm" alt="KuikForm"> </a> </td> </tr> <tr> <td style="height:20px;">&nbsp;</td> </tr> <tr> <td> <table 
    width="95%" border="0" align="center" cellpadding="0" cellspacing="0" style="max-width:670px;background:#fff; 
    border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 
    rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);"> <tr> <td style="height:40px;">&nbsp;</td> </tr> <tr> 
    <td style="padding:0 35px;"> <h1 style="color:#1e1e2d; font-weight:500; 
    margin:0;font-size:32px;font-family:'Rubik',sans-serif;">Activate KuikForm Account</h1> <span 
    style="display:inline-block; vertical-align:middle; margin:29px 0 26px; border-bottom:1px solid #cecece; 
    width:100px;"></span> <p style="color:#455056; font-size:15px;line-height:24px; margin:0;"> Your account creation 
    is successful . It will take only 5 second to activate your account. Click on the link below to verify mail & activate account . </p> <a href='""" + verify_link + """' 
                                            style="background:#20e277;text-decoration:none !important; font-weight:500; margin-top:35px; color:#fff;text-transform:uppercase; font-size:14px;padding:10px 24px;display:inline-block;border-radius:50px;">Verify Mail</a>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="height:40px;">&nbsp;</td>
                                </tr>
                            </table>
                        </td>
                    <tr>
                        <td style="height:20px;">&nbsp;</td>
                    </tr>
                    <tr>
                        <td style="text-align:center;">
                            <p style="font-size:14px; color:rgba(69, 80, 86, 0.7411764705882353); line-height:18px; margin:0 0 0;">&copy; <strong>kuikform.tanmoy.codes</strong></p>
                        </td>
                    </tr>
                    <tr>
                        <td style="height:80px;">&nbsp;</td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    <!--/100% body table-->
    </body>

    </html>"""
        part1 = MIMEText(html, "html")
        message.attach(part1)

        smtp_user = SMTP_USERID
        smtp_pass = SMTP_PASSWORD
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(smtp_user, smtp_pass)

        server.sendmail("kuikform@gmail.com", mail_id, message.as_string())
        print("Success Mailed")
    except Exception as e:
        print(e)
        # return  str(e)

