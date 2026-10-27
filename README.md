# Brasil em Evolução

Como o Brasil mudou ao longo do tempo, em gráficos, no espírito de *Factfulness* e do Gapminder.
O objetivo é mostrar o quanto o país melhorou sem esconder o que ainda falta.

## Regras dos dados

- Só fontes oficiais: IBGE, DATASUS, Senatran, SNIS, Ipea, PNUD/Atlas Brasil, Banco Mundial e FAO.
- Toda série tem fonte e link em `metadados/`, e as quebras de metodologia aparecem nos gráficos.
- Nenhum número é digitado à mão. Tudo vem da API ou do arquivo oficial e é conferido contra a fonte (`conferencia/`).

## Pipeline

```
coletar  →  dados/brutos/<indicador>/   (arquivo original + manifesto.json com URL, data, sha256)
limpar   →  dados/prontos/<indicador>.csv  (formato tidy, ver pipeline/schema.py)
validar  →  schema + conferência contra conferencia/<indicador>.csv
site     →  site/data/*.json
```

Rodar no Codespaces:

```bash
python -m pipeline.run expectativa_vida coletar
python -m pipeline.run expectativa_vida inspecionar
```
