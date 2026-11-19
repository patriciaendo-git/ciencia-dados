# Ciência de Dados · UPE Caruaru

Site com os materiais da disciplina de Ciência de Dados da Profa. Patricia Takako Endo (dotLAB · Universidade de Pernambuco).

Endereço: https://patriciaendo-git.github.io/ciencia-de-dados/

## Organização

```
index.html                 página da disciplina, com todas as aulas
logo.png                   logo do dotLAB
upe.png                    logo da Universidade de Pernambuco (topo das páginas, ao lado da logo do dotLAB)
aulas/<aula>/              os materiais de uma aula para as estudantes: página interativa e material de estudo (PDF)
```

## Publicar pela primeira vez

1. Crie o repositório `ciencia-de-dados` (público) na conta patriciaendo-git.
2. Em **Add file → Upload files**, arraste todo o conteúdo desta pasta (não a pasta em si) e confirme com a mensagem de commit.
3. Em **Settings → Pages**, escolha **Deploy from a branch**, branch `main`, pasta `/ (root)`, e salve.
4. Em um ou dois minutos, o site estará no endereço acima.

## Publicar um material novo

1. Envie os arquivos da aula para `aulas/<aula>/` (Add file → Upload files, navegando até a pasta).
2. Em `index.html`, procure a lista `AULAS` e preencha o material da aula:
   - página interativa: `material:{pagina:"aulas/<aula>/index.html", ver:"Versão 1.0 · mês de ano"}`
   - material de estudo em PDF: `apostila:{arq:"aulas/<aula>/<tema>-material-de-estudo.pdf", pag:14, ver:"Versão 1.0 · mês de ano"}`
   - material previsto, ainda sem arquivo: `{}` (aparece como “Em preparação”); material que não existe na aula: `null`.
3. Para atualizar um arquivo, envie com o mesmo nome e mude a versão em `ver`.

Os slides e a apresentação interativa de cada aula são de uso da professora e não vão para este repositório.
