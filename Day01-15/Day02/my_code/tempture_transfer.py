"""
將 攝氏溫度 轉換成 華氏溫度 
F = 1.8C + 32
"""

c = float(input("The 攝氏 tempture: "))
f = 1.8*c + 32
print('%.1f 攝氏溫度 = %.1f 華氏溫度' % (c,f))