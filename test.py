# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
import random

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

try:
    import unittest2 as unittest
except ImportError:
    import unittest
from datetime import datetime
from kakaocert import *

class KakaocertServiceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.kakocertService = KakaocertService('TESTER', 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I=')
        self.kakocertService.IPRestrictOnOff = True
        self.kakocertService.UseLocalTimeYN = True
        self.clientCode = "020040000001"

    def test_1_requestCMS(self):
        requestCMS = RequestCMS(
            CallCenterNum = '1600-8536',
            Expires_in = 60,
            ReceiverBirthDay = '19941219',
            ReceiverHP = '01068444508',
            ReceiverName = '홍길동',
            BankAccountName = '예금주명',
            BankAccountNum = '9-4324-5**7-58',
            BankCode = '004',
            ClientUserID = 'clientUserID-0423-01',
            SubClientID = '020040000001',
            TMSMessage = 'TMSMessage0423',
            TMSTitle = 'TMSTitle 0423',
            isAllowSimpleRegistYN = True,
            isVerifyNameYN = True,
            PayLoad = 'Payload123'
            )

        try:
            result = self.kakocertService.requestCMS(self.clientCode, requestCMS)
            print(result.receiptId)
        except KakaocertException as KE:
            print(str(KE.code) +" "+ KE.message)

    # def test_getCMSResult(self):
    #     info = self.kakocertService.getCMSResult(self.clientCode, "020050711485700001")
    #
    #     print(info.receiptID)
    #     print(info.clientCode)
    #     print(info.clientName)
    #     print(info.state)
    #     print(info.regDT)
    #     print(info.receiverHP)
    #     print(info.receiverName)
    #     print(info.receiverBirthday)
    #     print(info.bankAccountName)
    #     print(info.bankAccountNum)
    #     print(info.bankCode)
    #     print(info.clientUserID)
    #     print(info.expires_in)
    #     print(info.callCenterNum)
    #     print(info.allowSimpleRegistYN)
    #     print(info.verifyNameYN)
    #     print(info.payload)
    #     print(info.requestDT)
    #     print(info.expireDT)
    #     print(info.tmstitle)
    #     print(info.tmsmessage)
    #     print(info.signedData)
    #     print(info.subClientName)
    #     print(info.subClientCode)
    #     print(info.viewDT)
    #     print(info.completeDT)
    #     print(info.verifyDT)

    # def test_getVerifyAuthState(self) :
    #     try :
    #         response = self.kakocertService.getVerifyAuthState(self.clientCode, "020050711485700001")
    #     except KakaocertException as KE :
    #         print(KE.code)
    #         print(KE.message)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KakaocertServiceTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
