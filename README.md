iban
===========

A simple script that verifies an international bank account number (IBAN).

---

## Usage

```bash
>>> import iban
>>> iban.verify('NL02 ABNA 0123 4567 8999')
False
>>> iban.verify('MU17BOMM0101101030300200000MUR')
True
>>>
```

If you wish to include the list of catalogued IBANs from
[Nordea](https://en.wikipedia.org/wiki/Nordea):

```bash
>>> import iban
>>> iban.verify('DZ4000400174401001050486')
False
>>> iban.verify('DZ4000400174401001050486', nordea=True)
True
>>>
```
