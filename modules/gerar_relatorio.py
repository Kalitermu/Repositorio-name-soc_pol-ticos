from fpdf import FPDF
import matplotlib.pyplot as plt

def gerar_pdf(cidade, score, gasto_total):

    # criar gráfico
    labels = ["Score de risco"]
    valores = [score]

    plt.bar(labels, valores)
    plt.title("Indice de risco fiscal")

    grafico="grafico_risco.png"
    plt.savefig(grafico)
    plt.close()

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200,10,txt="Relatorio de Analise Fiscal",ln=True)

    pdf.cell(200,10,txt=f"Cidade: {cidade}",ln=True)
    pdf.cell(200,10,txt=f"Score de risco: {score}",ln=True)
    pdf.cell(200,10,txt=f"Gasto total: {gasto_total}",ln=True)

    pdf.image(grafico, x=10, y=80, w=100)

    arquivo="relatorio_fiscal.pdf"
    pdf.output(arquivo)

    return arquivo
