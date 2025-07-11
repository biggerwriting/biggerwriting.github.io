# 翻译 - 掌握Issues

https://guides.github.com/features/issues/



Issues 是一个跟踪项目的任务、增强、缺陷的好方法。它有点像电子邮件，还可以与团队成员分享和讨论。大部分软件项目有缺陷跟踪器，GitHub 的跟踪器就叫 __Issues__，在每个存储库中都有自己的部分。

![Highlighting navigation](https://guides.github.com/features/issues/navigation-highlight.png)



举个例子，我们来看下 [Bootstrap 的 Issues 部分](https://github.com/twbs/bootstrap/issues):

![List of issues](https://guides.github.com/features/issues/listing-screen.png)

GitHub 的issue 的特别之处在于：专注于协作、参考引用和出色的文本样式。一个典型的 issue 页面看起来像这样：

![An example issue](https://guides.github.com/features/issues/example-issue.png)

* 标题和描述描述了这个问题的全部内容。

* 颜色编码的标签有助于对问题进行分类和过滤（就像电子邮件中的标签一样）。

* 里程碑的作用就像一个问题的容器。这对于将问题与特定功能或项目阶段相关联非常有用（例如。每周冲刺9/5-9/16或航运1.0）。

* 一名受让人负责在任何特定时间处理该问题。

* 评论允许访问存储库的任何人提供反馈。

## 里程碑、标签和受让人
一旦你收集了很多问题，你可能会发现很难找到你关心的问题。里程碑、标签和受让人是筛选和分类问题的重要功能。

您可以通过单击右侧侧栏中的相应齿轮来更改或添加里程碑、受让人和标签。

![Viewing labels](https://guides.github.com/features/issues/labels.png)

如果您看不到编辑按钮，这是因为您没有编辑问题的权限。您可以要求存储库所有者将您添加为协作者以获得访问权限。

### 里程碑

![Viewing Milestones](https://guides.github.com/features/issues/milestones.png)

里程碑是与项目、功能或时间段相对应的一组问题。人们在软件开发中以许多不同的方式使用它们。GitHub上的里程碑示例包括：

* Beta启动：在启动项目的测试之前，您需要修复的文件错误。这是一个伟大的方式，以确保你没有错过任何东西。

* 10月冲刺：文件问题，您想在10月工作。一个伟大的方式集中你的努力时，有很多事情要做。

* 重新设计：与重新设计项目相关的文件问题。一个伟大的方式收集想法什么工作。

### 标签

标签是组织不同类型标签的好方法。问题可以有许多标签，也可以根据一个或多个标签过滤。

![Viewing label listings](https://guides.github.com/features/issues/labels-listing.png)



### 受让人

每个问题都可以有一个受让人——负责推进问题进展的人。和里程碑一样，通过问题上方的灰色条框选择受让人。

## 通知、@mentions和引用
通过在问题内部使用@mentions和引用，您可以通知其他GitHub用户和团队，并交叉问题到彼此。这些方法提供了一种灵活的方法，让合适的人参与到其中，以有效地解决问题，并且易于学习和使用。它们可以跨过GitHub上的所有文本字段，它们是我们称为GitHub风味标记 [GitHub Flavored Markdown](https://help.github.com/articles/writing-on-github#name-and-team-mentions-autocomplete)的文本格式语法的一部分。

![Example of Markdown](https://guides.github.com/features/issues/markdown-example.png)

PS：了解关于[Markdown](http://guides.github.com/features/mastering-markdown/)的内容

### 通知

通知是GitHub与您的问题保持最新的方式。您可以使用它们来了解资料库中的新问题，或者只是知道某人何时需要您的输入来推动某个问题。

有两种接收通知的方式：通过电子邮件和通过网络。您可以在设置中配置接收通知的方式。如果您计划接收大量通知，我们建议您对于要参加的活动通过web +电子邮件的方式通知，对于要观看的活动通过Web通知。

![Screenshot of notifications](https://guides.github.com/features/issues/notifications.png)

有了这些设置，当人们特别提到你时，你会收到电子邮件，然后访问基于Web的界面，以了解你感兴趣的资料库的最新信息。 

您可以通过通知屏幕访问您的通知。此屏幕非常适合一次扫描多个通知，并将它们标记为已读或静音线程。尝试使用键盘快捷键加快您的工作流程，按`?`查看哪些快捷方式可用。

![Screenshot of an individual notification](https://guides.github.com/features/issues/notification.png)

被静音的线程不会再次显示为未读，直到您再次被特别@提及。这使得静音对于你不太感兴趣的线程（也许你不太熟悉的子系统）是一个很好的策略。如果您将一个问题标记为已读，它将一直保持这种方式，直到有人再次对该线程进行评论。

GitHub还同步电子邮件通知的已读/未读状态†如果您在电子邮件客户端中阅读通知，它将在基于Web的界面被标记为已读（如果您喜欢此功能，请确保允许电子邮件客户端显示图像）。

### @mentions

@mentions是我们在GitHub问题中引用其他GitHub用户的方式。在问题描述或任何评论中，包括另一个GitHub用户的@username，以向他们发送通知。这与Twitter使用@mentions的方式非常相似。

我们喜欢使用`/cc`语法（抄送的缩写）将人员包含在问题中：

> 看起来新的小部件在Safari上被破坏了。当我尝试创建小部件时， Safari崩溃了。这在10.8上可以重现，但不能在10.9上重现。可能是浏览器的错误？
>
>  /cc @kneath @jresig

如果您知道要包括的特定用户，这工作很好，但很多时候我们跨团队工作，不知道谁可能能够帮助我们。@mentions也适用于您的GitHub组织内的Teams。如果在@acmeinc组织下创建了一个名为browser-bugs的Team，可以使用@mentions引用该Team：

> /cc @acmeinc/browser-bugs

这将向浏览器缺陷小组的每个成员发送通知。

### 参考信息

很多时候，问题依赖于其他问题，或者至少与它们相关，您希望将两者联系起来。您可以通过键入哈希标签加上问题编号来引用问题。

> Hey @kneath, I think the problem started in #42

当您执行此操作时，我们将在 issue #42 中创建一个事件，其内容类似：

![Screenshot of creating a reference](https://guides.github.com/features/issues/reference.png)

在另一个存储库中发出问题？只需在名称前包括存储库，如`kneath/example-project#42`。

使用GitHub问题的一个更有趣的方法是直接从提交中引用问题。在提交消息中包括问题编号。

![Screenshot of referencing a commit](https://guides.github.com/features/issues/commit.png)

通过在提交合并到main时，在提交前加上“Fixes”、“Fixed”、“Fix”、“Closes”、“Closed”或“Closed”，问题也会自动关闭。 

引用使人们能够将正在完成的工作与正在跟踪的错误深度联系起来，并且是将项目历史的可见性增加的好方法。

## 搜索

在每个页面的最顶端有一个搜索框，可以让你搜索所有问题。

![Screenshot of making a search](https://guides.github.com/features/issues/search.png)

搜索结果的范围可以通过以下方式确定：

* 关键字，如 [所有问题提到侧边栏](https://github.com/twbs/bootstrap/issues?q=sidebar)

* 声明，例如， [所有提及已关闭的侧边栏的问题](https://github.com/twbs/bootstrap/issues?q=sidebar+is%3Aclosed)
* 受让人，例如，[所有提到分配给@mdo的侧边栏的问题](https://github.com/twbs/bootstrap/issues?q=sidebar+is%3Aclosed+assignee%3Amdo)

我们关于[搜索问题的帮助文章](https://help.github.com/articles/using-search-to-filter-issues-and-pull-requests) 可以向您展示其他搜索方式：使用创建/更新的日期、标签、作者、评论计数、按存储库所有者进行搜索等。

## 概述和报告

在“问题”部分之外，还有另外两个页面可以帮助总结您的资料库和所有资料库中的问题发生的情况。

### 问题控制面板

如果您正在寻找一个更广泛地列出所有项目的问题， [问题仪表板](https://github.com/issues) 可以是一个很好的工具。仪表板的工作方式与问题部分非常相似，但收集问题的方式不同：

* 您拥有并协作存储库中的所有问题 
* 分配给您的问题 
* 您创建的问题

如果您使用组织，则每个组织都有自己的问题控制面板，该控制面板将组织内的问题分开。

### 脉冲

每个存储库下面有一个名为“脉冲”的部分，脉冲是存储库过去一周（或一天，或过去3个月等）中发生的所有事情的快照。

![Screenshot of the Pulse feature](https://guides.github.com/features/issues/pulse.png)

当您离开时，如果不想观看细粒度的资料库通知，那么它是一个很好的查看资料库的方法。

## 问题的其他用途

问题对于跟踪各种事情都很好，GitHub是一个轻松分享和协作问题的好地方。以下是我们最喜欢的一些：

* [开源项目的Bug跟踪程序](https://github.com/joyent/node/issues)
* [食谱请求](https://github.com/newmerator/recipes/issues)（也许你有一个好的[无麸质披萨面团食谱](https://github.com/newmerator/recipes/issues/3)?）

## 结语

**现在恭喜你自己吧**，这可是读了很多!问题管理是任何开发人员都可以使用的最强大的工具之一。我想剩下的就是现在真正修复错误了。




