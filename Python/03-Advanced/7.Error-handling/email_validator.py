import re


class Error(Exception):
    pass


class NameTooShortError(Error):
    pass


class MustContainAtSymbolError(Error):
    pass


class InvalidDomainError(Error):
    pass


while True:
    email = input()
    if email == "End":
        break
    try:
        username, at, domain = re.findall(r"([a-zA-Z1-9]+)(@?)[a-zA-Z1-9]+(\.(?:com|bg|org|net))?", email)[0]
    except IndexError:
        continue

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not at:
        raise MustContainAtSymbolError("Email must contain @")

    if not domain:
        raise InvalidDomainError("Domain must be on of the following: .com, .bg, .org, .net")

    print("Email is valid")