# Copa2022_StickerTrading
Função para identificar mais fácil as possíveis trocas de figurinhas do álbum da copa de 2022.

## Requisitos

O Script toma como input as listas de figurinhas repetidas e faltantes de cada um dos participantes, como as geradas pelo aplicativo da panini (PaniniCollectors).
A principio, só é possível realizar trocas de dois em dois, mas os outputs da função podem ser utilizados como inputs em execuções seguintes da função, permitindo simular cenários diferentes de troca


## Como utilizar?

No arquivo main.py, defina as seguintes variáveis:

 - myNeed: As figurinhas que te faltam completar a coleção
 - myRepeated: Suas figurinhas repetidas
 - peerNeed: As figurinhas que faltam para seu colega completar a coleção dele.
 - peerRepeated: As repetidas de seu colega
 - shinnyForShinny: Sabemos que existe uma cultura de trocar figurinhas brilhantes apenas por outras brilhantes (que não faz sentido nenhum, mas tudo bem). Esse parâmetro permite definir isso, e por Default, é settado como True


## Outputs

 - outputText: Texto resumido com as trocas que serão feitas (com breakdown de figurinhas brilhantes e não brilhantes, caso seja o caso) e as faltantes e repetidas de cada um dos envolvidos na troca.
 - need: As figurinhas que você receberá de seu colega
 - needShinny: As figurinhas brilhantes que você receberá de seu colega (caso shinnyForShinny==True)
 - give: As figurinhas que você dará ao seu colega
 - giveShinny: As figurinhas brilhantes que você dará ao seu colega (caso shinnyForShinny==True)
 - myRepeatedUpdated: Suas repetidas após a troca
 - peerRepeatedUpdated: As repetidas de seu colega após a troca
 - myNeed: As que você precisava antes da troca
 - myRepeated: Suas repetidas antes da troca
 - peerNeed: As que seu colega precisava antes da troca
 - peerRepeated: As repetidas de seu colega antes da troca
 - myNeedUpdated: As que você precisa após a troca
 - peerNeedUpdated: As que seu colega precisa após a troca


## Possíveis melhorias futuras

- Base de dados paralela para controle de repetidas e figurinhas "reservadas" para troca (Sugestão MVP: planilha online do google sheets)
- Simulação de diferentes cenários de troca
- Identificação de figurinhas críticas em trocas seguidas (Ex: Preciso receber da troca 1 para dar na troca 2)
- Simulação "online" de trocas
