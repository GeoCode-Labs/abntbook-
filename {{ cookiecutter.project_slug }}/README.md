# {{ cookiecutter.project_name }}

Documentação científica no padrão ABNT gerada via Cookiecutter.

## Informações do Projeto

- **Autor:** {{ cookiecutter.author_name }}
- **Email:** {{ cookiecutter.author_email }}
- **Instituição:** {{ cookiecutter.institution }}

## Estrutura do Projeto

```
{{ cookiecutter.project_slug }}/
├── README.md
├── .gitlab-ci.yml
├── requirements.txt
├── src/
│   └── main.tex
├── abntex2/
│   ├── preambulo.tex
│   ├── capa.tex
│   ├── folha_rosto.tex
│   └── referencias.bib
└── assets/
    └── logo.png
```

## Como Compilar

### Usando pdflatex

```bash
cd src
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

O PDF final será gerado em `src/main.pdf`.

### Usando Docker

Se você tem Docker instalado, pode usar a imagem texlive:

```bash
docker run --rm -v $(pwd):/workspace texlive/texlive bash -c "cd /workspace/src && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex"
```

## GitLab CI/CD

Este projeto está configurado para compilar automaticamente via GitLab CI. Cada commit irá:
1. Compilar o documento LaTeX
2. Gerar o PDF
3. Disponibilizar o PDF como artefato

## Edição

1. Edite o conteúdo principal em `src/main.tex`
2. Adicione suas referências bibliográficas em `abntex2/referencias.bib`
3. Customize o preâmbulo em `abntex2/preambulo.tex`
4. Adicione imagens na pasta `assets/`

## Requisitos

- TeX Live ou MiKTeX com abntex2 instalado
- BibTeX para gerenciamento de referências

Para instalar as dependências Python (se necessário):

```bash
pip install -r requirements.txt
```

## Sobre o abnTeX2

O abnTeX2 (ABsurd Norms for TeX) é uma suíte de classes e pacotes LaTeX para escrever documentos
acadêmicos brasileiros seguindo as normas da ABNT (Associação Brasileira de Normas Técnicas).

Para mais informações: https://www.abntex.net.br/
