from app import db, app_config
from run import config_name


class Company(db.Model):
    __tablename__ = 'empresas'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    id_usuario = db.Column(db.Integer, nullable=False)
    doc_empresa = db.Column(db.String(65), nullable=False)
    nome_fantasia = db.Column(db.String(65), nullable=False)
    razao_social = db.Column(db.String(65), nullable=False)
    Saldo = db.Column(db.Float, nullable=False)
    Saldo_bloqueado = db.Column(db.Float, nullable=False)
    Saldo_disponivel = db.Column(db.Float, nullable=False)
    ativa = db.Column(db.Integer, nullable=False)
    Salt = db.Column(db.String(65), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def serialize(company):
        return {
            'id': company.id,
            'Salt': company.Salt,
            'ativa': company.ativa,
            'Saldo': company.Saldo,
            'id_usuario': company.id_usuario,
            'doc_empresa': company.doc_empresa,
            'razao_social': company.razao_social,
            'nome_fantasia': company.nome_fantasia,
            'Saldo_bloqueado': company.Saldo_bloqueado,
            'Saldo_disponivel': company.Saldo_disponivel
        }

    @staticmethod
    def get_companies():
        companies = Company.query.filter_by().order_by(Company.id)

        if not companies:
            response = {
                'error_msg': "There's no card to show.",
                'return': False
            }
        else:
            resp = [Company.serialize(aux) for aux in companies]
            response = {
                'error_msg': False,
                'return': resp
            }
        return response

    @staticmethod
    def get_company(company_id):
        company = Company.query.filter_by(id=company_id).first()
        if not company:
            return None
        else:
            return company

    def update_saldo(self, valor, atualizado):
        taxa = app_config[config_name].porcentage
        self.Saldo = (float(self.Saldo) - (float(valor) * taxa)
                      ) + (float(atualizado) * taxa)
        self.Saldo_disponivel = (float(
            self.Saldo_disponivel) - (float(valor) * taxa)) + (float(atualizado) * taxa)
        try:
            db.session.commit()
            return 200
        except ConnectionRefusedError:
            return 500

    def decrease_saldo(self, valor):
        taxa = app_config[config_name].porcentage
        val = valor * taxa
        self.Saldo -= val
        self.Saldo_disponivel -= val
        try:
            db.session.commit()
            return 200
        except ConnectionRefusedError:
            return 500
