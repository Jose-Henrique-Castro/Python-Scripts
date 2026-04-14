# 🐍 Python-Scripts

Collection of Python utility scripts focused on file processing, automation, and data manipulation.

---

## 📁 Projects

### 📊 organizador_csv.py
Reads a sales CSV file, calculates totals per product and exports a structured JSON report.

**Features:**
- CSV file reading with `csv.DictReader`
- Aggregation of quantity and revenue per product
- Identification of the top-grossing product
- Export to formatted JSON file
- Error handling (file not found, invalid values, missing columns)

**How to use:**
1. Create a `vendas.csv` file in the same folder with the format below
2. Run the script:
```bash
python organizador_csv.py
```
3. A `relatorio_vendas.json` file will be generated

**CSV format expected:**
```csv
produto,quantidade,preco_unitario
Mouse,3,59.90
Teclado,2,120.00
Monitor,1,899.99
```

**Output example (`relatorio_vendas.json`):**
```json
{
    "total_produtos": 3,
    "produtos": [
        { "produto": "Mouse", "quantidade_total": 3, "valor_total": 179.70 },
        { "produto": "Teclado", "quantidade_total": 2, "valor_total": 240.00 },
        { "produto": "Monitor", "quantidade_total": 1, "valor_total": 899.99 }
    ],
    "produto_destaque": "Monitor",
    "maior_faturamento": 899.99
}
```

---

## 🛠️ Technologies

- **Language:** Python 3.x
- **Libraries:** `csv`, `json`, `collections` (all standard library — no pip install needed)

---

## 👤 Author

**José Henrique Castro**  
Computer Science Student — PUC Goiás  
📍 Goiânia, Goiás, Brazil  
🔗 [github.com/Jose-Henrique-Castro](https://github.com/Jose-Henrique-Castro)

---

## 📄 License

This repository is open for learning purposes. Feel free to use and adapt the code.
