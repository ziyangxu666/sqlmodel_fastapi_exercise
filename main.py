from typing import List
from sqlmodel import SQLModel, Field, Session, create_engine, select
from fastapi import FastAPI, Depends, HTTPException, status, Query

app = FastAPI()
engine = create_engine("sqlite:///./app.db", echo=False)

def get_session():
    with Session(engine) as s:
        yield s

class UserCreate(SQLModel): 
    name: str

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

class UserRead(SQLModel):
    id: int
    name: str

class UserUpdate(SQLModel):
    name: str | None = None

SQLModel.metadata.create_all(engine)

@app.post("/users",response_model=UserRead)
def create_user(data: UserCreate, s: Session = Depends(get_session)):
    u = User(name=data.name)
    s.add(u);s.commit();s.refresh(u)
    return u

@app.get("/users/{user_id}", response_model=UserRead)
def get_userid(user_id: int, s: Session = Depends(get_session)):
    u = s.get(User, user_id)
    if not u: raise HTTPException(404, "User not found")
    return u

@app.get("/users", response_model=List[UserRead])
def list_users(
    s: Session = Depends(get_session),
    offset: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),):
    stmt = select(User).order_by(User.id).offset(offset).limit(limit)
    return s.exec(stmt).all()


@app.patch("/users/{user_id}", response_model=UserRead)
def patch_name(user_id: int, data: UserUpdate, s: Session = Depends(get_session)):
    u = s.get(User, user_id)
    if not u: raise HTTPException(404, "User not found")
    if data.name is not None:   # 只在传了 name 时才更新
        u.name = data.name
    s.commit(); s.refresh(u)
    return u

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, s: Session = Depends(get_session)):
    u = s.get(User, user_id)
    if not u: raise HTTPException(204, "User not found")
    s.delete(u)
    s.commit()
    return