<div style="text-align:center;">
    <img src="img/PPGE3M_UFRGS_logo.png" alt="Logo PPGE3M-UFRGS" width="600px">
</div>

# DETECÇÃO DE DESCRIÇÕES LITOLÓGICAS ANÔMALAS UTILIZANDO ISOLATION FOREST: UM ESTUDO DE CASO EM MINA DE FOSFATO

**Notebook complementar ao artigo do CBMina 2025**

Autores: [Franco Naghetini](www.linkedin.com/in/fnaghetini); [Diego Marques](https://www.linkedin.com/in/diego-machado-marques-7336852b/); [Fernanda Niquini](https://www.linkedin.com/in/fernanda-gontijo-fernandes-niquini-0a6a7698/)

## Resumo
A qualidade dos dados geológicos na mineração é fundamental para a estimativa de recursos, sendo que descrições litológicas incorretas podem comprometer a definição de domínios de estimativa. Esses erros comumente estão associados à dificuldade de se diferenciar litologias apenas por critérios macroscópicos. Este estudo propõe a aplicação do algoritmo Isolation Forest—um método não supervisionado baseado no princípio do isolamento—para identificar possíveis erros de descrição litológica em furos de sondagem de uma mina de fosfato. O algoritmo constrói árvores de isolamento binárias, classificando como anomalias amostras com profundidade média de isolamento reduzida. O fluxo de trabalho incluiu: remoção de dados faltantes, análise exploratória, pré-processamento, amostragem do conjunto de treino, modelagem e validação do modelo. Os resultados demonstraram eficácia: na 
validação geoquímica, as cinco amostras identificadas como anomalias realmente são possíveis erros de descrição litológica, enquanto, na validação por injeção de anomalias artificiais, o modelo alcançou 100% de acurácia. Conclui-se que a metodologia é promissora para auxiliar na detecção de inconsistências litológicas que impactam diretamente a estimativa de recursos, oferecendo uma ferramenta robusta para aprimorar a confiabilidade dos dados na cadeia de mineração.

## Objetivo
o presente estudo visa aplicar o algoritmo Isolation Forest não-supervisionado para a detecção de descrições litológicas incorretas em furos de sondagem de uma mina de fosfato. A descrição litológica desempenha um papel fundamental na definição dos domínios de estimativa dessa mina, sendo crucial para a estimativa de recursos e a tomada de decisões operacionais. A detecção automatizada de anomalias nas descrições litológicas pode contribuir significativamente para a melhoria da qualidade dos dados e da eficiência operacional, minimizando erros humanos e garantindo a confiabilidade das informações geológicas.

## Versões do Software
- python v3.11.7
- numpy v1.26.4
- pandas v2.1.4
- matplotlib v3.8.0
- seaborn v0.13.2
- sklearn v1.2.2