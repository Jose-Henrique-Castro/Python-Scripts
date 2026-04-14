"""
arquivo: organizador_csv.py
data: 14/04/2026
descrição: Lê um arquivo CSV de vendas, calcula estatísticas básicas
e gera um relatório JSON com resumo por produto.
"""

import csv
import json
from collections import defaultdict

ARQUIVO_ENTRADA = "vendas.csv"
ARQUIVO_SAIDA = "relatorio_vendas.json"


def ler_vendas(nome_arquivo):
    vendas = []

    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            venda = {
                "produto": linha["produto"].strip(),
                "quantidade": int(linha["quantidade"]),
                "preco_unitario": float(linha["preco_unitario"])
            }
            vendas.append(venda)

    return vendas


def resumir_vendas(vendas):
    resumo = defaultdict(lambda: {"quantidade_total": 0, "valor_total": 0.0})

    for venda in vendas:
        produto = venda["produto"]
        quantidade = venda["quantidade"]
        valor = quantidade * venda["preco_unitario"]

        resumo[produto]["quantidade_total"] += quantidade
        resumo[produto]["valor_total"] += valor

    return resumo


def gerar_relatorio(resumo):
    relatorio = {
        "total_produtos": len(resumo),
        "produtos": []
    }

    maior_faturamento = 0
    produto_destaque = None

    for produto, dados in resumo.items():
        item = {
            "produto": produto,
            "quantidade_total": dados["quantidade_total"],
            "valor_total": round(dados["valor_total"], 2)
        }

        relatorio["produtos"].append(item)

        if dados["valor_total"] > maior_faturamento:
            maior_faturamento = dados["valor_total"]
            produto_destaque = produto

    relatorio["produto_destaque"] = produto_destaque
    relatorio["maior_faturamento"] = round(maior_faturamento, 2)

    return relatorio


def salvar_relatorio(relatorio, nome_arquivo):
    with open(nome_arquivo, mode="w", encoding="utf-8") as arquivo:
        json.dump(relatorio, arquivo, indent=4, ensure_ascii=False)


def main():
    try:
        vendas = ler_vendas(ARQUIVO_ENTRADA)
        resumo = resumir_vendas(vendas)
        relatorio = gerar_relatorio(resumo)
        salvar_relatorio(relatorio, ARQUIVO_SAIDA)

        print("Relatório gerado com sucesso!")
        print(f"Arquivo salvo em: {ARQUIVO_SAIDA}")
        print(f"Produto destaque: {relatorio['produto_destaque']}")
        print(f"Maior faturamento: R$ {relatorio['maior_faturamento']:.2f}")

    except FileNotFoundError:
        print(f"Erro: o arquivo '{ARQUIVO_ENTRADA}' não foi encontrado.")
    except KeyError as erro:
        print(f"Erro: coluna ausente no CSV -> {erro}")
    except ValueError:
        print("Erro: verifique se quantidade e preço_unitario possuem valores válidos.")


if __name__ == "__main__":
    main()
