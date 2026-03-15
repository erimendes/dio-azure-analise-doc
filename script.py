import os
from odf.opendocument import OpenDocumentText
from odf.style import Style, TextProperties, ParagraphProperties
from odf.text import H, P, Span

def gerar_relatorio_premium():
    doc = OpenDocumentText()

    # --- Definição de Estilos ---
    # Título Principal
    s_titulo = Style(name="TituloPrincipal", family="paragraph")
    s_titulo.addElement(TextProperties(fontweight="bold", fontsize="22pt", fontfamily="Arial"))
    s_titulo.addElement(ParagraphProperties(textalign="center", marginbottom="0.5cm"))
    doc.styles.addElement(s_titulo)

    # Subtítulos
    s_subtitulo = Style(name="Subtitulo", family="paragraph")
    s_subtitulo.addElement(TextProperties(fontweight="bold", fontsize="14pt", color="#2e5894"))
    s_subtitulo.addElement(ParagraphProperties(margintop="0.4cm", marginbottom="0.2cm"))
    doc.styles.addElement(s_subtitulo)

    # Código (Bloco Cinza)
    s_code = Style(name="BlocoCodigo", family="paragraph")
    s_code.addElement(TextProperties(fontfamily="Courier New", fontsize="10pt", color="#333333"))
    s_code.addElement(ParagraphProperties(backgroundcolor="#f4f4f4", padding="0.2cm", border="0.5pt solid #cccccc"))
    doc.styles.addElement(s_code)

    # --- Construção do Conteúdo ---
    
    # Capa/Título
    doc.text.addElement(P(stylename=s_titulo, text="Documentação de Integração: API ViaCEP"))
    doc.text.addElement(P(text="Desenvolvimento de Middleware para Validação e Consulta de Dados Cadastrais"))
    doc.text.addElement(P(text="-"*50))

    # 1. Resumo Executivo
    doc.text.addElement(H(outlinelevel=1, stylename=s_subtitulo, text="1. Resumo Executivo"))
    doc.text.addElement(P(text="Este projeto apresenta uma solução de backend desenvolvida no Node-RED para a automação da consulta de endereços. O foco principal foi a criação de uma camada de validação robusta que impede requisições desnecessárias a APIs externas, otimizando o tráfego de dados e o tempo de resposta."))

    # 2. Arquitetura de Entrada
    doc.text.addElement(H(outlinelevel=1, stylename=s_subtitulo, text="2. Interoperabilidade (GET/POST)"))
    doc.text.addElement(P(text="Para garantir a versatilidade do sistema, foram implementados dois endpoints simultâneos:"))
    doc.text.addElement(P(text="• Método GET: Facilita consultas rápidas via navegadores e testes simples de URL."))
    doc.text.addElement(P(text="• Método POST: Permite a integração com sistemas modernos que trafegam dados via corpo JSON, como aplicações Mobile e ferramentas de teste como Postman ou Insomnia."))

    # 3. Regras de Negócio (O Código)
    doc.text.addElement(H(outlinelevel=1, stylename=s_subtitulo, text="3. Implementação da Lógica de Validação"))
    doc.text.addElement(P(text="A lógica central foi isolada em um nó de função. O script limpa qualquer caractere não numérico e verifica a integridade do dado antes de prosseguir:"))
    
    codigo_js = [
        "// Normalização e Limpeza",
        "let cep = (msg.req.query.cep || (msg.payload && msg.payload.cep) || '').toString();",
        "let cepLimpo = cep.replace(/\\D/g, '');",
        "",
        "// Validação de Integridade (Edge Validation)",
        "if (cepLimpo.length !== 8) {",
        "    msg.payload = JSON.stringify({",
        "        'erro': 'CEP inválido',",
        "        'mensagem': 'O CEP deve conter 8 números.'",
        "    }, null, 4);",
        "    msg.headers = { 'Content-Type': 'application/json' };",
        "    return [null, msg]; ",
        "}"
    ]
    for linha in codigo_js:
        doc.text.addElement(P(stylename=s_code, text=linha))

    # 4. Resultados e Formatação
    doc.text.addElement(H(outlinelevel=1, stylename=s_subtitulo, text="4. Experiência do Desenvolvedor (UX)"))
    doc.text.addElement(P(text="A resposta de erro foi projetada com 'Pretty Print', utilizando recuo de 4 espaços para garantir que a mensagem seja legível tanto por humanos quanto por sistemas de log."))

    # Conclusão
    doc.text.addElement(H(outlinelevel=1, stylename=s_subtitulo, text="5. Conclusão"))
    doc.text.addElement(P(text="A implementação cumpre os requisitos de eficiência e escalabilidade, tratando exceções na borda do sistema e entregando dados estruturados de alta qualidade."))

    doc.save("Relatorio_Final_CEP.odt")
    print("Sucesso! Arquivo 'Relatorio_Final_CEP.odt' gerado.")

if __name__ == "__main__":
    gerar_relatorio_premium()