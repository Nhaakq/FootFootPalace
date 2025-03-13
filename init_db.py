from models import SessionLocal, Model

def init_db():
    db = SessionLocal()
    
    # Supprime les données existantes
    db.query(Model).delete()
    
    # Ajoute les modèles
    models_data = [
        {
            "name": "Brigitte",
            "description": "Toujours souriante et soucieuse de son hygiène, Brigitte sauras vous plaire grâce à sa voûte plantaire.",
            "avatar_path": "/static/img/model1_avatar.jpg",
            "gallery_folder": "brigitte"
        },
        {
            "name": "Stéphane",
            "description": "Stéphane est un passionné de la podologie et aime prendre soin de ses pieds. Ses orteils si gracieux vous rendront heureux.",
            "avatar_path": "/static/img/model2_avatar.jpg",
            "gallery_folder": "stephane"
        },
        {
            "name": "Nicole",
            "description": "Nicole est une sportive passionnée, ses pieds transpirent à la journée, une odeur qui va vous envoûter.",
            "avatar_path": "/static/img/model3_avatar.jpg",
            "gallery_folder": "nicole"
        }
    ]
    
    for data in models_data:
        model = Model(**data)
        db.add(model)
    
    db.commit()
    db.close()

if __name__ == "__main__":
    init_db() 