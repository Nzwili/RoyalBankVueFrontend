from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth

app = FastAPI()

# ✅ Allow your Vue frontend to connect
origins = [
    "http://localhost:5173",   # Vue dev server
    "http://127.0.0.1:5173",   # Sometimes Vue runs on 127.0.0.1
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],        # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],        # Allow all headers
)

# ✅ Include your routes
app.include_router(auth.router)
