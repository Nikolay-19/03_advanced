class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if len(name) < self.min_length:
            return False
        return True

    def __is_mail_valid(self, mail):
        if mail not in self.mails:
            return False
        return True

    def __is_domain_valid(self, domain):
        if domain not in self.domains:
            return False
        return True

    def validate(self, email):
        data = email.split("@")
        name = data[0]
        mail = data[1].split(".")[0]
        domain = data[1].split(".")[1]

        if EmailValidator.__is_name_valid(self, name) and EmailValidator.__is_mail_valid(self, mail) \
                and EmailValidator.__is_domain_valid(self, domain):
            return True
        return False
