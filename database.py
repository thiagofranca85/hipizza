from sqlmodel import SQLModel, create_engine
import models.model_hipizza

engine = create_engine("sqlite:///database.db")


SQLModel.metadata.create_all(engine)