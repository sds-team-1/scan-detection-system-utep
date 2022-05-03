from randmac import RandMac

macTemplate = "00:00:00:00:00:00"
randomMAC = str(RandMac(macTemplate))
print(type(randomMAC))
print(randomMAC)