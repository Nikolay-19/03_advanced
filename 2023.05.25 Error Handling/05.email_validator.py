class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = {".com", ".bg", ".org", ".net"}

while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    for char in email:
        if char == "@":
            name = email[:email.index(char)]
            if len(name) <= 4:
                raise NameTooShortError("Name must be more than 4 characters")

        if char == ".":
            domain = email[email.index(char):]
            if domain not in domains:
                raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
