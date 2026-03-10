from fpdf import FPDF

def gerar_pdf(cidade, score, gasto_total):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200,10,txt="Relatorio de Analise Fiscal",ln=True)

    pdf.cell(200,10,txt=f"Cidade: {cidade}",ln=True)
    pdf.cell(200,10,txt=f"Score de risco: {score}",ln=True)
    pdf.cell(200,10,txt=f"Gasto total: {gasto_total}",ln=True)

    arquivo="relatorio_fiscal.pdf"
    pdf.output(arquivo)

    return arquivo
