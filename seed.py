from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="Vanilla",
    size="medium",
    rating=5,
)
c2 = Cupcake(
    flavor="Tiramisu",
    size="Small",
    rating=9.5,
)
c3 = Cupcake(
    flavor="Orange",
    size="medium",
    rating=3,
)
c4 = Cupcake(
    flavor="Boston Cream",
    size="small",
    rating=2,
)

c5 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

db.session.add_all([c1, c2, c3, c4, c5])
db.session.commit()