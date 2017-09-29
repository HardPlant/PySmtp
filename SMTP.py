class SMTP(object):
    def __init__(self, domain):
        self.domain = domain
        self.source = ''
        self.sourceName = ''
        self.dest = ''
        self.destName = ''


    def helo(self):
        return 'HELO '+ self.domain + '\r\n'
    def quit(self):
        return 'QUIT\r\n'

    def mail(self, source, name):
        name = self.sourceName
        source = self.source
        return "MAIL FROM:" + source + '\r\n'

    def rept(self, dest):
        dest = self.destName
        dest = self.dest
        return "RCPT TO:" + dest + '\r\n'

    def data(self, subject, content, cc=None):
        data = ''
        data = data + 'From: ' + '"'+self.sourceName+'" <'+ self.source + '>\r\n'
        data = data + 'To: ' + '"'+self.destName+'" <'+ self.dest + '>\r\n'
        if cc:
            data = data + 'Cc: ' + cc + '\r\n'
        data = data + 'Date: ' + ''
        data = data + 'Subject: ' + subject + '\r\n'
        data = data + content
        data = data + "\r\n.\r\n"

        return data

    def quit(self):
        return 'QUIT'


class SMTPResponse(object):
    def __init__(self, code):
        pass

    def getCode(self, code):
        if code is 250:
            return 'OK'
        if code is 354:
            return 'End data with'
        if code is 221:
            return 'BYE'

