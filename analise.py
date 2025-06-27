import pandas as pd
import matplotlib.pyplot as plt

# Lê o CSV
df = pd.read_csv('dados_vendas.csv')

# Cria uma figura com 2 subplots lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# --------------------------------------------
# GRÁFICO 1: Vendas por Produto
# --------------------------------------------
quantidade_por_produto = df.groupby('Produto')['Valor_Total'].sum()
quantidade_por_produto.plot(kind='bar', ax=ax1, color=["#f0e8e0", "#000000"]) 
ax1.set_title("Vendas por Produto", fontsize=14)
ax1.set_xlabel("Produtos", fontsize=12)
ax1.set_ylabel("Valor Total (R$)", fontsize=12)
ax1.tick_params(axis='x', rotation=45)
# --------------------------------------------
# GRÁFICO 2: Quantidade por Categoria
# --------------------------------------------
quantidade_por_categoria = df.groupby('Categoria')['Quantidade'].sum()
quantidade_por_categoria.plot(kind='bar', ax=ax2, color=['#ff7f0e', '#2ca02c'])
ax2.set_title('Quantidade por Categoria', fontsize=14)
ax2.set_xlabel("Categoria", fontsize=12)
ax2.set_ylabel("Quantidade", fontsize=12)

plt.tight_layout()
plt.savefig('graficos_combinados.png', dpi=300, bbox_inches='tight')
plt.show()