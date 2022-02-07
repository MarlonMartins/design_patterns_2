## Factory
O Factory Method tem em semelhança ao padrão Simple Factory o nome e o objetivo de isolar código de criação 
(aquele que utiliza o new) das classes de negócio do projeto.

O Factory Method delega a implementação do código de criação para as suas subclasses ou classes que o implementam.

## Memento
O Memento é um padrão de projeto que nos ajuda a salvar e restaurar estados de objetos.

### Problemas do Memento
Um possível problema é a quantidade de memória que ele pode ocupar, afinal estamos guardando muitas instâncias de o
bjetos que podem ser pesados.

Por isso, dependendo do tamanho dos seus objetos, a classe Estado pode passar a guardar não o objeto todo, mas sim 
somente as propriedades que mais fazem sentido.

Nada impede você também de limitar a quantidade máxima de objetos no histórico que será armazenado.