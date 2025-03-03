from flask import request, Flask, send_file, render_template, url_for
from college_workbook import create
from openpyxl import load_workbook
app = Flask(__name__)
app.templates_auto_reload = True


courses_21 = ['ARTES VISUAIS ', 'CIÊNCIA DA COMPUTAÇÃO ', 'CIÊNCIAS BIOLÓGICAS ', 'CIÊNCIAS SOCIAIS ', 'DESIGN', 'EDUCAÇÃO FÍSICA ', 'FILOSOFIA ', 'FÍSICA ', 'GEOGRAFIA ', 'HISTÓRIA ', 'LETRAS - INGLÊS ', 'LETRAS-PORTUGUÊS ', 'LETRAS-PORTUGUÊS E ESPANHOL ', 'LETRAS-PORTUGUÊS E INGLÊS ', 'MATEMÁTICA ', 'MÚSICA ', 'PEDAGOGIA ', 'QUÍMICA ', 'SISTEMAS DE INFORMAÇÃO', 'TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS', 'TECNOLOGIA EM GESTÃO DA TECNOLOGIA DA INFORMAÇÃO', 'TECNOLOGIA EM REDES DE COMPUTADORES']

courses_19 = ['MEDICINA VETERINÁRIA', 'ODONTOLOGIA', 'MEDICINA', 'AGRONOMIA', 'FARMÁCIA', 'ARQUITETURA E URBANISMO', 'ENFERMAGEM', 'FONOAUDIOLOGIA', 'NUTRIÇÃO', 'FISIOTERAPIA', 'ZOOTECNIA', 'BIOMEDICINA', 'TECNOLOGIA EM RADIOLOGIA', 'TECNOLOGIA EM AGRONEGÓCIOS', 'TECNOLOGIA EM GESTÃO HOSPITALAR', 'TECNOLOGIA EM GESTÃO AMBIENTAL', 'TECNOLOGIA EM ESTÉTICA E COSMÉTICA', 'EDUCAÇÃO FÍSICA (BACHARELADO)', 'ENGENHARIA DA COMPUTAÇÃO', 'ENGENHARIA CIVIL', 'ENGENHARIA ELÉTRICA', 'ENGENHARIA DE CONTROLE E AUTOMAÇÃO', 'ENGENHARIA MECÂNICA', 'ENGENHARIA DE ALIMENTOS', 'ENGENHARIA QUÍMICA', 'ENGENHARIA DE PRODUÇÃO', 'ENGENHARIA AMBIENTAL', 'ENGENHARIA FLORESTAL', 'TECNOLOGIA EM SEGURANÇA NO TRABALHO']

courses_18 = ['DIREITO', 'CIÊNCIAS ECONÔMICAS', 'SERVIÇO SOCIAL', 'CIÊNCIAS CONTÁBEIS', 'ADMINISTRAÇÃO', 'RELAÇÕES INTERNACIONAIS', 'COMUNICAÇÃO SOCIAL - JORNALISMO', 'PSICOLOGIA', 'SECRETARIADO EXECUTIVO', 'TURISMO', 'TEOLOGIA', 'DESIGN', 'COMUNICAÇÃO SOCIAL - PUBLICIDADE E PROPAGANDA', 'ADMINISTRAÇÃO PÚBLICA', 'TECNOLOGIA EM GASTRONOMIA', 'TECNOLOGIA EM DESIGN DE MODA', 'TECNOLOGIA EM GESTÃO DE RECURSOS HUMANOS', 'TECNOLOGIA EM MARKETING', 'TECNOLOGIA EM GESTÃO FINANCEIRA', 'TECNOLOGIA EM DESIGN DE INTERIORES', 'TECNOLOGIA EM PROCESSOS GERENCIAIS', 'TECNOLOGIA EM GESTÃO DA QUALIDADE', 'TECNOLOGIA EM DESIGN GRÁFICO', 'TECNOLOGIA EM LOGÍSTICA', 'TECNOLOGIA EM GESTÃO COMERCIAL', 'TECNOLOGIA EM COMÉRCIO EXTERIOR', 'TECNOLOGIA EM GESTÃO PÚBLICA']

@app.route('/<path:year>/<path:type>/<path:raw_courses>', methods=['POST', 'GET'])
def login(year, type, raw_courses):
    raw_courses = raw_courses.replace('_', ' ')
    courses = raw_courses.split(';')
    print(courses)
    print(raw_courses)
    file = create(type=type, year=year, courses=courses)
    return send_file(file)
@app.route('/')
def index():
    return render_template('index.html', cursos2021 = courses_21, cursos2019 = courses_19, cursos2018 = courses_18)
