from .fUser import functionUser
from .fPersonal import functionPersonal


class Verify(object):

    def verifyUser(self, user):
        return functionUser().findUserByUserName(user)

    
    def verifyUserEncuesta(self, user):
        return functionPersonal().findUserbyNumTra(user)


    def verifyMail(self, email):
        return functionUser().findUserByEmail(email)

    def verify_password(self, user, password):
        return functionUser().verify_password(user, password)

    def getToken(self, user):
        return functionUser().setToken(user)


    def getTokenEncuesta(self, user):
        return functionPersonal().setTokenEncuesta(user)
