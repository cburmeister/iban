"""
A simple script that verifies an international bank account number (IBAN).
"""
#!/usr/bin/python

COUNTRY_CODE_TO_LENGTH = {
    'AD': 24,  # Andorra
    'AE': 23,  # United Arab Emirates
    'AL': 28,  # Albania
    'AT': 20,  # Austria
    'AZ': 28,  # Azerbaijan
    'BA': 20,  # Bosnia and Herzegovina
    'BE': 16,  # Belgium
    'BG': 22,  # Bulgaria
    'BH': 22,  # Bahrain
    'BR': 29,  # Brazil
    'CH': 21,  # Switzerland
    'CR': 21,  # Costa Rica
    'CY': 28,  # Cyprus
    'CZ': 24,  # Czech Republic
    'DE': 22,  # Germany
    'DK': 18,  # Denmark
    'DO': 28,  # Dominican Republic
    'EE': 20,  # Estonia
    'ES': 24,  # Spain
    'FI': 18,  # Finland
    'FO': 18,  # Faroe Islands
    'FR': 27,  # France + Central African Republic, French Guiana, French
    #            Polynesia, Guadeloupe, Martinique, Reunion,
    #            Saint-Pierre and Miquelon, New Caledonia, Wallis and Futuna
    'GB': 22,  # United Kingdom + Guernsey, Isle of Man, Jersey
    'GE': 22,  # Georgia
    'GI': 23,  # Gibraltar
    'GL': 18,  # Greenland
    'GR': 27,  # Greece
    'GT': 28,  # Guatemala
    'HR': 21,  # Croatia
    'HU': 28,  # Hungary
    'IE': 22,  # Ireland
    'IL': 23,  # Israel
    'IS': 26,  # Iceland
    'IT': 27,  # Italy
    'JO': 30,  # Jordan
    'KW': 30,  # Kuwait
    'KZ': 20,  # Kazakhstan
    'LB': 28,  # Lebanon
    'LI': 21,  # Liechtenstein
    'LT': 20,  # Lithuania
    'LU': 20,  # Luxembourg
    'LV': 21,  # Latvia
    'MC': 27,  # Monaco
    'MD': 24,  # Moldova
    'ME': 22,  # Montenegro
    'MK': 19,  # Macedonia
    'MR': 27,  # Mauritania
    'MT': 31,  # Malta
    'MU': 30,  # Mauritius
    'NL': 18,  # Netherlands
    'NO': 15,  # Norway
    'PK': 24,  # Pakistan
    'PL': 28,  # Poland
    'PS': 29,  # Palestine
    'PT': 25,  # Portugal + Sao Tome and Principe
    'QA': 29,  # Qatar
    'RO': 24,  # Romania
    'RS': 22,  # Serbia
    'SA': 24,  # Saudi Arabia
    'SE': 24,  # Sweden
    'SI': 19,  # Slovenia
    'SK': 24,  # Slovakia
    'SM': 27,  # San Marino
    'TN': 24,  # Tunisia
    'TR': 26,  # Turkey
    'VG': 24,  # British Virgin Islands
}

NORDEA_COUNTRY_CODE_TO_LENGTH = {
    'DZ': 24,  # Algeria
    'AO': 25,  # Angola
    'BJ': 28,  # Benin
    'BF': 27,  # Burkina Faso
    'BI': 16,  # Burundi
    'CM': 27,  # Cameroon
    'CV': 25,  # Cape Verde
    'IR': 26,  # Iran
    'CI': 28,  # Ivory Coast
    'MG': 27,  # Madagascar
    'ML': 28,  # Mali
    'MZ': 25,  # Mozambique
    'SN': 28,  # Senegal
    'UA': 29,  # Ukraine
}


def verify(value, nordea=False):
    """
    Verify an international bank account number (IBAN).

    https://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN
    """
    if nordea:
        COUNTRY_CODE_TO_LENGTH.update(NORDEA_COUNTRY_CODE_TO_LENGTH)

    value = value.upper().replace(' ', '').replace('-', '')

    # Ensure IBAN length is accurate per country
    country_code = value[:2]
    if country_code not in COUNTRY_CODE_TO_LENGTH:
        return False

    # Append the first four characters to the end
    value = value[4:] + value[:4]

    # Replace each letter in the string with two digits
    # Where A = 10, B = 11, ..., Z = 35.
    digits = ''
    for x in value:
        ord_value = ord(x)
        if 48 <= ord_value <= 57:  # 0 - 9
            digits += x
        elif 65 <= ord_value <= 90:  # A - Z
            digits += str(ord_value - 55)
        else:
            return False

    # Cast value as an integer and compute the remainder when divided by 97
    if int(digits) % 97 != 1:
        return False

    return True
