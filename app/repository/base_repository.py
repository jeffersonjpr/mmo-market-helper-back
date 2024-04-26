from ..database import session

class BaseRepository:
    def create(self, model):
        session.add(model)
        session.commit()
        return model

    def get(self, model_id):
        return session.query(self.model).filter(self.model.id == model_id).first()

    def get_all(self):
        return session.query(self.model).all()

    def get_by_name(self, name):
        return session.query(self.model).filter(self.model.name == name).first()

    def delete(self, model_id):
        model = self.get(model_id)
        if model:
            session.delete(model)
            session.commit()
            return True
        return False