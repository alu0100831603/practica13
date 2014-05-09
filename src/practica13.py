#!usr/bin/python
#!encoding: UTF-8

import pylab as dibujo

x=[1.500,1.2003,1.00,0.5, 0.01]
x1=[10,50,100,150,500,550,1000]
y=[10,20,50,80,100]
y1=[10,20,50,70,80]
y2=[5,10,20,50,90]
y3=[9,15,50,80,60]
y4=[5,10,20,30,40]
y5=[17,16,50,36,65]
y6=[10,45,68,20,90]
t=[0.000686,0.007109,0.032868,0.058673,0.651724,0.885562,2.693729]

p1=dibujo.subplot(211)
dibujo.title('Porcentaje de fallo')
dibujo.plot(x,y,marker='o',linestyle='-.',color='r',label='Aprox 10')                                                                        
dibujo.plot(x,y1,marker='o',linestyle='-.',color='g',label='Aprox 50')
dibujo.plot(x,y2,marker='*',linestyle='-.',color='y',label='Aprox 100')
dibujo.plot(x,y3,marker='+',linestyle='-.',color='b',label='Aprox 150')
dibujo.plot(x,y4,marker='o',linestyle='-.',color='c',label='Aprox 500')
dibujo.plot(x,y5,marker='*',linestyle='-.',color='m',label='Aprox 550')
dibujo.plot(x,y6,marker='+',linestyle=':',color='r',label='Aprox 1000')
dibujo.legend() 
dibujo.xlim(0,1.0)
dibujo.ylim(0,100)
dibujo.xticks(x)

p2=dibujo.subplot(212)
dibujo.xlabel('intervalos')
dibujo.ylabel('Tiempo en segundos')
dibujo.plot(x1,t,marker='+',linestyle='-',color='m',label='Linea 4')
dibujo.xlim(9,1000)
dibujo.ylim(0,2.8)
dibujo.show()