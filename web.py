from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import os
from models import get_db, Model

app = FastAPI()
templates = Jinja2Templates(directory="templates")
favicon_path = "./favicon.ico"
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, 'infos':{'status':0}})

@app.get("/choice", response_class=HTMLResponse)
async def choice_page(request: Request, db: Session = Depends(get_db)):
    models = db.query(Model).all()
    return templates.TemplateResponse("choice.html", {"request": request, "models": models})

@app.get("/gallery/{model_id}", response_class=HTMLResponse)
async def gallery(request: Request, model_id: int, db: Session = Depends(get_db)):
    model = db.query(Model).filter(Model.id == model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    
    # Récupérer les images de la galerie du modèle
    gallery_path = f"static/img/{model.gallery_folder}"
    gallery_images = []
    
    if os.path.exists(gallery_path):
        for img in os.listdir(gallery_path):
            if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                gallery_images.append({
                    "url": f"/static/img/{model.gallery_folder}/{img}",
                    "description": f"{model.name} - {img}"
                })
    
    gallery_data = {
        "model_name": model.name,
        "model_image": model.avatar_path,
        "model_description": model.description,
        "gallery_images": gallery_images
    }
    
    return templates.TemplateResponse("gallery_template.html", {"request": request, **gallery_data})

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)