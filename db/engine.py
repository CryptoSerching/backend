from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# .envファイルをロード
load_dotenv()

# 環境変数から接続URLを取得
DATABASE_URL = os.getenv("POSTGRES")

if DATABASE_URL is None:
    raise ValueError("環境変数 POSTGRES が設定されていません")

# エンジンの作成
Engine = create_engine(DATABASE_URL)
Base = declarative_base()


