import sqlite3

class Load:
    def create_comex_table(self, data_json, db_name, table_name, ano_referencia):
        con = sqlite3.connect(f"{db_name}.db")
        c = con.cursor()
        
        c.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name}
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ano INTEGER,
                mes INTEGER,
                tipo_fluxo TEXT,
                valor_fob REAL,
                peso_liquido REAL
                );
        ''')
        
        records = data_json.get('data', {}).get('list', [])
        
        is_export = "export" in str(data_json).lower()
        fluxo_texto = "Exportação" if is_export else "Importação"

        for item in records:
            
            mes = item.get('month') or item.get('monthNumber') or item.get('mes')
            
            c.execute(f'''
            INSERT INTO {table_name} (ano, mes, tipo_fluxo, valor_fob, peso_liquido) 
            VALUES (?, ?, ?, ?, ?);
            ''', (
                ano_referencia,
                mes,
                fluxo_texto,
                item.get('metricFOB'),
                item.get('metricKG')
            ))

        con.commit()
        con.close()