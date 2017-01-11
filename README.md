![](https://raw.githubusercontent.com/GaragemHacker/blog/master/garagemhacker-logo.png)

GaragemHacker Blog
==================

Pré-Requisitos
--------------

- Python
- Virtualenv
- Git


Instalando e Rodando
--------------------

- Assumindo que seu git e virtualenv já estão configurados, faça o clone do repositório

```bash
git clone git@github.com:garagemhacker/blog.git
```

- Crie uma virtualenv (pode chamar `garagem`). Se você não sabe como criar uma virtualenv, [leia isso](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


- Ative seu virtualenv e instale os pacotes necessários para rodar o projeto:

```bash
pip install -r requirements.txt
```

- Gere o output do site e Rode o projeto

```bash
make serve
```

Abra o browser em [localhost:8000](http://localhost:8000) para ver o conteúdo gerado.

Contribuindo
------------

Para contribuir com o projeto veja o guia de [Contribuição](https://github.com/garagemhacker/blog/blob/master/CONTRIBUTING.md).

Links Úteis
-----------

* Documentação Pelican - http://docs.getpelican.com/en/3.6.3/
* Virtualenv - http://docs.python-guide.org/en/latest/dev/virtualenvs/
* Pyenv - https://github.com/yyuu/pyenv
* Virtualenvwrapper - https://virtualenvwrapper.readthedocs.org/en/latest/
