# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo a todas as informações possiveis.
v=(input('Digite algo:'))
print('O tipo primitivo desse valor é: ' ,type(v))
print('è um número decimal ?',(v.isdecimal()))
print('Tem algum espaço?', (v.isspace()))
print('è um número ?',(v.isnumeric()))
print('é alfabetico?' ,(v.isalpha()))
print('é alfanumerico?', (v.isalnum()))