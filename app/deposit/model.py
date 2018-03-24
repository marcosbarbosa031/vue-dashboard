from app import db, app_config
from run import config_name
from ..company.model import Company


def dump_date(data):
    """Deserialize datetime object into string form for JSON processing.
    :param data:
    """
    if data is None:
        return None
    return data.strftime("%Y-%m-%d")


class Deposit(db.Model):
    __tablename__ = 'deposito'

    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(65), nullable=False)
    valor_brl = db.Column(db.Float, nullable=False)
    valor_usd = db.Column(db.Float, nullable=False)
    moeda = db.Column(db.String(5), nullable=True, default='USD')
    data = db.Column(db.String(65), nullable=False)
    n_deposito = db.Column(db.Integer, nullable=False)
    imglink = db.Column(db.String(60), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    ip = db.Column(db.String(45), nullable=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def check_status(self):
        if self.status == 2:
            return True
        return False

    def update(self, dep_id, empresa, nome, valor_brl, valor_usd, moeda, data, n_deposito, imglink,
               status, ip):
        valor_anterior = float(self.valor_brl)
        self.id = dep_id
        self.empresa = empresa
        self.nome = nome
        self.valor_brl = valor_brl
        self.valor_usd = valor_usd
        self.moeda = moeda
        self.data = data
        self.n_deposito = n_deposito
        self.imglink = imglink
        self.status = status
        self.ip = ip
        try:
            db.session.commit()
            if self.check_status():
                company = Company.get_company(self.empresa)
                company.update_saldo(valor_anterior, valor_brl)
            return 200

        except ConnectionRefusedError:
            return 500

    def cancel(self):
        self.status = 1
        try:
            db.session.commit()
            company = Company.get_company(self.empresa)
            company.decrease_saldo(self.valor_brl)
            return 200
        except ConnectionRefusedError:
            return 500

    def delete(self):
        dep = self
        print(self)
        try:
            if self.check_status():
                company = Company.get_company(self.empresa)
                company.decrease_saldo(self.valor_brl)
            db.session.delete(dep)
            db.session.commit()
            return 200
        except ConnectionRefusedError:
            return 500

    @staticmethod
    def serialize(deposit):
        return {
            'id': deposit.id,
            'empresa': deposit.empresa,
            'nome': deposit.nome,
            'valor_brl': deposit.valor_brl,
            'valor_usd': deposit.valor_usd,
            'moeda': deposit.moeda,
            'data': dump_date(deposit.data),
            'n_deposito': deposit.n_deposito,
            'imglink': deposit.imglink,
            'status': deposit.status,
            'ip': deposit.ip
        }

    @staticmethod
    def get_depositos():
        dep = Deposit.query.filter_by().order_by(Deposit.id.desc())

        if not dep:
            response = {
                'error_msg': "There's no Boleto to show.",
                'return': False
            }
        else:
            resp = [Deposit.serialize(aux) for aux in dep]
            response = {
                'error_msg': False,
                'return': resp
            }
        return response

    @staticmethod
    def get_deposito(deposito_id):
        deposito = Deposit.query.filter_by(id=deposito_id).first()
        if not deposito:
            return None
        else:
            return deposito

