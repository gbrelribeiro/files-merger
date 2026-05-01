<h1 align="center">
  Files Merger
</h1>

<p align="center">
  Este código Python percorre uma pasta de entrada (input), coleta arquivos de código por extensão e os consolida em um único arquivo Markdown dentro da pasta de saída (output).
</p>
## Descrição

O **Files Merger** varre recursivamente o diretório `input/`, encontra todos os arquivos com as extensões suportadas e gera um arquivo `output/all_files.md` contendo o conteúdo de cada arquivo formatado em blocos de código com syntax highlighting.

Ideal para preparar contexto de projetos para envio a LLMs, revisões de código ou documentação rápida de uma codebase.

**Extensões suportadas:**

| Extensão | Linguagem no Markdown |
|---|---|
| `.ts` | `typescript` |
| `.tsx` | `typescript` |
| `.css` | `css` |
| `.prisma` | `prisma` |

## Como usar

### Pré-requisitos

- Python 3.6+
- Sem dependências externas

### Instalação

```bash
git clone https://github.com/gbrelribeiro/files-merger.git
cd files-merger
```

### Estrutura esperada

```
files-merger/
├── input/          # Coloque na pasta 'input' os arquivos que deseja mesclar
│   ├── componente.tsx
│   ├── estilos.css
│   └── schema.prisma
├── output/         # Pasta 'output' é criada automaticamente
└── files_merger.py
```

### Execução

1. Adicione os arquivos desejados dentro da pasta `input/`
2. Execute o script:

```bash
python files_merger.py
```

3. O resultado estará em `output/all_files.md`

### Exemplo de saída

```markdown
# Arquivos do Projeto

Total de arquivos encontrados: **3**

---

## `componente.tsx`

```typescript
// conteúdo do arquivo...
```
##

```

## Personalização

Para adicionar suporte a novas extensões, edite as constantes no topo do arquivo:

```python
EXTENSIONS = (".ts", ".tsx", ".css", ".prisma", ".json")  # adicione aqui

EXTENSION_LANGUAGE_MAP = {
    ".json": "json",  # e aqui
    # ...
}
```
