// ==UserScript==
// @name 163 Music Downloader 网易云音乐下载助手
// @description 用于在网页端直接下载网易云音乐, 增加大封面下载，增加了歌词下载, 修复有时候不出现按钮的问题
// @author       Zszen John
// @namespace    https://www.jianshu.com/u/15893823363f
// @version 1.8
// @include /^https?://music\.163\.com/.*$/
// @require https://cdn.staticfile.org/jquery/3.3.1/jquery.min.js
// @compatible Chrome
// @compatible Safari
// @supportURL https://www.sunyq.xin/index.php/2019/01/29/%E6%B2%B9%E7%8C%B4%E8%84%9A%E6%9C%AC%E7%BC%96%E5%86%99%E5%85%A5%E9%97%A8-%E7%BD%91%E6%98%93%E4%BA%91%E4%B8%8B%E8%BD%BD%E5%B7%A5%E5%85%B7/
// @namespace https://www.sunyq.xin/index.php/2019/01/29/%E6%B2%B9%E7%8C%B4%E8%84%9A%E6%9C%AC%E7%BC%96%E5%86%99%E5%85%A5%E9%97%A8-%E7%BD%91%E6%98%93%E4%BA%91%E4%B8%8B%E8%BD%BD%E5%B7%A5%E5%85%B7/
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    // Your code here...
    var plugin_name = "163MD"
    var is_debug = 1;
    //is_debug = false;

    var iframe = $("#g_iframe");
    //if(is_debug) console.log([plugin_name,iframe]);
    iframe.on('load', function () {
        //_title.text("123");
        //alert([album.attr("data-src"),album.length]);
        if(is_debug) console.log([plugin_name,"init"]);
        var url = geturl(getid());
        if (window.location.href.search(".*://music\\.163\\.com/#/song\\?id=\\d+.*")!=-1){
            if(is_debug) console.log([plugin_name,"true"]);
            insertElem(url, iframe);
        }
    });

    function export_raw(name, data) {
        var urlObject = window.URL || window.webkitURL || window;

        var export_blob = new Blob([data]);

        var save_link = document.createElementNS("http://www.w3.org/1999/xhtml", "a")
        save_link.href = urlObject.createObjectURL(export_blob);
        save_link.download = name;
        fake_click(save_link);
    }

    function fake_click(obj) {
        var ev = document.createEvent("MouseEvents");
        ev.initMouseEvent(
            "click", true, false, window, 0, 0, 0, 0, 0
            , false, false, false, false, 0, null
        );
        obj.dispatchEvent(ev);
    }

    function getid() {
        var id = window.location.href.split('=')[1];
        return id;
    }

    function geturl(id) {
        var str1 = "http://music.163.com/song/media/outer/url?id=";
        var str2 = ".mp3"
        return str1 + id + str2;
    }

    function save_lyric(){
        var part1 = $("iframe#g_iframe").contents().find("div.bd.bd-open")[0].innerText;
        var part2 = $("iframe#g_iframe").contents().find("div#flag_more")[0].innerText;
        var idx = part1.lastIndexOf("展开")
        if(idx>=0){
            part1 = part1.substr(0,part1.lastIndexOf("展开"))
            part1 += "\n"+part2
        }
        export_raw("lyric.txt",part1)
    }

    function insertElem(url, iframe) {
        //var title = $(document).attr("title");
        //var titles = title.split(" - ");
        var content_frame = $("#content-operation", document.getElementById('g_iframe').contentWindow.document.body)
        if(is_debug) console.log([plugin_name,"content_frame=",content_frame]);
        var album = $("#g_iframe").contents().find(".u-cover.u-cover-6.f-fl>img");
        var element = $('<a class="u-btn2 u-btn2-2 u-btni-addply f-fl 1" hidefocus="true" title="直接下载" target="_blank" href="'+url+'"><i><em class="ply"></em>直接下载</i></a>');
        //element.click(()=>{
         //   var title = $(document).attr("title");
         //   var titles = title.split(" - ");
        //    var exts = url.split(".");
       //     export_raw(titles[0]+"."+exts[exts.length-1], url);
            //alert([titles[0]+"."+exts[exts.length-1], url]);
        //});
        content_frame.append(element);

        var element2 = $('<a class="u-btn2 u-btn2-2 u-btni-addply f-fl 2" hidefocus="true" title="下载封面" target="_blank" href="'+album.attr("data-src")+'"><i><em class="ply"></em>下载封面</i></a>');
        content_frame.append(element2);

        var el2img = $("<img src='"+album.attr("data-src")+"' style='width:30px;'>");
        //el2img.src = album.attr("data-src");
        content_frame.append(el2img);

        //alert($("div.bd.bd-open").length)

        var element3 = $('<a class="u-btn2 u-btn2-2 u-btni-addply f-fl 3" hidefocus="true" title="下载歌词"><i><em class="ply"></em>下载歌词</i></a>');
        content_frame.append(element3);
        element3.on("click",save_lyric)
    }
})();




