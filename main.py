import pandas as pd
from datetime import datetime


from module.telegram import TelegramBot
# inicio = str(input('Digite o início do período ex.(2022-06-01):'))
# fim = str(input('Digite o final do período ex.(2022-06-30):'))

pd.options.display.width = 0

inicio = '2021-01-01'
fim = '2100-12-31'

path =  'I'
excel_path = '{}:\Meu Drive\ARQUIVOS\GERENCIAL\Gerencial Guara.xlsx'.format(path)

today_df = datetime.today().strftime('%Y-%m-%d')
dia = datetime.today().strftime('%d')
mes = datetime.today().strftime('%m')
ano = datetime.today().strftime('%Y')


# print(today_df)
# print(dia)
# print(int(mes)-1)
# print(ano)




vales_df = pd.read_excel(excel_path,sheet_name='VALES', usecols=[0, 1, 2, 3, 4])
teste = vales_df[vales_df['DATA'].isin(pd.date_range(inicio, fim))]
vales_mes_funcionario = vales_df.groupby(by=['DATA','FUNCIONARIO','DEBITO']).sum()

debito = teste.groupby(by=['DATA','FUNCIONARIO','DEBITO']).sum()
debito_amout = debito.groupby(by=['FUNCIONARIO','DEBITO']).sum()
teste = debito_amout.groupby(by=['FUNCIONARIO']).sum()
debitos_teste = vales_df.loc[vales_df['PAGTO']!='OK']


x = debitos_teste.groupby(by=['DATA','FUNCIONARIO','DEBITO']).sum()
y = x.groupby(by=['FUNCIONARIO','DEBITO']).sum()
z = y.groupby(by=['FUNCIONARIO']).sum()
# teste = vales_mes_funcionario[vales_mes_funcionario['DATA'].isin(pd.date_range(inicio, fim))]
# contas_df_cx01 = pd.DataFrame(contas_table)
# )
# today_message = (datetime.today().strftime('%d-%m-%Y'))
# # print(df[['VENCIMENTO','FORNECEDOR','COD BARRAS','VALOR']])
# # Filtra o vencimento
# # vencimentos=tabela.loc[tabela['VENCIMENTO']==data]
# deadlines = contas_df[contas_df['VENCIMENTO'].isin(pd.date_range(today_df, today_df))]
# deadlines_message = deadlines.drop(columns='COD BARRAS')
# len_deadlines = len(deadlines)
# cod_barras = deadlines[['COD BARRAS']]

# amount = deadlines[['VALOR']].sum()

# amount_by_date_suplyer = contas_df.groupby(by=['FORNECEDOR', 'VENCIMENTO']).sum().groupby(level=[0]).cumsum()
# amount_by_date_suplyer_total = amount_by_date_suplyer.groupby(by=['FORNECEDOR', 'VALOR']).sum().groupby(level=[0]).cumsum()

# deadlines_message_formatted = deadlines_message.to_string(index=False, header=False)
# amount_formatted = amount.to_string(index=False, header=False)

z_formated = z.to_string(index=False, header=False)
print('Data Frames OK')
# print(vales_mes_funcionario)
# print(teste)
# print(debito_amout)
print(z)

def criar_tabelas_excel():
    
    vales_df.to_excel('tabelas\Vales.xlsx')
    # deadlines.to_excel('tabelas\Contas a Pagar--{}.xlsx'.format(today_message))
    # amount_by_date_suplyer.to_excel('tabelas\Compras por Fornecedor.xlsx')
    # amount_by_date_suplyer_total.to_excel('tabelas\Compras por Fornecedor Total.xlsx')
    print('Tabelas Criadas OK')

# criar_tabelas_excel()

def send_message():
    
    TelegramBot.send_message('Vales Funcionários em aberto:')
    TelegramBot.send_message('{}'.format(z))

    print('Mensagem Enviada!')
    

if __name__ == "__main__":
    
    TelegramBot.load_config()
    
    send_message()
    exit()