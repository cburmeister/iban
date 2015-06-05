#!/usr/bin/python

import unittest
import iban


class TestVerify(unittest.TestCase):
    def test_valid(self):
        """
        Ensure valid IBAN numbers are deemed valid.
        """
        valid = [
            'AD1200012030200359100100',
            'AL47212110090000000235698741',
            'AT611904300234573201',
            'BG80BNBG96611020345678',
            'BH29BMAG1299123456BH00',
            'CH9300762011623852957',
            'DZ4000400174401001050486',
            'FO97 5432 0388 8999 44',
            'GB29 RBOS 6016 1331 9268 19',
            'GB29N-WB K6016-13319-26819',
            'GB29NWBK60161331926819',
            'GB82 WEST 1234 5698 7654 32',
            'GB82WeST12345698765432',
            'GR16-0110-1250-0000-0001-2300-695',
            'GR1601101250000000012300695',
            'IL620108000000099999999',
            'IS14 0159 2600 7654 5510 7303 39',
            'MC5813488000010051108001292',
            'ME25 5050 0001 2345 6789 51',
            'MT84 MALT 0110 0001 2345 MTLC AST0 01S',
            'RS35260005601001611379',
            'SA03 8000 0000 6080 1016 7519',
            'SA0380 0 0000 06 0 8 0 1 0 1 6 7 519 ',
            'SA0380000000608010167519',
            'SE3550000000054910000003',
            'SM86 U032 2509 8000 0000 0270 100',
            'TN59 1000 6035 1835 9847 8831',
            'TR330006100519786457841326',
            'VG96VPVG0000012345678901',
        ]
        for value in valid:
            self.assertTrue(iban.verify(value, nordea=True))

    def test_invalid(self):
        """
        Ensure invalid IBAN numbers deemed invalid.
        """
        invalid = [
            'NL02ABNA012345678999',
            'NL02 ABNA 0123 4567 8999',
            'NL91ABNB0417164300',
            'NL91 ABNB 0417 1643 00',
            'MU17BOMM0101101030300200000MUR12345',
            'MU17 BOMM 0101 1010 3030 0200 000M UR12 345',
        ]
        for value in invalid:
            self.assertFalse(iban.verify(value))


if __name__ == '__main__':
    unittest.main()
