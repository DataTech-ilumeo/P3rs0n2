<h1>Persona</h1>
<h2>Pré-controle de versões</h2>

<h3>--Flight 23--</h3>

Awareness para o Ranking de Celebridades foi corrigido para:
	- Alto >= 70%
	- Baixo < 70%

Notou-se que as celebridades abaixo não existem no Software e portanto não há fotos para os mesmos:
	- Nikolas Antunes
	- Luiza Brunet

Arquivo de fotos e categorias teve os nomes das celebridades alterados conforme está no MySQL (software).
Foram adicionadas abas com consultas no powerquery para buscar dados de planilhas .csv exportadas do banco do software.
Como consequência, foi feita a alteração dos nomes das celebridades da série histórica para conseguir adicionar as categorias no dashboard.

---
<h2>Pós-controle de versões</h2>
* O controle de versões será feito só de arquivos .py e do log de alterações entre flights.
* O notebook do Jupyter (arquivo .ipynb) é armazenado na pasta padrão do projeto.
* Toda vez que for criar uma nova versão no Jupyter Notebook, é necessário fazer o commit da versão de python funcional e atual (que se tornará a versão anterior).

#1 Adicionado o script original chamado "PERSONA.py" do @Danilo que foi usado como base para as modificações