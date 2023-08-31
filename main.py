print('pour de continuer votre inscription suivait les instruction suivant.')
print(f'')
name = input('Veuillez saisir votre nom :')
firstName = input('Veuillez saisir votre prenom :')
print('Saisie réussite avec succés !')
print(f'')
print('pour pouvoir voir votre saisie veuillez ecrire : oui\nou ecrivez non pour ne pas le voir')

reponse = input('')


if reponse == 'non':
    print(f'votre saisie est donc terminé\n\nmerci de votre confiance :) ')

if reponse == 'oui':
    print(f'Voici votre saisie : {name} {firstName}')


