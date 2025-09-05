# FastAPI + scikit-learn MLアプリケーションテンプレート

これは、FastAPI、scikit-learn、Dockerを使用し、GitHub ActionsによるCI/CDパイプラインを備えた機械学習アプリケーションのテンプレートプロジェクトです。

## プロジェクト構成

```
ml-app-template/
├── app/
│   ├── main.py         # FastAPIのエントリーポイント
│   ├── model.py        # モデルの読み込みと予測
│   ├── utils.py        # ヘルパー関数
│   ├── data.csv        # 訓練データ
│   └── model.pkl       # 訓練済みモデルファイル
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
2.  **Lint & テスト**: (プレースホルダー) リンターとテストを実行します。
3.  **ビルド & プッシュ**: Dockerイメージをビルドし、GitHub Container Registryにプッシュします。
4.  **デプロイ**: Render.comのデプロイフックを使用して、新しいデプロイをトリガーします。

### セットアップ

CI/CDパイプラインを機能させるには、GitHubリポジトリで次のシークレットを設定する必要があります (`Settings > Secrets and variables > Actions`)。

-   `RENDER_API_KEY`: RenderからのAPIキー。
-   `RENDER_SERVICE_ID`: デプロイ先のRender上のサービスのID。

DockerイメージはGitHub Container Registryにプッシュされ、これはリポジトリで自動的に有効になるはずです。Renderサービスをこのコンテナレジストリに接続する必要があります。