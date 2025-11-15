# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

**Autor:** {{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})
**Instituição:** {{ cookiecutter.institution }}
**Versão:** {{ cookiecutter.version }}

---

## 📚 Sobre

Este é um projeto de documentação criado com [Jupyter Book](https://jupyterbook.org/), uma ferramenta moderna para criar livros e documentação técnica interativa usando Markdown e Jupyter Notebooks.

## 🚀 Início Rápido

### Pré-requisitos

- Python {{ cookiecutter.python_version }} ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📖 Uso

### Construir o Livro

Para construir o livro em HTML:

```bash
jupyter-book build .
```

O livro será gerado na pasta `_build/html/`. Abra `_build/html/index.html` no navegador para visualizar.

### Limpar Build Anterior

```bash
jupyter-book clean .
```

### Desenvolvimento Local

Para visualizar mudanças em tempo real, você pode usar um servidor HTTP local:

```bash
# Após construir o livro
cd _build/html
python -m http.server 8000
```

Acesse `http://localhost:8000` no navegador.

## 📝 Estrutura do Projeto

```
{{ cookiecutter.project_slug }}/
├── _config.yml              # Configurações do Jupyter Book
├── _toc.yml                 # Estrutura de navegação
├── intro.md                 # Página inicial
├── references.bib           # Referências bibliográficas
├── capitulos/               # Capítulos em Markdown
│   ├── introducao.md
│   ├── fundamentacao.md
│   ├── metodologia.md
│   ├── resultados.md
│   └── conclusao.md
├── notebooks/               # Jupyter Notebooks
│   ├── exemplo.md
│   └── analise_dados.ipynb
├── _static/                 # Arquivos estáticos (imagens, CSS)
└── _templates/              # Templates customizados
```

## ✍️ Editando o Conteúdo

### Markdown

A maioria do conteúdo está em arquivos `.md` usando MyST Markdown, que suporta:

- Markdown padrão
- Equações LaTeX: `$E = mc^2$` ou `$$\int_0^1 x dx$$`
- Citações: `{cite}autor2023`
- Referências cruzadas: `{numref}figura-1`
- Admonições: `{note}`, `{warning}`, `{tip}`

### Jupyter Notebooks

Adicione notebooks `.ipynb` na pasta `notebooks/` e inclua-os no `_toc.yml`.

### Referências

Adicione referências em BibTeX no arquivo `references.bib` e cite com `{cite}chave`.

## 🎨 Personalização

### Logo e Favicon

Adicione seus arquivos em `_static/`:
- `logo.png` - Logo do projeto
- `favicon.ico` - Ícone do navegador

Atualize `_config.yml` conforme necessário.

### Tema e Estilos

Edite `_config.yml` para personalizar cores, fontes e layout.

## 🚀 Deploy

{% if cookiecutter.use_github_actions == "yes" %}### GitHub Pages

O projeto está configurado para deploy automático no GitHub Pages via GitHub Actions.

1. Ative o GitHub Pages nas configurações do repositório
2. Selecione a branch `gh-pages` como fonte
3. Cada push na branch `main` irá construir e publicar automaticamente

URL: `https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}`
{% endif %}

{% if cookiecutter.use_gitlab_ci == "yes" %}### GitLab Pages

O projeto está configurado para deploy automático no GitLab Pages via CI/CD.

1. O pipeline será executado automaticamente em cada push
2. O site será publicado em GitLab Pages

URL: `https://{{ cookiecutter.github_username }}.gitlab.io/{{ cookiecutter.project_slug }}`
{% endif %}

### Outras Opções

- **Netlify**: Arraste a pasta `_build/html` para o Netlify Drop
- **Vercel**: Conecte o repositório e configure o build command: `jupyter-book build .`
- **Read the Docs**: Conecte o repositório e configure conforme a documentação

## 📄 Gerando PDF

Para gerar uma versão PDF do livro:

```bash
jupyter-book build . --builder pdflatex
```

O PDF será gerado em `_build/latex/book.pdf`.

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🔗 Links Úteis

- [Jupyter Book Documentation](https://jupyterbook.org/)
- [MyST Markdown Guide](https://myst-parser.readthedocs.io/)
- [Sphinx Documentation](https://www.sphinx-doc.org/)

## 📧 Contato

**{{ cookiecutter.author_name }}**
- Email: {{ cookiecutter.author_email }}
- GitHub: [@{{ cookiecutter.github_username }}](https://github.com/{{ cookiecutter.github_username }})

---

*Gerado com ❤️ usando [Jupyter Book](https://jupyterbook.org/)*
