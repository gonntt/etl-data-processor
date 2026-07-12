from pathlib import Path
import csv

INPUT_FILE = Path("input.csv")
OUTPUT_FILE = Path("output.csv")


def extract(file_path: Path):
    """Lê os dados de entrada em CSV."""
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    with file_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def transform(rows):
    """Aplica regras simples de limpeza e transformação."""
    transformed_rows = []

    for row in rows:
        nome = (row.get("nome") or "").strip().title()
        cidade = (row.get("cidade") or "").strip().upper()
        idade = int(row.get("idade") or 0)

        transformed_rows.append({
            "nome": nome,
            "idade": idade,
            "cidade": cidade,
        })

    return sorted(transformed_rows, key=lambda item: item["nome"])


def load(rows, file_path: Path):
    """Grava os dados transformados em CSV."""
    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["nome", "idade", "cidade"])
        writer.writeheader()
        writer.writerows(rows)


def main():
    """Executa o pipeline ETL."""
    data = extract(INPUT_FILE)
    transformed_data = transform(data)
    load(transformed_data, OUTPUT_FILE)

    print(f"ETL concluído com sucesso. {len(transformed_data)} registros processados.")


if __name__ == "__main__":
    main()






#alteração
