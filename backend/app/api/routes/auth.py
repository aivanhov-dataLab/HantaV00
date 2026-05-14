# FastAPI router
from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

# OAuth2 form
from fastapi.security import (
    OAuth2PasswordRequestForm
)

# SQLAlchemy session
from sqlalchemy.orm import Session

# DB dependency
from app.db.database import get_db

# Auth service
from app.auth.auth_service import (
    create_user,
    authenticate_user
)

# JWT token creation
from app.auth.security import (
    create_access_token
)

# Schemas
from app.schemas.user import (
    UserCreate,
    UserResponse
)


# Router auth
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# Route création utilisateur
@router.post(
    "/register",
    response_model=UserResponse
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user(
        db,
        user
    )


# Route login
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # Création JWT
    access_token = create_access_token(
        data={
            "sub": user.username
        }
    )

    return {

        "access_token": access_token,
        "token_type": "bearer"
    }