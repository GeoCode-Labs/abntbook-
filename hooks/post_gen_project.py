#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hook pós-geração do Cookiecutter.

Remove arquivos CI/CD não utilizados baseado nas escolhas do usuário.
"""
import os
import shutil


def remove_file(filepath):
    """Remove um arquivo se ele existir."""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Removed: {filepath}")


def remove_dir(dirpath):
    """Remove um diretório e todo seu conteúdo se ele existir."""
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)
        print(f"Removed directory: {dirpath}")


def main():
    """Lógica principal do hook."""
    use_github_actions = "{{ cookiecutter.use_github_actions }}"
    use_gitlab_ci = "{{ cookiecutter.use_gitlab_ci }}"

    # Remove GitHub Actions se não for usado
    if use_github_actions == "no":
        remove_dir(".github")
        print("✅ GitHub Actions: Não configurado (removido)")
    else:
        print("✅ GitHub Actions: Configurado")

    # Remove GitLab CI se não for usado
    if use_gitlab_ci == "no":
        remove_file(".gitlab-ci.yml")
        print("✅ GitLab CI: Não configurado (removido)")
    else:
        print("✅ GitLab CI: Configurado")

    # Mensagem final
    print("\n" + "=" * 70)
    print("🎉 Projeto gerado com sucesso!")
    print("=" * 70)
    print(f"\nProjeto: {{ cookiecutter.project_name }}")
    print(f"Diretório: {{ cookiecutter.project_slug }}")
    print(f"Autor: {{ cookiecutter.author_name }}")
    print("\n📚 Próximos passos:\n")
    print("1. cd {{ cookiecutter.project_slug }}")
    print("2. python -m venv venv")
    print("3. source venv/bin/activate  # Linux/Mac")
    print("   ou venv\\Scripts\\activate  # Windows")
    print("4. pip install -r requirements.txt")
    print("5. jupyter-book build .")
    print("6. open _build/html/index.html")
    print("\n📖 Documentação: https://jupyterbook.org/")
    print("=" * 70)


if __name__ == "__main__":
    main()
