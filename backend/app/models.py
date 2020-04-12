from app.database import db


wishlist_markers = db.Table('wishlist',
    db.Column('user_id', db.Integer, db.ForeignKey('Users.Id')),
    db.Column('marker_id', db.Integer, db.ForeignKey('Markers.Id'))
)

my_markers = db.Table('my',
    db.Column('user_id', db.Integer, db.ForeignKey('Users.Id')),
    db.Column('marker_id', db.Integer, db.ForeignKey('Markers.Id'))
)


class User(db.Model):
    __tablename__ = 'Users'
    Id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    Name = db.Column(db.Text(), nullable=True)
    Email = db.Column(db.Text(), nullable=False)
    DisplayName = db.Column(db.Text(), nullable=True)
    FamilyName = db.Column(db.Text(), nullable=True)
    RegistrationDate = db.Column(db.DateTime(), nullable=False)
    LastVisit = db.Column(db.DateTime(), nullable=False)

    wished_markers = db.relationship('Marker', secondary=wishlist_markers, backref='wishers')
    owned_markers = db.relationship('Marker', secondary=my_markers, backref='owners')
    cart_markers = db.relationship('Cart', backref='user')

    def to_dict(self):
        data = {
            'id': self.Id,
            'email': self.Email,
            'name': self.Name,
            'display_name': self.DisplayName,
            'family_name': self.FamilyName,
            'registration_date': self.RegistrationDate,
            'last_visit': self.LastVisit
            }
        return data


class Marker(db.Model):
    __tablename__ = 'Markers'
    Id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    Brand = db.Column(db.Text(), nullable=False)
    Series = db.Column(db.Text(), nullable=False)
    FullName = db.Column(db.Text(), nullable=False)
    ColorGroup = db.Column(db.Text(), nullable=True)
    ColorGroupFullName = db.Column(db.Text(), nullable=False)
    Hex = db.Column(db.Text(), nullable=False)
    ShortName = db.Column(db.Text(), nullable=False)

    carts = db.relationship('Cart', backref='marker')

    def __repr__(self):
        return self.Brand + self.Series + self.Hex

    def to_dict(self):
        data = {
            'id': self.Id,
            'full_name': self.FullName,
            'short_name': self.ShortName,
            'brand': self.Brand,
            'series': self.Series,
            'hex': self.Hex,
            'color_group_full_name': self.ColorGroupFullName,
            'color_group': self.ColorGroup
            }
        return data

    def by_brand_series_key(self):
        return self.Brand + self.Series


class Store(db.Model):
    __tablename__ = 'Stores'
    Id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    Name = db.Column(db.Text(), nullable=False)
    Site = db.Column(db.Text(), nullable=False)
    Logo = db.Column(db.Text(), nullable=False)

    def to_dict(self):
        data = {
            'id': self.Id,
            'name': self.Name,
            'site': self.Site,
            'logo': self.Logo
        }
        return data


class Cart(db.Model):
    __tablename__ = 'Carts'
    Id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    Amount = db.Column(db.Integer(), nullable=True)
    User_id = db.Column(db.Integer(), db.ForeignKey('Users.Id'))
    Marker_id = db.Column(db.Integer(), db.ForeignKey('Markers.Id'))


#class Price(db.Model):
#    __tablename__ = 'Prices'
#    marker_id = db.Column(db.Integer, db.ForeignKey('Markers.Id'))
#    store_id = db.Column(db.Integer, db.ForeignKey('Stores.Id'))
#    Value = db.Column(db.Integer(), nullable=False)

#    def to_dict(self):
#        data = {
#            'price': self.Price
#        }
#        return data
