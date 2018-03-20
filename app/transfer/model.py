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

class Transfer(db.Model):
    __tablename__ = 'transferencia'
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(65), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    valor_compra = db.Column(db.Float, nullable=False)
    valor_deposit = db.Column(db.Float, nullable=False)
    valor_currency = db.Column(db.Float, nullable=False)
    banco = db.Column(db.Integer, nullable=False)
    banco_name = db.Column(db.String(30), nullable=False)
    banco_img = db.Column(db.String(60), nullable=False)
    data = db.Column(db.String(65), nullable=False)
    n_transferencia = db.Column(db.Integer, nullable=False)
    imglink = db.Column(db.String(60), nullable=False)
    status_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    ip = db.Column(db.String(45), nullable=True, default=None)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def check_status(self):
        if self.status_id == 2:
            return True
        return False

    @staticmethod
    def serialize(transfer):
        return {
            'id': transfer.id,
            'empresa': transfer.empresa,
            'nome': transfer.nome,
            'currency': transfer.currency,
            'valor_compra': transfer.valor_compra,
            'valor_deposit': transfer.valor_deposit,
            'valor_currency': transfer.valor_currency,
            'banco': transfer.banco,
            'banco_name': transfer.banco_name,
            'banco_img': transfer.banco_img,
            'data': dump_date(transfer.data),
            'n_transferencia': transfer.n_transferencia,
            'imglink': transfer.imglink,
            'status_id': transfer.status_id,
            'status': transfer.status,
            'ip': transfer.ip
        }

    @staticmethod
    def get_transfers():
        transfer = Transfer.query.filter_by().order_by(Transfer.id.desc())

        if not transfer:
            response = {
                'error_msg': "There's no card to show.",
                'return': False
            }
        else:
            resp = [Transfer.serialize(aux) for aux in transfer]
            response = {
                'error_msg': False,
                'return': resp
            }
        return response

    @staticmethod
    def get_transfer(transfer_id):
        trans = Transfer.query.filter_by(id=transfer_id).first()
        if not trans:
            return None
        else:
            return trans

    def update(self, nome, currency, valor_compra, valor_deposit, valor_currency, banco, banco_name,
               data, n_transferencia, imglink, status_id, status):
        valor_anterior = float(self.valor_deposit)
        self.nome = nome
        self.currency = currency
        self.valor_compra = valor_compra
        self.valor_deposit = valor_deposit
        self.valor_currency = valor_currency
        self.banco = banco
        self.banco_name = banco_name
        self.data = data
        self.n_transferencia = n_transferencia
        self.imglink = imglink
        self.status_id = status_id
        self.status = status
        try:
            db.session.commit()
            if self.check_status():
                company = Company.get_company(self.empresa)
                company.update_saldo(valor_anterior, valor_deposit)
            return 200

        except ConnectionRefusedError:
            return 500
