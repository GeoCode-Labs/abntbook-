# Cookiecutter Jupyter Book – Template Acadêmico

Este é um modelo de projeto para gerar documentação científica e técnica usando **Jupyter Book** e **Cookiecutter**.

## 📋 O que é este template?

Este template Cookiecutter permite criar rapidamente projetos de documentação acadêmica e técnica usando [Jupyter Book](https://jupyterbook.org/), uma ferramenta moderna que permite escrever documentação bonita e interativa usando Markdown e Jupyter Notebooks.

## 🚀 Como usar

### Pré-requisitos

Instale o Cookiecutter:

```bash
pip install cookiecutter
```

### Gerando um novo projeto

Execute o comando abaixo e responda às perguntas interativas:

```bash
cookiecutter gh:GeoCode-Labs/abntbook-
```

Ou use diretamente o caminho local:

```bash
cookiecutter /caminho/para/este/repositorio
```

### Perguntas do Template

Durante a criação, você será questionado sobre:

- **project_name**: Nome completo do seu projeto (ex: "Meu Trabalho de Conclusão de Curso")
- **project_slug**: Nome técnico do projeto (ex: "meu_tcc")
- **author_name**: Seu nome completo
- **author_email**: Seu email
- **institution**: Nome da sua instituição
- **github_username**: Seu usuário do GitHub
- **project_description**: Descrição breve do projeto
- **version**: Versão inicial (padrão: 0.1.0)
- **use_gitlab_ci**: Se deseja usar GitLab CI/CD (yes/no)
- **use_github_actions**: Se deseja usar GitHub Actions (yes/no)
- **python_version**: Versão do Python (padrão: 3.9)

## 📁 Estrutura do Template Gerado

```
{{ cookiecutter.project_slug }}/
├── _config.yml                # Configurações do Jupyter Book
├── _toc.yml                   # Estrutura de navegação (Table of Contents)
├── intro.md                   # Página inicial
├── references.bib             # Referências bibliográficas (BibTeX)
├── referencias.md             # Página de referências
├── README.md                  # Documentação do projeto
├── requirements.txt           # Dependências Python
├── .gitignore                 # Arquivos ignorados pelo git
├── .gitlab-ci.yml             # Pipeline GitLab CI/CD (opcional)
├── .github/workflows/         # GitHub Actions (opcional)
│   └── deploy.yml
├── capitulos/                 # Capítulos em Markdown
│   ├── introducao.md
│   ├── fundamentacao.md
│   ├── metodologia.md
│   ├── resultados.md
│   └── conclusao.md
├── notebooks/                 # Jupyter Notebooks
│   ├── exemplo.md
│   └── analise_dados.ipynb
├── _static/                   # Arquivos estáticos (imagens, CSS)
│   └── .gitkeep
└── _templates/                # Templates customizados
```

## 🔧 Construindo o Livro

Após gerar o projeto:

1. Entre no diretório:
```bash
cd {{ cookiecutter.project_slug }}
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Construa o livro:
```bash
jupyter-book build .
```

4. Abra o livro no navegador:
```bash
# O HTML gerado estará em _build/html/index.html
open _build/html/index.html  # macOS
xdg-open _build/html/index.html  # Linux
start _build/html/index.html  # Windows
```

### Gerando PDF

```bash
jupyter-book build . --builder pdflatex
```

## ✨ Funcionalidades

- ✅ **Escrita fácil em Markdown** - MyST Markdown com suporte a LaTeX
- ✅ **Jupyter Notebooks** - Integre código executável na documentação
- ✅ **Referências bibliográficas** - Sistema automático com BibTeX
- ✅ **Equações matemáticas** - Suporte completo a LaTeX
- ✅ **Temas modernos** - Interface web responsiva e bonita
- ✅ **Deploy automático** - CI/CD para GitHub Pages ou GitLab Pages
- ✅ **Exportação PDF** - Gere PDFs de alta qualidade
- ✅ **Interatividade** - Gráficos, widgets e código executável
- ✅ **Estrutura pré-configurada** - 5 capítulos prontos para edição
- ✅ **Exemplos práticos** - Notebooks com análise de dados

## 📚 Recursos Adicionais

- [Jupyter Book - Documentação Oficial](https://jupyterbook.org/)
- [MyST Markdown Guide](https://myst-parser.readthedocs.io/)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Cookiecutter Documentation](https://cookiecutter.readthedocs.io/)
- [Python Scientific Stack](https://scipy.org/)

## 🎯 Casos de Uso

Este template é ideal para:

- **Trabalhos de Conclusão de Curso (TCC)**
- **Dissertações de Mestrado**
- **Teses de Doutorado**
- **Artigos Científicos**
- **Documentação Técnica**
- **Tutoriais Interativos**
- **Livros Didáticos**
- **Relatórios de Pesquisa**

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto é de código aberto e está disponível para uso acadêmico e educacional.

## 💡 Exemplos de Uso

### Trabalho de Conclusão de Curso (TCC)
```bash
cookiecutter gh:GeoCode-Labs/abntbook-
# project_name: Análise de Algoritmos de Machine Learning
# project_slug: tcc-ml-analise
# author_name: João Silva
# github_username: joaosilva
# institution: Universidade Federal de Exemplo
```

### Dissertação de Mestrado
```bash
cookiecutter gh:GeoCode-Labs/abntbook-
# project_name: Otimização de Redes Neurais Profundas
# project_slug: dissertacao-redes-neurais
# author_name: Maria Santos
# institution: Instituto de Tecnologia Exemplo
```

### Documentação Técnica
```bash
cookiecutter gh:GeoCode-Labs/abntbook-
# project_name: Guia Completo de Python para Ciência de Dados
# project_slug: guia-python-ds
# author_name: Pedro Costa
# institution: DataLab Research
```

## 🔍 Comparação: Jupyter Book vs LaTeX

| Característica | Jupyter Book | LaTeX Tradicional |
|----------------|--------------|-------------------|
| **Facilidade** | ⭐⭐⭐⭐⭐ Markdown simples | ⭐⭐ Sintaxe complexa |
| **Interatividade** | ⭐⭐⭐⭐⭐ Notebooks, widgets | ⭐ Apenas PDF estático |
| **Web** | ⭐⭐⭐⭐⭐ HTML responsivo | ⭐ Requer conversão |
| **PDF** | ⭐⭐⭐⭐ Via LaTeX | ⭐⭐⭐⭐⭐ Nativo |
| **Código** | ⭐⭐⭐⭐⭐ Executável | ⭐⭐ Apenas exibição |
| **Deploy** | ⭐⭐⭐⭐⭐ GitHub Pages grátis | ⭐ Manual |

## 🌟 Por que Jupyter Book?

- **Moderno**: Interface web bonita e responsiva
- **Fácil**: Escreva em Markdown, não em LaTeX
- **Interativo**: Inclua código executável e visualizações
- **Colaborativo**: Hospede gratuitamente no GitHub/GitLab
- **Flexível**: Exporte para HTML, PDF, e-book
- **Poderoso**: Todo o ecossistema Python científico

---

**Desenvolvido com ❤️ para a comunidade acadêmica e científica brasileira**
