from .data import users_feedback
import math

## Função que calcura a similaridade entre dois usuários, baseado na distância euclidiana
def euclidian_distance(dataset,user1,user2):
    ##Criando um dicionário que irá conter os itens que ambos os usuários tem em comum
    similarity = {}
    ##Loop que irá percorrer o dataset e verificar se o item está presente no dataset do usuário 1 e 2
    for item in dataset[user1]:
        if item in dataset[user2]:
            ##Caso o item esteja presente em ambos os datasets, ele será adicionado ao dicionário similarity
            similarity[item] = 1
    ##Caso não haja nenhum item em comum, a função retorna 0
    if len(similarity) == 0:
        return 0

    ##Caso haja itens em comum, a função irá calcular a distância euclidiana para cada item em comum
    sum_euclidian_distance = sum([math.pow(dataset[user1][item]-dataset[user2][item],2) 
                              for item in dataset[user1] 
                              if item in dataset[user2]])
    
    return 1/(1+math.sqrt(sum_euclidian_distance))

## Função que retorna os usuários mais similares com base em outros usuários
def get_similarities(dataset,user):
    similarity=[(euclidian_distance(dataset,user,other),other) for other in dataset if other != user]
    similarity.sort().reverse()
    return similarity