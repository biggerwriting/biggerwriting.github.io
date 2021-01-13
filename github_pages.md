layout: page
title: "10分钟开启 Github Pages 之旅"
permalink: /github_pages/

# 10分钟开启 Github Pages 之旅

GitHub页面是托管的公共网页，可以通过GitHub轻松发布。 最快的启动和运行方式是使用Jekyll Theme Chooser加载预制主题。 然后，您可以通过Web远程或在计算机上本地修改GitHub Pages的内容和样式。

![pages-home-page](https://guides.github.com/features/pages/pages-home-page.png)



## 建立您的网站 

登录后，您将创建一个新的存储库以开始使用。

![new-repo-button](https://guides.github.com/features/pages/create-new-repo-button.png)



在新建存储库页面上，需要为该存储库指定一个特殊名称以生成您的网站。

![new-repo-screen](https://guides.github.com/features/pages/create-new-repo-screen.png)

您网站的文件将存储在名为`username.github.io`（其中“用户名”是您实际的GitHub用户名）的存储库中。 要开始设置您的网站，您必须打开“设置”标签

![settings-tab](https://guides.github.com/features/pages/repo-settings.png)



如果您在设置页面上向下滚动，则会在底部附近看到“ GitHub页面”部分。 单击选择主题按钮以开始创建网站的过程。

![launch-theme-chooser](https://guides.github.com/features/pages/launch-theme-chooser.png)



单击该按钮后，您将被定向到主题选择器。 您会在页面顶部的轮播中看到几个主题选项。 单击图像以预览主题。 选择一个主题后，单击右侧的“选择主题”继续。 以后更改主题很容易，因此，如果不确定，就暂时选择一个。

![theme-chooser](https://guides.github.com/features/pages/theme-chooser.png)



在这里您将编写自己的内容（如果需要，您可以暂时保留默认内容）。

![code-editor](https://guides.github.com/features/pages/code-editor.png)



完成修改后，向下滚动到页面底部，然后点击提交更改。

![commit-edits](https://guides.github.com/features/pages/commit-edits.png)

GitHub负责将访问者定向到`username.github.io`以查看您的新网站。 这最多可能需要10分钟。 经过一段时间后，您可以在浏览器中打开一个新标签来访问您的网站！



## 做出改变 

您可以做的第一件事就是删除索引页面的默认标题，并向其中添加友好的消息。 由于这是一个非常快的更改，也是您的第一个更改，因此您将在默认分支：main上进行更改。

通过在“代码”选项卡中导航到_`config.yml`文件来查看它。 您可以通过单击铅笔图标来编辑文件。

![edit-page](https://guides.github.com/features/pages/edit-file.png)





目前，您的网站没有设置标题，因此我们回到仓库的名称上。要更改此设置，我将添加一行：`title: Welcome to the Octocat’s homepage!` 到这个文件。 除了您自己的用户名之外，其他都可以随意修改。 

在此标题下，您可以添加有关页面用途的消息，并描述您希望人们在这里时要做什么。 我将设置为`Feel free to bookmark this to keep an eye on my project updates`

![change-title-description](https://guides.github.com/features/pages/change-title-description.png)

完成较小的更改后，请滚动至页面底部以进行第二次提交。 关于此更改，您有两个地方可以写：主题和扩展说明。 扩展说明是可选的，因此让我们在主题中留下描述性信息。 

完成后，点击提交更改，您的更新将在几秒钟内生效！

![be-descriptive](https://guides.github.com/features/pages/commit-messages-matter.png)

