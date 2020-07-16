// ==UserScript==
// @name         Free Yun Keys 免密百度网盘
// @namespace    http://zszen.github.io/
// @version      1.0
// @description  免掉百度网盘写密码的麻烦, 包括解析短网址和跳转链接
// @author
// @require https://cdn.staticfile.org/jquery/3.3.1/jquery.min.js
// @include     *
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    var label = 'Zszen '
    var url = window.location.href;
    var res = /\/\/(.+?\..*?)(\/|\?)/.exec(url);
    var site = res[1];
    console.log(site);
    //parse
    if(site=="pan.baidu.com"){
        var regexp_codeback = /#([a-zA-Z0-9]{4})/
        $('input').first().val(regexp_codeback.exec(url)[1]);
        $('a[title="提取文件"]').click();
    }else{//deal
        var regexp_code = /(码|问)[\s|:|：]*([a-zA-Z0-9]{4})/
        var regexp_url = /(https:\/\/pan.baidu.com\/.*?\/(\d|\w|-)+)/
        var area = $(':contains("提取码")').last();
        var code = regexp_code.exec(area.text())[2];
        var atag = area.find('a[href*="pan.baidu.com"]');
        if(atag.length==0){
            atag = area.find('a');
        }
        var link = atag.attr('href');
        console.log(link);
        if(link.indexOf('https://pan.baidu.com')!=0){
            $.ajax({type:'get',url:link, success:function(res){
                link = regexp_url.exec(res)[0];
                area.find('a').attr('href', link + "#" + code);
            }});
        }else{
            area.find('a').attr('href', link + "#" + code);
        }
    }
})();