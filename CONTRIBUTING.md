Contribuindo
============

1. Fork o projeto
2. Crie uma branch para a feature em que trabalhará: `git checkout -b my-new-feature`
3. Faça commit das suas alterações: `git commit -m 'Add some feature'`
4. Faça push desses commits para sua branch: `git push origin my-new-feature`
5. Envie um pull request para o nosso repositório

Criar um novo Post
------------------

Para criar um novo post, rode o comando:

	make newpost NAME='NOME DO SEU POST'

Ele irá criar um novo arquivo `nome-do-seu-post.md` na pasta `content/blog` e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você só precisará adicionar o restante do conteúdo.

Após terminar o post, renderize-o com o comando:

	make html

Se tudo deu certo, seu novo post já estará disponível na página.


Criar uma nova Página
---------------------

Para criar uma nova página, rode o comando:

	make page NAME='NOME PAGINA'

Ele irá criar um novo arquivo `nome-pagina.md` na pasta `content/pages` e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você só precisará adicionar o restante do conteúdo.

Após terminar de editar a página, renderize-a com o comando:

	make html

Se tudo deu certo, sua página já estará disponível em `/slug-pagina/`.


Atualizar Github Pages
----------------------

Após realizar todos os testes locais, para fazer o upload do novo conteúdo no github pages, rode o comando:

	make github

Você poderá ir na página oficial e já observar suas alterações.
