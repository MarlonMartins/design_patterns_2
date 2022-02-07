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


## Interpreter
O padrão é bastante útil quando temos que implementar interpretadores para DSLs, ou coisas similares. É um padrão bem 
complicado, mas bastante interessante. Quando temos expressões que devem ser avaliadas, e a transformamos em uma 
estrutura de dados, e depois fazemos com que a própria árvore se avalie, damos o nome de Interpreter.

### Quando usar?

O padrão Interpreter é geralmente útil para interpretar DSLs (se você não sabe o que é uma DSL, pode ler mais sobre isso 
aqui: http://pt.wikipedia.org/wiki/Linguagem_de_dom%C3%ADnio_espec%C3%ADfico. É comum que, ao ler a string 
(como por exemplo 2+3/4), o programa transforme-o em uma melhor estrutura de dados (como as nossas classes Expressao) 
e aí interprete essa árvore.

É realmente um padrão de projeto bem peculiar, e com utilização bem específica.