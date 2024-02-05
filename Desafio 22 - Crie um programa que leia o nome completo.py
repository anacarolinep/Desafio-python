#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome: ')).strip()
print('Seu nome maiusculo:',nome.upper())
print('Seu nome menisculo:',nome.lower())
print('Seu nome tem total de {} letras'.format(len(nome)))
print('Seu primeiro nome tem total de {} letras'.format(nome.find(' ')))
