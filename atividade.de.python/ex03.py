import math 
ang = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}' .format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(ang, coss))
print('O ângulo de {} tem o TANGENTE de {:.2f}' .format(ang, tang))