import json
import os

# 读取产品数据
with open('data/products.json') as f:
    products = json.load(f)

# 为每个产品创建 Markdown 文件
for product in products:
    path = f"content/products/{product['slug']}.md"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # 写入 Markdown 内容（Hugo 自动识别 Front Matter）
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"""---
title: "{product['name']}"
product_id: "{product['id']}"
# 其他元数据...
---

产品详情内容...
""")