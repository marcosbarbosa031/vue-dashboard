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

class Card(db.Model):
    __tablename__ = 'credit_card'

    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.Integer, nullable=False)
    nome_cartao = db.Column(db.String(65), nullable=False)
    n_transacao = db.Column(db.String(65), nullable=True, default=None)
    tipo_cartao = db.Column(db.String(65), nullable=False)
    n_cartao = db.Column(db.String(65), nullable=False)
    n_order = db.Column(db.String(65), nullable=False)
    valor_brl = db.Column(db.Float, nullable=False)
    valor_usd = db.Column(db.Float, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    data = db.Column(db.String(65), nullable=False)
    status_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(30), nullable=False)
    motivo = db.Column(db.String(65), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(65), nullable=False)
    data_inicio = db.Column(db.String(65), nullable=True, default=None)
    data_fim = db.Column(db.String(65), nullable=True, default=None)
    tipo_pag = db.Column(db.String(20), nullable=True, default='a vista')
    recurrentId = db.Column(db.String(60), nullable=True, default=None)
    ip = db.Column(db.String(45), nullable=True, default=None)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def check_status(self):
        if self.status_id == 2:
            return True
        return False

    def update(self, nome_cartao, n_transacao, tipo_cartao, n_cartao, n_order, valor_brl,
               valor_usd, hora, data, status_id, status, motivo, currency, email, data_inicio,
               data_fim, tipo_pag):
        valor_anterior = self.valor_brl
        self.nome_cartao = nome_cartao
        self.n_transacao = n_transacao
        self.tipo_cartao = tipo_cartao
        self.n_cartao = n_cartao
        self.n_order = n_order
        self.valor_brl = valor_brl
        self.valor_usd = valor_usd
        self.hora = hora
        self.data = data
        self.status_id = status_id
        self.status = status
        self.motivo = motivo
        self.currency = currency
        self.email = email
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.tipo_pag = tipo_pag
        try:
            db.session.commit()
            if self.check_status():
                company = Company.get_company(self.empresa)
                company.update_saldo(valor_anterior, valor_brl)
            return 200
        except ConnectionRefusedError:
            return 500

    def cancel(self):
        self.status_id = 3
        self.status = "Pagamento Cancelado"
        try:
            db.session.commit()
            company = Company.get_company(self.empresa)
            company.decrease_saldo(self.valor_brl)
            return 200
        except ConnectionRefusedError:
            return 500

    def delete(self):
        c = self
        print(self)
        try:
            if self.check_status():
                print('entrou')
                company = Company.get_company(self.empresa)
                company.decrease_saldo(self.valor_brl)
            db.session.delete(c)
            db.session.commit()
            return 200
        except ConnectionRefusedError:
            return 500

    @staticmethod
    def serialize(card):
        return {
            'id': card.id,
            'empresa': card.empresa,
            'nome_cartao': card.nome_cartao,
            'n_transacao': card.n_transacao,
            'tipo_cartao': card.tipo_cartao,
            'n_cartao': card.n_cartao,
            'n_order': card.n_order,
            'valor_brl': card.valor_brl,
            'valor_usd': card.valor_usd,
            'hora': dump_time(card.hora),
            'data': dump_date(card.data),
            'status_id': card.status_id,
            'status': card.status,
            'motivo': card.motivo,
            'currency': card.currency,
            'email': card.email,
            'data_inicio': card.data_inicio,
            'data_fim': card.data_fim,
            'tipo_pag': card.tipo_pag,
            'recurrentId': card.recurrentId,
            'ip': card.ip
        }

    @staticmethod
    def get_cartao(card_id):
        card = Card.query.filter_by(id=card_id).first()
        if not card:
            return None
        else:
            return card

    @staticmethod
    def get_cards():
        card = Card.query.filter_by().order_by(Card.id.desc())

        if not card:
            response = {
                'error_msg': "There's no card to show.",
                'return': False
            }
        else:
            resp = [Card.serialize(aux) for aux in card]
            response = {
                'error_msg': False,
                'return': resp
            }
        return response