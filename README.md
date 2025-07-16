# 创建新的hugo主题用于写博客

## 初始化hugo

hugo new site biggerwriting --format yaml

## 设计首页

因为自己实在没啥审美且不会写样式，就请先写出最丑的原始版本再去优化吧。

关联到网站 [aiwith.fun](https://aiwith.fun)


## 部署到netlify
hugo --minify --baseURL $DEPLOY_PRIME_URL

### 需要安装
~~npm install hugo-cli --save-dev~~

### 本地预览
hugo server -e production --minify --cleanDestinationDir

### 官网参考文档
https://gohugo.io/host-and-deploy/host-on-netlify/

### 新建了模板
`hugo new content/otherfolder/notebook.md -k projects`
`hugo new projects/awesomeco.md`

## 代码语法高亮
hugo gen chromastyles --style=github > syntax.css
可以生成样式文件，但是不会用
