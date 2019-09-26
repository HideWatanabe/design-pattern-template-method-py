# Template Method

## Definição do GoF, no livro "Padrões de Projeto" (2000)

### Intenção: 
Definir o esqueleto de um algoritmo em uma operação, postergando algns passos para as subclasses. **Template Method**
permite que subclasses redefinam certos passos de um algoritmo sem mudar a estrutura do mesmo.

### Tipo de pattern:
Comportamental

### Também conhecido como:
?

### Aplicável quando:
- Para implementar as partes invariantes de um algoritmo uma só vez e deixar para as subclasses a implementação do 
comportamento que pode variar.
- Quando o comportamento comum entre subclasses deve ser fatorado e concentrado numa classe comum para evitar a 
duplicação de código. Esse é um bom exemplo de "refatorar para generalizar" (Opdyke e Johnson). Primeiramente, você 
identifica as diferenças no código existente e então separa as diferenças em novas operações. Por fim, você substitui 
o código que apresentava as diferenças por um **Template Method** que chama uma dessas novas operações.
- Para controlar extensões de subclasses. Você pode definir um **Template Method** que chama operadores "gancho" em
pontos específicos, desta forma permitindo extensões somente nesses pontos.

### Participantes:
- **AbstractClass:** Define operações primitivas abstratas qeu as subclasses concretas definem para implementar passos
de um algoritmo. Implementa um **Template Method** que define o esqueleto de um algoritmo. O **Template Method** invoca 
operações primitivas, bem como operações definidas em **AbstractClass** ou ainda outros objetos.
- **ConcreteClass:** Implementa as operações primitivas para executarem os passos específicos do algoritmo da subclasse.
