# 数据目录说明（隐私保护）

`data/` 存放使用者的**真实个人数据**，默认被 `.gitignore` 忽略，**绝不提交到仓库**。

## 目录结构

```
data/
├── _templates/          # 首次使用复制的空模板（本目录随仓库提交）
│   ├── trace.template.md          # 思维轨迹模板
│   ├── profile.template.md        # 偏好画像模板
│   └── perspective.template.md    # 视角银行模板
├── traces/              # 每次完整思考的轨迹档案（本地，不提交）
├── profiles/            # 跨次思考的偏好画像（本地，不提交）
└── perspectives/        # 跨问题复用的视角银行（本地，不提交）
```

## 首次使用

```bash
mkdir -p data/traces data/profiles data/perspectives
cp data/_templates/trace.template.md      data/traces/
cp data/_templates/profile.template.md    data/profiles/
cp data/_templates/perspective.template.md data/perspectives/
```

## 隐私规则

1. 轨迹 / 画像 / 视角银行包含真实决策信息与个人偏好——**任何情况下不提交**。
2. 示例演示请使用 `_templates/` 中的模板。
3. 想分享学习成果？请把真实数据改写为虚构示例后再提交。
