import json

with open('model1-config.json', 'r',encoding="utf-8") as f:
    config = json.load(f)

sharesHeld = config['sharesHeld']
sharesReserve = config['sharesReserve']
gainTarget = config['gainTarget']
yinnPrice = config['products'][0]['price']
print ("sharesHeld =", sharesHeld)
print ("sharesReserve =", sharesReserve)
print ("yinnPrice =", yinnPrice)

fundsReturn = 0
count = 0

while (fundsReturn + sharesHeld * yinnPrice) <= gainTarget and sharesHeld > sharesReserve :
    sharesHeld -= 2
    fundsReturn += 2 * yinnPrice
    yinnPrice *= 1.15
    count += 1
    print ("[count]", count)
    print ("sharesHeld =", sharesHeld)
    print ("yinnPrice =", yinnPrice)
    print ("fundsReturn =", fundsReturn)
    print ("funds =", fundsReturn + sharesHeld * yinnPrice)

print ("final funds =", fundsReturn + sharesHeld * yinnPrice)