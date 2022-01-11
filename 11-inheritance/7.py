from email import EMail
from sms import SMS

email1 = EMail("nowak@onet.pl", "kowalski@gmail.com", "Meeting on Thursday")
email1.set_message("i would like to inform you that our Thursday meeting has been canceled.")
email1.send()

sms1 = SMS("326433234", "498241154")
sms1.set_message("i would like to inform you that our Thursday meeting has been canceled.")
sms1.send()
