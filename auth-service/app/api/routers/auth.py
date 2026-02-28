from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

class RegisterReq(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginReq(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: RegisterReq):
        return {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "username": user.username,
        "email": user.email,
        "created_at": "2024-01-15T10:30:00Z",
        "message": "User registered successfully"
        }

@router.post("/login")
def login(user: LoginReq):
     return {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "token_type": "bearer",
            "user": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "username": user.username,
                "email": "john@example.com",
                "role": "user"
            }
        }

@router.post("/logout")
def logout(Auth):
    return {
        "message": "Successfully logged out"
    }