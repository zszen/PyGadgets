// ==UserScript==
// @name         [BFD]Block Fake Download 伪下载屏蔽助手
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  屏蔽遇到过的资源网站伪下载区域, 不定期更新
// @author       Zszen John
// @require https://cdn.staticfile.org/jquery/3.3.1/jquery.min.js
// @include     *
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    var label = 'Zszen '
    var url = window.location.href;
    var res = /\/\/.+?\.(.*?)\//.exec(url);
    var site = res[1];
    $('a[href*=".exe"]').parent().hide()
    $('span:contains("高速下载")').hide()
    var isDeal = true;
    var els;
    var dic = {
        '3xiazai.com':()=>{},
        'uzzf.com':()=>{},
        'pc6.com':()=>{},
        '9ht.com':()=>{},
        'onlinedown.net':()=>{},
        'qqtn.com':()=>{},
        'pcsoft.com.cn':()=>{},
        'xpgod.com':()=>{
            $('a[id="maodian"]').next().hide()
            $('ul[class="clearfix "]').hide().next().find('li[class!="new_xzq"]').hide()
        },
        'jisuxz.com':()=>{
            $('a:contains("高速下载")').hide();
        },
        'yesky.com':()=>{
            $('a:contains("高速下载")').hide();
        },
        'anyxz.com':()=>{
            $('p[class="fontcolor2"]>div').hide()
        },
        'cncrk.com':()=>{
            $('a:contains("高速下载")').hide();
        },
        'liangchan.net':()=>{
            $('img[class="bdxz"]').next().hide();
            $('li:contains("高速下载")').hide().parent().next().first().hide()
        },
        'aixuefu.com':()=>{
            $('p:contains("高速下载")').next().hide()
        },
        'xz7.com':()=>{
            $('span:contains("高速下载")').parent().hide();
            $('img[class="xx_yd"]').parent().hide()
        },
        'zdfans.com':()=>{
            $('li:contains("高速下载")').parent().hide();
        },
        'newyx.net':()=>{
            $('a:contains("高速下载")').hide();
            $('li:contains("高速下载")').parent().hide();
        },
        'yunqishi.net':()=>{
            $('a:contains("高速下载")').hide();
        },
        'veryhuo.com':()=>{
            $('a[class="downnow"]').next().hide();
            $('div[id="downlist"]>*').first().hide().next().hide();
        },
        'zuiben.com':()=>{
            $('div:contains("高速下载")').last().parent().hide();
        },
        'mydown.com':()=>{
            $('a:contains("高速下载")').hide();
        },
        'cr173.com':()=>{
            $('a:contains("高速下载")').hide();
        },
        'downcc.com':()=>{
            $('a:contains("高速下载")').hide();
        },
        'newasp.net':()=>{
            $('li:contains("高速下载")').hide();
        },
        '3h3.com':()=>{
            $('a:contains("高速下载")').parent().parent().hide()
        },
        'xue51.com':()=>{},
        'jb51.net':()=>{
            $('a[class="downnow"]').next().hide();
            $('a[class="downgs"]').parent().parent().hide();
        },
        'kxdw.com':()=>{
            $('a:contains("高速下载")').first().hide();
            $('a[class=dxzq]').parent().parent().hide()
        },
        '7down.com':()=>{
            $('li:contains("高速下载")').hide();
        },
        '32r.com':()=>{
            $('div[class*="DetCM1"][class*="Left"]>div>span').last().hide();
            $('div[class*="DCLxzdz"]:contains("高速下载")').last().find('dt').hide();
        },
        'jyrd.com':()=>{
            $('div[class*="xiazainav"]>a').last().hide();
            $('div[class^="xzbox-lf"]>div').hide();
        },
        'downza.cn':()=>{
            $('div[class*="downbtn"]>a').last().hide();
            $('div[class*="pc-down"]').last().find('a[id^=sub]').parent().hide();
        },
        'zol.com.cn':()=>{
            $('div[class=clearfix]>div>div').first().hide();
            els = $('div[class*=downLoad]>div>div')
            $(els[0]).hide();
            $(els[1]).find('span').hide();
        },
        'pconline.com.cn':()=>{
            $('div[class=links]>div').hide();
        },
        'ali213.net':()=>{
            els = $('div:contains("极速下载")[id*=down]>div>div');
            for(var i=els.length-1;i>=Math.max(0,els.length-3);i++){
                $(els[i]).hide();
            }
        },
        'baidu.com':()=>{
            // console.log(label, site);
            function delay_deal(){
                for(var key in dic){
                    if(key=='baidu.com')continue;
                    if(key=='bing.com')continue;
                    // console.log(label, key, $('a[href*="'+key+'"]'));
                    $('a[href*="'+key+'"]').css('text-decoration','line-through').css('color','red');
                }
            }
            setTimeout(delay_deal, 1000);
        },
    }
    dic['bing.com'] = dic['baidu.com'];
    if(dic[site]!=null){
        dic[site]();
        $('iframe').hide();
    }else{

    }
})();