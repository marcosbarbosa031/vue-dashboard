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

def dump_time(data):
    """Deserialize datetime object into string form for JSON processing.
    :param data:
    """
    if data is None:
        return None
    return data.strftime("%H:%M:%S")

class Boleto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.Date, nullable=False)
    data = db.Column(db.Date, nullable=False)
    d_vencimento = db.Column(db.String(65), nullable=False)
    documento = db.Column(db.String(65), nullable=False)
    num_pedido = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(65), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False)
    valor_brl = db.Column(db.Float, nullable=False)
    valor_moeda = db.Column(db.Float, nullable=False)
    moeda = db.Column(db.String(65), nullable=False)
    status = db.Column(db.Integer, default=1)
    verify = db.Column(db.String(70), nullable=True)
    hora = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return '<ID {}>\n<Valor {}>\n<Status {}>\n<Empresa {}>'.format(self.id, self.valor_brl, self.status, self.empresa)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def check_status(self):
        if int(self.status) == 2:

            return True
        return False

    def update(self, nome, data, d_vencimento, documento, num_pedido, cod_barra, email, valor_brl,
               valor_moeda, moeda, hora):
        valor_anterior = float(self.valor_brl)
        self.nome = nome
        self.data = data
        self.d_vencimento = d_vencimento
        self.documento = documento
        self.num_pedido = num_pedido
        self.cod_barra = cod_barra
        self.email = email
        self.valor_brl = valor_brl
        self.valor_moeda = valor_moeda
        self.moeda = moeda
        self.hora = hora
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
        bol = self
        print(self)
        try:
            if self.check_status():
                company = Company.get_company(self.empresa)
                company.decrease_saldo(self.valor_brl)
            db.session.delete(bol)
            db.session.commit()
            return 200
        except ConnectionRefusedError:
            return 500

    @staticmethod
    def serialize(boleto):
        return {
            'id': boleto.id,
            'empresa': boleto.empresa,
            'nome': boleto.nome,
            'data': dump_date(boleto.data),
            'd_vencimento': dump_date(boleto.d_vencimento),
            'documento': boleto.documento,
            'num_pedido': boleto.num_pedido,
            'cod_barra': boleto.cod_barra,
            'email': boleto.email,
            'valor_brl': boleto.valor_brl,
            'valor_moeda': boleto.valor_moeda,
            'moeda': boleto.moeda,
            'status': boleto.status,
            'verify': boleto.verify,
            'hora': dump_time(boleto.hora)
        }

    @staticmethod
    def get_boleto(boleto_id):
        boleto = Boleto.query.filter_by(id=boleto_id).first()
        if not boleto:
            return None
        else:
            return boleto

    @staticmethod
    def get_boletos():
        bol = Boleto.query.filter_by().order_by(Boleto.id.desc())

        if not bol:
            response = {
                'error_msg': "There's no Boleto to show.",
                'return': False
            }
        else:
            resp = [Boleto.serialize(aux) for aux in bol]
            response = {
                'error_msg': False,
                'return': resp
            }
        return response
