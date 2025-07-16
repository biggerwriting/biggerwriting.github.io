---
title: 'Washing Mathine'
date: '2025-07-16T22:46:54+08:00'
draft: true
author: 王十二
---
这里写文章的摘要
<!--more-->
这里可以填充文章细节

在 Go 中，math.Round 函数用于将浮动数四舍五入到最接近的整数。如果你想在 Go 模板中使用 math.Round，你需要将其作为一个自定义函数来传递到模板中。
下面是如何在 Go 模板中使用 math.Round 的步骤：

1.导入相关包：
首先，需要导入 math 包和 text/template 包。

```
   import (
       "fmt"
       "math"
       "text/template"
   )
```

2.定义模板并传递函数：
然后，在创建模板时，可以将 math.Round 函数作为模板的自定义函数传递。

```
   func main() {
       // 创建模板并传递自定义函数
       funcMap := template.FuncMap{
           "round": math.Round,
       }

       tmpl, err := template.New("roundExample").Funcs(funcMap).Parse("原始值: {{.Value}}, 四舍五入后的值: {{.Value | round}}\n")
       if err != nil {
           panic(err)
       }

       // 创建数据对象
       data := struct {
           Value float64
       }{
           Value: 3.14159,
       }

       // 执行模板
       err = tmpl.Execute(os.Stdout, data)
       if err != nil {
           panic(err)
       }
   }
```

3.运行示例：
如果运行这段代码，输出将是：

   原始值: 3.14159, 四舍五入后的值: 3

这样，你就可以在 Go 模板中使用 math.Round 来四舍五入浮动数了。