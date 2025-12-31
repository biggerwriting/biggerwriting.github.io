# 为什么用Spring Boot搭建Web应用，开发者都说“快到飞起”？

## 前置条件


`java -version `
openjdk version "17.0.10" 2024-01-16

`mvn -v`
Apache Maven 3.9.11

## 通过 Maven 设置项目

```pox.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

	<groupId>com.example</groupId>
	<artifactId>myproject</artifactId>
	<version>0.0.1-SNAPSHOT</version>

	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>4.0.1</version>
	</parent>

	<!-- Additional lines to be added here... -->

</project>
```

可以通过 `mvn package` 测试一下。

## 添加依赖包
一开始是没有任何依赖的，执行 `mvn dependency:tree` 就能知道。
接着在 `<parent>` 标签组后面添加 `spring-boot-starter-web` 依赖。

**pom.xml**
```xml
<dependencies>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-web</artifactId>
	</dependency>
</dependencies>
```
再次运行 `mvn dependency:tree` 可以发现添加了 tomcat 服务器。

## 写代码
创建文件 `src/main/java/com/example/MyApplication.java` 。可以使用以下命令：

```bash
mkdir -p src/main/java/com/example
vim src/main/java/com/example/MyApplication.java
```

**MyApplication.java**
```java
package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication
public class MyApplication {

	@RequestMapping("/")
	String home() {
		return "Hello World!";
	}

	public static void main(String[] args) {
		SpringApplication.run(MyApplication.class, args);
	}

}
```

## 运行程序
执行 `mvn spring-boot:run` ，项目启动完后可以访问 [localhost:8080](http://localhost:8080) ，会看到以下输出： `Hello World!` 。

通过 `control + C` 退出程序。

## 创建可执行文件
在 `pom.xml` 文件中的 `<dependencies>` 下方插入代码

```xml
<build>
	<plugins>
		<plugin>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-maven-plugin</artifactId>
		</plugin>
	</plugins>
</build>
```

执行 `mvn package` 打包项目，通过 `java -jar target/myproject-0.0.1-SNAPSHOT.jar` 运行。

如果报错端口被占用了
```bash
lsof -i :8080
kill -9 [pid]
```






