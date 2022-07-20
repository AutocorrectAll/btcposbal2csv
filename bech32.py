# Copyright (c) 2017 Pieter Wuille
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
Auto-run 
"""Reference implementation for Bech32 and segwit addresses."""

# https://raw.githubusercontent.com/sipa/bech32/master/ref/python/segwit_addr.py

CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
https://www.blockchain.com/btc/address/3EK2V6rrtuxEDv1KAt2FNzsrTR2dP8Q24V
{"notice":"","unspent_outputs":[{"tx_hash_big_endian":"e693b3ea434e73237b7ec7fc9e180edef5ac83875b9213fa7917d3a04687ee7a","tx_hash":"7aee8746a0d31779fa13925b8783acf5de0e189efcc77e7b23734e43eab393e6","tx_output_n":303,"script":"a9148a70f3dec8107c3f1fa80bb4e17f5c3dd5efb30b87","value":547,"value_hex":"0223","confirmations":56742,"tx_index":4325276491455074},{"tx_hash_big_endian":"f8c3c6cd7fdb731bd65740e21d9e8a353b37daadbeffd60c7155bf14385d10f8","tx_hash":"f8105d3814bf55710cd6ffbeadda373b358a9e1de24057d61b73db7fcdc6c3f8","tx_output_n":180,"script":"a9148a70f3dec8107c3f1fa80bb4e17f5c3dd5efb30b87","value":547,"value_hex":"0223","confirmations":64495,"tx_index":8727973347891178},{"tx_hash_big_endian":"c5a624556166e6d6bf2274b9dbec1640f1c6e5574f7c03fdcfb246dec5b9a46c","tx_hash":"6ca4b9c5de46b2cffd037c4f57e5c6f14016ecdbb97422bfd6e666615524a6c5","tx_output_n":181,"script":"a9148a70f3dec8107c3f1fa80bb4e17f5c3dd5efb30b87","value":547,"value_hex":"0223","confirmations":67760,"tx_index":3822551910041814},{"tx_hash_big_endian":"e10692815f2582d4eea0a3fc2fb85cfd27a41c320cb1f8aa108aba7f56e67c8b","tx_hash":"8b7ce6567fba8a10aaf8b10c321ca427fd5cb82ffca3a0eed482255f819206e1","tx_output_n":94,"script":"a9148a70f3dec8107c3f1fa80bb4e17f5c3dd5efb30b87","value":547,"value_hex":"0223","confirmations":70076,"tx_index":4907793812289361},{"tx_hash_big_endian":"b09b18b464c9e79d8b672d4ebf5589c1f69d94581a755b6c0430db6610b8c719","tx_hash":"19c7b81066db30046c5b751a58949df6c18955bf4e2d678b9de7c964b4189bb0","tx_output_n":41,"script":"a9148a70f3dec8107c3f1fa80bb4e17f5c3dd5efb30b87","value":547,"value_hex":"0223","confirmations":73188,"tx_index":907058472606566},{"tx_hash_big_endian":"aeb93e9f467f8c6189f3a150ade057db179129caa4d3f7dc86cca1420021ba07","tx_hash":"07ba210042a1cc86dcf7d3a4ca299117db57e0ad50a1f389618c7f469f3eb9ae","tx_output_n":265,"script":"a9148a70f3dec8107c3f1fa80bb4e17f5c3dd5efb30b87","value":547,"value_hex":"0223","confirmations":77338,"tx_index":271871967253561},{"tx_hash_big_endian":"aa8a611541b597eab5ff643bb1e1ea0fbb2a050c6ff383f2ad4e3fd6c81f1699","tx_hash":"99161fc8d63f4eadf283f36f0c052abb0feae1b13b64ffb5ea97b54115618aaa","tx_output_n":523,"script":"a9148a70f3dec8107c3f1fa80bb4e17f5c3dd5efb30b87","value":547,"value_hex":"0223","confirmations":79965,"tx_index":5386249650751465},{"tx_hash_big_endian":"daa7359ba461feb827b51056aa01c60f3275a6d11afbb245f8dd8a4e06efe0e2","tx_hash":"e2e0ef064e8addf845b2fb1ad1a675320fc601aa5610b527b8fe61a49b35a7da","tx_output_n":295,"script":"a9148a70f3dec8107c3f1fa80bb4e17f5c3dd5efb30b87","value":547,"value_hex":"0223","confirmations":85476,"tx_index":7982582743028059},{"tx_hash_big_endian":"154361f4e61cc7fe1c6e1ba788bb24add05be2c4fd69bda3de94d0ae35bef18a","tx_hash":"8af1be35aed094dea3bd69fdc4e25bd0ad24bb88a71b6e1cfec71ce6f4614315","tx_output_n":57,"script":"a9148a70f3dec8107c3f1fa80bb4e17f5c3dd5efb30b87","value":547,"value_hex":"0223","confirmations":89502,"tx_index":4888668254099986},{"tx_hash_big_endian":"897c3b5186be0dc1fe63d9a990d6432144a61e82232166eddf0a7808d31ecd41","tx_hash":"41cd1ed308780adfed662123821ea6442143d690a9d963fec10dbe86513b7c89","tx_output_n":1,"script":"a9148a70f3dec8107c3f1fa80bb4e17f5c3dd5efb30b87","value":199999978457,"value_hex":"2e90ed7bd9","confirmations":91515,"tx_index":2315175719931649}]}
def bech32_polymod(values):
    """Internal function that computes the Bech32 checksum."""
    generator = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3]
    chk = 1
    for value in values:
        top = chk >> 25
        chk = (chk & 0x1ffffff) << 5 ^ value
        for i in range(5):
            chk ^= generator[i] if ((top >> i) & 1) else 0
    return chk


