# {{ cookiecutter.project_name }}

{% if cookiecutter.co_authors %}**Autores:**
- {{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})
{%- for author in cookiecutter.co_authors.split(',') %}
- {{ author.strip() }}
{%- endfor %}
{% else %}**Autor:** {{ cookiecutter.author_name }}
**Email:** {{ cookiecutter.author_email }}
{% endif %}
**Instituição:** {{ cookiecutter.institution }}

---

## Bem-vindo

Este é um documento acadêmico criado com [Jupyter Book](https://jupyterbook.org/), uma ferramenta moderna para criar documentação bonita e interativa usando Markdown e Jupyter Notebooks.

## Sobre este Documento

Este documento foi gerado usando o template Cookiecutter para Jupyter Book, facilitando a criação de documentação técnica e científica em formato web e PDF.

### Características

- ✅ Escrita fácil em Markdown
- ✅ Suporte a Jupyter Notebooks
- ✅ Equações matemáticas com LaTeX
- ✅ Referências bibliográficas automáticas
- ✅ Geração de PDF e HTML
- ✅ Hospedagem gratuita no GitHub Pages

## Estrutura do Documento

```{tableofcontents}
```

## Como Citar

```bibtex
@misc{ {{- cookiecutter.project_slug -}} ,
  {% if cookiecutter.co_authors -%}
  author = { {{- cookiecutter.author_name }} and {{ cookiecutter.co_authors.replace(',', ' and ') -}} },
  {%- else -%}
  author = { {{- cookiecutter.author_name -}} },
  {%- endif %}
  title = { {{- cookiecutter.project_name -}} },
  year = {2024},
  institution = { {{- cookiecutter.institution -}} }
}
```

---

*Gerado com Jupyter Book*
