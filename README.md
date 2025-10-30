# Users Mini API — FastAPI + SQLModel + SQLite
English / 日本語 / 中文

---

## English

### Overview
A tiny FastAPI + SQLModel + SQLAlchemy project demonstrating CRUD for a single entity `User` on SQLite.

**What it shows**
- Pydantic-style request/response schemas: `UserCreate`, `UserRead`, `UserUpdate`
- SQLModel table model: `User`
- SQLAlchemy session usage: `create_engine`, `Session`, `commit`, `refresh`
- FastAPI routes: Create / Read / List (pagination) / Patch / Delete

### Requirements
- Python 3.11+
- See `requirements.txt`

### Quick Start
```bash
# 0) (optional) create venv
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 1) install
pip install -r requirements.txt

# 2) run
uvicorn main:app --reload
# -> http://127.0.0.1:8000/docs

| Method | Path               | Purpose                 | Params / Body                          | Response           |
| -----: | ------------------ | ----------------------- | -------------------------------------- | ------------------ |
|   POST | `/users`           | Create a user           | body: `{"name":"Alice"}`               | `UserRead`         |
|    GET | `/users/{user_id}` | Get a user by id        | path: `user_id:int`                    | `UserRead`         |
|    GET | `/users`           | List users (pagination) | query: `offset>=0`, `1<=limit<=100`    | `List[UserRead]`   |
|  PATCH | `/users/{user_id}` | Partially update `name` | body: `{"name":"New Name"}` (optional) | `UserRead`         |
| DELETE | `/users/{user_id}` | Delete a user           | path: `user_id:int`                    | **204 No Content** |

Quick Test (curl)
# Create
curl -sX POST http://127.0.0.1:8000/users \
  -H 'Content-Type: application/json' -d '{"name":"Alice"}'

# Get by id
curl -s http://127.0.0.1:8000/users/1

# List with pagination
curl -s 'http://127.0.0.1:8000/users?offset=0&limit=2'

# Patch name
curl -sX PATCH http://127.0.0.1:8000/users/1 \
  -H 'Content-Type: application/json' -d '{"name":"Alice Chen"}'

# Delete (expects 204)
curl -i -X DELETE http://127.0.0.1:8000/users/1

Notes

UserUpdate.name is optional; only provided fields are updated.

Ensure tables exist at startup (e.g., call SQLModel.metadata.create_all(engine)).

To reset, stop the server and delete app.db, then start again.

日本語
概要

SQLite を使った FastAPI + SQLModel + SQLAlchemy の極小 CRUD デモです。

ポイント

Pydantic 風入出力スキーマ: UserCreate, UserRead, UserUpdate

SQLModel テーブルモデル: User

SQLAlchemy セッション: create_engine, Session, commit, refresh

エンドポイント: 作成 / 取得 / 一覧（ページング）/ 部分更新 / 削除

事前準備

Python 3.11+

requirements.txt を参照

使い方
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
# → http://127.0.0.1:8000/docs
|   メソッド | パス                 | 目的           | パラメータ / ボディ                       | 応答                 |
| -----: | ------------------ | ------------ | --------------------------------- | ------------------ |
|   POST | `/users`           | ユーザー作成       | ボディ: `{"name":"Alice"}`           | `UserRead`         |
|    GET | `/users/{user_id}` | ID 取得        | パス: `user_id:int`                 | `UserRead`         |
|    GET | `/users`           | 一覧（ページング）    | クエリ: `offset>=0`, `1<=limit<=100` | `List[UserRead]`   |
|  PATCH | `/users/{user_id}` | `name` の部分更新 | ボディ: `{"name":"New Name"}`（任意）    | `UserRead`         |
| DELETE | `/users/{user_id}` | ユーザー削除       | パス: `user_id:int`                 | **204 No Content** |
動作確認（curl）

（英語セクションのコマンドをご利用ください）

注意

UserUpdate.name は任意。指定フィールドのみ更新します。

起動時に SQLModel.metadata.create_all(engine) でテーブル作成を行ってください。

リセットするには app.db を削除して再起動。

中文
简介

使用 FastAPI + SQLModel + SQLAlchemy + SQLite 的超小型 CRUD 示例。

包含

请求/响应模型：UserCreate, UserRead, UserUpdate

表模型：User

会话与事务：create_engine, Session, commit, refresh

路由：新增 / 按ID查询 / 分页列表 / 部分更新 / 删除

环境

Python 3.11+

依赖见 requirements.txt

运行
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
# → http://127.0.0.1:8000/docs
|     方法 | 路径                 | 说明          | 入参                               | 返回                 |
| -----: | ------------------ | ----------- | -------------------------------- | ------------------ |
|   POST | `/users`           | 新建用户        | 体: `{"name":"Alice"}`            | `UserRead`         |
|    GET | `/users/{user_id}` | 按 ID 查询     | 路径: `user_id:int`                | `UserRead`         |
|    GET | `/users`           | 分页列表        | 查询: `offset>=0`, `1<=limit<=100` | `List[UserRead]`   |
|  PATCH | `/users/{user_id}` | 部分更新 `name` | 体: `{"name":"New Name"}`（可选）     | `UserRead`         |
| DELETE | `/users/{user_id}` | 删除用户        | 路径: `user_id:int`                | **204 No Content** |


备注

UserUpdate.name 设为可选，仅更新传入字段。

启动时确保建表（SQLModel.metadata.create_all(engine)）。

重置：删除 app.db 后重启。