class Repository:
    def __init__(self, model, session):
        self.model = model
        self.session = session

    def get(self, id):
        return self.session.query(self.model).filter(self.model.id == id).first()

    def get_all(self):
        return self.session.query(self.model).all()

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def update(self, entity):
        self.session.merge(entity)
        self.session.commit()

    def delete(self, id):
        entity = self.get(id)
        if entity:
            self.session.delete(entity)
            self.session.commit()