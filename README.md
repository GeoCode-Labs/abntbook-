# Cookiecutter ABNT – Template

Este é um modelo de projeto para gerar documentação científica no formato ABNT usando **Cookiecutter**.

## 📋 O que é este template?

Este template Cookiecutter permite criar rapidamente projetos de documentos acadêmicos brasileiros usando LaTeX com a classe abnTeX2, que segue as normas da ABNT (Associação Brasileira de Normas Técnicas).

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
- **use_gitlab_ci**: Se deseja usar GitLab CI/CD (yes/no)

## 📁 Estrutura do Template Gerado

```
{{ cookiecutter.project_slug }}/
├── README.md                  # Documentação do projeto
├── .gitlab-ci.yml             # Pipeline CI/CD (se habilitado)
├── requirements.txt           # Dependências Python opcionais
├── src/
│   └── main.tex              # Arquivo principal do documento
├── abntex2/
│   ├── preambulo.tex         # Configurações e pacotes LaTeX
│   ├── capa.tex              # Template da capa
│   ├── folha_rosto.tex       # Template da folha de rosto
│   └── referencias.bib       # Referências bibliográficas
└── assets/
    └── .gitkeep              # Pasta para imagens e logos
```

## 🔧 Compilando o Documento

Após gerar o projeto, entre no diretório e compile:

```bash
cd {{ cookiecutter.project_slug }}/src
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Ou use Docker:

```bash
docker run --rm -v $(pwd):/workspace texlive/texlive bash -c "cd /workspace/src && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex"
```

## ✨ Funcionalidades

- ✅ Template pré-configurado com abnTeX2
- ✅ Estrutura modular para fácil manutenção
- ✅ Suporte a referências bibliográficas (BibTeX)
- ✅ GitLab CI/CD para compilação automática
- ✅ Estrutura de pastas organizada
- ✅ Exemplos de capítulos pré-configurados

## 📚 Recursos Adicionais

- [abnTeX2 - Site Oficial](https://www.abntex.net.br/)
- [Normas ABNT](https://www.abnt.org.br/)
- [Cookiecutter Documentation](https://cookiecutter.readthedocs.io/)
- [LaTeX Tutorial](https://www.overleaf.com/learn)

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
# project_name: Trabalho de Conclusão de Curso em Ciência da Computação
# author_name: João Silva
# institution: Universidade Federal de Exemplo
```

### Dissertação de Mestrado
```bash
cookiecutter gh:GeoCode-Labs/abntbook-
# project_name: Dissertação de Mestrado em Engenharia de Software
# author_name: Maria Santos
# institution: Instituto de Tecnologia Exemplo
```

### Artigo Científico
```bash
cookiecutter gh:GeoCode-Labs/abntbook-
# project_name: Artigo sobre Inteligência Artificial
# author_name: Pedro Costa
# institution: Centro de Pesquisa em IA
```

---

**Desenvolvido com ❤️ para a comunidade acadêmica brasileira**
