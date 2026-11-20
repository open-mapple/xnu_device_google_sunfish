# The Pixel 4a's device tree values, for build/mapple/tools/mkadt.py (with tools/soc/sm7150.py). From ios-sweet's
# tools/mkadt.py --highmem (damjankakak3) and ios-sweet-pixel's --sunfish (frokfrdk); MIT.

# The whole upper DDR bank (live FDT memory <0x1_00000000 0xfcc00000>); every fixed reserved-memory carve-out is in the
# low bank and the dynamic pools are limited below 4G: (base, size).
RAM = (0x100000000, 0xfcc00000)
# ABL's splash framebuffer, sunfish's sofef01 panel (1080x2340).
FB = dict(base=0x9c000000, size=0x1700000, width=1080, height=2340, stride=1080 * 4)
ECID = 0x5357454554000001  # 'SWEET' + 1, synthetic
PRODUCT_NAME = 'Pixel 4a'
DISPLAY_GAMUT = 'P3'    # as ios-sweet: the iPhone X's
# About: PRODUCT_MODEL := Pixel 4a in LineageOS android_device_google_sunfish (lineage-24.0, 264006f) lineage_sunfish.mk.
# serial-number is a placeholder the shim overwrites at each boot with ABL's androidboot.serialno.
ABOUT = dict(serial='MAPPLE0000000000', model='Pixel 4a', region='', regulatory='Pixel 4a')


def devices(a, ph, phandle, gic_ph, ecid, flags):
    """/arm-io devices: none; the kernel line's drivers find theirs by address."""
    return []
