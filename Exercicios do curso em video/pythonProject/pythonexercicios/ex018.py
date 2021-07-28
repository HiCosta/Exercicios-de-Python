import math
ang = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(ang))
print('O ângulo {} tem o seno {:.2f}'.format(ang, seno))
cos = math.cos(math.radians(ang))
print('O ângulo {} tem o cosseno {:.2f}'.format(ang, cos))
tan = math.tan(math.radians(ang))
print('O ângulo {} tem a tangente {:.2f}'.format(ang, tan))