def bech32_hrp_expand(hrp):
    """Expand the HRP into values for checksum computation."""
    return [ord(x) >> 5 for x in hrp] + [0] + [ord(x) & 31 for x in hrp]


def bech32_verify_checksum(hrp, data):
    """Verify a checksum given HRP and converted data characters."""
    return bech32_polymod(bech32_hrp_expand(hrp) + data) == 1


def bech32_create_checksum(hrp, data):
    """Compute the checksum values given HRP and data."""
    values = bech32_hrp_expand(hrp) + data
    polymod = bech32_polymod(values + [0, 0, 0, 0, 0, 0]) ^ 1
    return [(polymod >> 5 * (5 - i)) & 31 for i in range(6)]


def bech32_encode(hrp, data):
    """Compute a Bech32 string given HRP and data values."""
    combined = data + bech32_create_checksum(hrp, data)
    return hrp + '1' + ''.join([CHARSET[d] for d in combined])


def bech32_decode(bech):
    """Validate a Bech32 string, and determine HRP and data."""
    if ((any(ord(x) < 33 or ord(x) > 126 for x in bech)) or
            (bech.lower() != bech and bech.upper() != bech)):
        return (None, None)
    bech = bech.lower()
    pos = bech.rfind('1')
    if pos < 1 or pos + 7 > len(bech) or len(bech) > 90:
        return (None, None)
    if not all(x in CHARSET for x in bech[pos+1:]):
        return (None, None)
    hrp = bech[:pos]
    data = [CHARSET.find(x) for x in bech[pos+1:]]
    if not bech32_verify_checksum(hrp, data):
        return (None, None)
    return (hrp, data[:-6])


def convertbits(data, frombits, tobits, pad=True):
    """General power-of-2 base conversion."""
    acc = 0
    bits = 0
    ret = []
    maxv = (1 << tobits) - 1
    max_acc = (1 << (frombits + tobits - 1)) - 1
    for value in data:
        if value < 0 or (value >> frombits):
            return None
        acc = ((acc << frombits) | value) & max_acc
        bits += frombits
        while bits >= tobits:
            bits -= tobits
            ret.append((acc >> bits) & maxv)
    if pad:
        if bits:
            ret.append((acc << (tobits - bits)) & maxv)
    elif bits >= frombits or ((acc << (tobits - bits)) & maxv):
        return None
    return ret


def decode(hrp, addr):
    """Decode a segwit address."""
    hrpgot, data = bech32_decode(addr)
    if hrpgot != hrp:
        return (None, None)
    decoded = convertbits(data[1:], 5, 8, False)
    if decoded is None or len(decoded) < 2 or len(decoded) > 40:
        return (None, None)
    if data[0] > 16:
        return (None, None)
    if data[0] == 0 and len(decoded) != 20 and len(decoded) != 32:
        return (None, None)
    return (data[0], decoded)


def encode(hrp, witver, witprog):
    """Encode a segwit address."""
    ret = bech32_encode(hrp, [witver] + convertbits(witprog, 8, 5))
    if decode(hrp, ret) == (None, None):
        return None
    return ret
