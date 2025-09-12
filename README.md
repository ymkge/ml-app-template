# FastAPI + scikit-learn MLアプリケーションテンプレート

これは、FastAPI、scikit-learn、Dockerを使用し、GitHub ActionsによるCI/CDパイプラインを備えた機械学習アプリケーションのテンプレートプロジェクトです。

## このテンプレートから学べること

このリポジトリは、機械学習モデルをWebアプリケーションとしてデプロイするための、実践的なテンプレートです。このリポジトリから、以下のことを体系的に学べます。

### 1. 機械学習モデルのAPI化
- **FastAPI**: PythonのモダンなWebフレームワークであるFastAPIを使い、学習済みモデル（scikit-learn）を推論APIとして外部に提供する方法。
- **データバリデーション**: Pydanticを利用して、APIが受け取る入力データの型や構造を定義し、バリデーションをかける方法。

### 2. コンテナ技術の活用 (Docker)
- **Dockerfile**: Pythonアプリケーションを実行環境ごとパッケージ化するためのDockerfileの書き方。
- **Docker Compose**: ローカルでの開発環境を簡単に立ち上げるための `docker-compose.yml` の設定方法。コードの変更を即座に反映させる（ホットリロード）設定も含まれています。

### 3. CI/CDによる開発・デプロイの自動化
- **GitHub Actions**: GitHubにコードをプッシュしたタイミングで、以下のような一連の処理を自動実行するCI/CDパイプラインの構築方法。
    - **モデルの自動トレーニング**: 新しいコードでモデルを再学習する。
    - **Dockerイメージのビルド**: アプリケーションをDockerイメージとしてビルドし、GitHub Container Registryに登録する。
    - **本番環境への自動デプロイ**: Render.comのようなPaaS（Platform as a Service）に、ビルドしたイメージを自動でデプロイする。

### 4. 実践的なプロジェクト構成
- **関心の分離**: モデルを学習させるコード (`train.py`) と、推論APIを提供するコード (`app/`) が分離されており、見通しの良いプロジェクト構成を学べます。
- **依存関係の管理**: `requirements.txt` を使って、プロジェクトが依存するPythonライブラリを管理する方法。

要約すると、**「scikit-learnで作成したモデルを、Dockerコンテナ上で動くFastAPIアプリとして公開し、その一連のプロセス（テスト、ビルド、デプロイ）をGitHub Actionsで自動化する」** という、モダンな機械学習アプリケーション開発のベストプラクティスを学ぶことができます。

## プロジェクト構成

```
ml-app-template/
├── app/
│   ├── main.py         # FastAPIのエントリーポイント
│   ├── model.py        # モデルの読み込みと予測
│   ├── utils.py        # ヘルパー関数
│   ├── data.csv        # 訓練データ
│   └── model.pkl       # 訓練済みモデルファイル (CI/CD実行時に生成)
├── train.py            # モデル再訓練スクリプト
├── requirements.txt    # 依存関係
├── Dockerfile          # Dockerコンテナ定義
├── docker-compose.yml  # ローカル開発用
├── .github/
│   └── workflows/
│       └── ci-cd.yml   # GitHub Actions CI/CD パイプライン
└── README.md
```

## はじめに

### ローカル開発

1.  **コンテナをビルドして実行します:**
    ```bash
    docker-compose up --build
    ```
    アプリケーションは `http://localhost:8000` で利用可能になります。

2.  **エンドポイントをテストします:**
    -   ヘルスチェック: `curl http://localhost:8000/health`
    -   予測:
        ```bash
        curl -X POST "http://localhost:8000/predict" \
        -H "Content-Type: application/json" \
        -d '{"feature1": 0.5, "feature2": 0.5}'
        ```

### モデルの再訓練

1.  必要に応じて、新しいデータで **`app/data.csv` を更新します**。

2.  **訓練スクリプトを実行します:**
    ```bash
    python3 train.py
    ```
    これにより、`app/model.pkl` が新しく訓練されたモデルで上書きされます。

3.  **新しいモデルを含めるためにDockerイメージを再ビルドします:**
    ```bash
    docker-compose up --build
    ```

## CI/CDパイプライン

CI/CDパイプラインは `.github/workflows/ci-cd.yml` で設定されており、アプリケーションのテスト、ビルド、デプロイを自動化します。

### フロー

1.  **トリガー**: `main` ブランチへのプッシュ。
2.  **モデル訓練**: `train.py` を実行してモデルを生成します。
3.  **Lint & テスト**: (プレースホルダー) リンターとテストを実行します。
4.  **ビルド & プッシュ**: Dockerイメージをビルドし、GitHub Container Registryにプッシュします。
5.  **デプロイ**: Render.comのデプロイフックを使用して、新しいデプロイをトリガーします。

### セットアップ

CI/CDパイプラインを機能させるには、GitHubリポジトリで次のシークレットを設定する必要があります (`Settings > Secrets and variables > Actions`)。

-   `RENDER_API_KEY`: RenderからのAPIキー。
-   `RENDER_SERVICE_ID`: デプロイ先のRender上のサービスのID。

DockerイメージはGitHub Container Registryにプッシュされ、これはリポジトリで自動的に有効になるはずです。Renderサービスをこのコンテナレジストリに接続する必要があります。
