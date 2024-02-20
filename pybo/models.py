# Created by user at 2024-02-14


from pybo import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True) #숫자
    username = db.Column(db.String(150),nullable=False) #문자, not null
    password = db.Column(db.String(200),nullable=False) #문자, not null
    email    = db.Column(db.String(320),nullable=False,unique=True) #문자, not null

class Question(db.Model):
    id = db.Column(db.Integer,primary_key=True) #숫자
    subject = db.Column(db.String(200),nullable=False) #문자
    contents = db.Column(db.Text(),nullable=False) #오라클 CLOB
    create_date = db.Column(db.DateTime(),nullable=False) #날짜
    #server_default, default : server_default는 기존 데이터에도 적용, default는 신규 데이터에만 적용
    user_id     = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE'),nullable=False)#User와 fk연결
    user        = db.relationship('User', backref=db.backref('question_set')) #User모델을 참조하기 위한 속성

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer,db.ForeignKey('question.id',ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    contents = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    #server_default, default : server_default는 기존 데이터에도 적용, default는 신규 데이터에만 적용
    user_id     = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE'),nullable=False)#User와 fk연결
    user        = db.relationship('User', backref=db.backref('answer_set')) #User모델을 참조하기 위한 속성
